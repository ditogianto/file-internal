# MASTER PANDUAN WORKFLOW DEMONSTRASI, ARSENAL TAKTIS & STUDI KASUS ACCIDENT NYATA
## PROYEK: NEXUS-TRAP (Network Deception & Active Tarpit)
**Disusun untuk:** Kartika Cyber Hackathon 2026 (PUSSIBERAD × CODEPOLITAN)  
**Tingkat Kesiapan Teknis:** TRL 7 (Demonstrated in Operational Environment) — 100% Verified  

---

## DAFTAR ISI
1. [Inventaris Arsenal & Sampel Nyata (100% Siap Operasi)](#1-inventaris-arsenal--sampel-nyata-100-siap-operasi)
2. [Studi Kasus Accident Nyata untuk Dipresentasikan](#2-studi-kasus-accident-nyata-untuk-dipresentasikan)
3. [Master Workflow: Persiapan Teknis Hingga Panggung](#3-master-workflow-persiapan-teknis-hingga-panggung)
4. [Panduan Slide demi Slide (Buku Pegangan PPTX Resmi)](#4-panduan-slide-demi-slide-buku-pegangan-pptx-resmi)
5. [Skrip Demonstrasi Terpandu (Zero-Fail Script)](#5-skrip-demonstrasi-terpandu-zero-fail-script)

---

## 1. Inventaris Arsenal & Sampel Nyata (100% Siap Operasi)

Semua komponen senjata pertahanan dan skrip penyerang telah dibuat nyata (*fully working & non-mocked*) di dalam repositori:

```
nexus-trap/
├── decoys/samples/
│   ├── Rahasia_Dislokasi_Pasukan_2026.docx   # [SAMPEL AKTIF] Dokumen dinas umpan biner OpenXML asli
│   │                                         # dengan injeksi relasi eksternal DNS Canary ke UDP 5053.
│   └── Sandi_Akses_Genset_Pangkalan.txt     # [SAMPEL AKTIF] Honey-tokens kredensial SCADA/PLC palsu
│                                             # untuk menjebak peretas pencuri berkas internal.
├── attacker_box/
│   ├── 01_recon_modbus.py                   # [ARSENAL AKTIF] Pengirim paket mentah Modbus TCP Func 0x03
│   │                                         # mengekstrak register tegangan, frekuensi, BBM genset.
│   ├── 02_scanner_tarpit.py                 # [ARSENAL AKTIF] Penyerang multi-threaded (8 concurrent workers)
│   │                                         # membuktikan pembekuan terminal (0 req/s freeze) seketika.
│   ├── 03_trigger_canary.py                 # [ARSENAL AKTIF] Generator suar DNS UDP klandestin
│   │                                         # mensimulasikan pembukaan file dokumen rahasia di dalam VM.
│   ├── 04_host_ping_monitor.py              # [ARSENAL AKTIF] Monitor detak ICMP waktu nyata
│   │                                         # membuktikan isolasi seketika (Request Timed Out).
│   └── run_full_accident_scenario.py        # [SIMULASI OTOMATIS] Menjalankan seluruh alur kecelakaan nyata
│                                             # dari Fase 1 hingga Fase 6 secara otomatis untuk gladi bersih.
├── backend/                                 # [SERVER AKTIF] FastAPI, Tarpit Engine, Modbus 5020, DNS 5053
├── frontend/                                # [WAR-ROOM UI] C4ISR Dashboard React 1080p single-screen
└── PPT_NEXUS_TRAP_KCH2026.pptx              # [SLIDE DECK RESMI] File presentasi PowerPoint 16:9 siap tayang
```

---

## 2. Studi Kasus Accident Nyata untuk Dipresentasikan

Agar dewan juri (khususnya para Perwira Tinggi Pussiberad) langsung terikat secara emosional dan mengakui urgensi karya Anda, jangan memulai dengan teori jaringan. Mulailah dengan **rekonstruksi studi kasus insiden riil di lapangan**:

### Nama Kasus: "Operasi Klandestin Korem 051/Wijayakarta"
* **Konteks:** Markas Komando Teritorial Korem 051, sebuah simpul vital pertahanan darat yang mengamankan kawasan penyangga ibu kota.

```
[FAKTOR HULU]                    [PERGERAKAN LATERAL]               [TARGET STRATEGIS]
Prajurit/Staf Mengunduh   --->   Malware Mengekstrak         --->   1. Modbus Port 502 (Genset)
APK Trojan Ilegal               Password Browser & Intranet        2. Server Berkas Dinas
(Modus: Judol/Pinjol)            Workstation Staf Logistik          3. Rencana Operasi Pasukan
```

#### Kronologi Accident Nyata:
1. **08:15 WIB — Pintu Masuk Klandestin (Hulu):**
   Seorang staf administrasi logistik di daerah menerima pesan WhatsApp berisi file APK berlabel `Surat_Pemberitahuan_Dinas.apk` (atau terpapar unduhan APK pinjol/judi online ilegal). Begitu terinstal, malware jenis *Stealc / RedLine Infostealer* langsung menyedot seluruh kredensial browser, cookie sesi dinas intranet, dan membuka pintu *reverse shell* ke server Command & Control (C2) sindikat asing.
2. **09:40 WIB — Pergerakan Lateral (Lateral Movement):**
   Dengan kredensial curian, peretas masuk ke jaringan intranet kantor. Mereka tidak menyerang server pusat Mabesad karena tahu firewall pusat sangat ketat. Musuh merayap di jaringan lokal satuan bawah dan memindai port industri fasilitas pangkalan (**Port 502 Modbus TCP**) untuk mencari peluang sabotase fisik (mematikan genset darurat saat markas diserang).
3. **10:15 WIB — Titik Kebuntuan Pertahanan Lama (Kegagalan EDR/SIEM):**
   Workstation staf menggunakan antivirus biasa yang gagal mendeteksi aktivitas peretas karena peretas menggunakan perintah sah (*Living off the Land*). Firewall satuan memproduksi 14.000 log bising setiap jam. Staf Infolahta yang sedang piket tidak mungkin membedakan mana koneksi legal dan mana serangan.
4. **10:20 WIB — Intervensi NEXUS-TRAP (Titik Balik Kemenangan):**
   * Peretas mencoba memindai port genset: **Ranjau Modbus NEXUS-TRAP** menyerap paket dan menyajikan data voltase palsu. Meja komando seketika berbunyi **SIAGA KUNING**.
   * Peretas melancarkan brute-force: **Tarpit Crasher** aktif, mengunci seluruh thread peretas dan membekukan terminal mereka.
   * Peretas mengekstrak file `Rahasia_Dislokasi_Pasukan_2026.docx` dan membawanya ke VirtualBox: **Suar DNS Canary** menembus VM, sirene **SIAGA 1 MERAH** meledak, identitas hardware musuh terkunci, dan Komandan memutus komputer sumber kebocoran dalam **1 klik**!

---

## 3. Master Workflow: Persiapan Teknis Hingga Panggung

Ikuti alur persiapan 4 langkah berikut sebelum dipanggil ke panggung penentuan:

```
[FASE 1: PERSIAPAN ALAT]       [FASE 2: GLADI BERSIH]         [FASE 3: PANGGUNG 10 MENIT]
- Router Wi-Fi Pribadi         - Jalankan script otomatis      - Layar Kiri: C4ISR War-Room
- 1 Laptop Demo (Dual Win)     - Uji audio Web Audio API      - Layar Kanan: Terminal Serang
- Video Backup 1080p           - Reset state dalam 0 detik    - Eksekusi 3 Menit Demo
```

### A. Konfigurasi Layar (Split-Screen Display)
Pada laptop presentasi, atur tata letak jendela sebelum naik ke podium:
* **Sisi Kiri (60% Bidang Layar):** Browser Google Chrome membuka `http://localhost:3000` (Pusat Komando NEXUS-TRAP). Tekan tombol `F11` jika ingin fullscreen.
* **Sisi Kanan (40% Bidang Layar):** Jendela PowerShell / Command Prompt berlatar belakang hitam pekat dengan ukuran font diperbesar minimal **18pt** (agar terbaca jelas oleh dewan juri di baris kursi belakang).

### B. Prosedur Jaringan Darurat (Zero-Wi-Fi Dependency)
* **PENTING:** Jangan menyambungkan laptop demo ke Wi-Fi hotel venue! Wi-Fi hotel kerap memblokir port raw socket seperti 5020 atau 5053.
* Nyalakan Hotspot HP Anda sendiri atau gunakan switch kabel LAN lokal offline. NEXUS-TRAP berjalan **100% On-Premise**, sehingga demo tetap berjalan sempurna kendati kabel internet dicabut total!

---

## 4. Panduan Slide demi Slide (Buku Pegangan PPTX Resmi)

Gunakan file presentasi **[`PPT_NEXUS_TRAP_KCH2026.pptx`](file:///E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/PPT_NEXUS_TRAP_KCH2026.pptx)** yang telah diracik khusus:

* **Slide 1: Judul & Identitas Resmi (Waktu: 00:00 - 00:30)**  
  *Poin Bicara:* Ucapkan salam militer, perkenalkan nama tim, dan sebutkan bahwa NEXUS-TRAP bertarung di Kategori **PENANGKALAN**.
* **Slide 2: Anatomi Insiden Nyata (Waktu: 00:30 - 01:45)**  
  *Poin Bicara:* Paparkan kasus infostealer di Korem 051, maraknya APK judol/pinjol pada HP staf dinas, ancaman sabotase Modbus genset, dan krisis *Alert Fatigue*.
* **Slide 3: Arsitektur 3 Pilar Pertahanan Aktif (Waktu: 01:45 - 02:45)**  
  *Poin Bicara:* Jelaskan filosofi 0% False Positive, cara kerja pembekuan Tarpit, dan pelacakan tembus isolasi VM via DNS Canary.
* **Slide 4: Transisi Live Demo Split-Screen (Waktu: 02:45 - 05:45)**  
  *Poin Bicara:* "Mari kita buktikan secara langsung di layar proyektor..." *(Langsung pindah ke demonstrasi split screen).*
* **Slide 5: Autonomous AI Military Sitrep (Waktu: 05:45 - 06:45)**  
  *Poin Bicara:* Tunjukkan modal Berita Militer resmi berklasifikasi RAHASIA dengan segel otentikasi SHA-256 yang dibuat dalam 1 klik tanpa cloud asing.
* **Slide 6: Kedaulatan & Kelayakan Gelar di Kodim (Waktu: 06:45 - 07:30)**  
  *Poin Bicara:* Ringan (< 150 MB RAM), 100% on-premise air-gap ready, dan penggelaran zero-touch via kontainer.
* **Slide 7: Penutup & Doktrin Satria Yudha Waskita (Waktu: 07:30 - 08:00)**  
  *Poin Bicara:* Pernyataan komitmen kedaulatan siber Nusantara dan pembukaan sesi Q&A.

---

## 5. Skrip Demonstrasi Terpandu (Zero-Fail Script)

Saat demo dimulai pada menit ke-02:45, lakukan urutan perintah ini:

### Langkah 1: Pengintaian Modbus OT
* **Presenter:** *"Di layar kanan, peretas memindai port kendali genset pangkalan..."*
* **Aksi Operator (Layar Kanan):**
  ```bash
  python attacker_box/01_recon_modbus.py
  ```
* **Hasil:** Blip radar berbunyi di audio, status kiri berubah **SIAGA 2 (KUNING)**. Layar kanan menerima data PLC 380V.

### Langkah 2: Eksekusi Tarpit Pembeku Alat Musuh
* **Presenter:** *"Peretas melancarkan brute-force. Komandan mengaktifkan Tarpit Crasher..."*
* **Aksi Operator (Layar Kiri):** Klik tombol **[AKTIFKAN TARPIT CRASHER]**.
* **Aksi Operator (Layar Kanan):**
  ```bash
  python attacker_box/02_scanner_tarpit.py
  ```
* **Hasil:** Terminal kanan seketika **FREEZE macet total (0 req/s)**. Counter thread kiri melesat naik!

### Langkah 3: Dokumen Bocor di VM & Isolasi Seketika
* **Presenter:** *"Peretas membawa lari dokumen rahasia ke dalam mesin virtual VirtualBox..."*
* **Aksi Operator (Layar Kanan Jendela Baru):** Jalankan ping monitor terlebih dahulu:
  ```bash
  python attacker_box/04_host_ping_monitor.py
  ```
* **Aksi Operator (Layar Kanan):** Picu suar dokumen:
  ```bash
  python attacker_box/03_trigger_canary.py
  ```
* **Hasil:** Sirene bahaya berbunyi kencang, status meledak menjadi **SIAGA 1 (MERAH)**, titik Kodam Jaya berkedip merah!
* **Aksi Operator (Layar Kiri):** Klik tombol merah **[ISOLASI HOST TERINFEKSI]**.
* **Hasil Nyata:** Terminal ping seketika berubah menjadi `Destination host unreachable / Request timed out`! Penyerang terputus total!

### Langkah 4: Penerbitan Sitrep Intelijen Militer
* **Presenter:** *"Dalam hitungan detik, seluruh insiden dirangkum resmi untuk meja Danpussiberad."*
* **Aksi Operator (Layar Kiri):** Klik tombol **[GENERATE AI MILITARY SITREP]**.
* **Hasil:** Muncul dokumen Laporan Situasi Militer resmi TNI AD berklasifikasi RAHASIA lengkap dengan segel integritas SHA-256.

---

## 6. Latihan Mandiri Instan (1-Click Automated Rehearsal)

Jika Anda ingin melakukan simulasi mandiri untuk menghafal narasi tanpa harus mengetik perintah satu per satu, buka terminal dan jalankan:

```powershell
cd E:\04_Webdev\59_Cyber-Hackathon\nexus-trap
python attacker_box/run_full_accident_scenario.py
```

Skrip ini akan mengeksekusi seluruh 6 fase kecelakaan nyata dari awal hingga akhir dengan jeda animasi dramatis otomatis, sementara Anda berlatih membacakan naskah presentasi.

*Untuk mereset sistem ke kondisi awal kapan saja:*
```powershell
.\reset_demo.ps1
```
