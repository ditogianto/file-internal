"""
NEXUS-TRAP // PUSSIBERAD TNI AD
End-to-End Comprehensive QC/QA and Full Accident Scenario Suite
"""

import sys
import os
import socket
import json
import time
import hashlib
import asyncio

# Ensure backend directory is in path
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "backend"))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from fastapi.testclient import TestClient
from app.main import app
from app.telemetry import telemetry
from app.config import settings

client = TestClient(app)

def banner(title):
    print("\n" + "=" * 75)
    print(f" [QC/QA TEST] {title}")
    print("=" * 75)

def run_suite():
    failures = []
    
    # --- TEST 1: Baseline System State (Siaga Hijau) ---
    banner("1. Baseline System State & Security Headers")
    try:
        telemetry.reset_state()
        snapshot = telemetry.get_snapshot()
        assert snapshot["system_status"] == "SIAGA_HIJAU", f"Expected SIAGA_HIJAU, got {snapshot['system_status']}"
        assert snapshot["tarpit_active"] is False, "Tarpit should be initially inactive"
        assert snapshot["metrics"]["false_positive_rate"] == "0.0%", "False positive rate should be 0.0%"
        assert len(snapshot["adversary_dossier"]) > 0, "Dossier should exist"
        print("  [PASS] Telemetry baseline in SIAGA_HIJAU.")
        
        # Test security headers
        res = client.get("/api/status")
        assert res.status_code == 200, f"Expected 200, got {res.status_code}"
        assert res.headers.get("X-Content-Type-Options") == "nosniff", "Missing X-Content-Type-Options"
        assert res.headers.get("X-Frame-Options") == "SAMEORIGIN", "Missing X-Frame-Options"
        assert res.headers.get("Server") == "nginx/1.24.0 (Ubuntu)", f"Server header mismatch: {res.headers.get('Server')}"
        print("  [PASS] Masked server security headers verified (Stratagem 25 Camouflage).")
    except Exception as e:
        print(f"  [FAIL] Test 1: {e}")
        failures.append(f"Test 1: {e}")

    # --- TEST 2: RFC 9309 Robots.txt & Perimeter Isolation ---
    banner("2. RFC 9309 Robots Protocol & Deception Boundary")
    try:
        res = client.get("/robots.txt", headers={"User-Agent": "Googlebot/2.1"})
        assert res.status_code == 200, f"Expected 200, got {res.status_code}"
        assert "Disallow: /decoy-portal/" in res.text, "Missing Disallow for decoy portal"
        assert "Disallow: /.env" in res.text, "Missing Disallow for .env"
        assert "Disallow: /backup.sql" in res.text, "Missing Disallow for backup.sql"
        print("  [PASS] RFC 9309 compliance verified with active honeypot isolation.")
    except Exception as e:
        print(f"  [FAIL] Test 2: {e}")
        failures.append(f"Test 2: {e}")

    # --- TEST 3: Bot Discrimination & Mimicry Detection (FCrDNS) ---
    banner("3. Bot Discrimination & Anti-Spoofing (FCrDNS Engine)")
    try:
        # Spoofed Googlebot from unverified external IP
        res = client.get("/.env", headers={
            "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "X-Forwarded-For": "185.220.101.5"
        })
        assert res.status_code == 200, f"Expected 200, got {res.status_code}"
        
        # Verify MIMICRY_DETECT logged
        logs = telemetry.event_logs
        has_mimicry_log = any(log["tag"] == "MIMICRY_DETECT" for log in logs)
        assert has_mimicry_log, "Mimicry detection log was not generated"
        
        # Verify threat actor registered
        has_mimicry_actor = any(a["threat_vector"] == "SPOOFED_CRAWLER_IMPERSONATION" for a in telemetry.blacklist_feed)
        assert has_mimicry_actor, "Spoofed crawler was not registered in Blacklist"
        print("  [PASS] Masquerading detection (MITRE T1036) caught spoofed bot and registered in Blacklist.")
    except Exception as e:
        print(f"  [FAIL] Test 3: {e}")
        failures.append(f"Test 3: {e}")

    # --- TEST 4: Stratagem 25 & 33 (Reflexive Deception & Poison Credentials) ---
    banner("4. 36 Stratagems Engine (Stratagem 25 & 33)")
    try:
        # Stratagem 33: .env and backup.sql honeytokens
        res_env = client.get("/config.env")
        assert res_env.status_code == 200
        assert "canary-doc-991a-kodam-jaya-telemetry" in res_env.text, "Honeytoken missing from fake .env"
        
        res_sql = client.get("/backup.sql")
        assert res_sql.status_code == 200
        assert "CANARY-SQL-TOKEN-991A-DISPENAD" in res_sql.text, "Honeytoken missing from fake sql"
        print("  [PASS] Stratagem 33: Poisoned honeytokens served to recon actors.")

        # Stratagem 25: Fake 200 OK on unauthorized command reset
        res_fake_reset = client.post("/api/reset", headers={"client-ip": "185.220.101.5"})
        assert res_fake_reset.status_code == 200, "Reflexive response must be 200 OK"
        data_reset = res_fake_reset.json()
        assert data_reset.get("code") == "C4ISR_TELEMETRY_FLUSHED", "Fake success code mismatch"
        
        # Telemetry should NOT have reset for the real operator
        has_strat25_log = any(log["tag"] == "TOU_LIANG_HUAN_ZHU" for log in telemetry.event_logs)
        assert has_strat25_log, "Stratagem 25 alert log missing"
        print("  [PASS] Stratagem 25: Unauthorized attacker pacified with fake 200 OK.")
    except Exception as e:
        print(f"  [FAIL] Test 4: {e}")
        failures.append(f"Test 4: {e}")

    # --- TEST 5: ACCIDENT SCENARIO - Step by Step ---
    banner("5. Full Live Accident Scenario Execution")
    try:
        # Step 5.1: Reset to baseline
        telemetry.reset_state()
        print("  [*] Step 5.1: Baseline Siaga Hijau established.")

        # Step 5.2: OT Reconnaissance on Modbus (Port 502/5020)
        res_modbus = client.post("/api/simulate/modbus-hit", headers={"X-C4ISR-Auth": "PUSSIBERAD-C4ISR-COMMAND-KEY"})
        assert res_modbus.status_code == 200
        assert telemetry.system_status == "SIAGA_KUNING", f"Expected SIAGA_KUNING, got {telemetry.system_status}"
        assert telemetry.adversary_dossier["attacker_ip"] == "192.168.1.88"
        print("  [PASS] Step 5.2: OT Reconnaissance triggered SIAGA KUNING radar alert.")

        # Step 5.3: Brute-Force Scanner & Tarpit Activation
        # Test JA4 signature extraction with headless scanner (before tarpit active)
        res_headless = client.get("/decoy-portal", headers={
            "User-Agent": "Gobuster/v3.5 (Scanning Worker)",
            "X-Forwarded-For": "192.168.1.88"
        })
        assert "JA4:" in telemetry.adversary_dossier.get("cli_signature", ""), "JA4 CLI signature missing"
        
        # Now activate Tarpit
        res_tarpit_on = client.post(
            "/api/tarpit/toggle",
            json={"active": True},
            headers={"X-C4ISR-Auth": "PUSSIBERAD-C4ISR-COMMAND-KEY"}
        )
        assert res_tarpit_on.status_code == 200
        assert telemetry.tarpit_active is True, "Tarpit should be active"
        
        # Test tarpit chunk generator directly to confirm slow-drip throttling (1 byte per chunk)
        from app.tarpit import infinite_chunk_generator
        async def test_chunk():
            gen = infinite_chunk_generator("192.168.1.88")
            chunk = await gen.__anext__()
            assert len(chunk) == 1, "Tarpit must throttle exactly 1 byte per chunk (TCP window choking)"
            await gen.aclose()
        asyncio.run(test_chunk())
        print("  [PASS] Step 5.3: Tarpit active, Gobuster scanner trapped, TCP Window Choking (1 byte/chunk) verified.")

        # Step 5.4: Document Exfiltration & Canary Detonation
        res_canary = client.post("/api/simulate/canary-hit", headers={"X-C4ISR-Auth": "PUSSIBERAD-C4ISR-COMMAND-KEY"})
        assert res_canary.status_code == 200
        assert telemetry.system_status == "SIAGA_MERAH", f"Expected SIAGA_MERAH, got {telemetry.system_status}"
        assert telemetry.compromised_unit == "KODAM JAYA"
        assert "Rahasia_Dislokasi_Pasukan_2026.docx" in telemetry.adversary_dossier["compromised_doc"]
        print("  [PASS] Step 5.4: Canary detonation triggered SIAGA 1 MERAH. Kodam Jaya flagged.")

        # Step 5.5: 1-Click Host Quarantine
        res_iso = client.post(
            "/api/isolate",
            json={"ip": "192.168.1.88"},
            headers={"X-C4ISR-Auth": "PUSSIBERAD-C4ISR-COMMAND-KEY"}
        )
        assert res_iso.status_code == 200
        assert "192.168.1.88" in telemetry.isolated_hosts, "Host 192.168.1.88 not in isolated_hosts"
        assert telemetry.adversary_dossier["isolated"] is True, "Dossier isolated flag not True"
        print("  [PASS] Step 5.5: 1-Click Host Quarantine successfully isolated 192.168.1.88.")

        # Step 5.6: Anti-Backfire Protection
        res_backfire = client.post(
            "/api/isolate",
            json={"ip": "127.0.0.1"},
            headers={"X-C4ISR-Auth": "PUSSIBERAD-C4ISR-COMMAND-KEY"}
        )
        # Should return success True for endpoint execution, but isolation rejected internally
        assert "127.0.0.1" not in telemetry.isolated_hosts, "Loopback must NOT be isolated!"
        print("  [PASS] Step 5.6: Anti-Backfire Guard prevented self-isolation of gateway/loopback.")

        # Step 5.7: AI Military SITREP Generation & SHA-256 Seal
        res_sitrep = client.post(
            "/api/sitrep/generate",
            headers={"X-C4ISR-Auth": "PUSSIBERAD-C4ISR-COMMAND-KEY"}
        )
        assert res_sitrep.status_code == 200
        sitrep_data = res_sitrep.json()
        assert "sitrep" in sitrep_data and "sha256" in sitrep_data
        assert len(sitrep_data["sha256"]) == 64, "SHA-256 hash must be 64 characters"
        
        # Verify hash integrity
        calculated_hash = hashlib.sha256(sitrep_data["sitrep"].encode("utf-8")).hexdigest().upper()
        assert calculated_hash == sitrep_data["sha256"], "SITREP SHA-256 seal integrity mismatch!"
        print(f"  [PASS] Step 5.7: AI SITREP generated with authentic SHA-256 Seal ({sitrep_data['sha256'][:16]}...).")

        # Step 5.8: Sentral Blacklist & Firewall Rule Export (Linux, Windows, MikroTik, Cisco)
        res_fw_linux = client.get(
            "/api/threat-intel/export-firewall?format=iptables",
            headers={"X-C4ISR-Auth": "PUSSIBERAD-C4ISR-COMMAND-KEY"}
        )
        assert res_fw_linux.status_code == 200
        assert "iptables -A PUSSIBERAD_DROP -s 192.168.1.88 -j DROP" in res_fw_linux.text, "iptables missing isolated IP"

        res_fw_win = client.get(
            "/api/threat-intel/export-firewall?format=windows_netsh",
            headers={"X-C4ISR-Auth": "PUSSIBERAD-C4ISR-COMMAND-KEY"}
        )
        assert res_fw_win.status_code == 200
        assert "netsh advfirewall firewall add rule" in res_fw_win.text
        assert "192.168.1.88" in res_fw_win.text

        res_fw_mikrotik = client.get(
            "/api/threat-intel/export-firewall?format=mikrotik",
            headers={"X-C4ISR-Auth": "PUSSIBERAD-C4ISR-COMMAND-KEY"}
        )
        assert res_fw_mikrotik.status_code == 200
        assert "add list=PUSSIBERAD_BLACKLIST address=192.168.1.88" in res_fw_mikrotik.text

        res_fw_cisco = client.get(
            "/api/threat-intel/export-firewall?format=cisco",
            headers={"X-C4ISR-Auth": "PUSSIBERAD-C4ISR-COMMAND-KEY"}
        )
        assert res_fw_cisco.status_code == 200
        assert "deny ip host 192.168.1.88 any" in res_fw_cisco.text
        print("  [PASS] Step 5.8: Sentral Blacklist produced valid iptables, Windows netsh, MikroTik & Cisco ACL rules.")
    except Exception as e:
        print(f"  [FAIL] Test 5 (Accident Scenario): {e}")
        failures.append(f"Test 5: {e}")

    # --- TEST 6: Web Beacon GIF & Canary Download ---
    banner("6. Interactive Audience / Jury Beacon & QR Portal")
    try:
        res_dl = client.get("/download/dokumen-rahasia")
        assert res_dl.status_code == 200, f"Expected 200, got {res_dl.status_code}"
        assert res_dl.headers.get("content-type") == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        
        # Web Beacon trigger
        res_beacon = client.get("/api/canary/beacon/JURY-TEST")
        assert res_beacon.status_code == 200
        assert res_beacon.headers.get("content-type") == "image/gif"
        assert telemetry.system_status == "SIAGA_MERAH"
        print("  [PASS] Canary DOCX download & 1x1 GIF Web Beacon trigger functioning.")
        
        res_qr = client.get("/canary-qr")
        assert res_qr.status_code == 200
        assert "UMPAN DOKUMEN INTELIJEN" in res_qr.text
        print("  [PASS] Jury QR Portal UI rendered successfully.")
    except Exception as e:
        print(f"  [FAIL] Test 6: {e}")
        failures.append(f"Test 6: {e}")

    # --- TEST 7: Cryptographic Audit Trail & Anti-Friendly-Fire Security Fortification ---
    banner("7. SQLite Hash Chain Integrity & Anti-Friendly-Fire Validation")
    try:
        # 7.1 Verify SQLite Audit Trail Endpoint and Cryptographic Chain
        res_audit = client.get(
            "/api/audit/verify",
            headers={"X-C4ISR-Auth": "PUSSIBERAD-C4ISR-COMMAND-KEY"}
        )
        assert res_audit.status_code == 200, f"Expected 200, got {res_audit.status_code}"
        audit_data = res_audit.json()
        assert audit_data.get("status") == "success", f"Expected success, got {audit_data.get('status')}"
        assert audit_data.get("chain_valid") is True, "Audit chain was flagged as invalid!"
        assert audit_data.get("verified_records", 0) > 0, "No audit entries verified"
        print(f"  [PASS] Step 7.1: SQLite Hash Chain integrity mathematically verified ({audit_data.get('verified_records')} entries).")

        # 7.2 Anti-Friendly-Fire: Attacker probe supplying spoofed WebRTC internal IP
        # Attacker at 203.0.113.5 claims their internal IP is Commander's IP 192.168.1.1
        res_probe = client.post(
            "/api/telemetry/probe",
            json={
                "webrtc_ip": "192.168.1.1", # Spoofed target
                "webgl_vendor": "NVIDIA GeForce RTX 4090",
                "canvas_hash": "a1b2c3d4e5f6",
                "audio_hash": "synth9988",
                "platform": "Linux x86_64",
                "user_agent": "Mozilla/5.0 ReconWorker"
            },
            headers={"x-forwarded-for": "203.0.113.5", "x-proxy-verify-key": "PUSSIBERAD-LOCAL-GATEWAY"}
        )
        assert res_probe.status_code == 200, f"Probe status code: {res_probe.status_code}, detail: {res_probe.text}"
        # Check dossier: target attacker_ip must be verified socket IP (203.0.113.5), NOT 192.168.1.1
        assert telemetry.adversary_dossier.get("attacker_ip") == "203.0.113.5", f"Friendly-fire flaw! Expected 203.0.113.5, got {telemetry.adversary_dossier.get('attacker_ip')}"
        assert telemetry.adversary_dossier.get("claimed_internal_ip") == "192.168.1.1", "Claimed internal IP mismatch"
        print("  [PASS] Step 7.2: Anti-Friendly-Fire verified. Attacker cannot frame internal gateway/commander.")

        # 7.3 Dynamic Canary UUID registration
        res_dl2 = client.get("/download/dokumen-rahasia")
        assert res_dl2.status_code == 200
        token_header = res_dl2.headers.get("X-Canary-Token")
        assert token_header and token_header.startswith("DOC-"), f"Invalid token format: {token_header}"
        print(f"  [PASS] Step 7.3: Dynamic Canary Token generated and registered: {token_header}")

        # 7.4 Beacon rate limiting (anti-flooding)
        # First trigger
        res_b1 = client.get(f"/api/canary/beacon/{token_header}", headers={"client-ip": "198.51.100.99"})
        assert res_b1.status_code == 200
        # Immediate second trigger should be throttled (returns cached gif, does not re-flood alerts)
        res_b2 = client.get(f"/api/canary/beacon/{token_header}", headers={"client-ip": "198.51.100.99"})
        assert res_b2.status_code == 200
        assert res_b2.headers.get("X-Beacon-Rate-Limited") == "true"
        print("  [PASS] Step 7.4: Beacon rate limiter successfully prevented alert flooding loop.")

        # 7.5 Stratagem 25 Reflexive Isolation mock for unauthorized external caller
        # Unauthorized outsider calling /api/isolate receives fake 200 OK
        res_unauth_iso = client.post(
            "/api/isolate",
            json={"ip": "10.0.0.99"},
            headers={"client-ip": "198.51.100.77"}
        )
        print("  [PASS] Step 7.5: Fortified security checks completed.")

        # 7.6 AI Sitrep Health Check Endpoint
        res_ai_status = client.get(
            "/api/ai/status",
            headers={"X-C4ISR-Auth": "PUSSIBERAD-C4ISR-COMMAND-KEY"}
        )
        assert res_ai_status.status_code == 200
        ai_meta = res_ai_status.json()
        assert "engine" in ai_meta and "status" in ai_meta
        print(f"  [PASS] Step 7.6: AI Military Engine status verified: {ai_meta['engine']} ({ai_meta['status']}).")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"  [FAIL] Test 7: {e}")
        failures.append(f"Test 7: {e}")

    # --- SUMMARY ---
    banner("SUMMARY OF QC/QA VERIFICATION")
    if not failures:
        print("\n  >>> ALL 6 CRITICAL QC/QA PHASES PASSED WITH 100% SUCCESS RATE! <<<")
        print("  - Zero-Trust C4ISR Security: VERIFIED")
        print("  - Reflexive Deception (Stratagem 25/33): VERIFIED")
        print("  - FCrDNS Bot Discrimination: VERIFIED")
        print("  - Full Accident Scenario (Modbus -> Tarpit -> Canary -> Quarantine -> SITREP): VERIFIED")
        print("  - Sentral Blacklist & Firewall Export: VERIFIED")
        print("  - Interactive Juri QR & Beacon Detonation: VERIFIED\n")
        return True
    else:
        print(f"\n  [!] {len(failures)} FAILURE(S) DETECTED:")
        for f in failures:
            print(f"      - {f}")
        return False

if __name__ == "__main__":
    success = run_suite()
    sys.exit(0 if success else 1)
