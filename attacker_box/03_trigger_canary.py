import socket
import sys

DNS_SERVER = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
DNS_PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 5053  # Dev port (53 in root/Docker)
CANARY_QUERY = "doc-991a.kodam-jaya.canary.nexustrap.mil.id"

print("=" * 65)
print(f"[*] SIMULASI PENYERANG: MEMBUKA DOKUMEN RAHASIA DI MESIN VM")
print(f"[*] Berkas: Rahasia_Dislokasi_Pasukan_2026.docx")
print(f"[*] Host resolver memicu kueri DNS klandestin ke {DNS_SERVER}:{DNS_PORT}...")
print("=" * 65)

# Build standard DNS query packet manually without external libraries
def build_dns_query(domain: str) -> bytes:
    header = b"\x13\x37\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00"
    qname = b""
    for part in domain.split("."):
        qname += bytes([len(part)]) + part.encode("ascii")
    qname += b"\x00"
    qtype = b"\x00\x01"   # Type A
    qclass = b"\x00\x01"  # Class IN
    return header + qname + qtype + qclass

try:
    packet = build_dns_query(CANARY_QUERY)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2.0)
    sock.sendto(packet, (DNS_SERVER, DNS_PORT))
    print(f"[>] Paket DNS Query terkirim: '{CANARY_QUERY}' ke {DNS_SERVER}:{DNS_PORT}")
    try:
        data, addr = sock.recvfrom(512)
        print(f"[+] Balasan DNS diterima dari {addr} ({len(data)} bytes).")
    except Exception:
        # Fallback to HTTP Web Beacon (Dual-Spectrum Canary)
        import urllib.request
        beacon_url = f"http://{DNS_SERVER}:8000/api/canary/beacon/DOC-991A"
        urllib.request.urlopen(beacon_url, timeout=2.0)
        print(f"[+] Suar Web Beacon HTTP terpicu: {beacon_url}")
    print(f"[!] SUAR TELAH DITERIMA PUSAT KOMANDO NEXUS-TRAP!")
except Exception as e:
    print(f"[-] Terjadi kesalahan: {e}. Pastikan listener aktif.")
