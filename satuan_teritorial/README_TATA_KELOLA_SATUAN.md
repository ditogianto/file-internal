# TATA KELOLA PEMISAHAN KOMANDO & SATUAN TERITORIAL
**PUSSIBERAD TNI AD // KARTIKA CYBER HACKATHON 2026**

---

## 1. Arsitektur Pemisahan Struktur

Sistem **NEXUS-TRAP** memisahkan secara ketat antara **Infrastruktur Pusat Komando** dan **Satuan Teritorial (Cabang-cabang yang dipantau)**:

```
nexus-trap/
│
├── [ PUSAT KOMANDO C4ISR / MABES PUSSIBERAD ]
│   ├── backend/                    <- Server Listener Deception, Modbus OT, DNS Canary, AI SITREP
│   ├── frontend/                   <- Dashboard War Room C4ISR Interaktif (Peta Operasi NKRI)
│   ├── JALANKAN_PUSAT_KOMANDO.bat  <- Skrip 1-Klik Menjalankan Pusat Komando
│   └── start_all.ps1               <- Launcher Service Komando
│
├── [ SATUAN TERITORIAL / CABANG KODIM YANG DIPANTAU ]
│   ├── satuan_teritorial/
│   │   ├── KODIM-0501_JAKARTA_PUSAT/    <- Satuan Binaan Kodam Jaya
│   │   ├── KODIM-0733_KOTA_SEMARANG/    <- Satuan Binaan Kodam IV/Diponegoro
│   │   ├── KODIM-0832_SURABAYA_SELATAN/ <- Satuan Binaan Kodam V/Brawijaya
│   │   ├── KODIM-0901_SAMARINDA_IKN/    <- Satuan Binaan Kodam VI/Mulawarman
│   │   ├── KODIM-1701_JAYAPURA/         <- Satuan Binaan Kodam XVII/Cenderawasih
│   │   └── ...
│   │
│   └── TAMBAH_SATUAN_KODIM_BARU.bat     <- Generator Otomatis Unit Baru (Zero Recompile)
```

---

## 2. Struktur Dalam Tiap Folder Satuan Kodim

Setiap folder satuan yang dipantau memiliki 3 kompartemen standar militer:

```
KODIM-XXXX_NAMA_KOTA/
├── 01_DOKUMEN_RAHASIA_UMPAN/
│   ├── RAHASIA_DISLOKASI_PASUKAN_2026_XXXX.docx  <- Dokumen umpan ber-token Canary FQDN unik
│   └── PETUNJUK_PENGGELARAN_UMPAN.txt           <- SOP penggelaran di workstation pangkalan
│
├── 02_KREDENSIAL_SISTEM_UMPAN/
│   └── Sandi_Akses_Genset_Pangkalan.txt          <- Kredensial jebakan menuju OT Modbus 5020
│
├── 03_SIMULASI_DETONASI/
│   └── UJI_DETONASI_KEBOCORAN_KODIM.bat         <- Skrip uji coba detonasi beacon DNS
│
├── TEST_DETONASI_XXXX.bat                       <- Shortcut 1-klik simulasi kebocoran
└── identitas_satuan.json                        <- Metadata unit & token FQDN
```

---

## 3. Mengapa Tidak Perlu Recompile?

1. **Dynamic Runtime DNS Resolution**:
   Backend mengurai subdomain FQDN (`doc-xxxx.kodim-xxxx.canary.lan`) secara langsung pada saat paket UDP DNS diterima di port 5053.
2. **Registry JSON Dinamis**:
   Data satuan tersimpan di `backend/app/satuan_registry.json`. File ini diperbarui secara instan saat skrip `.bat` dijalankan, dan dibaca langsung oleh backend tanpa perlu restart ataupun kompilasi ulang.
3. **Reactivity Peta C4ISR**:
   Frontend menerima nama Kodam induk melalui koneksi WebSocket, dan komponen peta SVG secara otomatis mencocokkan koordinat Kodam yang bersangkutan untuk menyalakan indikator bahaya merah berkedip.
