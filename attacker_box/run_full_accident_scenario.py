import time
import socket
import urllib.request
import json
import sys

BACKEND_URL = "http://127.0.0.1:8000"
MODBUS_HOST = "127.0.0.1"
MODBUS_PORT = 5020
DNS_PORT = 5053

def print_step(title, desc):
    print("\n" + "=" * 70)
    print(f"[*] {title.upper()}")
    print(f"    -> {desc}")
    print("=" * 70)
    time.sleep(1.5)

def main():
    print("""
    ====================================================================
      SIMULASI ANATOMI INSIDEN NYATA: OPERASI KONTRA-SPIONASE KODIM 0501
      Platform: NEXUS-TRAP (Network Deception & Active Tarpit)
    ====================================================================
    """)
    time.sleep(1)

    # STEP 1: HULU INSIDEN
    print_step("FASE 1: HULU INSIDEN (INFEKSI MALWARE INFOSTEALER)",
               "Komputer Staf Logistik Korem 051 (PC-ADMIN-LOGISTIK-04) terinfeksi\n"
               "       malware Stealc akibat pengunduhan file APK ilegal.\n"
               "       Peretas mendapatkan akses remote shell ke subnet 192.168.1.0/24.")
    time.sleep(2)

    # STEP 2: PENGINTAIAN MODBUS OT
    print_step("FASE 2: RECONNAISSANCE FASILITAS GENSET (PORT 502/5020)",
               "Peretas memindai port industri untuk mencari celah sabotase listrik markas.")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3.0)
        s.connect((MODBUS_HOST, MODBUS_PORT))
        # Function 0x03 read holding registers
        s.sendall(b"\x00\x01\x00\x00\x00\x06\x01\x03\x00\x00\x00\x03")
        resp = s.recv(1024)
        s.close()
        print(f"    [+] Respon Modbus Berhasil Ditangkap: PLC Genset 380V / 50Hz / BBM 85%")
        print(f"    [!] REAKSI DASHBOARD: SIAGA KUNING (BLIP RADAR MENYALA!)")
    except Exception as e:
        print(f"    [-] Gagal terhubung: {e}")
    time.sleep(3)

    # STEP 3: TARPIT CRASHER MEMBEKUKAN SCANNER
    print_step("FASE 3: SERANGAN BRUTE-FORCE WEB & PELUMPUHAN TARPIT",
               "Peretas meluncurkan scanner otomatis ke portal internal pangkalan.\n"
               "       Operator Komando menekan [AKTIFKAN TARPIT CRASHER].")
    
    # Toggle Tarpit on backend
    try:
        req = urllib.request.Request(
            f"{BACKEND_URL}/api/tarpit/toggle",
            data=b'{"active": true}',
            headers={"Content-Type": "application/json", "X-C4ISR-Auth": "PUSSIBERAD-C4ISR-COMMAND-KEY"}
        )
        urllib.request.urlopen(req)
        print("    [OK] Tarpit Crasher AKTIF di Pusat Komando.")
        
        # Scanner thread probe
        print("    [>] Meluncurkan worker scanner Gobuster...")
        probe_req = urllib.request.Request(
            f"{BACKEND_URL}/decoy-portal",
            headers={"User-Agent": "Gobuster/v3.5 (Scanning Worker)"}
        )
        try:
            with urllib.request.urlopen(probe_req, timeout=1.5) as resp:
                resp.read(16)
        except Exception:
            # Expected slow-drip timeout
            pass
        print("    [!] REAKSI TERMINAL: Pemindai musuh MACET (< 0.5 req/s slow-drip timeout)!")
        print("    [!] REAKSI DASHBOARD: Thread Lawan Terkunci bertambah, Signature JA4 tercatat!")
    except Exception as e:
        print(f"    [-] Tarpit phase note: {e}")
    time.sleep(3)

    # STEP 4: PENCURIAN DOKUMEN & SUAR DNS CANARY TEMBUS VM
    print_step("FASE 4: PENCURIAN DOKUMEN & PEMBONGKARAN ISOLASI VM",
               "Peretas menyalin 'Rahasia_Dislokasi_Pasukan_2026.docx' ke VirtualBox terisolasi.\n"
               "       Saat dokumen dibuka, suar DNS klandestin menembus keluar jaringan isolasi!")
    
    try:
        # Build DNS query packet
        header = b"\x13\x37\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00"
        qname = b"\x08doc-991a\x0akodam-jaya\x06canary\x09nexustrap\x03mil\x02id\x00"
        packet = header + qname + b"\x00\x01\x00\x01"
        dns_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dns_sock.settimeout(2.0)
        dns_sock.sendto(packet, ("127.0.0.1", DNS_PORT))
        dns_sock.recvfrom(512)
        dns_sock.close()
        print("    [+] Suar UDP 5053 Berhasil Menembus Keluar Mesin Virtual.")
        print("    [!] REAKSI DASHBOARD: SIAGA 1 (MERAH) MELEDAK! Peta Kodam Jaya Berkedip Merah!")
        print("    [!] Profil Buronan, Workstation, GPU Hash & Rute Terbongkar 100%!")
    except Exception as e:
        print(f"    [-] DNS Canary phase note: {e}")
    time.sleep(3)

    # STEP 5: ISOLASI 1-KLIK
    print_step("FASE 5: PENINDAKAN 1-KLIK & KARANTINA HOST",
               "Komandan Pussiberad menekan tombol [ISOLASI HOST TERINFEKSI].\n"
               "       Rute komunikasi komputer penyusup langsung diputus total.")
    try:
        iso_req = urllib.request.Request(
            f"{BACKEND_URL}/api/isolate",
            data=b'{"ip": "192.168.1.88"}',
            headers={"Content-Type": "application/json", "X-C4ISR-Auth": "PUSSIBERAD-C4ISR-COMMAND-KEY"}
        )
        urllib.request.urlopen(iso_req)
        print("    [OK] Host 192.168.1.88 Diisolasi.")
        print("    [!] Aturan isolasi aktif di kernel firewall, koneksi penyerang ke pangkalan terputus!")
    except Exception as e:
        print(f"    [-] Host Isolation phase note: {e}")
    time.sleep(2)

    # STEP 6: AI SITREP MILITER
    print_step("FASE 6: GENERATE AI MILITARY SITREP",
               "Sistem secara otonom merumuskan Berita Militer Resmi siap kirim ke Kasad.")
    try:
        sitrep_req = urllib.request.Request(
            f"{BACKEND_URL}/api/sitrep/generate",
            data=b"",
            headers={"X-C4ISR-Auth": "PUSSIBERAD-C4ISR-COMMAND-KEY"}
        )
        sitrep_resp = urllib.request.urlopen(sitrep_req)
        data = json.loads(sitrep_resp.read().decode())
        print(f"    [+] Dokumen Laporan Situasi Militer Resmi Berhasil Digenerate!")
        print(f"    [+] Segel Keabsahan: SHA-256 Terverifikasi ({data.get('sha256', '')[:16]}...).")
    except Exception as e:
        print(f"    [-] Sitrep phase note: {e}")

    print("\n" + "=" * 70)
    print(" [SUKSES] SIMULASI SELESAI DENGAN KEMENANGAN MUTLAK (PERTAHANAN BERHASIL)")
    print("====================================================================")

if __name__ == "__main__":
    main()
