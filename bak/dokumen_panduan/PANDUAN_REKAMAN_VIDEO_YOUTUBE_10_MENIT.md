# PANDUAN REKAMAN VIDEO DEMO YOUTUBE 10 MENIT
## KARTIKA CYBER HACKATHON 2026 (PUSSIBERAD TNI AD × CODEPOLITAN)
**Kategori:** Penangkalan (*Active Cyber Defense & Deception*)  
**Batas Durasi Resmi Rulebook:** Maksimal 10 (sepuluh) menit  
**Format Resolusi Video:** Full HD (1920×1080) 60 FPS (Widescreen 16:9)  
**Platform Publikasi:** YouTube (Unlisted atau Public)

---

## 1. Metadata Publikasi YouTube (Siap Salin)

### Judul Video Resmi:
```text
NEXUS-TRAP: Platform Pertahanan Siber Aktif & Deception Terpadu TNI AD | Kartika Cyber Hackathon 2026
```

### Deskripsi Video YouTube (Lengkap dengan Timestamps):
```text
Video Demonstrasi dan Paparan Solusi Resmi untuk Kartika Cyber Hackathon 2026
Penyelenggara: Pusat Siber Angkatan Darat (PUSSIBERAD) × PT Codepolitan Integrasi Indonesia

Proyek: NEXUS-TRAP (Network Deception & Active Tarpit)
Kategori: PENANGKALAN (Active Cyber Defense, Deception & Incident Response)
Arsitektur: 100% On-Premise Air-Gapped (Nir-Ketergantungan Cloud Asing)

TIMESTAMPS:
00:00 - 01:15 | 1. Latar Belakang: Krisis Asimetris di Satuan Teritorial TNI AD
01:15 - 02:45 | 2. Paradoks Pertahanan Pasif & Solusi Doktrin NEXUS-TRAP
02:45 - 04:00 | 3. Arsitektur 4 Pilar & Eliminasi Alarm Palsu (Zero False Positive)
04:00 - 05:15 | 4. Live Demo Babak 1: Intersepsi Pengintaian OT Modbus (Siaga Kuning)
05:15 - 06:30 | 5. Live Demo Babak 2: Pembekuan Scanner Musuh via Active Tarpit
06:30 - 07:45 | 6. Live Demo Babak 3: Suar Canary Tembus VM & Karantina Host 1-Klik
07:45 - 08:45 | 7. Live Demo Babak 4: Otomasi AI Military SITREP Berstempel SHA-256
08:45 - 09:30 | 8. Fitur Interaktif QR Code Detonation untuk Dewan Juri
09:30 - 10:00 | 9. Kelayakan Implementasi di Seluruh Kodim & Penutup

Teknologi: FastAPI, React 18, TailwindCSS, Raw Modbus TCP Daemons, Asynchronous Sticky Tarpit, OpenXML Canary Tokens, SQLite Cryptographic Hash-Chain (POMAD Standard), Local AI/SLM.

#Pussiberad #TNIAD #Codepolitan #KartikaCyberHackathon #CyberSecurity #ActiveDefense #Honeypot #Tarpit #C4ISR
```

---

## 2. Persiapan Teknis Rekaman (Checklist Sebelum Rekam)

1. **Software Perekam:** Gunakan OBS Studio (Direkomendasikan) atau Windows Game Bar (`Win + G`).
   * Canvas Resolution: 1920×1080.
   * Frame Rate: 60 FPS.
   * Audio Mic: Jernih, gunakan noise suppression.
   * Desktop Audio: Pastikan aktif agar efek audio Web Audio API (blip radar dan sirine Siaga Merah) terdengar jelas di rekaman.
2. **Pengaturan Tampilan Layar (Split-Screen):**
   * Sisi Kiri (60% layar): Browser menampilkan C4ISR Dashboard di `http://localhost:3000` (Tekan F11 untuk fullscreen).
   * Sisi Kanan (40% layar): Terminal PowerShell / Kali Linux untuk menjalankan skrip penyerang dari folder `attacker_box`.
3. **Status Awal:** Jalankan `.\reset_demo.ps1` sebelum memulai rekaman agar dashboard berada dalam status **SIAGA 3 (HIJAU)**.

---

## 3. Skrip Kata-demi-Kata & Panduan Aksi (Teleprompter 10 Menit)

### [00:00 - 01:15] Segmen 1: Latar Belakang & Ancaman Riil di Lapangan
* **Tampilan Visual:** Tampilkan Slide 1 Cover PPTX atau Dashboard C4ISR Status Siaga Hijau.
* **Narasi Suara:**
  > *"Assalamu’alaikum Warahmatullahi Wabarakatuh, salam sejahtera, Syalom, Om Swastiastu, Namo Buddhaya.  
  > Yang terhormat Dewan Juri Kartika Cyber Hackathon 2026 dari PUSSIBERAD TNI AD dan CODEPOLITAN.  
  > Dalam perang siber modern, musuh tidak lagi menyerang perimeter pusat di Mabesad yang berbenteng tebal. Musuh menyusup melalui titik terlemah: satuan teritorial kewilayahan di Kodam, Korem, hingga Kodim.  
  > Faktanya, laptop dinas staf administrasi di daerah rentan terinfeksi malware Infostealer akibat maraknya peredaran APK ilegal—seperti jebakan pinjol dan judi online. Sekali laptop dinas staf piket terinfeksi, peretas asing mulai merayap dalam senyap, mencari dokumen rahasia rencana operasi dan menyusup ke fasilitas vital markas."*

---

### [01:15 - 02:45] Segmen 2: Mengapa Firewall & Antivirus Konvensional Gagal?
* **Tampilan Visual:** Tampilkan Diagram Kasus Nyata (`screenshots/diagram_2_workflow_incident.png`) atau Slide 2 PPTX.
* **Narasi Suara:**
  > *"Mengapa sistem pertahanan lama kita gagal?  
  > Pertama, peretas menggunakan kredensial resmi staf yang tercuri—teknik Living off the Land. Firewall tidak bisa membedakan mana klik prajurit kita dan mana klik peretas.  
  > Kedua, krisis Alert Fatigue. SIEM konvensional memproduksi belasan ribu log bising setiap hari. Personel Infolahta di daerah kewalahan dan tanda bahaya tenggelam dalam lautan alarm palsu.  
  > Ketiga, kerentanan fatal fasilitas fisik Operational Technology. Telemetri genset darurat dan radar pangkalan berjalan menggunakan protokol Modbus TCP pada Port 502 tanpa password dan tanpa enkripsi.  
  > Untuk itulah kami mempersembahkan: **NEXUS-TRAP (Network Deception & Active Tarpit)**. Platform pertahanan siber aktif yang mengubah seluruh jaringan satuan TNI AD menjadi ladang ranjau klandestin."*

---

### [02:45 - 04:00] Segmen 3: Arsitektur 4 Pilar & Doktrin Seni Perang Kuno
* **Tampilan Visual:** Tampilkan Slide Arsitektur 4 Pilar (`screenshots/slide_04_arsitektur_4_pilar.svg`) lalu beralih ke browser Dashboard C4ISR (`http://localhost:3000`).
* **Narasi Suara:**
  > *"NEXUS-TRAP berdiri di atas 4 pilar taktis:  
  > 1. **Umpan Fasilitas OT Modbus:** Meniru register genset pangkalan secara presisi.  
  > 2. **Active Asynchronous Tarpit Crasher:** Bukan sekadar mencatat log, tetapi secara fisik mencekik dan membekukan scanner musuh.  
  > 3. **Dual-Spectrum Canary Token:** Suar klandestin yang menembus isolasi mesin virtual lawan.  
  > 4. **AI Military SITREP Berstempel SHA-256:** Otomasi laporan intelijen militer yang sah secara hukum di hadapan Polisi Militer (POMAD).  
  > Dan yang terpenting: sistem kami memegang doktrin **Zero False Positive**. Aset umpan kami tidak memiliki fungsi operasional legal. Siapa pun yang menyentuhnya, 100% dipastikan adalah anomali atau peretas!"*

---

### [04:00 - 05:15] Segmen 4: Live Demo Babak 1 — Pengintaian OT Modbus
* **Tampilan Visual:** Pindah ke mode Split-Screen (Kiri C4ISR Dashboard, Kanan Terminal).
* **Aksi Operator:** Di terminal kanan jalankan:
  ```bash
  python attacker_box/01_recon_modbus.py 127.0.0.1 5020
  ```
* **Efek Sistem:** Bunyi blip radar berbunyi, status berubah **SIAGA KUNING**, terminal kanan menerima voltase palsu 380V.
* **Narasi Suara:**
  > *"Mari kita saksikan demonstrasi langsung. Di layar kanan adalah terminal penyerang yang telah menyusup ke intranet Kodim. Penyerang mulai mencari kontrol genset markas pada Port 502 Modbus TCP.  
  > Perhatikan layar kiri meja komando: seketika membunyikan Siaga Kuning!  
  > Hebatnya, sensor kami membalas dengan register palsu: tegangan 380V, 50Hz, BBM 85%. Mengadopsi Doktrin Perang Stratagem 25, penyerang dibuat yakin telah menemukan genset asli, padahal koordinat mereka telah terekam di meja komando."*

---

### [05:15 - 06:30] Segmen 5: Live Demo Babak 2 — Pelumpuhan Scanner via Tarpit
* **Tampilan Visual:** Fokus pada tombol Tarpit di Dashboard C4ISR dan Terminal Penyerang.
* **Aksi Operator:**
  1. Di layar kiri, tekan tombol **[AKTIFKAN TARPIT CRASHER]** (atau tekan hotkey `T`).
  2. Di terminal kanan, jalankan scanner:
     ```bash
     python attacker_box/02_scanner_tarpit.py 127.0.0.1 8000
     ```
* **Efek Sistem:** Terminal kanan MACET TOTAL (0.0 req/s), layar kiri counter `LOCKED THREADS` naik.
* **Narasi Suara:**
  > *"Penyerang kemudian meluncurkan alat otomatis multi-threaded untuk membobol direktori pangkalan.  
  > Operator komando mengaktifkan Tarpit Crasher. Perhatikan terminal penyerang di layar kanan: seketika MACET TOTAL, kecepatan anjlok ke 0 request per detik!  
  > Mesin Asynchronous Sticky Tarpit kami menahan TCP Window 1 byte per beberapa detik. Seluruh worker thread musuh tersedot dan lumpuh, sementara server pangkalan kita tetap ringan karena menggunakan non-blocking I/O dengan konsumsi memori di bawah 120 MB."*

---

### [06:30 - 07:45] Segmen 6: Live Demo Babak 3 — Suar Canary & Isolasi 1-Klik
* **Tampilan Visual:** Split-screen aktif.
* **Aksi Operator:**
  1. Di terminal kanan, buka berkas dokumen umpan:
     ```bash
     python attacker_box/03_trigger_canary.py 127.0.0.1 5053
     ```
  2. Layar kiri MELEDAK **SIAGA 1 MERAH**, sirine berbunyi, titik Kodam Jaya berkedip merah.
  3. Di terminal kanan jalankan ping: `ping 192.168.1.88 -t` (atau jelaskan isolasi).
  4. Di layar kiri, tekan tombol merah **[ISOLASI HOST TERINFEKSI]** (atau tekan hotkey `K`).
* **Narasi Suara:**
  > *"Penyerang frustrasi lalu mengunduh dokumen dinas rahasia umpan dan membukanya di mesin virtual terisolasi.  
  > Seketika meja komando MELEDAK SIAGA 1 MERAH! Sirine bahaya menyalak, titik Kodam Jaya berkedip merah terang!  
  > Suar DNS klandestin kami menembus isolasi sandbox VM musuh. Di kartu Adversary Dossier kanan bawah, identitas hardware penyerang, WebGL GPU hash, dan tanda tangan JA4 scanner mereka telah terkunci permanen!  
  > Untuk mengamankan markas, Komandan cukup menekan satu tombol: **ISOLASI HOST TERINFEKSI**. Dalam tempo 1 detik, aturan kernel firewall memutus total host terkompromi dari seluruh rute pangkalan!"*

---

### [07:45 - 08:45] Segmen 7: Live Demo Babak 4 — Otomasi AI Military SITREP
* **Tampilan Visual:** Klik tombol **[GENERATE AI MILITARY SITREP]** (atau hotkey `S`). Modal laporan militer muncul di layar.
* **Aksi Operator:** Scroll pelan modal SITREP memperlihatkan kop resmi, nomor surat, tabel IoC, dan stempel SHA-256.
* **Narasi Suara:**
  > *"Langkah terakhir pasca-insiden: Operator menekan tombol **GENERATE AI MILITARY SITREP**.  
  > Sistem secara otonom merumuskan Laporan Situasi Militer resmi berklasifikasi RAHASIA berstandar Mabesad. Laporan ini lengkap dengan nomor surat dinas, kronologi teknis 5W+1H, tabel Indikator Kompromi (IoC), dan ditutup dengan Segel Integritas Kriptografis SHA-256.  
  > Seluruh rantai peristiwa ini tersimpan dalam SQLite hash-chaining berstempel HMAC-SHA256, menjamin keabsahan barang bukti digital di hadapan persidangan Oditur Militer."*

---

### [08:45 - 09:30] Segmen 8: Fitur Interaktif QR Code Demo untuk Dewan Juri
* **Tampilan Visual:** Buka halaman QR Code di `http://localhost:8000/canary-qr` (atau klik tombol kuning QR DEMO JURI).
* **Narasi Suara:**
  > *"NEXUS-TRAP juga kami lengkapi dengan fitur **Live Audience Detonation**.  
  > Pada saat presentasi offline di hadapan Dewan Juri di Hotel Aston Kartika tanggal 24 November nanti, Dewan Juri dapat langsung memindai QR Code taktis ini menggunakan kamera ponsel pribadi.  
  > Ketika juri mengunduh dan membuka berkas dokumen uji coba di Word atau WPS HP mereka, detik itu juga meja komando di proyektor akan membunyikan Siaga Merah dan menampilkan alamat IP ponsel juri secara langsung! Ini adalah pembuktian langsung yang tak terbantahkan."*

---

### [09:30 - 10:00] Segmen 9: Kelayakan Implementasi di Jajaran Satuan & Penutup
* **Tampilan Visual:** Tampilkan Slide Penutup / Arsitektur Hub-and-Spoke.
* **Narasi Suara:**
  > *"NEXUS-TRAP dibangun 100% on-premise, mandiri, bebas ketergantungan cloud asing, dan siap dipasang di seluruh Kodim, Korem, hingga Kodam jajaran TNI AD besok pagi.  
  > Inilah kontribusi nyata kami untuk mewujudkan Kedaulatan Pertahanan Siber Semesta yang Mandiri, Tangguh, dan Berwibawa.  
  > Terima kasih. Cakra Yudha Waskita!  
  > Wassalamu’alaikum Warahmatullahi Wabarakatuh."*

---

## 4. Tips Pascamerekam
1. Periksa kembali total durasi video di timeline editing (Pastikan di bawah 09:55 menit agar tidak melewati batas 10 menit rulebook).
2. Export video dengan format **MP4 / H.264**, 1080p, audio AAC 192 kbps.
3. Upload ke YouTube, paste Judul, Deskripsi, dan Timestamps di atas.
4. Salin URL link YouTube (misal: `https://youtu.be/xxxxxx`) ke formulir submission platform Codepolitan.
