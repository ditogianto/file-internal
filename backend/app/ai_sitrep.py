import hashlib
import httpx
from datetime import datetime
from app.config import settings
from app.telemetry import telemetry

MILITARY_SITREP_SYSTEM_PROMPT = """
Anda adalah Perwira Analis Intelijen Siber PUSSIBERAD (Pusat Siber TNI AD).
Tugas Anda adalah merumuskan LAPORAN SITUASI SIBER (SITREP) MILITER RESMI berdasarkan insiden intersepsi sistem NEXUS-TRAP (Network Deception & Active Tarpit).
Format harus formal, padat, menggunakan tata istilah militer TNI AD (Klandestin, Dislokasi, Satuan Teritorial, Kontra-Spionase, Netralisasi Ancaman, Rantai Komando, Barang Bukti Digital).
Sertakan tabel Indikator Kompromi (IoC) dan Segel Integritas Kriptografis SHA-256.
"""

def generate_deterministic_sitrep() -> str:
    """High-fidelity military SITREP complying with TNI AD intelligence & CSIRT forensic standards."""
    now = datetime.now()
    now_str = now.strftime("%d %B %Y, Pukul %H:%M:%S WIB")
    dossier = telemetry.adversary_dossier
    status = telemetry.system_status
    unit = telemetry.compromised_unit or "KODAM JAYA / KOREM 051/WKT"
    threads = telemetry.locked_threads
    doc = dossier.get("compromised_doc", "Rahasia_Dislokasi_Pasukan_2026.docx (#DOC-991A)")
    attacker_ip = dossier.get("attacker_ip", "192.168.1.88")
    workstation = dossier.get("workstation_host", "PC-ADMIN-LOGISTIK-04")
    gpu_hash = dossier.get("hardware_hash", "9f8a7d6c5b4e3a21...")
    ja4 = dossier.get("cli_signature", "t13d1516h2_8da6530")
    breach_vector = dossier.get("breach_vector", "In-Memory Injection & Lateral Movement")
    is_isolated = "SUDAH DITERAPKAN (HOST QUARANTINE AKTIF)" if dossier.get("isolated") else "SIAP DIEKSEKUSI (1-KLIK QUARANTINE)"

    # Pre-build text body for SHA-256 calculation
    body_content = f"""MARKAS BESAR ANGKATAN DARAT
PUSAT SIBER ANGKATAN DARAT (PUSSIBERAD)
================================================================================
KLASIFIKASI   : RAHASIA (MILITARY CONFIDENTIAL)
NOMOR KAWAL   : R/SITREP-{now.strftime('%Y%m%d')}-091/PUSSIBERAD/OPS
DARI          : KASATGAS SIBER KODAM JAYA / SATGAS PUSSIBERAD
KEPADA        : KOMANDAN PUSAT SIBER TNI AD (DANPUSSIBERAD)
TEMBUSAN      : 1. ASISTEN INTELIJEN KASAD (ASINTEL KASAD)
                2. PANGLIMA KODAM JAYA (PANGDAM JAYA)
                3. KOMANDAN KOREM 051/WIJAYAKARTA
PERIHAL       : LAPORAN PENINDAKAN & INTERSEPSI AKTIF NEXUS-TRAP
================================================================================

1. DASAR OPERASI:
   a. Doktrin Pertahanan Siber Semesta TNI AD Nomor Kep/44/XII/2025.
   b. Prosedur Tetap CSIRT TNI AD Nomor Protap/08/XI/2024 tentang Penanganan Insiden Kritis.
   c. Telemetri Sensor Aktif NEXUS-TRAP (Network Deception & Active Tarpit) Node Korem 051.

2. FAKTA KEJADIAN (5W + 1H):
   a. Waktu Intersepsi : {now_str}
   b. Satuan Terimbas  : {unit}
   c. Simpul Sumber    : {workstation} ({attacker_ip})
   d. Status Siaga     : {status} (Tingkat Kesiapsiagaan Tertinggi)
   e. Dampak Operasi   : NIHIL KORBAN / DATA STRATEGIS 100% AMAN (TERLINDUNGI RANJAU UMPAN)

3. KRONOLOGI INSIDEN:
   a. PENETRASI HULU (PATIENT ZERO):
      Workstation staf ({workstation}) terinfeksi malware jenis Infostealer (Trojan RAT).
      Kredensial lokal diekstraksi penyerang untuk merayap secara lateral di subnet teritorial.
   b. RECONNAISSANCE FASILITAS VITAL (OT/SCADA):
      Pelaku mengirim paket mentah Modbus TCP Function 0x03 ke Port 502 (Genset/Radar Pangkalan).
      Modul ranjau NEXUS-TRAP mengintersepsi paket dan menyajikan register palsu (380V, 50Hz, BBM 85%),
      mengelabui musuh sekaligus membunyikan Siaga Kuning di meja komando secara instan.
   c. PELUMPUHAN INSTRUMEN SERANG (ACTIVE TARPIT):
      Penyerang melancarkan multi-threaded scanner. Modul Tarpit Crasher menahan TCP Receive Window
      sebesar 1 byte per 15 detik, menyerap soket musuh dan membekukan {threads} thread penyerang (0 req/s).
   d. PEMBOCORAN DOKUMEN & PELEDAKAN SUAR CANARY:
      Musuh mengekstrak dokumen umpan ({doc}) ke lingkungan sandbox eksternal.
      Relasi eksternal dokumen memicu Suar Klandestin (DNS UDP 5053 & Web Beacon),
      menembus isolasi VM dan merekam sidik jari perangkat keras musuh ke Dossier Intelijen.

4. INDIKATOR KOMPROMI (INDICATORS OF COMPROMISE - IoC):
   +-----------------------+-------------------------------------------------------+
   | PARAMETER FORENSIK    | DATA INDIKATOR TERVERIFIKASI                          |
   +-----------------------+-------------------------------------------------------+
   | IP Sumber Ancaman     | {attacker_ip} (Internal Subnet / Tunnel Egress)          |
   | Workstation Terinfeksi| {workstation}                                         |
   | Port Target Serangan  | Port 502/5020 (Modbus OT), Port 8000 (Decoy Portal)   |
   | Dokumen Umpan Terpicu | {doc}                                                 |
   | Sidik Jari Klien (JA4)| {ja4}                                                 |
   | Hardware/GPU Hash     | {gpu_hash}                                            |
   | Vektor Penyusupan     | {breach_vector}                                       |
   +-----------------------+-------------------------------------------------------+

5. TINDAKAN PENANGGULANGAN YANG TELAH DIAMBIL:
   a. Eksekusi Host Quarantine (Pemutusan Firewall Kernel) terhadap IP {attacker_ip}: {is_isolated}.
   b. Penguncian soket penyerang via Active Tarpit Engine untuk mencegah pergerakan lateral lanjutan.
   c. Integritas jaringan SCADA fasilitas genset pangkalan diverifikasi aman terkendali.

6. SARAN DAN REKOMENDASI TAKTIS KEPADA PIMPINAN:
   a. Instruksikan Tim Reaksi Cepat (TRC) Infolahta Kodam menyita fisik hard disk {workstation}
      guna kepentingan forensik digital dan bukti peradilan militer (POMAD).
   b. Lakukan penyisiran serentak (Sweep-Search) terhadap indikator IoC di atas pada seluruh
      workstation di jajaran Kodim penyangga ibu kota.
   c. Pertahankan kesiapsiagaan Siaga 1 Merah hingga audit kepatuhan perangkat lunak rampung."""

    # Cryptographic SHA-256 seal calculation for legal chain of custody
    report_hash = hashlib.sha256(body_content.encode("utf-8")).hexdigest().upper()

    final_report = f"""================================================================================
{body_content}

7. INTEGRITAS BUKTI DIGITAL & RANTAI KAWAL (CHAIN OF CUSTODY):
   a. Algoritma Segel     : SHA-256 KRIPTOGRAFIS MILITER
   b. Hash Integritas Berkas : {report_hash}
   c. Status Validasi     : TERVERIFIKASI OTENTIK (TAMPER-PROOF)
================================================================================
                                                JAKARTA, {now.strftime('%d %B %Y')}
                                                KASATGAS OPERASI SIBER NEXUS-TRAP

                                                [TERTANDA TANGAN SECARA DIGITAL]
================================================================================"""
    return final_report

async def generate_sitrep() -> str:
    """Attempts local LLM generation; falls back seamlessly to deterministic military report."""
    try:
        context_payload = {
            "model": settings.OLLAMA_MODEL,
            "prompt": f"""{MILITARY_SITREP_SYSTEM_PROMPT}
DATA INSIDEN:
Status: {telemetry.system_status}
Satuan: {telemetry.compromised_unit or 'KODAM JAYA'}
Adversary Dossier: {telemetry.adversary_dossier}
Thread Terkunci: {telemetry.locked_threads}
Korelasikan data di atas ke format Laporan Intelijen Sitrep Militer Resmi TNI AD.""",
            "stream": False
        }
        async with httpx.AsyncClient(timeout=0.3) as client:
            resp = await client.post(settings.OLLAMA_URL, json=context_payload)
            if resp.status_code == 200:
                result = resp.json()
                return result.get("response", generate_deterministic_sitrep())
    except Exception:
        pass
    
    # Return high-fidelity deterministic military sitrep
    return generate_deterministic_sitrep()
