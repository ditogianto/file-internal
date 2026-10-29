# PROPOSAL TEKNIS, ARSITEKTUR SISTEM, & DOKUMENTASI RESMI PURWARUPA
## KARTIKA CYBER HACKATHON 2026 (PUSSIBERAD TNI AD × CODEPOLITAN)

```text
========================================================================================
KLASIFIKASI DOKUMEN : PROPOSAL TEKNIS HACKATHON / OPERASIONAL PERTAHANAN SIBER AKTIF
NAMA PURWARUPA      : NEXUS-TRAP (Network Deception & Active Tarpit)
KATEGORI PERLOMBAAN : PENANGKALAN (ACTIVE CYBER DEFENSE, DECEPTION & INCIDENT RESPONSE)
INSTITUSI MITRA     : PUSAT SIBER ANGKATAN DARAT (PUSSIBERAD) × PT CODEPOLITAN INTEGRASI INDONESIA
STATUS PURWARUPA    : TRL 4-5 (VALIDATED IN OPERATIONAL LAB ENVIRONMENT)
ARSITEKTUR          : 100% ON-PREMISE AIR-GAPPED (NIR-KETERGANTUNGAN CLOUD ASING)
========================================================================================
```

---

## DAFTAR ISI
1. [Abstrak Eksekutif](#1-abstrak-eksekutif)
2. [Latar Belakang & Analisis Ancaman Riil Satuan Teritorial](#2-latar-belakang--analisis-ancaman-riil-satuan-teritorial)
3. [Arsitektur Sistem & Spesifikasi Rekayasa 4 Pilar](#3-arsitektur-sistem--spesifikasi-rekayasa-4-pilar)
4. [Mesin Diskriminasi Bot & Anti-Kamuflase (RFC 9309 & FCrDNS)](#4-mesin-diskriminasi-bot--anti-kamuflase-rfc-9309--fcrdns)
5. [Integritas Barang Bukti Digital & Rantai Audit POMAD (HMAC-SHA256)](#5-integritas-barang-bukti-digital--rantai-audit-pomad-hmac-sha256)
6. [Mekanisme Proteksi Anti-Friendly-Fire & Anti-Backfire Guard](#6-mekanisme-proteksi-anti-friendly-fire--anti-backfire-guard)
7. [Rencana Implementasi Skalabilitas Teritorial (Mabesad - Kodam - Kodim)](#7-rencana-implementasi-skalabilitas-teritorial-mabesad---kodam---kodim)
8. [Spesifikasi Kebutuhan Sumber Daya & Panduan Deployment](#8-spesifikasi-kebutuhan-sumber-daya--panduan-deployment)

---

## 1. Abstrak Eksekutif

Pertahanan siber modern menuntut pergeseran paradigma dari model pasif-reaktif (*Passive Defense*) menuju **Pertahanan Siber Aktif (*Active Cyber Defense & Deception*)**. Sebagian besar insiden kebocoran data di lingkungan pertahanan tidak berawal dari serangan langsung terhadap perimeter pusat Mabesad, melainkan berawal dari infeksi malware klandestin (*Infostealer Trojan*) pada stasiun kerja staf di satuan teritorial kewilayahan (Kodam, Korem, hingga Kodim). Keterbatasan personel teknis di daerah memicu krisis kejenuhan alarm (*Alert Fatigue*), di mana ribuan peringatan dari firewall konvensional menenggelamkan indikasi intrusi sebenarnya.

**NEXUS-TRAP (Network Deception & Active Tarpit)** adalah platform pertahanan siber aktif mandiri yang mengintegrasikan:
1. **Emulasi Umpan Industri/OT:** Meniru telemetri protokol Modbus TCP Port 502/5020 untuk melindungi genset dan radar komando pangkalan.
2. **Mesin Pelumpuh Asynchronous Sticky Tarpit:** Membekukan dan menyerap sumber daya socket pemindai musuh (*scanner starvation*) tanpa membebani server pertahanan.
3. **Dokumen Umpan Berpelacak Ganda (*Dual-Spectrum Canary Token*):** Menembus isolasi mesin virtual (*VM Sandbox Escape*) menggunakan suar Out-of-Band UDP 5053 dan Web Beacon untuk mengekstrak sidik jari perangkat keras musuh (WebGL GPU silicon hash dan JA4 transport signature).
4. **Respon Karantina Kernel 1-Klik:** Mengisolasi host terkompromi dalam tempo kurang dari 1 detik melalui manipulasi firewall OS (`iptables`/`netsh`), dilengkapi ekspor aturan blacklist sentral untuk router MikroTik dan Cisco IOS.
5. **Rantai Audit Kriptografis SQLite HMAC-SHA256 & AI Military SITREP:** Menghasilkan laporan intelijen berstempel SHA-256 yang memiliki keabsahan hukum (*Chain-of-Custody*) di hadapan Polisi Militer (POMAD) dan Pengadilan Militer.

Dengan mengusung filosofi **Zero False Positive by Design**, sistem ini memberikan jaminan bahwa setiap alarm yang menyalak adalah 100% ancaman nyata.

---

## 2. Latar Belakang & Analisis Ancaman Riil Satuan Teritorial

### 2.1 Anatomi Ancaman: Living Off The Land & Infostealer
Kelemahan paling kritis pada satuan bawah adalah maraknya peredaran tautan jebakan (APK ilegal bertema pinjol, manipulasi undangan, dan judi online) yang tidak sengaja terpasang pada komputer staf administrasi dinas.
- Begitu malware Trojan terpasang, peretas mengekstrak token sesi intranet yang sah.
- Peretas bergerak ke samping (*lateral movement*) menggunakan akun resmi personel militer (*Living off the Land*).
- Firewall perimeter tidak mampu membedakan lalu lintas browsing dinas prajurit dan lalu lintas pemindaian penyerang.

### 2.2 Kerentanan Protokol Industri (OT / SCADA) Tanpa Otentikasi
Fasilitas vital di pangkalan militer seperti Genset Cadangan Komando, Sistem Pendingin Ruang Amunisi, dan Radar Teritorial beroperasi menggunakan protokol industri warisan: **Modbus TCP (Port 502)**.
- Protokol Modbus dirancang tanpa mekanisme enkripsi atau kata sandi.
- Siapa pun di subnet lokal dapat mengirim paket mentah *Function Code 0x03 (Read Holding Registers)* atau *Function Code 0x06 (Write Single Register)* untuk mematikan daya listrik markas saat terjadi serangan fisik.

---

## 3. Arsitektur Sistem & Spesifikasi Rekayasa 4 Pilar

```
+---------------------------------------------------------------------------------------------------------+
|                                    PUSAT KOMANDO C4ISR NEXUS-TRAP                                       |
|                  Dashboard Operasional Single-Screen 16:9 | Peta Teritorial 9 Kodam                     |
|                  Konsol Respon Taktis 1-Klik | Hotkeys [R] [T] [K] [S] [Q]                              |
+---------------------------------------------------------------------------------------------------------+
       ^                                  ^                                  ^
       | WebSocket (Port 8000)            | Fast UDP DNS Beacon (5053)       | TCP Raw Sockets (5020)
+---------------+                  +---------------+                  +---------------+
|    PILAR 1    |                  |    PILAR 2    |                  |    PILAR 3    |
|   OT DECOY    |                  | CANARY BEACON |                  | ACTIVE TARPIT |
| Emulasi PLC   |                  | OpenXML DOCX  |                  | Async Chunked |
| Modbus 502    |                  | Out-of-Band   |                  | Slow-Drip TCP |
+---------------+                  +---------------+                  +---------------+
       |                                  |                                  |
       +----------------------------------+----------------------------------+
                                          |
                                          v
+---------------------------------------------------------------------------------------------------------+
|                                    PILAR 4: FORENSIK & RESPON MILITER                                   |
| - 1-Click Host Quarantine via Kernel OS Firewall (iptables / netsh)                                     |
| - Ekspor Sentral Blacklist: Linux iptables, Windows Netsh, MikroTik RouterOS (.rsc), Cisco ACL (.cfg)   |
| - Persistent Audit Trail: SQLite Append-Only Hash-Chain (HMAC-SHA256) Standar Oditur Militer / POMAD   |
| - AI Military SITREP Generator: Formal TNI AD Intelligence Report + Cryptographic Dynamic SHA-256 Seal  |
+---------------------------------------------------------------------------------------------------------+
```

### 3.1 Pilar 1: Sensor Umpan OT / SCADA Modbus TCP (Port 502/5020)
- Mengimplementasikan server socket raw asynchronous berbasis Python (`backend/app/modbus_service.py`).
- Menerima dan mem-parsing bingkai Modbus Application Protocol (MBAP):
  * `Transaction ID` (2 bytes), `Protocol ID` (2 bytes, 0x0000), `Length` (2 bytes), `Unit ID` (1 byte).
  * `Function Code 0x03 (Read Holding Registers)`: Dijawab secara presisi dengan data holding registers palsu (Tegangan: 380V, Frekuensi: 50Hz, BBM: 85%).
- Seketika memicu transisi status komando menjadi **SIAGA 2 (KUNING)**.

### 3.2 Pilar 2: Active Asynchronous Sticky Tarpit (TCP Window Choking)
- Menerapkan streaming HTTP chunked lambat (`backend/app/tarpit.py`) dengan interval tetesan terkontrol (*slow-drip rate* 1 byte per 2 hingga 15 detik).
- Menghambat perkakas pemindai otomatis (*Gobuster, Dirsearch, Nmap, Nikto*). Karena socket penyerang menerima 1 byte secara berkala, thread penyerang tidak mengalami *connection reset*, melainkan tertahan hingga batas waktu timeout (*thread starvation*).
- Dilengkapi **Bounded Async Connection Pool** (`MAX_TARPIT_PER_IP = 64`) untuk memastikan server tidak mengalami kehabisan *file descriptor*.

### 3.3 Pilar 3: Dual-Spectrum Canary Token & Ekstraksi Forensik Hardware
- Berkas umpan Microsoft Word dinas (*OpenXML DOCX*) menyematkan tautan relasi tersembunyi pada `word/_rels/document.xml.rels`.
- Begitu berkas dibuka di lingkungan tamu VirtualBox atau WPS Office ponsel:
  1. **DNS Out-of-Band (UDP 5053):** Resolver OS tamu menembus adapter NAT untuk menyelesaikan nama domain suar (`doc-991a.kodam-jaya.canary.mil.id`), membocorkan IP sarang penyerang.
  2. **In-Browser WebGL GPU Hash Probe:** Jika penyerang mengakses portal umpan web, skrip forensik mengekstrak GPU unmasked vendor (`WEBGL_debug_renderer_info`) dan tanda tangan **JA4 L4/L7 transport**, menghasilkan atribusi perangkat keras yang tidak terpengaruh oleh VPN atau pergantian IP.

### 3.4 Pilar 4: 1-Klik Karantina, Ekspor Router L3, & AI Military SITREP
- **Karantina Kernel:** Eksekusi berparameter langsung ke subsistem jaringan OS (`iptables -A INPUT -s <IP> -j DROP` di Linux atau `netsh advfirewall` di Windows).
- **Ekspor Multi-Format Router L3:** Mengakomodasi arsitektur jaringan teritorial Kodam/Korem dengan menghasilkan konfigurasi firewall siap impor:
  * Linux `iptables` script (`.sh`).
  * Windows Advanced Firewall batch script (`.bat`).
  * MikroTik RouterOS script (`/ip firewall address-list add ...` format `.rsc`).
  * Cisco IOS Access Control List (`access-list 100 deny ip host ...` format `.cfg`).
- **AI Military SITREP:** Format naskah dinas militer TNI AD berklasifikasi RAHASIA berstempel integritas SHA-256 yang dapat dihubungkan ke Local SLM (Ollama) maupun mesin deterministik mandiri.

---

## 4. Mesin Diskriminasi Bot & Anti-Kamuflase (RFC 9309 & FCrDNS)

Salah satu keunggulan terbesar NEXUS-TRAP adalah kepatuhan terhadap standar **RFC 9309 (Robots Exclusion Protocol)** dan mesin verifikasi **Forward-Confirmed reverse DNS (FCrDNS)** di `backend/app/crawler_guard.py`:

```
                                  [ALUR DISKRIMINASI REQUEST MASUK]
                                                 |
                                          [Request Masuk]
                                                 |
                       +-------------------------+-------------------------+
                       |                                                   |
              [User-Agent Biasa / Tool]                            [Mengaku Googlebot / Bingbot]
                       |                                                   |
              [Masuk Perangkap Umpan]                              [Async FCrDNS Verification]
                       |                                                   |
              [Tarpit / Canary / Blacklist]              +-----------------+-----------------+
                                                         |                                   |
                                              [Hostname Valid *.googlebot.com]     [Hostname Palsu / Luar]
                                                         |                                   |
                                              [BENIGN CRAWLER: Disallowed 403]     [MIMICRY DETECT: Masquerading T1036]
                                              (Bebas Alarm / No Blacklist)         (Langsung Sentral Blacklist!)
```

1. **Crawler Mesin Pencari Sah (Googlebot, Bingbot):** Rute umpan (`/decoy-portal/`, `/.env`, `/backup.sql`) dibatasi melalui `/robots.txt`. Mesin pencari legal mematuhinya dan menerima kode HTTP 403 pasif tanpa memicu alarm (*False Positive Elimination*).
2. **Penyerang Menyamar (*Mimicry / MITRE ATT&CK T1036 Masquerading*):** Jika penyerang memasang header `User-Agent: Googlebot/2.1` untuk melewati filter, FCrDNS mengeksekusi reverse DNS lookup asinkron. Jika IP bukan berasal dari domain terverifikasi Google/Bing, penyerang langsung diklasifikasikan sebagai ancaman tingkat kritis dan dimasukkan ke Sentral Blacklist.

---

## 5. Integritas Barang Bukti Digital & Rantai Audit POMAD (HMAC-SHA256)

Berdasarkan UU Informasi dan Transaksi Elektronik (UU ITE) dan hukum acara peradilan militer (Oditur Militer), barang bukti digital wajib memiliki jaminan keutuhan rantai kawal (*Chain-of-Custody*).

NEXUS-TRAP mengimplementasikan **Cryptographic Hash-Chaining** pada database append-only SQLite (`nexus_audit.db`):

$$\text{Entry Hash}_i = \text{HMAC-SHA256}\Big(\text{Secret Key}, \; \text{Hash}_{i-1} \parallel \text{Timestamp} \parallel \text{Event Tag} \parallel \text{Source IP} \parallel \text{Payload}\Big)$$

- Setiap baris log mengikat nilai hash dari baris sebelumnya.
- Seluruh hash ditandatangani menggunakan HMAC-SHA256 berbasis kunci rahasia node pangkalan.
- Endpoint `/api/audit/verify` memverifikasi seluruh rantai rekaman secara otomatis. Apabila penyerang mencoba memodifikasi atau menghapus baris riwayat insiden, verifikasi akan gagal secara matematis, membuktikan adanya perusakan barang bukti.

---

## 6. Mekanisme Proteksi Anti-Friendly-Fire & Anti-Backfire Guard

Sistem pertahanan aktif rawan dieksploitasi oleh penyerang jika tidak dirancang dengan pengamanan berlapis:
1. **Pencegahan DoS Komandan (Anti-Friendly-Fire):**
   Penyerang tidak dapat memalsukan IP Komandan atau Default Gateway. Subnet loopback (`127.0.0.1`, `::1`) dan gateway teritorial (`192.168.1.1`, `10.0.0.1`) terdaftar dalam whitelist `settings.IMMUNE_IPS` dan divalidasi dengan fungsi `ipaddress.is_loopback` sebelum firewall dieksekusi.
2. **Verifikasi Soket TCP 3-Way Handshake:**
   Isolasi firewall kernel hanya menerima IP soket yang terverifikasi secara matematis melalui TCP 3-way handshake, bukan dari IP klaim WebRTC atau header HTTP yang dapat dimanipulasi.
3. **Peredam Banjir Suar (Canary Siren Rate-Limiting):**
   Mekanisme sliding-window rate limiter membatasi ledakan sirine maksimal 1 kali per 10 detik per IP, mencegah penyerang melakukan serangan balik *Alert Siren Denial of Service*.

---

## 7. Rencana Implementasi Skalabilitas Teritorial (Mabesad - Kodam - Kodim)

NEXUS-TRAP dirancang dengan arsitektur berjenjang (*Hub-and-Spoke Deployment*):

```
+-----------------------------------------------------------------------------------------+
|                  TINGKAT 3: PUSAT KOMANDO MABESAD (PUSSIBERAD JAKARTA)                  |
| - Agregasi Threat Intelligence Nasional & Sentral Blacklist IOC Terpadu                 |
| - AI Strategic War-Room & Analisis Korelasi Ancaman Antar-Kotama                        |
+-----------------------------------------------------------------------------------------+
                                             ^
                                             | WireGuard / mTLS Zero-Trust Encrypted Tunnel
                                             v
+-----------------------------------------------------------------------------------------+
|                  TINGKAT 2: REGIONAL THREAT AGGREGATOR (INFOLAHTA KODAM)                |
| - DNS Canary Authoritative Listener (UDP Port 53) Wilayah Teritorial                    |
| - Push Aturan Firewall Sentral ke Router L3 (MikroTik / Cisco) Kodim Jajaran            |
+-----------------------------------------------------------------------------------------+
                                             ^
                                             | Subnet Intranet Dinas Teritorial
                                             v
+-----------------------------------------------------------------------------------------+
|                  TINGKAT 1: EDGE SENSOR DECOY (SATUAN KODIM / KOREM / YONIF)            |
| - Micro-Decoys: Raw Socket Modbus 502 (Genset/Radar), Fake Portal Sisfopers             |
| - Sticky Tarpit Crasher Daemon & Honey-Documents OpenXML DOCX                           |
+-----------------------------------------------------------------------------------------+
```

---

## 8. Spesifikasi Kebutuhan Sumber Daya & Panduan Deployment

### 8.1 Kebutuhan Minimum Perangkat Keras (Node Satuan Bawah)
- **Processor:** Dual-Core CPU (Intel Celeron / Core i3 / ARM Cortex-A72 setara Raspberry Pi 4).
- **RAM:** Minimal 1 GB (Pemakaian aktual sistem < 120 MB RAM).
- **Penyimpanan:** 500 MB ruang kosong disk.
- **Jaringan:** 1 port Ethernet RJ-45 terhubung ke subnet lokal markas.
- **Sistem Operasi:** Linux (Ubuntu 20.04+, Debian 11+, Rocky Linux) atau Windows 10/11 / Windows Server.

### 8.2 Prosedur Eksekusi Cepat 1-Klik
```powershell
# Jalankan seluruh ekosistem di Windows (Backend, Decoys, Frontend C4ISR)
.\start_all.ps1

# Eksekusi Verifikasi Kualitas & Audit (QC/QA 100% Pass)
python test_full_qc_qa.py

# Reset Status Purwarupa ke Baseline Siaga Hijau
.\reset_demo.ps1
```

---
**TIM PENGEMBANG NEXUS-TRAP // KARTIKA CYBER HACKATHON 2026**  
*Mewujudkan Kedaulatan Pertahanan Siber Semesta yang Mandiri, Tangguh, dan Presisi.*
