# PANDUAN & NASKAH LENGKAP VIDEO DEMO PANGGUNG
## PURWARUPA NEXUS-TRAP C4ISR (PUSSIBERAD TNI AD)

**Peruntukan:** Video Presentasi / Pitching & Demonstrasi Produk (Durasi Target: 3 – 5 Menit)  
**Kompetisi:** Kartika Cyber Hackathon 2026 (PUSSIBERAD TNI AD × CODEPOLITAN)  
**Target Audiens:** Dewan Juri Eksekutif, Perwira Tinggi Militer, & Penonton Non-Teknis  
**Fokus Utama:** Menyampaikan konsep pertahanan aktif asimetris menggunakan **analogi dunia nyata**, bahasa lugas, dan pembuktian visual sebab-akibat secara langsung.

---

## 1. Panduan Tata Letak Rekaman Layar (Split-Screen Blueprint)

Untuk memaksimalkan dampak visual, gunakan format **layar terbagi dua (*split-screen*)** menggunakan OBS Studio atau software perekam layar:

```
+---------------------------------------------------+---------------------------------------------------+
|               SISI KIRI LAYAR                     |                 SISI KANAN LAYAR                  |
|          "PERSPEKTIF PENYERANG / MUSUH"           |          "PUSAT KOMANDO C4ISR NEXUS-TRAP"         |
|         (Terminal Penyerang / Layar HP)           |          (Tampilan Petugas / Analis Siber)        |
+---------------------------------------------------+---------------------------------------------------+
| [AKSI 1] Penyerang membuka file DOCX atau juri    | [RESPONS 1] Sirene berbunyi, status meledak       |
|          melakukan scan QR dari smartphone.       |             SIAGA 1 MERAH, IP & Device terdeteksi.|
|                                                   |                                                   |
| [AKSI 2] Penyerang menjalankan brute-force/scan   | [RESPONS 2] Widget Tarpit berputar, kecepatan     |
|          menggunakan tools otomatis.              |             dicekik, konsumsi CPU tetap < 1%.     |
|                                                   |                                                   |
| [AKSI 3] Layar penyerang terputus seketika        | [RESPONS 3] Tombol [ISOLASI] diklik, status host  |
|          (Connection Timed Out / Blocked).        |             terisolasi, AI SITREP terbit.         |
+---------------------------------------------------+---------------------------------------------------+
```

---

## 2. Naskah Verbatim Lengkap & Petunjuk Sutradara (Scene by Scene)

### SCENE 01: Hook Pembuka & Latar Belakang Masalah (Durasi: ~45 Detik)
* **[Tampilan Layar]:** Wajah pembicara (kamera penuh) atau menampilkan Slide 2: *"Penyusup Memakai Kredensial Sah. Firewall Buta."*
* **[Mood / Tempo]:** Serius, tegas, berwibawa, tempo sedang.

> **[BACA NASKAH]:**  
> *"Ada pepatah keamanan siber yang sangat terkenal:  
> **'Hanya ada dua jenis institusi di dunia: institusi yang sudah diretas, dan institusi yang belum tahu bahwa mereka telah diretas.'**  
>  
> Mengapa hal ini bisa terjadi?  
> Karena di setiap sistem pertahanan tercanggih di dunia, selalu ada satu titik rawan tanpa batas yang tidak pernah bisa ditambal oleh firewall termahal sekalipun: yaitu **Faktor Manusia (*The Human Vector*)**.  
>  
> Ratusan juta data kependudukan, pemilih, hingga surat dinas instansi di Indonesia bocor bukan karena peretas merusak enkripsi militer. Musuh masuk lewat pintu depan menggunakan kata sandi staf yang dicuri lewat malware APK di ponsel atau phishing di komputer kantor. Di mata firewall perimeter gerbang depan, peretas dianggap prajurit yang sah.  
>  
> Menyadari kelemahan fatal ini, dan dengan memahami bagaimana cara berpikir seorang penyusup—kami membangun **NEXUS-TRAP**.  
>  
> Prinsip kami sederhana: **Kita sediakan panggungnya di dalam markas**. Begitu musuh melangkah masuk, kita tahu detik itu juga, lalu melakukan penangkalan tepat dan cepat tanggap!"*

---

### SCENE 02: Cara Kerja & Analogi Markas (Durasi: ~25 Detik)
* **[Tampilan Layar]:** Transisi ke mode **Split-Screen**. Layar C4ISR di sebelah kanan dalam status **SIAGA HIJAU (Aman)**.

> **[BACA NASKAH]:**  
> *"Cara kerjanya dapat diibaratkan seperti mengamankan sebuah markas komando:  
> Jika musuh berhasil mencuri seragam dan kartu tanda pengenal prajurit untuk menyelinap masuk melewati pos penjagaan depan—kita tidak lagi mengandalkan pagar luar.  
>  
> **Kita ubah seluruh perabotan di dalam markas menjadi ranjau jebakan aktif.**  
> Mari kita lihat tiga pembuktian langsungnya:"*

---

### SCENE 03: Demonstrasi 1 — Umpan Dokumen Ber-GPS (Durasi: ~60 Detik)
* **[Aksi Sisi Kiri (Penyerang)]:** Buka file Word `Rahasia_Dislokasi_Pasukan_2026.docx` (atau scan QR Code dari smartphone).
* **[Aksi Sisi Kanan (C4ISR)]:** Seketika sirine audio menyala, lampu berkedip merah menyala: **[SIAGA 1 MERAH]**, kartu log muncul menampilkan alamat IP musuh, browser/aplikasi Word, dan timestamp presisi milidetik.

> **[BACA NASKAH]:**  
> *"Demonstrasi pertama: Dokumen Umpan Berpelacak (*Canary Token*).  
>  
> Di layar kiri, penyusup berhasil mencuri file berjudul **'Rahasia Dislokasi Pasukan'**. Di mata musuh dan antivirus di komputernya, berkas ini 100% bersih tanpa virus berbahaya sedikit pun, sehingga Windows Defender atau Antivirus musuh tidak akan pernah curiga.  
>  
> Namun, ibarat **tas uang bank yang disusupi pelacak GPS dan bom tinta**—perhatikan layar kanan Pusat Komando kita:  
> **Tepat pada detik pertama dokumen tersebut dibuka di laptop musuh, suar klandestin seketika meledak!**  
>  
> Pusat Komando C4ISR langsung membunyikan alarm SIAGA 1 MERAH, mengunci alamat IP asli penyerang, tipe perangkat yang digunakan, hingga koordinatnya secara deterministik tanpa ada alarm palsu (*Zero False Positive*)!"*

---

### SCENE 04: Demonstrasi 2 — Pasir Hisap Digital / Tarpit (Durasi: ~45 Detik)
* **[Aksi Sisi Kiri (Penyerang)]:** Jalankan terminal penyerang (script Gobuster / scanner). Terlihat proses scanning macet total di angka 0 req/detik.
* **[Aksi Sisi Kanan (C4ISR)]:** Indikator Tarpit menyala biru/kuning, menunjukkan transfer dicekik ke 1 byte per 2 detik, sedangkan grafik CPU server tetap sangat rendah (< 1%).

> **[BACA NASKAH]:**  
> *"Demonstrasi kedua: Pasir Hisap Digital (*Sticky Tarpit*).  
>  
> Ketika musuh mencoba memindai celah lain di dalam jaringan pangkalan, alih-alih memblokir mereka secara terbuka yang justru membuat musuh berganti taktik—kami menjebak mereka ke dalam **lem lalat digital**.  
>  
> Perhatikan terminal musuh di sebelah kiri: alat pemindai mereka mendadak membeku dan macet total. Kami mencekik koneksi soket mereka dengan hanya mengirimkan data 1 byte setiap dua detik. Alat musuh terkunci berjam-jam dan membuang habis sumber daya komputasi mereka, sementara server pertahanan kita di sebelah kanan tetap bekerja sangat ringan dan tenang."*

---

### SCENE 05: Demonstrasi 3 — Respons 1-Klik & Laporan POMAD (Durasi: ~50 Detik)
* **[Aksi Sisi Kanan (C4ISR)]:** Klik tombol merah **[ISOLASI HOST PENYERANG]**. Status musuh berubah menjadi `ISOLATED / QUARANTINED`.
* **[Aksi Sisi Kiri (Penyerang)]:** Penyerang mencoba mengetik perintah/akses apa pun $\rightarrow$ langsung muncul pesan error `Connection Timed Out / Refused`.
* **[Aksi Sisi Kanan (C4ISR)]:** Klik tombol **[LIHAT AI SITREP MILITER]**, perlihatkan dokumen resmi dengan stempel digital SHA-256 HMAC.

> **[BACA NASKAH]:**  
> *"Demonstrasi ketiga: Penangkalan Seketika & Bukti Hukum Militer.  
>  
> Komandan di posko tidak perlu menguasai baris kode rumit untuk bertindak.  
> Cukup dengan **satu kali klik pada tombol 'Isolasi Host'**, dinding api aktif seketika memutus total seluruh jalur komunikasi perangkat musuh dari markas komando kita.  
>  
> Pada saat yang sama, kecerdasan buatan Nexus-Trap langsung menerbitkan **Laporan Situasi Militer (AI SITREP)** lengkap dengan stempel kriptografis SHA-256 yang tidak dapat dimanipulasi oleh siapa pun—siap diserahkan detik itu juga sebagai alat bukti berkekuatan hukum tetap untuk penyidikan Polisi Militer (POMAD) maupun persidangan militer."*

---

### SCENE 06: Penutup & Value Proposition Strategis (Durasi: ~30 Detik)
* **[Tampilan Layar]:** Kamera penuh pembicara dengan latar belakang Dashboard C4ISR Nexus-Trap yang beroperasi aktif.
* **[Mood / Tempo]:** Mantap, meyakinkan, patriotik, berwibawa.

> **[BACA NASKAH]:**  
> *"Bapak/Ibu Dewan Juri yang kami hormati,  
> Membangun kedaulatan siber tidak selalu harus bergantung pada alat luar negeri berbiaya miliaran rupiah.  
>  
> Dengan NEXUS-TRAP:  
> 1. Waktu deteksi penyusup (*dwell time*) yang biasanya berbulan-bulan, kita pangkas menjadi **nol detik**.  
> 2. Berjalan **100% mandiri secara lokal (Air-Gapped On-Premise)** tanpa ketergantungan cloud pihak ketiga.  
> 3. Dan **biaya lisensi Rp 0,-**, sepenuhnya berdaulat di tangan prajurit TNI Angkatan Darat.  
>  
> Siap menjaga kedaulatan ruang siber Nusantara.  
> Terima kasih. Cakra!"*

---

## 3. Lembar Sontekan Analogi Non-Tech (Cheat-Sheet)

Jika ada pertanyaan spontan dari Dewan Juri non-teknis, gunakan tabel padanan istilah ini:

| Istilah Teknis Asli | Analogi Sederhana untuk Juri Non-Tech |
|:---|:---|
| **Canary Token / OpenXML Beacon** | **"Tas Uang Bank Berisi Bom Tinta & Pelacak GPS"** (Kelihatan biasa saja, tapi begitu dibuka di rumah pencuri, langsung meledak dan memancarkan koordinat lokasi). |
| **Active TCP Tarpit** | **"Pasir Hisap / Lem Lalat"** (Musuh yang masuk tidak ditembak mati, tapi dibiarkan terjebak sampai kehabisan tenaga dan alatnya macet total). |
| **Reflexive Deception (Stratagem 25/33)** | **"Taktik Perang Tipu Daya / Ranjau Palsu"** (Membiarkan musuh mengira mereka berhasil, padahal mereka sedang masuk ke dalam perangkap kita). |
| **Host Isolation via Firewall** | **"Menutup Pintu Sel Besi Otomatis"** (Mengurung musuh agar tidak bisa berbicara dengan ruangan lain di markas). |
| **HMAC-SHA256 Hash Chain** | **"Segel Lilin / Stempel Segel Militer Anti-Palsu"** (Bukti forensik yang jika diubah 1 huruf saja, seluruh stempel akan rusak dan ketahuan di pengadilan). |

---

## 4. Checklist Persiapan Teknis Sebelum Menekan Tombol "Record"

1. **Jalankan Ekosistem C4ISR:**
   ```powershell
   cd E:\04_Webdev\59_Cyber-Hackathon\nexus-trap
   .\start_all.bat
   ```
2. **Pastikan Browser Menampilkan Tampilan Optimal:**
   - Sisi Kanan: Buka `http://localhost:3000` (Fullscreen `F11`, zoom 90% atau 100%).
   - Sisi Kiri (Terminal Penyerang): Buka jendela PowerShell atau WSL Ubuntu warna gelap.
3. **Uji Coba Suara Sirine:**
   - Pastikan audio desktop terekam di OBS/Camtasia agar bunyi bip radar dan sirene alarm Siaga Merah terdengar renyah dan dramatis.
4. **Siapkan Tombol Reset Bersih:**
   - Jika ingin mengulang take rekaman dari awal, jalankan perintah reset:
   ```powershell
   .\reset_demo.ps1
   ```
   *(Sistem akan otomatis kembali ke SIAGA HIJAU bersih siap rekam ulang).*
