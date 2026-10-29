# Panduan Kontribusi & Pengembangan NEXUS-TRAP
## KARTIKA CYBER HACKATHON 2026 (PUSSIBERAD TNI AD × CODEPOLITAN)

Terima kasih atas minat Anda untuk berkontribusi pada pengembangan platform pertahanan siber aktif **NEXUS-TRAP**.

### Prinsip Utama Rekayasa:
1. **100% On-Premise Air-Gapped:** Dilarang menambahkan dependensi yang membutuhkan koneksi internet luar atau layanan API cloud pihak ketiga (Nir-Cloud).
2. **Zero False Positive by Design:** Setiap modul umpan (*decoy*) baru tidak boleh bertabrakan dengan port atau alamat layanan resmi pangkalan.
3. **Non-Blocking / Low-Resource:** Seluruh modul jaringan (Modbus, Tarpit, DNS) wajib menggunakan pemrograman asynchronous (`asyncio`) agar dapat berjalan pada perangkat keras berdaya rendah (mini PC / server pangkalan di daerah pelosok).
4. **Keabsahan Forensik POMAD:** Seluruh mutasi keadaan atau pencatatan insiden wajib mematuhi skema sequential hash-chaining (HMAC-SHA256) pada SQLite.

### Alur Uji Kualitas (QC/QA):
Sebelum mengajukan *pull request*, pastikan seluruh rangkaian tes end-to-end lulus 100%:
```bash
python test_full_qc_qa.py
```
Seluruh 6 fase QC/QA wajib menghasilkan status `[PASS]`.
