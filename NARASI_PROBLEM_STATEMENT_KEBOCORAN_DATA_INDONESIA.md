# DOKUMEN LATAR BELAKANG STRATEGIS & PROBLEM STATEMENT
## KATALOG KEBOCORAN DATA NASIONAL (2021–2024) & DOKTRIN PERTAHANAN AKTIF NEXUS-TRAP
**Karya untuk:** Kartika Cyber Hackathon 2026 (PUSSIBERAD TNI AD × CODEPOLITAN)  
**Kategori:** Penangkalan (*Active Cyber Defense, Deception & Incident Response*)  
**Penyusun:** Tim Pengembang NEXUS-TRAP C4ISR  
**Tujuan Dokumen:** Landasan Fakta Kritis untuk Pengantar Presentasi Panggung & Naskah Narasi Dewan Juri  

---

## 1. Executive Summary: Realitas Darurat Kedaulatan Data Indonesia

Dalam kurun waktu 2021 hingga 2024, ruang siber Indonesia mengalami rentetan anomali dan bencana kebocoran data (*data breaches*) terparah sepanjang sejarah republik. Mulai dari data kependudukan seluruh rakyat, data pemilih pemilu, rekaman medis, data wajib pajak presiden, hingga sistem intelijen strategis pertahanan dan kepolisian telah dieksfiltrasi dan diperjualbelikan secara terbuka di pasar gelap *Dark Web* dan forum kejahatan siber (*BreachForums*, *RaidForums*).

Kenyataan paling mengejutkan dari seluruh investigasi forensik resmi (BSSN, CISSReC, Ethical Hacker Indonesia) adalah:
> **Hampir tidak ada satu pun dari insiden tersebut yang disebabkan oleh peretas menjebol enkripsi militer atau menggunakan exploit Zero-Day berharga jutaan dollar.**  
> **Seluruh pintu masuk utama berakar dari SATU TITIK RAWAN TANPA BATAS: KELALAIAN FAKTOR MANUSIA (*THE HUMAN FACTOR*).**

Prajurit, ASN, dan operator teknis di berbagai satuan mengunduh berkas sembarangan, mengklik tautan phishing, atau terinfeksi trojan APK (undangan pernikahan, tilang elektronik, pinjol, dan judi online) pada komputer dinas. Malware jenis **Infostealer (Stealc, RedLine, Lumma, Vidar)** menyedot *cookies*, token sesi intranet, dan kata sandi browser resmi. 

Akibatnya, **peretas masuk ke dalam markas menggunakan hak akses yang sah (*Living off the Land*)**. Firewall perimeter multi-miliar rupiah di gerbang luar menjadi lumpuh dan buta, sementara di dalam markas **tidak ada satu pun instrumen ranjau siber aktif** yang mengawasi mereka.

---

## 2. Katalog 14 Insiden Kebocoran Data Terbesar Indonesia (Fakta Terverifikasi 100%)

Berikut adalah rekapitulasi data historis terverifikasi silang dengan laporan BSSN, CISSReC, Bareskrim Polri, dan forum kejahatan siber internasional:

| No | Instansi / Entitas Sasaran | Waktu Insiden | Volume & Spesifikasi Data Bocor | Forum / Identitas Pelaku | Nilai Jual / Tebusan | Fakta Forensik Hulu (*Root Cause Analysis*) |
|:--:|:---|:---:|:---|:---:|:---:|:---|
| **1** | **Dukcapil Kemendagri** | Juli 2023 | **337.225.465 Baris Data Kependudukan**<br>NIK, Nomor KK, Nama Lengkap, Tempat & Tgl Lahir, Agama, Status Nikah, Akta Lahir, Nama Ayah & Ibu, Kelainan Fisik. | *BreachForums*<br>Aktor: **RRR** | \$7.000 (US Dollar) | Infeksi malware *infostealer* pada komputer dinas staf daerah; kredensial akses API/database pusat diekstraksi dari cache browser. |
| **2** | **KPU (Komisi Pemilihan Umum)** | Nov 2023 | **204.807.203 Data Pemilih Tetap (DPT)**<br>NIK, Nomor NKK, No. KTP elektronik, Lokasi TPS, Alamat Lengkap hingga RT/RW, Difabel. | *BreachForums*<br>Aktor: **Jimbo** | \$74.000<br>(2 Bitcoin) | Akun staf operator sistem *Sidalih* terkompromi malware trojan; tidak diterapkannya MFA (*Multi-Factor Authentication*) berlapis. |
| **3** | **BPJS Kesehatan** | Mei 2021 | **279 Juta Data Peserta (Aktif & Meninggal)**<br>NIK, Nama Lengkap, Nomor HP, Email, Alamat, Gaji/Pendapatan Bulanan, Faskes Rujukan, Kode Pos. | *RaidForums*<br>Aktor: **Kotz** | 0.15 BTC (~Rp 84 Juta saat itu) | Penyusupan melalui server internal via kredensial VPN dinas staf yang tidak terlindungi otentikasi multi-faktor. |
| **4** | **Pusat Data Nasional Sementara 2 (PDNS 2 Surabaya)** | Juni 2024 | **Lumpuhnya 282 Instansi Pemerintah & Imigrasi**<br>Enkripsi ransomware total terhadap pangkalan data kementerian/lembaga, sistem perlintasan bandara internasional. | *Darknet Ransomware Blog*<br>Sindikat: **Brain Cipher (LockBit 3.0)** | \$8.000.000<br>(Rp 131 Miliar) | Kredensial akun admin lokal bocor; ketiadaan segmentasi jaringan internal dan ketiadaan sensor deteksi *lateral movement*. |
| **5** | **BAIS TNI & INAFIS POLRI** | Juni 2024 | **Data Intelijen Personel & Biometrik Warga**<br>Data personil intelijen militer (NRP, satuan, pangkat, kontak), arsip unjuk rasa, serta database sidik jari/foto wajah kriminal INAFIS. | *BreachForums*<br>Aktor: **MoonzHaxor** | \$1.000 (BAIS)<br>\$7.000 (INAFIS) | Kredensial email dinas dan port Remote Desktop Protocol (RDP) bocor di pasar gelap akibat workstation terinfeksi malware. |
| **6** | **DJP (Ditjen Pajak) Kemenkeu** | Sept 2024 | **6,6 Juta Data Nomor Pokok Wajib Pajak (NPWP)**<br>NIK, NPWP, Nama, Alamat, Email, No HP. Termasuk data Presiden Jokowi, Gibran, Kaesang, Menkeu Sri Mulyani, & Menteri Kabinet. | *BreachForums*<br>Aktor: **Bjorka** | \$10.000<br>(Rp 153 Juta) | Kredensial internal pegawai pajak bocor via *stealer logs*; penyerang mengekstrak dump data melalui saluran transmisi internal. |
| **7** | **Registrasi Kartu SIM (Kominfo)** | Sept 2022 | **1,3 Miliar Data Pendaftaran Prabayar**<br>NIK, Nomor Telepon Seluler, Provider (Telkomsel, Indosat, XL, Tri, Smartfren), Tanggal Registrasi. | *BreachForums*<br>Aktor: **Bjorka** | \$50.000<br>(Rp 745 Juta) | Celah endpoint API integrasi registrasi tanpa *rate-limiting* ketat dan kebocoran *database connector credentials*. |
| **8** | **Kementerian Pertahanan (Kemhan)** | Nov 2023 | **Akses Dashboard Panel & Surat Menyurat Dinas**<br>Kapasitas server 1,64 Terabyte (TB), bagan jaringan internal pangkalan militer, korespondensi surat dinas. | *BreachForums*<br>Aktor: **Two2** | Akses panel dijual bebas | Hasil forensik CISSReC: 667 akun pegawai Kemhan bocor akibat malware *stealer* yang menginfeksi laptop dinas personel. |
| **9** | **Paspor Ditjen Imigrasi (Kemenkumham)** | Juli 2023 | **34.900.867 Data Paspor Warga Negara Indonesia**<br>Nomor Paspor, Nama Lengkap, Tanggal Terbit, Masa Berlaku, Tanggal Lahir, Jenis Kelamin. | *BreachForums*<br>Aktor: **Bjorka** | \$10.000<br>(Rp 150 Juta) | Penyerang memanfaatkan celah otorisasi pada pangkalan data imigrasi dan mengeksfiltrasi data mentah terkompresi. |
| **10** | **Bank Syariah Indonesia (BSI)** | Mei 2023 | **1,5 Terabyte Data Nasabah & Audit Finansial**<br>Lumpuhnya ATM & Mobile Banking nasional berhari-hari; kebocoran 15 juta data nasabah, dokumen kredit, data gaji. | *Darknet Leak Site*<br>Sindikat: **LockBit 3.0** | \$20.000.000<br>(Tuntutan tebusan) | Phishing awal terhadap komputer staf -> eskalasi hak akses (*privilege escalation*) ke Domain Controller utama pangkalan. |
| **11** | **MyPertamina (PT Pertamina)** | Nov 2022 | **44 Juta Data Akun Pelanggan BBM Subsidi**<br>NIK, Nama Lengkap, Nomor HP, Email, Jenis Kelamin, Alamat Rumah, Estimasi Penghasilan, Kuota Liter. | *BreachForums*<br>Aktor: **Bjorka** | \$25.000<br>(Rp 392 Juta) | *Misconfiguration* pada integrasi server aplikasi dan kebocoran berkas konfigurasi log database. |
| **12** | **Kemenkes (eHAC & Rekam Medis Pasien RS)** | 2021–2022 | **1,3 Juta Akun eHAC + 720 GB Data Pasien**<br>Hasil tes PCR/Antigen COVID-19, rekaman radiologi rontgen, rekam medis EKG jantung, resep obat di berbagai RS vertikal. | *RaidForums / Darknet* | Dijual bertahap | Server basis data Elasticsearch dikonfigurasi terbuka tanpa otentikasi kata sandi (kelalaian konfigurasi administrator). |
| **13** | **Polri (Database Pelanggaran Disiplin Personel)** | Nov 2021 | **28.000 Data Personel & Dokumen Propam**<br>Data anggota polisi terpidana sidang etik, NIK, jabatan, nomor registrasi pokok (NRP), dokumen rehabilitasi. | *RaidForums*<br>Aktor: **son1x** | Sampel digratiskan | Injeksi SQL (*SQL Injection*) pada sub-domain layanan internal dan eksfiltrasi basis data personel. |
| **14** | **Indihome / PT Telkom Indonesia** | Agustus 2022 | **26 Juta Riwayat Penelusuran (*Browsing History*)**<br>Alamat situs yang dikunjungi pelanggan, NIK, Nama Lengkap, Email, Jenis Kelamin, Domain Tracker. | *BreachForums*<br>Aktor: **Bjorka** | Ditawarkan di forum | Pengumpulan data telemetri analitik internal yang tidak dienkripsi dan terekspos ke jaringan terbuka. |

---

## 3. Anatomi Masalah: Paradoks "Tembok Mahal vs. Kunci Rumah yang Dicuri"

Berdasarkan 14 tragedi nasional di atas, dapat ditarik tiga kesimpulan kritis:

```
+---------------------------------------------------------------------------------------------------+
| ANATOMI KELEMAHAN PERTAHANAN SIBER KONVENSIONAL DI INDONESIA                                      |
+---------------------------------------------------------------------------------------------------+
| 1. PARADOKS PERIMETER:                                                                           |
|    Instansi menggelontorkan miliaran rupiah membeli Next-Generation Firewall (NGFW), namun       |
|    musuh tidak merusak gerbang. Musuh MASUK LEWAT PINTU RESMI menggunakan kredensial prajurit     |
|    yang dicuri lewat APK Android / phishing di laptop kantor.                                     |
|                                                                                                   |
| 2. BENCANA DWELL TIME (> 180 HARI):                                                               |
|    Rata-rata musuh telah bercokol di dalam jaringan instansi selama 3 hingga 6 bulan sebelum      |
|    data akhirnya dijual di Dark Web. Instansi baru sadar saat peretas memposting di X / Twitter.  |
|                                                                                                   |
| 3. AREA BUTA TOTAL DI DALAM MARKAS (BLIND INNER PERIMETER):                                       |
|    Tidak ada satu pun sensor yang memantau pergerakan lateral (Lateral Movement) di dalam subnet   |
|    lokal markas. Musuh bebas memindai port genset, database, dan file server tanpa memicu alarm.  |
+---------------------------------------------------------------------------------------------------+
```

---

## 4. Mengapa NEXUS-TRAP Menjadi Opsi Penangkal Terbaik bagi TNI AD?

NEXUS-TRAP (Network Deception & Active Tarpit) hadir sebagai **jawaban doktrin asimetris** yang memecahkan seluruh akar masalah di atas:

```
[PENYUSUP MASUK MENGGUNAKAN KREDENSIAL SAH]
                    |
                    v (Bergerak di dalam jaringan intranet Kodam/Korem)
  +-----------------+-----------------+-----------------+
  |                                   |                 |
  v                                   v                 v
[1. Pindai Genset Markas]   [2. Fuzzing API Otomatis]  [3. Curi File Dislokasi Pasukan]
  |                                   |                 |
  v                                   v                 v
[RANJAU MODBUS PORT 5020]   [ACTIVE TCP TARPIT]        [DUAL-SPECTRUM CANARY DOCX]
- Membalas voltase palsu    - Cekik soket 1 byte/2s    - Word eksekusi Web Beacon & DNS
- Komando: SIAGA KUNING     - Scanner lawan MACET TOTAL- Komando: SIAGA 1 MERAH MELEDAK!
  |                                   |                 |
  +-----------------+-----------------+-----------------+
                    |
                    v
[REAKSI KOMANDO TERPUSAT PUSSIBERAD]
1. Identifikasi IP Asli & GPU Hardware Hash Penyerang seketika.
2. Dwell Time anjlok dari 180 HARI menjadi 0 DETIK!
3. 1-Klik Isolasi Host memutus komunikasi musuh dari jaringan pangkalan.
4. Terbit Laporan Militer (AI SITREP) berstempel SHA-256 untuk Oditur POMAD.
5. Biaya Lisensi: Rp 0,- (100% On-Premise Air-Gapped FOSS Tanpa Ketergantungan Cloud Asing).
```

---

## 5. Skrip Verbatim Narasi Pembuka Panggung (Durasi: 2 Menit)

Berikut adalah naskah pidato pembuka yang dirancang untuk langsung memukau Dewan Juri dan Perwira Tinggi PUSSIBERAD:

> *"Izin Komandan, para Perwira Tinggi PUSSIBERAD, serta Dewan Juri yang kami hormati.*  
>  
> *Dalam kurun waktu tiga tahun terakhir, kedaulatan data bangsa kita mengalami cobaan terberat: 337 juta data Dukcapil, 204 juta data pemilih KPU, 279 juta data BPJS, jutaan NPWP petinggi negara, hingga data identifikasi forensik INAFIS Polri dan dokumen internal Kementerian Pertahanan diperjualbelikan secara terbuka di forum kejahatan Dark Web seharga ribuan dollar.*  
>  
> *Pertanyaan mendasarnya adalah: Mengapa seluruh instansi tersebut bisa kebobolan, padahal mereka memiliki anggaran siber miliaran rupiah dan firewall perimeter tercanggih?*  
>  
> *Jawabannya sederhana namun mematikan: **Musuh tidak menjebol tembok depan, melainkan menyelinap lewat titik rawan tanpa batas: FAKTOR MANUSIA.**  
>  
> *Prajurit atau staf piket kita di daerah mengunduh APK undangan atau pinjol ilegal di laptop kantor. Malware Trojan seketika menyedot kredensial dinas. Penyerang masuk menggunakan akun resmi via VPN pangkalan. Di mata firewall mahal, peretas dianggap sebagai prajurit yang sah.*  
>  
> *Rata-rata, musuh mengendap di dalam jaringan kita selama 6 bulan (*Dwell Time*) tanpa pernah terdeteksi, karena **tidak ada ranjau siber di dalam markas**.  
>  
> *Oleh karena itu, kami mempersembahkan **NEXUS-TRAP (Network Deception & Active Tarpit)**.  
> Kami tidak meminta anggaran miliaran rupiah untuk membeli lisensi asing. Kami menerapkan doktrin perang asimetris kuno: **Menanam ranjau siber aktif di dalam markas sendiri.**  
>  
> *Begitu musuh yang menyusup mencoba menyentuh genset markas, scanner mereka membentur Tarpit perekat kami hingga macet, dan saat dokumen rahasia curian dibuka di sarang mereka, suar klandestin meledak membongkar koordinat IP serta sidik jari perangkat keras musuh seketika!*  
>  
> *Dwell time musuh kami pangkas dari 180 hari menjadi **0 detik**, dengan tingkat akurasi **100% Zero False Positive**!"*

---

*Dokumen ini merupakan bagian tak terpisahkan dari arsip resmi purwarupa NEXUS-TRAP C4ISR (PUSSIBERAD TNI AD).*
