import os
import zipfile
import io

def generate_canary_docx(
    output_path: str,
    canary_domain: str = "doc-991a.kodam-jaya.canary.nexustrap.mil.id",
    beacon_http_url: str = "http://192.168.1.9:8000/api/canary/beacon/DOC-991A"
):
    """Generates an authentic Microsoft Word (.docx) bait file embedded with DUAL-SPECTRUM Canaries:
    1. Out-of-band DNS Canary (via attachedTemplate relationship)
    2. Real-time HTTP Web Beacon Pixel (via external image relationship)
    When opened in any Word processor (Word, WPS, Docs) on local Wi-Fi or public network,
    it automatically notifies NEXUS-TRAP and triggers SIAGA 1 MERAH."""

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
      <w:r><w:rPr><w:b/><w:sz w:val="32"/><w:color w:val="FF0000"/></w:rPr>
        <w:t>RAHASIA - TENTARA NASIONAL INDONESIA ANGKATAN DARAT</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:pPr><w:jc w:val="center"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="24"/></w:rPr>
        <w:t>RENCANA DISLOKASI SATUAN &amp; GELAR KESIAPSIAGAAN OPERASI 2026</w:t>
      </w:r>
    </w:p>
    <w:p><w:r><w:t>Nomor Dokumen: KCH-TNIAD-DOC-991A</w:t></w:r></w:p>
    <w:p><w:r><w:t>Klasifikasi   : SANGAT RAHASIA (MILITARY CONFIDENTIAL)</w:t></w:r></w:p>
    <w:p><w:r><w:t>Isi Perintah  : Penataan ulang perimeter radar taktis dan genset otomatis Kodam Jaya.</w:t></w:r></w:p>
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
                    <pic:cNvPr id="0" name="pixel.gif"/>
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

    # Dual-Spectrum Relationships:
    # rId1337 -> DNS Canary (resolves template.dotx via DNS)
    # rIdBeacon -> HTTP Web Beacon (triggers instant GET request to local or remote server)
    document_rels = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1337" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate" Target="http://{canary_domain}/template.dotx" TargetMode="External"/>
  <Relationship Id="rIdBeacon" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="{beacon_http_url}" TargetMode="External"/>
</Relationships>"""

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", content_types)
        docx.writestr("_rels/.rels", root_rels)
        docx.writestr("word/document.xml", document_xml)
        docx.writestr("word/_rels/document.xml.rels", document_rels)

    print(f"[+] Berhasil membuat file umpan Canary DOCX: {output_path}")
    print(f"    DNS Canary Target : {canary_domain}")
    print(f"    HTTP Beacon Target: {beacon_http_url}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sample_path = os.path.join(script_dir, "samples", "Rahasia_Dislokasi_Pasukan_2026.docx")
    generate_canary_docx(sample_path)
