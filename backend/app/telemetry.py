import asyncio
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional
from fastapi import WebSocket
from app.audit_store import init_db, append_audit_log, get_recent_logs, save_blacklist_actor, load_blacklist_feed

class TelemetryManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self._lock = asyncio.Lock()
        init_db()
        self.reset_state()

    def reset_state(self):
        """Reset state to baseline normal Siaga Hijau with cryptographic persistence."""
        self.system_status: str = "SIAGA_HIJAU"  # SIAGA_HIJAU | SIAGA_KUNING | SIAGA_MERAH
        self.tarpit_active: bool = False
        self.locked_threads: int = 0
        self.active_tarpit_conns: int = 0
        self.compromised_unit: Optional[str] = None
        self.isolated_hosts: List[str] = []
        
        # Load persisted blacklist feed if available
        persisted_feed = load_blacklist_feed()
        if persisted_feed:
            self.blacklist_feed = persisted_feed
        else:
            self.blacklist_feed: List[Dict[str, Any]] = [
                {
                    "ioc_id": "IOC-PUSSIBERAD-BASELINE-01",
                    "ip": "103.145.22.45",
                    "classification": "EXTERNAL_SPIONAGE",
                    "threat_vector": "KNOWN_C2_RECON_FEED",
                    "severity": "HIGH",
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "status": "BLOCKED",
                    "fingerprint": "JA4: t13d1516h2_8daaf6152771_b326079c6a7e",
                    "unit_target": "PUSSIBERAD-GATEWAY",
                    "notes": "Sindikat APT terdeteksi pada feed BSSN"
                }
            ]
        
        self.metrics = {
            "false_positive_rate": "0.0%",
            "active_decoys": 64,
            "locked_threads": 0,
            "canary_triggers": 0,
            "accuracy_score": "100.0%"
        }
        
        self.adversary_dossier = {
            "status": "TIDAK TERDETEKSI",
            "attacker_ip": "-",
            "claimed_internal_ip": "-",
            "workstation_host": "-",
            "hardware_hash": "-",
            "gpu_vendor": "-",
            "cli_signature": "-",
            "compromised_doc": "-",
            "breach_vector": "-",
            "isolated": False
        }
        
        # Load persisted logs if available
        persisted_logs = get_recent_logs(20)
        if persisted_logs:
            self.event_logs = persisted_logs
        else:
            self.event_logs: List[Dict[str, Any]] = [
                {
                    "id": 1,
                    "timestamp": datetime.now().strftime("%H:%M:%S"),
                    "level": "INFO",
                    "tag": "SISTEM",
                    "message": "Sistem Pertahanan Aktif NEXUS-TRAP online. Sensor Kodam & OT 64 Node Aktif.",
                    "source_ip": "127.0.0.1"
                }
            ]

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        # Send initial snapshot immediately
        await websocket.send_json(self.get_snapshot())

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    def get_registered_units(self) -> List[Dict[str, Any]]:
        registry_path = Path(__file__).parent / "satuan_registry.json"
        if registry_path.exists():
            try:
                with open(registry_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return list(data.values())
            except Exception:
                pass
        return []

    def get_snapshot(self) -> Dict[str, Any]:
        units = self.get_registered_units()
        return {
            "system_status": self.system_status,
            "tarpit_active": self.tarpit_active,
            "metrics": self.metrics,
            "adversary_dossier": self.adversary_dossier,
            "event_logs": self.event_logs[-50:],  # last 50 events
            "compromised_unit": self.compromised_unit,
            "registered_units": units,
            "total_registered_units": len(units)
        }

    async def broadcast(self):
        """Broadcast state updates to all connected UI clients."""
        if not self.active_connections:
            return
        snapshot = self.get_snapshot()
        disconnected = []
        for connection in self.active_connections:
            try:
                await connection.send_json(snapshot)
            except Exception:
                disconnected.append(connection)
        for dc in disconnected:
            self.disconnect(dc)

    async def add_log(self, level: str, tag: str, message: str, source_ip: str = "-"):
        async with self._lock:
            # Persist to append-only SQLite hash chain
            persisted = append_audit_log(level, tag, message, source_ip)
            log_entry = {
                "id": persisted["id"],
                "timestamp": persisted["timestamp"],
                "level": level,
                "tag": tag,
                "message": message,
                "source_ip": source_ip,
                "entry_hash": persisted["entry_hash"][:16] + "..."
            }
            self.event_logs.append(log_entry)
        await self.broadcast()

    async def set_status(self, status: str):
        self.system_status = status
        await self.broadcast()

    async def update_dossier(self, updates: Dict[str, Any]):
        self.adversary_dossier.update(updates)
        await self.broadcast()

    async def set_tarpit(self, active: bool):
        self.tarpit_active = active
        if not active:
            self.locked_threads = 0
            self.metrics["locked_threads"] = 0
        await self.broadcast()

    async def register_threat_actor(self, ip: str, vector: str, severity: str = "CRITICAL", fingerprint: str = "-", unit: str = "GARNISUN-KODAM", notes: str = "-"):
        if not ip or ip in ["-", "127.0.0.1", "localhost", "testclient"]:
            return
        async with self._lock:
            # Check if exists
            for item in self.blacklist_feed:
                if item["ip"] == ip:
                    item["threat_vector"] = vector
                    item["status"] = "ISOLATED" if ip in self.isolated_hosts else "BLOCKED"
                    item["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    if fingerprint != "-":
                        item["fingerprint"] = fingerprint
                    save_blacklist_actor(item)
                    await self.broadcast()
                    return
            
            is_internal = ip.startswith(("192.168.", "10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.2", "172.3"))
            classification = "INTERNAL_INSIDER" if is_internal else "EXTERNAL_SPIONAGE"
            ioc_id = f"IOC-PUSSIBERAD-{len(self.blacklist_feed) + 1:03d}"
            
            entry = {
                "ioc_id": ioc_id,
                "ip": ip,
                "classification": classification,
                "threat_vector": vector,
                "severity": severity,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": "ISOLATED" if ip in self.isolated_hosts else "BLOCKED",
                "fingerprint": fingerprint,
                "unit_target": unit,
                "notes": notes
            }
            self.blacklist_feed.append(entry)
            save_blacklist_actor(entry)
        await self.broadcast()

    async def increment_thread_lock(self, count: int = 1):
        self.locked_threads += count
        self.metrics["locked_threads"] = self.locked_threads
        await self.broadcast()

telemetry = TelemetryManager()
