import socket
import sys

DNS_SERVER = "127.0.0.1"
DNS_PORT = 5053  # Dev port (53 in root/Docker)
CANARY_QUERY = "doc-991a.kodam-jaya.canary.nexustrap.mil.id"

print("=" * 65)
print(f"[*] SIMULASI PENYERANG: MEMBUKA DOKUMEN RAHASIAN CURselected DI MESIN VM")
print(f"[*] Berkas: Rahasia_Dislokasi_Pasukan_2026.docx")
print(f"[*] Host resolver memicu kueri DNS klandestin ke DNS Port {DNS_PORT}...")
print("=" * 65)

# Build standard DNS query packet manually without external libraries
def build_dns_query(domain: str) -> bytes:
    # Transaction ID (0x1337), Flags: standard query (0x0100), QDCOUNT: 1
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
    sock.settimeout(3.0)
    sock.sendto(packet, (DNS_SERVER, DNS_PORT))
    print(f"[>] Paket DNS Query terkirim: '{CANARY_QUERY}' ke {DNS_SERVER}:{DNS_PORT}")
    data, addr = sock.recvfrom(512)
    print(f"[+] Balasan DNS diterima dari {addr} ({len(data)} bytes).")
    print(f"[!] SUAR TELAH DITERIMA PUSAT KOMANDO NEXUS-TRAP!")
except Exception as e:
    print(f"[-] Terjadi kesalahan: {e}. Pastikan listener aktif.")
