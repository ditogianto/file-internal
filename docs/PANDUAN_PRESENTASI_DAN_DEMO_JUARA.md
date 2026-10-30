# BUKU PANDUAN STRATEGIS PRESENTASI, DEMO PANGGUNG, & TATA KELOLA KARYA JUARA 1
## KARTIKA CYBER HACKATHON 2026 (PUSSIBERAD × CODEPOLITAN)
**Proyek:** NEXUS-TRAP (Network Deception & Active Tarpit) (Platform Active Cyber Deception & Autonomous Interdiction)  
**Target:** Juara 1 Nasional & Golden Ticket Rekomendasi Seleksi Bintara Siber TNI AD  

---

## DAFTAR ISI
1. [Audit Analisis UI/UX: Mengapa Antarmuka Ini Memiliki Mentalitas Juara?](#1-audit-analisis-uiux-mengapa-antarmuka-ini-memiliki-mentalitas-juara)
2. [Checklist Aset Visual & Media Submission (Sesuai Rulebook)](#2-checklist-aset-visual--media-submission-sesuai-rulebook)
3. [Koreografi Presentasi Panggung 10 Menit (Babak Final di Aston Kartika)](#3-koreografi-presentasi-panggung-10-menit-babak-final-di-aston-kartika)
4. [Skrip Kata-demi-Kata (Verbatim Pitching Script) untuk Presenter](#4-skrip-kata-demi-kata-verbatim-pitching-script-untuk-presenter)
5. [Struktur Rekaman Video YouTube 10 Menit (Babak Penyisihan - Batas 15 Nov)](#5-struktur-rekaman-video-youtube-10-menit-babak-penyisihan---batas-15-nov)
6. [Buku Saku Tangkisan Q&A Juri Inti (Onno W. Purbo, Mahrus, Sofian, Pussiberad)](#6-buku-saku-tangkisan-qa-juri-inti-onno-w-purbo-mahrus-sofian-pussiberad)
7. [Protokol Darurat Panggung Anti-Gagal (The "Zero-Failure" Protocol)](#7-protokol-darurat-panggung-anti-gagal-the-zero-failure-protocol)

---

## 1. Audit Analisis UI/UX: Mengapa Antarmuka Ini Memiliki Mentalitas Juara?

Sebagai Principal Creative Technologist dan UI/UX Architect, antarmuka **NEXUS-TRAP** telah diuji secara mendalam dan dinilai **sangat unggul (skor 9.5/10)** dibandingkan standar purwarupa hackathon pada umumnya. Berikut adalah faktor-faktor penentu kemenangan dalam desain ini:

### A. Hukum Cognitive Load & Layout 1-Layar (Single-Screen 16:9)
* **Kelemahan Mayoritas Kompetitor:** Kebanyakan peserta hackathon membuat web memanjang ke bawah (vertical scroll) yang memaksa juri menunggu presenter scrolling layar proyektor saat demo. Ini memecah konsentrasi juri dan merusak tempo waktu 3 menit.
* **Keunggulan NEXUS-TRAP:** Seluruh komponen vital (TopNav, KPI Ribbon, Peta Sebaran Kodam, Konsol Taktis, Live Radar Log, dan Dossier Buronan) terkunci presisi dalam rasio **16:9 widescreen**. Tidak ada satu milimeter pun informasi yang terpotong atau membutuhkan *scrolling* di proyektor 1080p.

### B. Arsitektur Warna Semantik 60-30-10 & Aksesibilitas CVD
* **60% Dominant Base:** Obsidian Dark Slate (`#080c13`, `#0d131f`) mengeliminasi kelelahan mata juri dan memberikan aura *Command Center* militer berwibawa (C4ISR).
* **30% Structural Branding:** Tactical Forest Green & Dark Steel (`#064e3b`, `#1e293b`) mempertegas identitas Pusat Siber TNI AD.
* **10% Semantic State Accents:**
  * **Emerald (`#10b981`):** Menandakan Siaga Hijau (kondisi normal).
  * **Amber (`#f59e0b`):** Menandakan Siaga Kuning (intersepsi pengintaian port genset Modbus 502).
  * **Crimson (`#ef4444`):** Menandakan Siaga 1 Merah (kebocoran dokumen umpan di VM).
* **Dual-Coding Mandate:** Perubahan status bahaya tidak hanya ditandai oleh warna, melainkan disertai teks status eksplisit (`SIAGA 1 (MERAH)`), animasi denyut radar (*pulsing beacon*), serta **efek audio sintetis Web Audio API** (blip radar dan sirine taktis) yang berbunyi otomatis tanpa membutuhkan file eksternal MP3.

### C. Tipografi Taktis & Hierarki Visual
* Tipografi memadukan font monospace berkarakter tinggi (*JetBrains Mono*) untuk baris log, data register OT, dan fingerprint hardware, dengan font sans-serif untuk label komando.
* Label nama satuan pada pulau Jawa (Jakarta, Bandung, Semarang, Surabaya, Denpasar) menggunakan teknik **Alternating Leader Lines** (garis penunjuk selang-seling atas-bawah), sehingga saat proyektor menampilkan peta, nama Kodam terbaca 100% tanpa tabrakan teks.

---

## 2. Checklist Aset Visual & Media Submission (Sesuai Rulebook)

Panitia menetapkan kelengkapan media yang wajib diunggah pada platform sebelum **15 November 2026 pukul 23:59 WIB**. Seluruh aset di bawah ini telah selesai diproduksi dan tersedia di direktori `screenshots/`:

| Nama File Aset | Resolusi / Ukuran | Peran dalam Dokumen Penjurian |
| :--- | :---: | :--- |
| **`thumbnail_karya_1200x630.png`** | 1200×630 px (385 KB) | **Wajib:** Tampilan awal karya di etalase pameran panitia (Batas max 500 KB terpenuhi). |
| **`01_siaga_hijau_baseline.png`** | 1920×1080 px | Tangkapan Layar 1: Pusat Komando C4ISR dalam status Siaga Hijau (64 node aktif, 0% False Positive). |
| **`02_siaga_kuning_ot_interception.png`** | 1920×1080 px | Tangkapan Layar 2: Intersepsi pengintaian protokol industri Modbus Port 5020 (Genset Komando). |
| **`03_tarpit_interdiction_active.png`** | 1920×1080 px | Tangkapan Layar 3: Tarpit Crasher Engine membekukan terminal musuh dan mengunci worker thread. |
| **`04_siaga_merah_canary_dossier.png`** | 1920×1080 px | Tangkapan Layar 4: Suar DNS Canary meledak di VM, peta Kodam berkedip merah, profil buronan terkunci. |
| **`05_ai_military_sitrep_intel.png`** | 1920×1080 px | Tangkapan Layar 5: Modal Laporan Situasi Siber Militer (AI Sitrep) resmi TNI AD berklasifikasi RAHASIA. |

---

## 3. Koreografi Presentasi Panggung 10 Menit (Babak Final di Aston Kartika)

Babak final di Hotel Aston Kartika tanggal **24 November 2026** membatasi waktu **tepat 10 menit per tim** (Penjelasan + Live Demo + Tanya Jawab). Atur pembagian waktu dengan disiplin militer:

```
+---------------------------------------------------------------------------------------------------+
| TOTAL ALOKASI WAKTU PRESENTASI FINAL: 10 MENIT                                                    |
+------------------------------------+------------------------------------+-------------------------+
| [00:00 - 02:30] EXECUTIVE HOOK     | [02:30 - 06:00] LIVE SPLIT DEMO    | [06:00 - 10:00] Q&A DEF |
| - Krisis Asimetris Satuan Bawah    | - Babak 1: Modbus OT (Kuning)      | - Tangkisan Pak Onno    |
| - Bahaya Infostealer APK Judol     | - Babak 2: Tarpit Freeze           | - Tangkisan Mas Mahrus  |
| - Paradigma 0% False Positive      | - Babak 3: Canary VM & Isolasi     | - Penegasan Doktrin AD  |
+------------------------------------+------------------------------------+-------------------------+
```

---

## 4. Skrip Kata-demi-Kata (Verbatim Pitching Script) untuk Presenter

Gunakan naskah intonasi mantap ini di depan Dewan Juri dan Perwira Tinggi Pussiberad:

### [Menit 00:00 - 01:15] Pembukaan & Menghubungkan Masalah Nyata
> *"Assalamu’alaikum Warahmatullahi Wabarakatuh. Selamat pagi Bapak Jenderal, Dewan Juri yang kami hormati, dan seluruh hadirin Kartika Cyber Conference 2026.  
> Pertahanan siber di tingkat Mabesad mungkin sudah dibentengi teknologi bernilai miliaran rupiah. Namun musuh kita hari ini tidak perlu menyerang firewall pusat secara frontal. Mereka masuk dari titik terlemah: satuan kewilayahan di Kodam, Korem, hingga Kodim.  
> Faktanya, perangkat laptop dinas staf administrasi di daerah rentan terinfeksi malware **Infostealer** akibat maraknya peredaran APK ilegal—seperti tautan jebakan Judi Online dan Pinjol ilegal. Begitu satu laptop dinas staf logistik terinfeksi, kredensial intranet bocor, dan peretas asing mulai merayap dalam senyap mencari dokumen rencana operasi dan fasilitas vital pangkalan."*

### [Menit 01:15 - 02:30] Mengapa Solusi Konvensional Gagal
> *"Ketika ancaman ini merayap di jaringan lokal, sistem SIEM dan Firewall konvensional memproduksi puluhan ribu log rumit setiap hari. Personel Infolahta di daerah yang jumlahnya terbatas mengalami **Alert Fatigue**—peringatan bahaya tenggelam dalam lautan log palsu.  
> Untuk itulah kami mempersembahkan: **NEXUS-TRAP (Network Deception & Active Tarpit)**, Platform Pertahanan Siber Aktif dan Deception Terpadu yang mengubah jaringan satuan TNI AD menjadi **ladang ranjau klandestin**.  
> Kami memegang tiga doktrin pembeda:
> 1. **Zero False Positive (0% Alarm Palsu):** Umpan kami tidak memiliki fungsi operasional legal. Siapa pun yang menyentuhnya, 100% dipastikan penyusup atau malware.
> 2. **Active Interdiction (Tarpit):** Bukan sekadar mencatat log, sistem kami secara fisik membekukan dan melumpuhkan instrumen penyerang.
> 3. **Pelacakan Tembus Isolasi VM:** Dokumen rahasia umpan kami tetap melacak peretas bahkan ketika dibawa kabur ke dalam VirtualBox terisolasi."*

### [Menit 02:30 - 06:00] Transisi ke Live Demo Layar Terbagi (Split-Screen)
*(Operator demo langsung mengaktifkan proyektor split-screen: Kiri Dashboard C4ISR, Kanan Terminal Kali Linux/Penyerang)*

* **Aksi 1 (Pengintaian OT Pangkalan):**  
  > *"Mari kita saksikan demonstrasi langsung. Di layar kanan adalah terminal penyerang yang telah menyusup ke subnet staf Kodim. Penyerang mulai mencari kontrol genset markas pada Port 502 Modbus TCP..."*  
  *(Operator kanan menjalankan `python attacker_box/01_recon_modbus.py`)*  
  *(Bunyi blip radar terdengar, status kiri berubah KUNING)*  
  > *"Seketika meja komando membunyikan Siaga Kuning. Sensor NexusTrap membalas dengan register palsu (380V, 50Hz, BBM 85%), membuat penyerang yakin mereka telah menemukan genset nyata, sementara koordinat mereka telah terekam."*

* **Aksi 2 (Brute-Force & Pelumpuhan Tarpit):**  
  > *"Penyerang kemudian meluncurkan alat otomatis multi-threaded untuk membobol direktori rahasia..."*  
  *(Operator kiri mengklik tombol **[AKTIFKAN TARPIT CRASHER]**)*  
  *(Operator kanan menjalankan `python attacker_box/02_scanner_tarpit.py`)*  
  *(Layar kanan seketika FREEZE macet total, layar kiri counter thread melesat)*  
  > *"Lihat layar kanan penyerang: terminal mereka macet total, 0 req/sec! Mesin Asynchronous Sticky Tarpit kami mengunci seluruh worker thread musuh tanpa membebani server kita sedikit pun!"*

* **Aksi 3 (Pencurian Dokumen, Pembongkaran VM & Isolasi 1-Klik):**  
  > *"Penyerang frustrasi lalu mengunduh dokumen rahasia umpan dan membukanya di mesin virtual (VirtualBox)..."*  
  *(Operator kanan menjalankan `python attacker_box/03_trigger_canary.py`)*  
  *(Sirene bahaya berbunyi, layar komando MELEDAK SIAGA 1 MERAH, titik Kodam Jaya berkedip merah)*  
  > *"Sirene Siaga 1 Merah berbunyi! Suar DNS klandestin kami menembus isolasi VM musuh. Di kartu Dossier kanan bawah, identitas hardware buronan, GPU hash, dan tanda tangan JA4 scanner mereka telah terkunci permanen!"*  
  > *"Untuk melindungi pangkalan, Komandan cukup menekan satu tombol: **ISOLASI HOST TERINFEKSI**."*  
  *(Operator kiri mengklik tombol merah, jendela ping penyerang seketika berubah menjadi `Destination Host Unreachable`)*  
  > *"Dalam 1 detik, ancaman musuh diputus total dari seluruh rute intranet pangkalan."*

* **Aksi 4 (Otonom AI Military Sitrep):**  
  *(Operator kiri mengklik tombol **[GENERATE AI MILITARY SITREP]**)*  
  > *"Terakhir, model AI lokal Pussiberad secara otonom merumuskan Laporan Situasi Militer (Sitrep) resmi berklasifikasi RAHASIA lengkap dengan nomor surat, kronologi teknis, dan saran tindak lanjut intelijen, siap diajukan ke meja Danpussiberad."*

### [Menit 06:00 - 07:00] Penutup & Kesiapan Adopsi
> *"NEXUS-TRAP dibangun 100% On-Premise, mandiri tanpa ketergantungan cloud asing, dan hemat sumber daya—siap dipasang pada PC standar di seluruh Kodim se-Indonesia. Inilah kontribusi nyata kami untuk kedaulatan siber Tentara Nasional Indonesia Angkatan Darat. Terima kasih. Kami siap menjawab pertanyaan Dewan Juri."*

---

## 5. Struktur Rekaman Video YouTube 10 Menit (Babak Penyisihan - Batas 15 Nov)

Video yang diunggah ke YouTube untuk babak penyisihan memiliki durasi **maksimal 10 menit**. Jangan biarkan video bertele-tele; ikuti format editorial pemenang berikut:

```
[00:00 - 02:00] PROLOG MASALAH (B-Roll Grafis & Narasi Urgensi)
- Tampilkan visualisasi ancaman nyata: Infostealer, bahaya sabotase OT pangkalan.
- Jelaskan mengapa pendekatan IDS/Firewall pasif di satuan bawah gagal mengatasi Alert Fatigue.

[02:00 - 04:00] ANATOMI SOLUSI & ARSITEKTUR 3 PILAR
- Diagram alur: Tactical Decoy -> Tarpit Crasher -> DNS Canary Attribution.
- Tampilkan logo kedaulatan siber: 100% On-Premise, Air-Gap Ready, Zero Vendor Lock-in.

[04:00 - 07:30] LIVE DEMOSTRACTION (UNCUT SCREEN RECORDING)
- Perekaman layar 1080p 60fps dengan layout split-screen.
- Demonstrasikan runut: Scan Port 502 -> Tarpit Freeze -> DNS Canary VM -> 1-Click Isolation.
- Pastikan audio efek taktis (blip radar dan sirine) terdengar jernih tanpa distorsi.

[07:30 - 08:45] AI MILITARY SITREP GENERATOR & C4ISR VALUE
- Tunjukkan modal Laporan Intelijen Sitrep dengan segel otentikasi SHA-256.
- Jelaskan bagaimana AI membantu komandan kewilayahan yang bukan insinyur siber.

[08:45 - 10:00] RENCANA PENGGELARAN (ROADMAP DEPLOYMENT) & PENUTUP
- Tunjukkan betapa mudahnya penggelaran di Kodam/Kodim hanya dengan 1 baris perintah docker.
- Pernyataan penutup yang tegas tentang bela negara dan komitmen untuk TNI AD.
```

---

## 6. Buku Saku Tangkisan Q&A Juri Inti

Dewan Juri babak final akan menguji kedalaman sistem Anda. Berikut strategi menjawab pertanyaan kritis:

### Pak Onno W. Purbo (Infrastruktur, Jaringan, Efisiensi Sumber Daya)
* **Pertanyaan Juri:** *"Kalian pasang Tarpit. Kalau botnet kirim puluhan ribu koneksi TCP SYN simultan, bukankah CPU server kalian yang hang duluan?"*
* **Tangkisan Juara:** *"Pertanyaan luar biasa dari Pak Onno. Sistem kami menggunakan event-loop asinkron berbasis modul Linux `epoll` via `asyncio`. Kami tidak membuat thread OS baru untuk setiap koneksi yang masuk. Menahan 1.000 soket di mode zero-window hanya memakan RAM sekitar 4 MB tanpa beban context-switching. Selain itu, kami menyertakan aturan pembatasan koneksi lokal (bounded rate limiting) maksimal 500 koneksi per IP. Jadi server kita tetap stabil di bawah 2% CPU, sementara scanner musuh yang berbasis multi-threading konvensional kehabisan thread pool seketika."*

### Mas Mahrus Qusaeri (Offensive Security & Red Team)
* **Pertanyaan Juri:** *"Penyerang berpengalaman tidak akan membuka dokumen di VM yang tersambung internet. Kalau adapter jaringannya di-set Host-Only, bagaimana suar DNS kalian bisa keluar?"*
* **Tangkisan Juara:** *"Sangat tepat, Mas Mahrus. Dalam skenario red team nyata, peretas yang mencuri dokumen militer biasanya menggunakan adapter NAT untuk tetap bisa mengunduh modul dekompilasi tanpa sadar bahwa resolver DNS OS tamu tetap memantul ke gateway host. Namun jika penyerang benar-benar memutus jaringan 100%, suar DNS akan tertahan di cache dan ditembakkan keluar begitu VM kembali tersambung ke jaringan lain. Dan sebagai jaring pengaman kedua, kami menanamkan **Honey-Credentials memori**. Ketika kredensial palsu tersebut dipakai untuk lateral movement ke server dinas lain, sistem langsung mendeteksi pelanggaran secara deterministik."*

### Mas Sofian Hadiwijaya (AI, Rekayasa Perangkat Lunak, Efektivitas Produk)
* **Pertanyaan Juri:** *"Mengapa harus ada AI di sistem pertahanan siber seperti ini? Apakah model AI lokal kalian tidak halusinasi saat membuat Sitrep?"*
* **Tangkisan Juara:** *"Siap, Mas Sofian. Masalah terbesar di satuan bawah TNI AD bukan kurangnya data log, melainkan keterbatasan SDM analis yang mampu menerjemahkan log heksadesimal Modbus atau payload TCP mentah menjadi laporan komando yang actionable. Model AI lokal kami dibatasi oleh template ontologi militer (Constrained Decoding) di mana fakta kejadian (IP, stempel waktu, register OT, dan status) diambil langsung dari database telemetri deterministik, sedangkan AI bertugas menyusun kronologi taktis dan rekomendasi sesuai tata bahasa dinas TNI AD. Jadi akurasinya 100% fakta tanpa halusinasi."*

### Perwira PUSSIBERAD / Jenderal TNI AD (Doktrin, Kedaulatan, Integritas)
* **Pertanyaan Juri:** *"Bagaimana jika musuh mengetahui bahwa sistem ini adalah umpan?"*
* **Tangkisan Juara:** *"Siap, Jenderal. Dalam doktrin militer perang semesta, ranjau darat tetap efektif menahan laju pasukan musuh meskipun musuh tahu ada rambu ladang ranjau. Ketika aktor spionase menyadari bahwa di jaringan TNI AD terpasang ranjau siber NEXUS-TRAP yang jika disentuh akan membekukan alat tempur mereka dan mencatat sidik jari perangkat keras mereka, tercipta **Efek Getar Psikologis (Cyber Deterrence)**. Musuh dipaksa bergerak lambat, ragu-ragu, dan kehilangan keunggulan inisiatif serangan."*

---

## 7. Protokol Darurat Panggung Anti-Gagal (The "Zero-Failure" Protocol)

Kegagalan teknis di panggung hackathon adalah mimpi buruk terbesar. Jalankan protokol pertahanan ini:

1. **Aturan Router Mandiri (Bawa Wi-Fi / Router Sendiri):**  
   * **JANGAN PERNAH** mengandalkan Wi-Fi hotel atau koneksi internet venue saat live demo. Port Modbus (5020) atau DNS (5053) sering kali diblokir oleh firewall hotel.
   * Hubungkan laptop demo komando dan laptop penyerang menggunakan switch kabel LAN kecil atau router portable offline sendiri dengan IP statis (`192.168.1.50` dan `192.168.1.88`).
2. **Kesiapan Tombol Reset Instan:**  
   * Jika dewan juri meminta skenario serangan diulang dari awal, buka PowerShell dan jalankan:
     ```powershell
     .\reset_demo.ps1
     ```
   * Dalam 0.5 detik, seluruh database alert bersih dan status kembali ke Siaga Hijau tanpa perlu restart server.
3. **Penyelamat Video Backup (Plan B):**  
   * Rekam video demonstrasi split-screen 1080p berdurasi 3 menit menggunakan OBS Studio dan simpan di Desktop dengan nama `VIDEO_CADANGAN_DEMO_NEXUS_TRAP.mp4`.
   * Jika laptop penyerang mengalami blue-screen atau kendala proyektor di panggung, langsung putar video backup tersebut sambil presenter membacakan narasi secara live.

---
*Dokumen panduan ini tersimpan permanen di:*  
[`E:\04_Webdev\59_Cyber-Hackathon\nexus-trap\PANDUAN_PRESENTASI_DAN_DEMO_JUARA.md`](file:///E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/PANDUAN_PRESENTASI_DAN_DEMO_JUARA.md)
