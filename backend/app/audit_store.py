"""
NEXUS-TRAP // PUSSIBERAD TNI AD
Cryptographic Audit Trail & Append-Only Legal Evidence Store (POMAD Standard)

Fitur:
1. SQLite Local Persistent Storage (Tidak hilang saat server restart).
2. Hash Chaining Kriptografis (prev_hash -> entry_hash) berbasis SHA-256.
3. Otentikasi Integritas Asli berbasis HMAC-SHA256 menggunakan secret key militer.
4. Verifikasi Chain-of-Custody mandiri untuk kebutuhan barang bukti persidangan POMAD.
"""

import os
import sqlite3
import hashlib
import hmac
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "nexus_audit.db"))
HMAC_SECRET = os.getenv("C4ISR_AUDIT_HMAC_KEY", "PUSSIBERAD-MILITARY-CHAIN-OF-CUSTODY-KEY-2026").encode("utf-8")
GENESIS_HASH = "0000000000000000000000000000000000000000000000000000000000000000"

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, timeout=30.0)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes tables for persistent cryptographic audit trail."""
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # 1. Append-Only Hash-Chained Audit Logs
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS audit_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                level TEXT NOT NULL,
                tag TEXT NOT NULL,
                message TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                prev_hash TEXT NOT NULL,
                entry_hash TEXT NOT NULL,
                hmac_signature TEXT NOT NULL
            )
        """)
        
        # 2. Sentral Blacklist Persistent Records
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS blacklist_records (
                ioc_id TEXT PRIMARY KEY,
                ip TEXT NOT NULL,
                classification TEXT NOT NULL,
                threat_vector TEXT NOT NULL,
                severity TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                status TEXT NOT NULL,
                fingerprint TEXT,
                unit_target TEXT,
                notes TEXT
            )
        """)
        
        # 3. Dynamic Canary Token Registry (Tracking unique document downloads)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS canary_tokens (
                token TEXT PRIMARY KEY,
                created_at TEXT NOT NULL,
                issued_to_ip TEXT NOT NULL,
                doc_name TEXT NOT NULL,
                triggered INTEGER DEFAULT 0,
                triggered_at TEXT,
                trigger_ip TEXT,
                trigger_ua TEXT
            )
        """)
        conn.commit()

def get_last_entry_hash() -> str:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT entry_hash FROM audit_logs ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        if row and row["entry_hash"]:
            return row["entry_hash"]
        return GENESIS_HASH

def append_audit_log(level: str, tag: str, message: str, source_ip: str = "-") -> Dict[str, Any]:
    """Appends an immutable entry to the cryptographic hash chain."""
    prev_hash = get_last_entry_hash()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_short = datetime.now().strftime("%H:%M:%S")
    
    # Calculate SHA-256 Hash of this block linked to previous hash
    raw_payload = f"{prev_hash}|{timestamp}|{level}|{tag}|{message}|{source_ip}".encode("utf-8")
    entry_hash = hashlib.sha256(raw_payload).hexdigest().upper()
    
    # Calculate HMAC-SHA256 signature proving authenticity from PUSSIBERAD node
    hmac_signature = hmac.new(HMAC_SECRET, entry_hash.encode("utf-8"), hashlib.sha256).hexdigest().upper()
    
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO audit_logs (timestamp, level, tag, message, source_ip, prev_hash, entry_hash, hmac_signature)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (timestamp, level, tag, message, source_ip, prev_hash, entry_hash, hmac_signature))
        conn.commit()
        entry_id = cursor.lastrowid

    return {
        "id": entry_id,
        "timestamp": time_short,
        "full_timestamp": timestamp,
        "level": level,
        "tag": tag,
        "message": message,
        "source_ip": source_ip,
        "entry_hash": entry_hash,
        "prev_hash": prev_hash,
        "hmac_signature": hmac_signature
    }

def get_recent_logs(limit: int = 50) -> List[Dict[str, Any]]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM audit_logs ORDER BY id DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        result = []
        for r in reversed(rows):
            # Parse short time for UI display
            raw_ts = r["timestamp"]
            short_ts = raw_ts.split(" ")[1] if " " in raw_ts else raw_ts
            result.append({
                "id": r["id"],
                "timestamp": short_ts,
                "full_timestamp": raw_ts,
                "level": r["level"],
                "tag": r["tag"],
                "message": r["message"],
                "source_ip": r["source_ip"],
                "entry_hash": r["entry_hash"]
            })
        return result

def save_blacklist_actor(entry: Dict[str, Any]):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO blacklist_records (ioc_id, ip, classification, threat_vector, severity, timestamp, status, fingerprint, unit_target, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(ioc_id) DO UPDATE SET
                threat_vector=excluded.threat_vector,
                severity=excluded.severity,
                timestamp=excluded.timestamp,
                status=excluded.status,
                fingerprint=excluded.fingerprint,
                notes=excluded.notes
        """, (
            entry.get("ioc_id"),
            entry.get("ip"),
            entry.get("classification", "EXTERNAL_SPIONAGE"),
            entry.get("threat_vector", "UNKNOWN"),
            entry.get("severity", "HIGH"),
            entry.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            entry.get("status", "BLOCKED"),
            entry.get("fingerprint", "-"),
            entry.get("unit_target", "PUSSIBERAD-GATEWAY"),
            entry.get("notes", "-")
        ))
        conn.commit()

def load_blacklist_feed() -> List[Dict[str, Any]]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM blacklist_records ORDER BY timestamp DESC")
        rows = cursor.fetchall()
        return [dict(r) for r in rows]

def register_canary_token(token: str, issued_to_ip: str, doc_name: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO canary_tokens (token, created_at, issued_to_ip, doc_name)
            VALUES (?, ?, ?, ?)
        """, (token, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), issued_to_ip, doc_name))
        conn.commit()

def mark_canary_triggered(token: str, trigger_ip: str, user_agent: str) -> Optional[Dict[str, Any]]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM canary_tokens WHERE token = ?", (token,))
        row = cursor.fetchone()
        
        cursor.execute("""
            UPDATE canary_tokens
            SET triggered = triggered + 1,
                triggered_at = ?,
                trigger_ip = ?,
                trigger_ua = ?
            WHERE token = ?
        """, (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), trigger_ip, user_agent[:64], token))
        conn.commit()
        return dict(row) if row else None

def verify_audit_chain_integrity() -> Tuple[bool, int, str]:
    """
    Verifies that no log records have been altered, deleted, or inserted out of order.
    Returns: (is_valid, verified_count, diagnostic_message)
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM audit_logs ORDER BY id ASC")
        rows = cursor.fetchall()
        
        if not rows:
            return True, 0, "Audit trail is empty (Genesis state)."
            
        expected_prev = GENESIS_HASH
        for idx, row in enumerate(rows):
            if row["prev_hash"] != expected_prev:
                return False, idx, f"Chain broken at record #{row['id']}: prev_hash does not match preceding block!"
                
            raw_payload = f"{row['prev_hash']}|{row['timestamp']}|{row['level']}|{row['tag']}|{row['message']}|{row['source_ip']}".encode("utf-8")
            recalc_hash = hashlib.sha256(raw_payload).hexdigest().upper()
            if recalc_hash != row["entry_hash"]:
                return False, idx, f"Payload tampering detected at record #{row['id']}: recalculated hash mismatch!"
                
            # Verify HMAC
            expected_hmac = hmac.new(HMAC_SECRET, recalc_hash.encode("utf-8"), hashlib.sha256).hexdigest().upper()
            if expected_hmac != row["hmac_signature"]:
                return False, idx, f"Signature forgery detected at record #{row['id']}: HMAC verification failed!"
                
            expected_prev = row["entry_hash"]
            
        return True, len(rows), f"All {len(rows)} audit records cryptographically verified with zero tampering."
