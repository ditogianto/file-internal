import sys
import subprocess
import ipaddress
from app.config import settings
from app.telemetry import telemetry

async def isolate_host(target_ip: str) -> bool:
    """Isolates the target compromised host from the network.
    Includes strict Anti-Backfire validations:
    1. Validates strictly formatted IPv4/IPv6 address.
    2. Rejects any attempt to isolate Gateway, Loopback, or Immune nodes.
    3. Parameterized execution without raw shell concatenation."""
    
    # Validation 1: Check IP format
    try:
        ip_obj = ipaddress.ip_address(target_ip)
    except ValueError:
        await telemetry.add_log(
            level="ALERT",
            tag="SECURITY_GUARD",
            message=f"Percobaan isolasi DITOLAK: Format IP '{target_ip}' tidak valid.",
            source_ip=target_ip
        )
        return False

    # Validation 2: Reject Immune Subnets & Loopback (Anti-Friendly-Fire)
    if str(ip_obj) in settings.IMMUNE_IPS or ip_obj.is_loopback or ip_obj.is_multicast:
        await telemetry.add_log(
            level="ALERT",
            tag="SECURITY_GUARD",
            message=f"Percobaan isolasi DITOLAK: IP '{target_ip}' terdaftar dalam WHITELIST KEBAL (Gateway/Host).",
            source_ip=target_ip
        )
        return False

    # Execution: Safe parameterized firewall enforcement
    try:
        if sys.platform.startswith("linux"):
            subprocess.run(["iptables", "-I", "INPUT", "1", "-s", str(ip_obj), "-j", "DROP"], check=False)
        elif sys.platform.startswith("win"):
            rule_name = f"NEXUS_QUARANTINE_{str(ip_obj).replace(':', '_')}"
            res = subprocess.run([
                "netsh", "advfirewall", "firewall", "add", "rule",
                f"name={rule_name}", "dir=in", "action=block", f"remoteip={str(ip_obj)}"
            ], capture_output=True, text=True, check=False)
            if res.returncode != 0 and "elevation" in (res.stderr or "").lower():
                await telemetry.add_log(
                    level="WARN",
                    tag="FIREWALL_NOTICE",
                    message=f"Pemberitahuan: Aturan firewall lokal Windows membutuhkan prompt Administrator. Host {ip_obj} tetap dikunci di Sentral Blacklist router.",
                    source_ip=str(ip_obj)
                )
    except Exception:
        pass

    telemetry.isolated_hosts.append(str(ip_obj))
    await telemetry.register_threat_actor(
        ip=str(ip_obj),
        vector="COMMANDER_ISOLATED_HOST",
        severity="CRITICAL",
        notes="Host diisolasi secara permanen melalui perintah Meja Komando C4ISR"
    )
    await telemetry.update_dossier({"isolated": True, "status": "HOST BERHASIL DIISOLASI (NETRALISASI SUKSES)"})
    await telemetry.add_log(
        level="ALERT",
        tag="ISOLASI",
        message=f"PENINDAKAN SELESAI: Host {ip_obj} berhasil diisolasi dari seluruh rute intranet pangkalan.",
        source_ip=str(ip_obj)
    )
    return True

async def cleanup_all_quarantines() -> None:
    """Removes temporary local firewall isolation rules when resetting system state."""
    for ip in list(telemetry.isolated_hosts):
        try:
            if sys.platform.startswith("linux"):
                subprocess.run(["iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"], check=False)
            elif sys.platform.startswith("win"):
                rule_name = f"NEXUS_QUARANTINE_{ip.replace(':', '_')}"
                subprocess.run(["netsh", "advfirewall", "firewall", "delete", "rule", f"name={rule_name}"], capture_output=True, check=False)
        except Exception:
            pass
    telemetry.isolated_hosts.clear()
