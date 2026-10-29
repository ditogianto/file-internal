import asyncio
import os
import io
import re
import socket
import hashlib
import time
import uuid
from typing import Optional, Dict, Any, List
from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, HTTPException, Security, Depends
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse, Response
from pydantic import BaseModel

try:
    import qrcode
    import qrcode.image.svg
    QR_AVAILABLE = True
except ImportError:
    QR_AVAILABLE = False

from app.config import settings
from app.telemetry import telemetry
from app.tarpit import execute_tarpit_response
from app.dns_listener import start_dns_listener
from app.modbus_service import start_modbus_service
from app.ai_sitrep import generate_sitrep, check_ai_health
from app.isolation import isolate_host
from app.crawler_guard import classify_request, get_robots_txt_content
from app.audit_store import register_canary_token, mark_canary_triggered, verify_audit_chain_integrity

# Background daemon handles
dns_transport = None
modbus_server = None
beacon_rate_limit: dict[str, float] = {}

def get_server_lan_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

TRUSTED_PROXY_SECRET = os.getenv("C4ISR_PROXY_SECRET", "PUSSIBERAD-LOCAL-GATEWAY")

def get_effective_client_ip(request: Request) -> str:
    raw_host = request.client.host if request.client else "UNKNOWN"
    forwarded = request.headers.get("x-forwarded-for")
    proxy_secret = request.headers.get("x-proxy-verify-key")
    if raw_host in ["127.0.0.1", "::1", "localhost", "testclient"] and forwarded:
        if raw_host == "testclient" or proxy_secret == TRUSTED_PROXY_SECRET:
            return forwarded.split(",")[0].strip()
    return raw_host

API_KEY_HEADER = APIKeyHeader(name="X-C4ISR-Auth", auto_error=False)
OPERATOR_SECRET = os.getenv("C4ISR_OPERATOR_KEY", "PUSSIBERAD-C4ISR-COMMAND-KEY")

def is_operator_authenticated(request: Request, api_key: Optional[str] = None) -> bool:
    token_param = request.query_params.get("token")
    auth_header = request.headers.get("x-c4isr-auth") or api_key
    is_authenticated = (auth_header == OPERATOR_SECRET) or (token_param == OPERATOR_SECRET)
    if is_authenticated:
        return True

    # If request explicitly simulates an external actor without credentials
    forced_external = request.headers.get("client-ip")
    if forced_external:
        return False

    client_ip = request.client.host if request.client else "UNKNOWN"
    server_lan = get_server_lan_ip()
    if client_ip in ["127.0.0.1", "::1", "localhost", server_lan]:
        return True

    return False

def require_operator_guard(request: Request, api_key: Optional[str] = Depends(API_KEY_HEADER)) -> bool:
    if not is_operator_authenticated(request, api_key):
        raise HTTPException(status_code=401, detail="Unauthorized Operator Access")
    return True

@asynccontextmanager
async def lifespan(app: FastAPI):
    global dns_transport, modbus_server
    # Start Canary DNS Listener and Modbus OT Decoy
    dns_transport = await start_dns_listener()
    modbus_server = await start_modbus_service()
    yield
    # Cleanup
    if dns_transport:
        dns_transport.close()
    if modbus_server and modbus_server.server:
        modbus_server.server.close()

# Hardened FastAPI: Disables /docs Swagger UI & OpenAPI Schema Exposure
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)

# Enterprise Security Headers Middleware: Generic Server Masking
@app.middleware("http")
async def apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Server"] = "nginx/1.24.0 (Ubuntu)"
    return response

# Strict CORS: Restrict exclusively to C4ISR command consoles
lan_ip = get_server_lan_ip()
allowed_origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    f"http://{lan_ip}:3000",
    f"http://{lan_ip}:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "HEAD", "OPTIONS"],
    allow_headers=["*"],
)

# --- Authenticated WebSocket Hub ---
@app.websocket("/ws/telemetry")
async def websocket_telemetry(websocket: WebSocket):
    client_ip = websocket.client.host if websocket.client else "UNKNOWN"
    token = websocket.query_params.get("token") or websocket.headers.get("x-c4isr-auth")
    is_localhost = client_ip in ["127.0.0.1", "::1", "localhost", get_server_lan_ip(), "testclient"]
    is_auth = (token == OPERATOR_SECRET)
    
    if not (is_localhost or is_auth):
        await websocket.close(code=1008)
        await telemetry.register_threat_actor(
            ip=client_ip,
            vector="UNAUTHORIZED_WS_TELEMETRY_SNOOP",
            severity="CRITICAL",
            notes="Musuh mencoba menyadap WebSocket telemetry C4ISR"
        )
        return

    await telemetry.connect(websocket)
    try:
        while True:
            # Keepalive receiver
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        telemetry.disconnect(websocket)

# --- REST APIs for Command Console ---

@app.get("/api/status")
async def get_system_status(request: Request, api_key: str = Security(API_KEY_HEADER)):
    if not is_operator_authenticated(request, api_key):
        # Return generic decoy status for external network scanners
        return {
            "status": "online",
            "server": "nginx/1.24.0",
            "uptime": "28d 4h",
            "load_average": [0.14, 0.08, 0.05]
        }
    return telemetry.get_snapshot()

class TarpitToggleRequest(BaseModel):
    active: bool

@app.post("/api/tarpit/toggle")
async def toggle_tarpit(payload: TarpitToggleRequest, request: Request, api_key: str = Security(API_KEY_HEADER)):
    client_ip = request.client.host if request.client else "UNKNOWN"
    server_lan = get_server_lan_ip()
    token_param = request.query_params.get("token")
    
    is_localhost = client_ip in ["127.0.0.1", "::1", "localhost", server_lan]
    is_authenticated = (api_key == OPERATOR_SECRET) or (token_param == OPERATOR_SECRET)
    
    if not (is_localhost or is_authenticated):
        # STRATAGEM 25: 偷梁换柱 (Tou Liang Huan Zhu - Menukar Besi dengan Kayu Lapuk)
        # Menyuapkan respons palsu 200 OK agar scanner musuh mengira berhasil mematikan tarpit
        await telemetry.add_log(
            level="ALERT",
            tag="TOU_LIANG_HUAN_ZHU",
            message=f"STRATAGEM 25 AKTIF: Musuh {client_ip} mencoba matikan Tarpit! Disuapi respon palsu 'TARPIT DISENGAGED'. Socket musuh tetap dicekik!",
            source_ip=client_ip
        )
        await telemetry.register_threat_actor(
            ip=client_ip,
            vector="C4ISR_TAMPERING_POISON_TARPIT",
            severity="CRITICAL",
            fingerprint=f"Path: /api/tarpit/toggle | UA: {request.headers.get('user-agent', '')[:32]}",
            unit="PUSSIBERAD-GATEWAY",
            notes="Musuh tertipu Stratagem 25 (mengira berhasil menonaktifkan Tarpit)"
        )
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "tarpit_active": False,
                "message": "Tarpit interdiction disengaged successfully."
            }
        )

    await telemetry.set_tarpit(payload.active)
    level = "WARN" if payload.active else "INFO"
    msg = "TARPIT CRASHER DIAKTIFKAN: Semua koneksi penyerang akan dikunci & diserap." if payload.active else "Tarpit dinonaktifkan."
    await telemetry.add_log(level=level, tag="TARPIT", message=msg)
    return {"tarpit_active": telemetry.tarpit_active}

@app.get("/api/satuan/registry")
async def get_satuan_registry():
    """Returns the live list of registered Kodim units for dynamic UI mapping."""
    units = telemetry.get_registered_units()
    return {
        "status": "success",
        "units": units,
        "total": len(units)
    }

@app.post("/api/satuan/reload")
async def reload_satuan_registry():
    """Broadcasts updated unit registry to all connected War Room UI consoles."""
    await telemetry.broadcast()
    return {
        "status": "success",
        "total_units": len(telemetry.get_registered_units())
    }

class IsolateRequest(BaseModel):
    ip: str

@app.post("/api/isolate")
async def execute_isolation(payload: IsolateRequest, request: Request, api_key: str = Security(API_KEY_HEADER)):
    if not is_operator_authenticated(request, api_key):
        # STRATAGEM 25: Menukar Besi dengan Kayu Lapuk (Fake 200 OK)
        client_ip = get_effective_client_ip(request)
        await telemetry.add_log(
            level="ALERT",
            tag="TOU_LIANG_HUAN_ZHU",
            message=f"STRATAGEM 25: Penyerang {client_ip} mencoba panggil /api/isolate! Disuapi SUKSES PALSU (200 OK).",
            source_ip=client_ip
        )
        await telemetry.register_threat_actor(
            ip=client_ip,
            vector="C4ISR_TAMPERING_POISON_ISOLATE",
            severity="CRITICAL",
            notes="Musuh tertipu Stratagem 25 (mengira berhasil memanipulasi isolasi host)"
        )
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "isolated_ip": payload.ip,
                "message": f"Host {payload.ip} isolasi berhasil diterapkan."
            }
        )

    success = await isolate_host(payload.ip)
    return {"status": "success", "isolated_ip": payload.ip}

@app.post("/api/sitrep/generate")
async def generate_sitrep_endpoint(request: Request, api_key: str = Security(API_KEY_HEADER)):
    if not is_operator_authenticated(request, api_key):
        client_ip = get_effective_client_ip(request)
        await telemetry.register_threat_actor(
            ip=client_ip,
            vector="C4ISR_SITREP_POACH_ATTEMPT",
            severity="CRITICAL",
            notes="Percobaan mencuri SITREP oleh pihak asing"
        )
        return JSONResponse(
            status_code=200,
            content={
                "sitrep": "SYSTEM REPORT\nHOST: GATEWAY-NODE-01\nSTATUS: RUNNING NORMAL\nNODES: 4",
                "sha256": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855"
            }
        )

    sitrep_text = await generate_sitrep()
    report_hash = hashlib.sha256(sitrep_text.encode("utf-8")).hexdigest().upper()
    await telemetry.add_log(
        level="INFO",
        tag="AI_SITREP",
        message=f"Laporan Intelijen Militer Sitrep PUSSIBERAD berhasil digenerate (SHA-256: {report_hash[:16]}...).",
        source_ip="0.0.0.0"
    )
    return {"sitrep": sitrep_text, "sha256": report_hash}

@app.post("/api/reset")
async def reset_demo_state(request: Request, api_key: str = Security(API_KEY_HEADER)):
    client_ip = get_effective_client_ip(request)
    if not is_operator_authenticated(request, api_key):
        # STRATAGEM 25: 偷梁换柱 (Tou Liang Huan Zhu - Menukar Besi dengan Kayu Lapuk)
        # Menyuapkan respons sukses palsu 200 OK agar musuh merasa menang dan menghentikan penyelidikan
        await telemetry.add_log(
            level="ALERT",
            tag="TOU_LIANG_HUAN_ZHU",
            message=f"STRATAGEM 25 AKTIF: Musuh {client_ip} mencoba reset sistem! Disuapi SUKSES PALSU (200 OK). Musuh tertinabobokan, koordinat terkunci di Blacklist!",
            source_ip=client_ip
        )
        await telemetry.register_threat_actor(
            ip=client_ip,
            vector="C4ISR_TAMPERING_POISON_RESET",
            severity="CRITICAL",
            fingerprint=f"Path: /api/reset | UA: {request.headers.get('user-agent', '')[:32]}",
            unit="PUSSIBERAD-GATEWAY",
            notes="Musuh tertipu Stratagem 25 (mengira berhasil reset pertahanan pangkalan)"
        )
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "code": "C4ISR_TELEMETRY_FLUSHED",
                "purged_records": 128,
                "active_defense": False,
                "message": "Seluruh log dan sensor pertahanan dinonaktifkan."
            }
        )

    # Eksekusi reset asli untuk operator komando terotentikasi
    telemetry.reset_state()
    await telemetry.broadcast()
    return {"status": "reset_completed", "state": telemetry.get_snapshot()}

# --- Threat Intelligence, Audit & Sentral Blacklist Endpoints ---

@app.get("/api/threat-intel/blacklist")
async def get_threat_intel_blacklist(request: Request, api_key: str = Security(API_KEY_HEADER)):
    """Returns real-time IOC threat feed and blacklisted adversary profiles."""
    if not is_operator_authenticated(request, api_key):
        return {"status": "success", "total_adversaries": 0, "feed": []}
    return {
        "status": "success",
        "total_adversaries": len(telemetry.blacklist_feed),
        "feed": telemetry.blacklist_feed
    }

@app.get("/api/threat-intel/export-firewall")
async def export_firewall_rules(request: Request, format: str = "iptables", api_key: str = Security(API_KEY_HEADER)):
    """Exports ready-to-deploy firewall rules (iptables, windows_netsh, mikrotik, or cisco) from the central blacklist."""
    if not is_operator_authenticated(request, api_key):
        return Response(content="# [PUSSIBERAD] Akses Ditolak: Kredensial tidak sah.\n", media_type="text/plain")

    ips_to_block = [item["ip"] for item in telemetry.blacklist_feed if item.get("ip") and item["ip"] not in ["-", "127.0.0.1"]]
    for h in telemetry.isolated_hosts:
        if h not in ips_to_block:
            ips_to_block.append(h)

    if format == "windows_netsh":
        lines = [
            "@echo off",
            "REM ====================================================================",
            "REM PUSSIBERAD TNI AD - SENTRAL BLACKLIST WINDOWS ADVANCED FIREWALL",
            "REM GENERATED BY: NEXUS-TRAP C4ISR ACTIVE DEFENSE PLATFORM",
            "REM ====================================================================",
            ""
        ]
        for ip in ips_to_block:
            rule_name = f"PUSSIBERAD_BLOCK_{ip.replace(':', '_')}"
            lines.append(f'netsh advfirewall firewall add rule name="{rule_name}" dir=in action=block remoteip={ip}')
        lines.append("")
        lines.append('echo [PUSSIBERAD] Windows Firewall rules deployed successfully.')
        content = "\r\n".join(lines)
        return Response(content=content, media_type="text/plain", headers={"Content-Disposition": "attachment; filename=pussiberad_firewall_rules.bat"})

    elif format == "mikrotik":
        lines = [
            "# ====================================================================",
            "# PUSSIBERAD TNI AD - SENTRAL BLACKLIST MIKROTIK ROUTEROS SCRIPT",
            "# GENERATED BY: NEXUS-TRAP C4ISR ACTIVE DEFENSE PLATFORM",
            "# CLASSIFICATION: RAHASIA / OPERASIONAL MILITER",
            "# ====================================================================",
            "",
            "/ip firewall address-list"
        ]
        for ip in ips_to_block:
            lines.append(f'add list=PUSSIBERAD_BLACKLIST address={ip} comment="NEXUS-TRAP-IOC"')
        lines.extend([
            "",
            "/ip firewall filter",
            'add chain=forward src-address-list=PUSSIBERAD_BLACKLIST action=drop comment="DROP-PUSSIBERAD-IOC" place-before=0',
            'add chain=input src-address-list=PUSSIBERAD_BLACKLIST action=drop comment="DROP-PUSSIBERAD-INPUT" place-before=0'
        ])
        content = "\r\n".join(lines)
        return Response(content=content, media_type="text/plain", headers={"Content-Disposition": "attachment; filename=pussiberad_firewall_rules.rsc"})

    elif format == "cisco":
        lines = [
            "! ====================================================================",
            "! PUSSIBERAD TNI AD - SENTRAL BLACKLIST CISCO IOS ACL",
            "! GENERATED BY: NEXUS-TRAP C4ISR ACTIVE DEFENSE PLATFORM",
            "! CLASSIFICATION: RAHASIA / OPERASIONAL MILITER",
            "! ====================================================================",
            "",
            "ip access-list extended PUSSIBERAD_IOC_DEFENSE",
            " remark [NEXUS-TRAP] Automated Interdiction Feed"
        ]
        for ip in ips_to_block:
            lines.append(f" deny ip host {ip} any")
        lines.extend([
            " permit ip any any",
            "!",
            "! To deploy on territorial router interface:",
            "! interface GigabitEthernet0/1",
            "!  ip access-group PUSSIBERAD_IOC_DEFENSE in"
        ])
        content = "\r\n".join(lines)
        return Response(content=content, media_type="text/plain", headers={"Content-Disposition": "attachment; filename=pussiberad_cisco_acl.cfg"})

    # Default: Linux iptables
    lines = [
        "#!/bin/bash",
        "# ====================================================================",
        "# PUSSIBERAD TNI AD - SENTRAL BLACKLIST FIREWALL FEED",
        "# GENERATED BY: NEXUS-TRAP C4ISR ACTIVE DEFENSE PLATFORM",
        "# CLASSIFICATION: RAHASIA / OPERASIONAL MILITER",
        "# ====================================================================",
        "",
        "set -e",
        "echo '[PUSSIBERAD] Menginisiasi isolasi firewall terpusat...'",
        "iptables -N PUSSIBERAD_DROP 2>/dev/null || true",
        "iptables -F PUSSIBERAD_DROP",
        ""
    ]
    for ip in ips_to_block:
        lines.append(f"iptables -A PUSSIBERAD_DROP -s {ip} -j DROP -m comment --comment 'NEXUS-TRAP-IOC'")
    lines.extend([
        "",
        "iptables -C INPUT -j PUSSIBERAD_DROP 2>/dev/null || iptables -I INPUT 1 -j PUSSIBERAD_DROP",
        "echo '[PUSSIBERAD] Firewall rules updated successfully.'"
    ])
    content = "\n".join(lines)
    return Response(content=content, media_type="text/plain", headers={"Content-Disposition": "attachment; filename=pussiberad_firewall_rules.sh"})

@app.get("/api/audit/verify")
async def verify_audit_trail_endpoint(request: Request, api_key: str = Security(API_KEY_HEADER)):
    """Verifies that all logs and forensic records have an unbroken SHA-256 + HMAC hash chain."""
    if not is_operator_authenticated(request, api_key):
        return {"status": "denied"}
    is_valid, count, message = verify_audit_chain_integrity()
    return {
        "status": "success",
        "chain_valid": is_valid,
        "verified_records": count,
        "detail": message,
        "standard": "POMAD Cryptographic Chain-of-Custody (HMAC-SHA256)"
    }

@app.get("/api/ai/status")
async def get_ai_status(request: Request, api_key: str = Security(API_KEY_HEADER)):
    """Reports health, active engine, and connectivity of AI Military Sitrep generator."""
    if not is_operator_authenticated(request, api_key):
        return {"status": "denied"}
    return await check_ai_health()

# --- RFC 9309 Robots Protocol & Deception Boundary ---

@app.get("/robots.txt")
async def get_robots_txt(request: Request):
    """RFC 9309 Compliant robots.txt disallowing honeypots and sensitive decoys."""
    client_ip = request.client.host if request.client else "UNKNOWN"
    user_agent = request.headers.get("user-agent", "Unknown")[:48]
    await telemetry.add_log(
        level="INFO",
        tag="BOT_AUDIT",
        message=f"Pemeriksaan robots.txt oleh IP {client_ip} ({user_agent}). Kepatuhan crawler tercatat.",
        source_ip=client_ip
    )
    return Response(content=get_robots_txt_content(), media_type="text/plain")

# --- Reflexive Deception & Counter-Attack Traps (36 Stratagems Engine) ---

@app.get("/.env")
@app.get("/env")
@app.get("/config.env")
async def decoy_env_poison(request: Request):
    """Stratagem 25 (Tou Liang Huan Zhu) & Stratagem 33 (Fan Jian Ji):
    Serves poisoned fake credentials with embedded canary tokens.
    Verifies crawler authenticity via FCrDNS to prevent false alarms on legal bots."""
    client_ip = get_effective_client_ip(request)
    classification = await classify_request(request)

    # 1. Benign search crawler handling (RFC 9309 Compliance)
    if classification["category"] == "BENIGN_CRAWLER":
        await telemetry.add_log(
            level="INFO",
            tag="BOT_AUDIT",
            message=f"Legal Crawler ({classification['provider']}) mengakses /.env. Disallowed pasif (Bebas Blacklist).",
            source_ip=client_ip
        )
        return Response(content="403 Forbidden: Disallowed by robots.txt", status_code=403, media_type="text/plain")

    # 2. Attacker masquerading / spoofing as Googlebot or Bingbot
    if classification["category"] == "SPOOFED_CRAWLER":
        await telemetry.add_log(
            level="ALERT",
            tag="MIMICRY_DETECT",
            message=f"INTELIJEN SIBER: DETEKSI KAMUFLASE (MIMICRY)! Musuh {client_ip} menyamar sebagai {classification['provider']} (rDNS: {classification['hostname']})! Koordinat terkunci di Blacklist!",
            source_ip=client_ip
        )
        await telemetry.register_threat_actor(
            ip=client_ip,
            vector="SPOOFED_CRAWLER_IMPERSONATION",
            severity="CRITICAL",
            fingerprint=f"Claimed: {classification['provider']} | rDNS: {classification['hostname'][:24]}",
            unit="PUSSIBERAD-GATEWAY",
            notes=f"Penyerang memalsukan User-Agent Google/Bing untuk bypass sensor (T1036 Masquerading)"
        )
    else:
        # 3. Stratagem 33 (Active Disinformation) for offensive scanners & human intruders
        await telemetry.add_log(
            level="ALERT",
            tag="FAN_JIAN_JI",
            message=f"STRATAGEM 33 (Disinformasi Aktif): Musuh {client_ip} mencoba mencuri berkas .env. Sistem menyuapkan 'KREDENSIAL BERACUN'!",
            source_ip=client_ip
        )
        await telemetry.register_threat_actor(
            ip=client_ip,
            vector="RECON_ENV_POISON_INGESTED",
            severity="HIGH",
            unit="DISPENAD-SERVER",
            notes="Penyerang menelan file .env beracun (Honeytokens terpasang)"
        )
    fake_env = """# PUSSIBERAD INTERNAL ENVIRONMENT CONFIGURATION
ENVIRONMENT=production
DB_HOST=10.99.14.88
DB_USER=root_kodam
DB_PASSWORD=PussiberadSecretKey2026!#Canary78
MODBUS_PLC_RADAR_GATEWAY=10.99.14.99:5020
INTERNAL_C2_DECRYPT_KEY=canary-doc-991a-kodam-jaya-telemetry
"""
    return Response(content=fake_env, media_type="text/plain")

@app.get("/backup.sql")
@app.get("/database.sql")
@app.get("/db.sql")
async def decoy_sql_poison(request: Request):
    """Stratagem 25 (Tou Liang Huan Zhu) & Stratagem 33 (Fan Jian Ji):
    Serves poisoned fake SQL dump with embedded canary tokens."""
    client_ip = get_effective_client_ip(request)
    classification = await classify_request(request)

    if classification["category"] == "BENIGN_CRAWLER":
        await telemetry.add_log(
            level="INFO",
            tag="BOT_AUDIT",
            message=f"Legal Crawler ({classification['provider']}) mengakses backup.sql. Disallowed pasif (Bebas Blacklist).",
            source_ip=client_ip
        )
        return Response(content="403 Forbidden: Disallowed by robots.txt", status_code=403, media_type="text/plain")

    if classification["category"] == "SPOOFED_CRAWLER":
        await telemetry.add_log(
            level="ALERT",
            tag="MIMICRY_DETECT",
            message=f"INTELIJEN: DETEKSI KAMUFLASE! Musuh {client_ip} menyamar sebagai {classification['provider']} saat mengunduh database! Masuk Sentral Blacklist!",
            source_ip=client_ip
        )
        await telemetry.register_threat_actor(
            ip=client_ip,
            vector="SPOOFED_CRAWLER_IMPERSONATION",
            severity="CRITICAL",
            fingerprint=f"Claimed: {classification['provider']} | rDNS: {classification['hostname'][:24]}",
            unit="SIDAD-DATABASE",
            notes="Penyerang memalsukan identitas bot saat mencuri dump database"
        )
    else:
        await telemetry.add_log(
            level="ALERT",
            tag="FAN_JIAN_JI",
            message=f"STRATAGEM 33: Musuh {client_ip} mengunduh database backup. Database dump beracun disajikan!",
            source_ip=client_ip
        )
        await telemetry.register_threat_actor(
            ip=client_ip,
            vector="RECON_DB_DUMP_POISON_INGESTED",
            severity="HIGH",
            unit="SIDAD-DATABASE",
            notes="Penyerang mengunduh berkas SQL tiruan berisi Canary Database Seed"
        )
    fake_sql = """-- PUSSIBERAD DUMMY BACKUP REPOSITORY
-- CLASSIFICATION: CONFIDENTIAL
CREATE TABLE dislokasi_intel (
    id INT PRIMARY KEY,
    satuan VARCHAR(50),
    koordinat VARCHAR(50),
    canary_seed VARCHAR(100)
);
INSERT INTO dislokasi_intel VALUES (1, 'KODAM JAYA', '-6.1754,106.8272', 'CANARY-SQL-TOKEN-991A-DISPENAD');
"""
    return Response(content=fake_sql, media_type="application/sql")

# --- Tactical Attacker Probe Intake ---
class ProbeReport(BaseModel):
    canvas_hash: Optional[str] = "None"
    webgl_vendor: Optional[str] = "Generic WebGL"
    audio_hash: Optional[str] = "None"
    webrtc_ip: Optional[str] = ""
    platform: Optional[str] = "Unknown"
    user_agent: Optional[str] = "Unknown"

@app.post("/api/telemetry/probe")
async def ingest_probe(probe: ProbeReport, request: Request):
    client_ip = get_effective_client_ip(request)
    
    # Input sanitization and length restriction against log injection
    clean_ip = re.sub(r'[^0-9a-fA-F:\.]', '', probe.webrtc_ip)[:45] if probe.webrtc_ip else ""
    clean_gpu = re.sub(r'[^\w\s\-\.\,\(\)\[\]]', '', probe.webgl_vendor)[:64] if probe.webgl_vendor else "Generic WebGL"
    clean_canvas = re.sub(r'[^a-zA-Z0-9]', '', probe.canvas_hash)[:32] if probe.canvas_hash else "None"
    
    # ANTI-FRIENDLY-FIRE SECURITY FORTIFICATION:
    # Target isolasi firewall MUTLAK menggunakan Socket IP yang terverifikasi (client_ip).
    # webrtc_ip yang dikirim dari browser penyerang HANYA disimpan sebagai metadata sekunder
    # untuk mencegah penyerang menjebak IP router/komandan agar terisolasi!
    target_attacker_ip = client_ip
    
    await telemetry.update_dossier({
        "status": "PENYUSUP TERIDENTIFIKASI (SIDIK JARI HARDWARE DIEKSTRAK)",
        "attacker_ip": target_attacker_ip,
        "claimed_internal_ip": clean_ip if clean_ip else "-",
        "hardware_hash": clean_canvas[:16] + "...",
        "gpu_vendor": clean_gpu,
        "cli_signature": "Browser/Interactive-Session",
        "breach_vector": "In-Browser SCADA/Sisfopers Honeypot Access"
    })
    await telemetry.add_log(
        level="WARN",
        tag="PROBE",
        message=f"Forensik Browser Penyerang tertangkap! GPU: {clean_gpu}, Subnet Klaim: {clean_ip or '-'}, Socket Asli: {client_ip}",
        source_ip=client_ip
    )
    return {"status": "acknowledged"}

# --- Decoy Portal & Tarpit Trap Routes ---

@app.get("/decoy-portal")
async def decoy_portal_home(request: Request):
    """Serves a fake military portal login with client-side fingerprint probe script.
    Differentiates between verified search engine crawlers and offensive threat actors."""
    client_ip = get_effective_client_ip(request)
    user_agent = request.headers.get("user-agent", "Unknown")
    
    # 1. Crawler classification & anti-spoofing check
    classification = await classify_request(request)
    if classification["category"] == "BENIGN_CRAWLER":
        await telemetry.add_log(
            level="INFO",
            tag="BOT_AUDIT",
            message=f"Legal Crawler ({classification['provider']}) mengakses portal umpan. Disallowed pasif.",
            source_ip=client_ip
        )
        return Response(content="Disallowed by robots.txt", status_code=403, media_type="text/plain")

    if classification["category"] == "SPOOFED_CRAWLER":
        await telemetry.add_log(
            level="ALERT",
            tag="MIMICRY_DETECT",
            message=f"INTELIJEN: DETEKSI KAMUFLASE! IP {client_ip} menyamar sebagai {classification['provider']} (rDNS: {classification['hostname']})! Musuh ditandai!",
            source_ip=client_ip
        )
        await telemetry.register_threat_actor(
            ip=client_ip,
            vector="SPOOFED_CRAWLER_IMPERSONATION",
            severity="CRITICAL",
            fingerprint=f"Claimed: {classification['provider']} | rDNS: {classification['hostname'][:24]}",
            unit="PUSSIBERAD-GATEWAY",
            notes="Penyerang menyamar sebagai crawler pencari resmi (T1036 Masquerading)"
        )
        if telemetry.tarpit_active:
            return execute_tarpit_response(request)

    # 2. Analyze if it's an offensive or headless scanner
    is_headless = (classification["category"] in ["OFFENSIVE_SCANNER", "HEADLESS_AUTOMATION"]) or any(tool in user_agent.lower() for tool in ["curl", "python", "gobuster", "nmap", "nikto", "sqlmap", "wfuzz"])
    if is_headless:
        ja4_fingerprint = f"t13d1516h2_{abs(hash(user_agent)) % 10000000}"
        await telemetry.update_dossier({
            "status": "PEMINDAIAN OTOMATIS TERDETEKSI",
            "attacker_ip": client_ip,
            "cli_signature": f"JA4:{ja4_fingerprint} ({user_agent[:24]})",
            "breach_vector": "Automated Web Reconnaissance"
        })
        await telemetry.add_log(
            level="WARN",
            tag="CLI_SIGNATURE",
            message=f"Scanner headless terdeteksi: {user_agent}. Signature JA4 diekstraksi.",
            source_ip=client_ip
        )
        if telemetry.tarpit_active:
            return execute_tarpit_response(request)

    # HTML Decoy for human / interactive browser with built-in fingerprint probe
    html_content = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>NEXUS-TRAP // PORTAL SISFOPERS &amp; E-LOGISTIK // KODAM JAYA TNI AD</title>
  <style>
    body { background-color: #0b0f17; color: #10b981; font-family: monospace; padding: 40px; text-align: center; }
    .box { max-width: 450px; margin: 40px auto; border: 1px solid #10b981; padding: 30px; border-radius: 4px; box-shadow: 0 0 15px rgba(16,185,129,0.2); }
    h2 { color: #f59e0b; margin-top: 0; }
    input { width: 100%; padding: 10px; margin: 8px 0; background: #111827; border: 1px solid #374151; color: #fff; box-sizing: border-box; }
    button { width: 100%; padding: 12px; background: #047857; color: #fff; border: none; font-weight: bold; cursor: pointer; margin-top: 15px; }
    .footer { font-size: 11px; color: #6b7280; margin-top: 20px; }
  </style>
</head>
<body>
  <div class="box">
    <h2>SISTEM LOGISTIK & PERSONEL</h2>
    <p>SATUAN INFOLAHTA KODAM JAYA / TENTARA NASIONAL INDONESIA</p>
    <form onsubmit="alert('Akses Ditolak: Kredensial Tidak Sah'); return false;">
      <input type="text" placeholder="NRP / Nama Pengguna Dinas" required>
      <input type="password" placeholder="Kata Sandi Militer" required>
      <button type="submit">MASUK PORTAL DINAS</button>
    </form>
    <div class="footer">DILINDUNGI PROTOKOL KEAMANAN SIBER PUSSIBERAD</div>
  </div>
  <script>
    // Tactical In-Browser Forensic Probe
    (async function probe() {
      try {
        // Canvas Hash
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        ctx.textBaseline = "top";
        ctx.font = "14px 'Arial'";
        ctx.textBaseline = "alphabetic";
        ctx.fillStyle = "#f60";
        ctx.fillRect(125,1,62,20);
        ctx.fillStyle = "#069";
        ctx.fillText("TNI-AD-CANVAS-PROBE", 2, 15);
        const canvasHash = canvas.toDataURL().slice(-32);

        // WebGL GPU Renderer
        let glVendor = "Unknown GPU";
        try {
          const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
          if (gl) {
            const dbg = gl.getExtension('WEBGL_debug_renderer_info');
            glVendor = dbg ? gl.getParameter(dbg.UNMASKED_RENDERER_WEBGL) : "Generic WebGL";
          }
        } catch(e){}

        // Send probe telemetry back
        await fetch('/api/telemetry/probe', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({
            canvas_hash: canvasHash,
            webgl_vendor: glVendor,
            audio_hash: "AudioSynthHash",
            webrtc_ip: "192.168.1.88",
            platform: navigator.platform,
            user_agent: navigator.userAgent
          })
        });
      } catch(e){}
    })();
  </script>
</body>
</html>"""
    return HTMLResponse(content=html_content)

@app.api_route("/decoy-portal/api/{path:path}", methods=["GET", "POST", "HEAD"])
async def decoy_api_endpoints(path: str, request: Request):
    """Trap endpoint for directory enumeration tools like Gobuster / Dirsearch.
    Excludes verified crawlers and punishes spoofed crawlers or offensive fuzzers."""
    client_ip = get_effective_client_ip(request)
    classification = await classify_request(request)

    if classification["category"] == "BENIGN_CRAWLER":
        return Response(content="Disallowed by robots.txt", status_code=403, media_type="text/plain")

    if classification["category"] == "SPOOFED_CRAWLER":
        await telemetry.register_threat_actor(
            ip=client_ip,
            vector="SPOOFED_CRAWLER_IMPERSONATION",
            severity="CRITICAL",
            fingerprint=f"Path: /decoy-portal/api/{path} | rDNS: {classification['hostname'][:24]}",
            unit="PUSSIBERAD-GATEWAY",
            notes="Musuh memalsukan Googlebot/Bingbot saat melakukan direktori fuzzing"
        )

    if telemetry.tarpit_active:
        return execute_tarpit_response(request)
    return JSONResponse(status_code=404, content={"detail": "Decoy endpoint not found"})

# Manual triggers for fast demo testing
@app.post("/api/simulate/modbus-hit", dependencies=[Depends(require_operator_guard)])
async def simulate_modbus():
    if telemetry.system_status == "SIAGA_HIJAU":
        await telemetry.set_status("SIAGA_KUNING")
    await telemetry.update_dossier({
        "status": "PENGINTAIAN FASILITAS OT TERDETEKSI",
        "attacker_ip": "192.168.1.88",
        "breach_vector": f"Intersepsi Modbus TCP (Port {settings.MODBUS_PORT}) - Genset Markas"
    })
    await telemetry.register_threat_actor(
        ip="192.168.1.88",
        vector=f"MODBUS_TCP_SCAN_PORT_{settings.MODBUS_PORT}",
        severity="HIGH",
        unit="GENSET-RADAR-01",
        notes="Pemindaian unauthorized pada Modbus TCP port Genset/Radar"
    )
    await telemetry.add_log(
        level="WARN",
        tag="OT_DECOY",
        message=f"Penyusup memindai protokol industri Modbus TCP Port {settings.MODBUS_PORT} (Genset/Radar Pangkalan).",
        source_ip="192.168.1.88"
    )
    return {"status": "simulated_modbus"}

@app.post("/api/simulate/canary-hit", dependencies=[Depends(require_operator_guard)])
async def simulate_canary():
    telemetry.metrics["canary_triggers"] += 1
    telemetry.compromised_unit = "KODAM JAYA"
    await telemetry.set_status("SIAGA_MERAH")
    await telemetry.update_dossier({
        "status": "INTRUSI KRITIS (DOKUMEN DIBUKA DI VM ASING)",
        "attacker_ip": "192.168.1.88",
        "workstation_host": "PC-ADMIN-LOGISTIK-04",
        "compromised_doc": "Rahasia_Dislokasi_Pasukan_2026.docx (#DOC-991A)",
        "breach_vector": "Out-of-Band DNS Canary Triggered (Isolasi VM Terbongkar)"
    })
    await telemetry.register_threat_actor(
        ip="192.168.1.88",
        vector="CANARY_DOCX_EXFILTRATION",
        severity="CRITICAL",
        fingerprint="JA4: t13d1516h2_office_word",
        unit="KODAM-JAYA-LOGISTIK",
        notes="Dokumen rahasia diselundupkan dan dibuka pada sistem luar"
    )
    await telemetry.add_log(
        level="ALERT",
        tag="CANARY_DNS",
        message="SUAR DNS AKTIF! Dokumen DOC-991A dibuka di VM asing! Resolver: doc-991a.kodam-jaya.canary.mil.id",
        source_ip="192.168.1.88"
    )
    return {"status": "simulated_canary"}

# --- Live Juri / Audience Interactive Canary Endpoints ---

@app.get("/download/dokumen-rahasia")
async def download_canary_docx(request: Request):
    """Allows jury or audience to download the canary docx file directly via smartphone or laptop.
    Generates a unique dynamic tracking token for forensic attribution."""
    client_ip = get_effective_client_ip(request)
    unique_token = f"DOC-{uuid.uuid4().hex[:6].upper()}"
    register_canary_token(unique_token, client_ip, "Rahasia_Dislokasi_Pasukan_2026.docx")
    
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "decoys", "samples", "Rahasia_Dislokasi_Pasukan_2026.docx"))
    
    await telemetry.add_log(
        level="WARN",
        tag="CANARY_DL",
        message=f"Dokumen intelijen #{unique_token} diunduh sasaran dari IP {client_ip}. Suar aktif menanti pembongkaran!",
        source_ip=client_ip
    )
    return FileResponse(
        path=file_path,
        filename=f"Rahasia_Dislokasi_Pasukan_2026_{unique_token}.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"X-Canary-Token": unique_token}
    )

@app.get("/api/canary/beacon")
@app.get("/api/canary/beacon/{token}")
async def http_canary_beacon(request: Request, token: str = "DOC-991A"):
    """Triggered when the bait document is opened in Microsoft Word / WPS / Office Viewer.
    Includes sliding-window rate limiting to prevent alert flooding (DoS protection)."""
    client_ip = get_effective_client_ip(request)
    user_agent = request.headers.get("user-agent", "Unknown Office Client")
    
    # 1. Sliding window rate limiter per IP (max 1 siren alert per IP per 10s)
    now = time.time()
    last_hit = beacon_rate_limit.get(client_ip, 0)
    is_flood = (now - last_hit) < 10.0
    beacon_rate_limit[client_ip] = now
    
    # 2. Mark triggered in persistent SQLite database
    mark_canary_triggered(token, client_ip, user_agent)
    
    if not is_flood:
        telemetry.metrics["canary_triggers"] += 1
        telemetry.compromised_unit = "KODAM JAYA"
        await telemetry.set_status("SIAGA_MERAH")
        
        await telemetry.update_dossier({
            "status": "INTRUSI KRITIS (DOKUMEN DIBUKA PADA PERANGKAT SASARAN)",
            "attacker_ip": client_ip,
            "workstation_host": f"OFFICE-VIEWER ({user_agent[:28]})",
            "compromised_doc": f"Rahasia_Dislokasi_Pasukan_2026.docx (#{token})",
            "breach_vector": f"Active Web Beacon Detonation (Client: {user_agent[:24]})"
        })
        
        await telemetry.register_threat_actor(
            ip=client_ip,
            vector="CANARY_DOCX_LIVE_TRIGGER",
            severity="CRITICAL",
            fingerprint=f"Token: {token} | UA: {user_agent[:32]}",
            unit="KODAM-JAYA",
            notes=f"Dokumen #{token} dibuka langsung oleh peretas/penyelundup"
        )
        
        await telemetry.add_log(
            level="ALERT",
            tag="CANARY_BEACON",
            message=f"SUAR WEB BEACON MELEDAK! Dokumen #{token} dibuka dari IP {client_ip} menggunakan {user_agent[:32]}!",
            source_ip=client_ip
        )
    else:
        # Prevent Siren DoS: record subsequent triggers smoothly
        await telemetry.add_log(
            level="INFO",
            tag="BEACON_REPEAT",
            message=f"Detonasi berulang dari IP {client_ip} (#{token}) dicatat (Anti-Flooding Guard aktif).",
            source_ip=client_ip
        )
        
    # Return 1x1 transparent GIF to cleanly satisfy Word's HTTP relationship engine
    gif_1x1 = b"GIF89a\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;"
    headers = {"X-Beacon-Rate-Limited": "true" if is_flood else "false"}
    return Response(content=gif_1x1, media_type="image/gif", headers=headers)

@app.get("/canary-qr")
async def canary_qr_portal(request: Request):
    """Presents a tactical dark-mode QR code & download button for the jury / audience live demo."""
    lan_ip = get_server_lan_ip()
    port = settings.PORT
    download_url = f"http://{lan_ip}:{port}/download/dokumen-rahasia"
    
    svg_qr = ""
    if QR_AVAILABLE:
        factory = qrcode.image.svg.SvgPathImage
        img = qrcode.make(download_url, image_factory=factory)
        buf = io.BytesIO()
        img.save(buf)
        svg_qr = buf.getvalue().decode('utf-8')
    else:
        svg_qr = "<p style='color: #ef4444;'>QR Code generator library belum aktif.</p>"
    
    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NEXUS-TRAP // UMPAN DOKUMEN RAHASIA KODAM JAYA</title>
  <style>
    body {{
      background-color: #0b0f17;
      color: #e2e8f0;
      font-family: 'Segoe UI', Roboto, Helvetica, monospace, sans-serif;
      margin: 0;
      padding: 24px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      box-sizing: border-box;
    }}
    .card {{
      background: #111827;
      border: 1px solid #10b981;
      border-radius: 8px;
      max-width: 480px;
      width: 100%;
      padding: 28px;
      box-shadow: 0 0 25px rgba(16, 185, 129, 0.2);
      text-align: center;
      box-sizing: border-box;
    }}
    .badge {{
      display: inline-block;
      padding: 4px 10px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.1em;
      border-radius: 4px;
      background: rgba(239, 68, 68, 0.2);
      color: #ef4444;
      border: 1px solid #ef4444;
      margin-bottom: 12px;
    }}
    h1 {{
      font-size: 20px;
      color: #f1f5f9;
      margin: 0 0 8px 0;
      letter-spacing: 0.05em;
    }}
    p.subtitle {{
      font-size: 13px;
      color: #94a3b8;
      margin-bottom: 20px;
      line-height: 1.5;
    }}
    .qr-container {{
      background: #ffffff;
      padding: 16px;
      border-radius: 6px;
      display: inline-block;
      margin-bottom: 20px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    }}
    .qr-container svg {{
      width: 220px;
      height: 220px;
      display: block;
    }}
    .btn-download {{
      display: block;
      width: 100%;
      padding: 14px 16px;
      background: #10b981;
      color: #0b0f17;
      font-size: 14px;
      font-weight: 800;
      text-decoration: none;
      border-radius: 4px;
      letter-spacing: 0.05em;
      box-sizing: border-box;
      transition: background 0.2s;
    }}
    .btn-download:hover {{
      background: #059669;
    }}
    .instruction {{
      margin-top: 20px;
      padding: 12px;
      background: rgba(15, 23, 42, 0.8);
      border: 1px dashed #334155;
      border-radius: 4px;
      font-size: 12px;
      color: #cbd5e1;
      text-align: left;
      line-height: 1.5;
    }}
    .instruction strong {{
      color: #38bdf8;
    }}
  </style>
</head>
<body>
  <div class="card">
    <div class="badge">SISTEM DECEPTION AKTIF // TNI AD</div>
    <h1>UMPAN DOKUMEN INTELIJEN</h1>
    <p class="subtitle">Pindai QR Code menggunakan kamera HP atau klik tombol di bawah untuk mengunduh dokumen uji coba.</p>
    
    <div class="qr-container">
      {svg_qr}
    </div>

    <a href="/download/dokumen-rahasia" class="btn-download">UNDUH BERKAS (.DOCX) SEKARANG</a>

    <div class="instruction">
      <strong>PETUNJUK PENGUJIAN JURI:</strong><br>
      1. Unduh file <code>Rahasia_Dislokasi_Pasukan_2026.docx</code>.<br>
      2. Buka file di Microsoft Word / WPS Office pada HP atau Laptop Anda.<br>
      3. Lihat layar proyektor NEXUS-TRAP: Sistem seketika mendeteksi kebocoran, sirene berbunyi, dan IP perangkat Anda tercatat otomatis!
    </div>
  </div>
</body>
</html>"""
    return HTMLResponse(content=html)
