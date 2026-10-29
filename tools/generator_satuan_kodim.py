import os
import sys
import json
import zipfile
import argparse
from pathlib import Path
from datetime import datetime

# Root workspace paths
SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
REGISTRY_PATH = ROOT_DIR / "backend" / "app" / "satuan_registry.json"
SATUAN_DIR = ROOT_DIR / "satuan_teritorial"

KODAM_LIST = [
    ("KODAM_IM", "Kodam Iskandar Muda", "Aceh"),
    ("KODAM_I", "Kodam I/Bukit Barisan", "Sumut / Sumbar / Riau"),
    ("KODAM_II", "Kodam II/Sriwijaya", "Sumsel / Lampung / Jambi / Bengkulu"),
    ("KODAM_JAYA", "Kodam Jaya", "DKI Jakarta & Sekitarnya"),
    ("KODAM_III", "Kodam III/Siliwangi", "Jawa Barat & Banten"),
    ("KODAM_IV", "Kodam IV/Diponegoro", "Jawa Tengah & D.I. Yogyakarta"),
    ("KODAM_V", "Kodam V/Brawijaya", "Jawa Timur"),
    ("KODAM_IX", "Kodam IX/Udayana", "Bali, NTB, NTT"),
    ("KODAM_VI", "Kodam VI/Mulawarman", "Kalimantan Timur / IKN / Kalsel / Kaltara"),
    ("KODAM_XIV", "Kodam XIV/Hasanuddin", "Sulawesi Selatan / Barat / Tenggara"),
    ("KODAM_XVII", "Kodam XVII/Cenderawasih", "Papua"),
]

def generate_canary_docx(output_path: Path, doc_id: str, unit_name: str, kodam_name: str, canary_domain: str, http_beacon: str):
    """Generates an authentic Microsoft Word (.docx) bait document embedded with DNS & HTTP Canaries."""
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>"""

    root_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

    document_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
            xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
            xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
            xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
            xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
  <w:body>
    <w:p>
      <w:pPr><w:jc w:val="center"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="32"/><w:color w:val="CC0000"/></w:rPr>
        <w:t>TENTARA NASIONAL INDONESIA ANGKATAN DARAT</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:pPr><w:jc w:val="center"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="26"/><w:color w:val="1A365D"/></w:rPr>
        <w:t>{kodam_name.upper()} // {unit_name.upper()}</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:pPr><w:jc w:val="center"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="22"/></w:rPr>
        <w:t>RENCANA KESIAPSIAGAAN OPERASI &amp; DISLOKASI PASUKAN 2026</w:t>
      </w:r>
    </w:p>
    <w:p><w:r><w:t>--------------------------------------------------------------------------------------------------</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Nomor Dokumen : </w:t></w:r><w:r><w:t>KCH-TNIAD-{doc_id}</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Klasifikasi    : </w:t></w:r><w:r><w:rPr><w:color w:val="FF0000"/><w:b/></w:rPr><w:t>SANGAT RAHASIA (MILITARY STRICT ACCESS)</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Satuan Pemegang: </w:t></w:r><w:r><w:t>{unit_name}</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Tanggal Berlaku: </w:t></w:r><w:r><w:t>{datetime.now().strftime('%d %B %Y')}</w:t></w:r></w:p>
    <w:p><w:r><w:t>--------------------------------------------------------------------------------------------------</w:t></w:r></w:p>
    <w:p>
      <w:r>
        <w:t>PERINGATAN RESMI: Dokumen ini terproteksi sistem deteksi perimeter klandestin PUSSIBERAD TNI AD. Segala pembukaan atau pemindahan berkas di luar jaringan militer resmi akan memicu intersepsi intelijen dan isolasi host seketika.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:drawing>
          <wp:inline distT="0" distB="0" distL="0" distR="0">
            <wp:extent cx="9525" cy="9525"/>
            <wp:docPr id="1337" name="BeaconPixel"/>
            <a:graphic>
              <a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
                <pic:pic>
                  <pic:nvPicPr>
                    <pic:cNvPr id="0" name="beacon.gif"/>
                    <pic:cNvPicPr/>
                  </pic:nvPicPr>
                  <pic:blipFill>
                    <a:blip r:link="rIdBeacon"/>
                    <a:stretch><a:fillRect/></a:stretch>
                  </pic:blipFill>
                  <pic:spPr>
                    <a:xfrm><a:off x="0" y="0"/><a:ext cx="9525" cy="9525"/></a:xfrm>
                    <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
                  </pic:spPr>
                </pic:pic>
              </a:graphicData>
            </a:graphic>
          </wp:inline>
        </w:drawing>
      </w:r>
    </w:p>
  </w:body>
</w:document>"""

    document_rels = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1337" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate" Target="http://{canary_domain}/template.dotx" TargetMode="External"/>
  <Relationship Id="rIdBeacon" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="{http_beacon}" TargetMode="External"/>
</Relationships>"""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", content_types)
        docx.writestr("_rels/.rels", root_rels)
        docx.writestr("word/document.xml", document_xml)
        docx.writestr("word/_rels/document.xml.rels", document_rels)

KODAM_DICT = {
    "KODAM_IM": {"x": 55, "y": 55},
    "KODAM_I": {"x": 92, "y": 82},
    "KODAM_II": {"x": 178, "y": 158},
    "KODAM_JAYA": {"x": 242, "y": 198},
    "KODAM_III": {"x": 262, "y": 216},
    "KODAM_IV": {"x": 318, "y": 205},
    "KODAM_V": {"x": 378, "y": 212},
    "KODAM_IX": {"x": 436, "y": 223},
    "KODAM_VI": {"x": 408, "y": 138},
    "KODAM_XIV": {"x": 448, "y": 178},
    "KODAM_XVII": {"x": 742, "y": 142},
}

def calculate_kodim_coords(kodam_id: str, kodim_num: str):
    info = KODAM_DICT.get(kodam_id, {"x": 242, "y": 198})
    digits = "".join(filter(str.isdigit, kodim_num))
    num_val = int(digits) if digits else 1
    dx = ((num_val * 7) % 27) - 13
    dy = ((num_val * 11) % 23) - 11
    return max(35, min(765, info["x"] + dx)), max(35, min(250, info["y"] + dy))

def update_registry(kodim_id: str, unit_name: str, kodam_id: str, kodam_name: str, wilayah: str, canary_domain: str, x: int = 242, y: int = 198):
    """Registers unit into backend/app/satuan_registry.json without needing restart or compile."""
    registry = {}
    if REGISTRY_PATH.exists():
        try:
            with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
                registry = json.load(f)
        except Exception:
            registry = {}
            
    registry[kodim_id] = {
        "kodim_id": kodim_id,
        "nama": unit_name,
        "kodam_id": kodam_id,
        "kodam_name": kodam_name,
        "wilayah": wilayah,
        "x": x,
        "y": y,
        "canary_domain": canary_domain,
        "status": "MONITORED",
        "registered_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

    # Hot-reload broadcast trigger to live C4ISR frontend
    try:
        import urllib.request
        req = urllib.request.Request("http://localhost:8000/api/satuan/reload", data=b"{}", headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=1.0)
        print("    [✓] Sinyal reload otomatis terkirim ke War Room (Live WebSocket Broadcast).")
    except Exception:
        pass

def create_kodim_package(kodim_num: str, kota: str, kodam_idx: int):
    """Generates the full directory structure, canary bait doc, credentials, and simulation bat script."""
    kodim_clean = kodim_num.strip().replace("KODIM", "").replace("-", "").strip()
    kodim_id = f"KODIM-{kodim_clean}"
    kota_clean = kota.strip().title()
    unit_name = f"Kodim {kodim_clean}/{kota_clean}"
    
    kodam_id, kodam_name, default_wilayah = KODAM_LIST[kodam_idx]
    wilayah = f"{kota_clean}, {default_wilayah}"
    
    doc_serial = f"DOC-{kodim_clean}A"
    subdomain_slug = f"kodim-{kodim_clean.lower()}"
    canary_domain = f"{doc_serial.lower()}.{subdomain_slug}.canary.lan"
    http_beacon = f"http://localhost:8000/api/canary/beacon/{doc_serial}"
    
    # 1. Create Target Directory
    folder_name = f"{kodim_id}_{kota_clean.upper().replace(' ', '_')}"
    unit_folder = SATUAN_DIR / folder_name
    folder_dokumen = unit_folder / "01_DOKUMEN_RAHASIA_UMPAN"
    folder_kredensial = unit_folder / "02_KREDENSIAL_SISTEM_UMPAN"
    folder_simulasi = unit_folder / "03_SIMULASI_DETONASI"
    
    for f in [folder_dokumen, folder_kredensial, folder_simulasi]:
        f.mkdir(parents=True, exist_ok=True)
        
    # 2. Build Authentic Canary DOCX
    docx_file = folder_dokumen / f"RAHASIA_DISLOKASI_PASUKAN_2026_{kodim_clean}.docx"
    generate_canary_docx(docx_file, doc_serial, unit_name, kodam_name, canary_domain, http_beacon)
    
    # Readme for Document
    readme_doc = folder_dokumen / "PETUNJUK_PENGGELARAN_UMPAN.txt"
    readme_doc.write_text(f"""========================================================================
PUSSIBERAD TNI AD // DOKTRIN PERTAHANAN AKTIF (NEXUS-TRAP)
BERKAS UMPAN CANARY DIGITAL: {unit_name}
========================================================================

PETUNJUK PENGGUNAAN:
1. File 'RAHASIA_DISLOKASI_PASUKAN_2026_{kodim_clean}.docx' adalah dokumen jebakan.
2. Tempatkan file ini di Desktop atau folder Dokumen pada workstation staf logistik / intelijen.
3. JANGAN DIBUKA OLEH STAF RESMI.
4. Jika komputer staf disusupi peretas atau dicuri, pembukaan dokumen di komputer asing
   akan langsung mengirimkan sinyal DNS klandestin ke Pusat Komando PUSSIBERAD:
   Target Subdomain: {canary_domain}
5. Meja Komando C4ISR seketika akan menyalakan SIAGA 1 MERAH dan mengidentifikasi:
   - Satuan: {unit_name} ({kodam_name})
   - IP Penyerang & Geolocation
========================================================================
""", encoding="utf-8")

    # 3. Build Kredensial & OT Trap
    genset_txt = folder_kredensial / "Sandi_Akses_Genset_Pangkalan.txt"
    genset_txt.write_text(f"""[SISTEM KENDALI OT / SCADA KODIM {kodim_clean}]
LOKASI   : Ruang Daya & Genset Cadangan {unit_name}
PROTOKOL : Modbus/TCP Industrial Protocol
PORT     : 5020 (Decoy Trap Port Pangkalan)
HOST IP  : 192.168.1.9 (NEXUS-TRAP Sensor Emulation)
REGISTER : Holding Register 40001 (Tegangan 380V), 40002 (Frekuensi 50Hz), 40003 (BBM Solar 85%)

PERHATIAN: Akses manual hanya melalui izin Perwira Jaga Pangkalan.
Setiap percobaan koneksi tidak sah akan direkam oleh SIEM PUSSIBERAD.
""", encoding="utf-8")

    # 4. Build Simulation BAT runner
    simulasi_bat = folder_simulasi / "UJI_DETONASI_KEBOCORAN_KODIM.bat"
    bat_content = f"""@echo off
chcp 65001 >nul
title SIMULASI DETONASI KEBOCORAN - {unit_name}
color 0C
cls
echo ========================================================================
echo   PUSSIBERAD TNI AD // SIMULASI DETONASI CANARY TOKEN
echo   Satuan : {unit_name}
echo   Induk  : {kodam_name}
echo   Token  : {canary_domain}
echo ========================================================================
echo.
echo [*] Mensimulasikan dokumen rahasia dibuka di komputer peretas luar...
echo [*] Mengirimkan paket Out-of-Band UDP DNS Query ke NEXUS-TRAP (Port 5053)...
echo.
powershell -Command "Resolve-DnsName -Name '{canary_domain}' -Server 127.0.0.1 -Port 5053 -Type A"
echo.
echo ========================================================================
echo [+] DETONASI BERHASIL DIKIRIM!
echo [*] Silakan periksa layar C4ISR Meja Komando (http://localhost:3000):
echo     1. Status bertransisi ke SIAGA 1 MERAH
echo     2. Pin {kodam_name} di Peta Operasi NKRI berkedip merah
echo     3. Banner menampilkan: INTERSEPSI AKTIF: {unit_name}
echo ========================================================================
echo.
pause
"""
    simulasi_bat.write_text(bat_content, encoding="utf-8")
    
    # Also write a root shortcut in unit folder
    root_shortcut_bat = unit_folder / f"TEST_DETONASI_{kodim_clean}.bat"
    root_shortcut_bat.write_text(f"""@echo off
call "03_SIMULASI_DETONASI\\UJI_DETONASI_KEBOCORAN_KODIM.bat"
""", encoding="utf-8")

    # Calculate accurate geographic anchor coordinate
    coords_x, coords_y = calculate_kodim_coords(kodam_id, kodim_clean)

    # 5. Metadata JSON
    meta_json = unit_folder / "identitas_satuan.json"
    with open(meta_json, "w", encoding="utf-8") as f:
        json.dump({
            "kodim_id": kodim_id,
            "nama": unit_name,
            "kodam_id": kodam_id,
            "kodam_name": kodam_name,
            "wilayah": wilayah,
            "x": coords_x,
            "y": coords_y,
            "canary_domain": canary_domain,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }, f, indent=2, ensure_ascii=False)

    # 6. Update Central Registry
    update_registry(kodim_id, unit_name, kodam_id, kodam_name, wilayah, canary_domain, coords_x, coords_y)
    
    return {
        "unit_folder": str(unit_folder),
        "unit_name": unit_name,
        "kodam_name": kodam_name,
        "canary_domain": canary_domain
    }

def main():
    parser = argparse.ArgumentParser(description="Generator Satuan Kodim & Dokumen Canary NEXUS-TRAP")
    parser.add_argument("--kodim", help="Nomor Kodim (contoh: 0733, 0501, 1701)")
    parser.add_argument("--kota", help="Nama Kota/Kabupaten (contoh: Semarang, Jayapura, Badung)")
    parser.add_argument("--kodam", type=int, help="Indeks Kodam (0-10)")
    args = parser.parse_args()
    
    if args.kodim and args.kota and args.kodam is not None:
        res = create_kodim_package(args.kodim, args.kota, args.kodam)
        print(f"[+] SATUAN TERITORIAL BERHASIL DIBUAT SECARA OTOMATIS:")
        print(f"    Satuan  : {res['unit_name']} ({res['kodam_name']})")
        print(f"    Folder  : {res['unit_folder']}")
        print(f"    Token   : {res['canary_domain']}")
        return

    # Interactive mode
    print("========================================================================")
    print("  PUSSIBERAD TNI AD // GENERATOR OTOMATIS SATUAN KODIM BARU")
    print("  Pembuatan Struktur Satuan & Dokumen Umpan Canary (Zero Recompile)")
    print("========================================================================")
    print()
    kodim_input = input("Masukkan Nomor Satuan Kodim (contoh: 0733, 1701, 0101): ").strip()
    kota_input = input("Masukkan Nama Kota/Kabupaten Satuan (contoh: Semarang, Jayapura, Banda Aceh): ").strip()
    
    print("\nPilih Komando Daerah Militer (Kodam) Naungan:")
    for idx, (k_id, k_name, wil) in enumerate(KODAM_LIST):
        print(f"  [{idx:2d}] {k_name} ({wil})")
    
    while True:
        try:
            choice = int(input(f"\nMasukkan Nomor Pilihan Kodam [0-{len(KODAM_LIST)-1}]: ").strip())
            if 0 <= choice < len(KODAM_LIST):
                break
            print("Pilihan di luar jangkauan, coba lagi.")
        except ValueError:
            print("Masukkan angka yang valid.")
            
    res = create_kodim_package(kodim_input, kota_input, choice)
    print("\n" + "="*72)
    print("  BERHASIL! PAKET SATUAN TERITORIAL BARU TELAH DIBUAT")
    print("="*72)
    print(f"  Satuan         : {res['unit_name']}")
    print(f"  Komando Induk  : {res['kodam_name']}")
    print(f"  Lokasi Direktori: {res['unit_folder']}")
    print(f"  Token FQDN     : {res['canary_domain']}")
    print("="*72)
    print("  [*] Registry Pusat diperbarui secara runtime tanpa perlu recompile!")
    print("="*72 + "\n")

if __name__ == "__main__":
    main()
