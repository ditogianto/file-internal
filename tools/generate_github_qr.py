import qrcode
import qrcode.image.svg

download_url = 'https://github.com/ditogianto/file-internal/raw/master/Rahasia_Dislokasi_Pasukan_2026.docx'
repo_url = 'https://github.com/ditogianto/file-internal'

# High resolution PNG
qr = qrcode.QRCode(box_size=12, border=3)
qr.add_data(download_url)
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')
img.save('E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/qr_download_file_internal.png')

# Pure SVG
svg_factory = qrcode.image.svg.SvgPathImage
img_svg = qrcode.make(download_url, image_factory=svg_factory)
with open('E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/qr_download_file_internal.svg', 'wb') as f:
    img_svg.save(f)

# Also create SVG string for the HTML viewer
with open('E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/qr_download_file_internal.svg', 'r', encoding='utf-8') as f:
    svg_content = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>QR Code Unduh Dokumen Rahasia - PUSSIBERAD</title>
  <style>
    body {{
      margin: 0;
      padding: 0;
      background: #020617;
      color: #f8fafc;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }}
    .card {{
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 16px;
      padding: 40px;
      text-align: center;
      max-width: 440px;
      width: 90%;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
    }}
    .badge {{
      display: inline-block;
      background: rgba(239, 68, 68, 0.15);
      color: #ef4444;
      border: 1px solid rgba(239, 68, 68, 0.4);
      padding: 6px 14px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.1em;
      margin-bottom: 20px;
    }}
    h1 {{
      font-size: 22px;
      font-weight: 800;
      margin: 0 0 10px 0;
      color: #ffffff;
      letter-spacing: -0.02em;
    }}
    p {{
      color: #94a3b8;
      font-size: 13.5px;
      line-height: 1.5;
      margin: 0 0 24px 0;
    }}
    .qr-box {{
      background: #ffffff;
      padding: 20px;
      border-radius: 12px;
      display: inline-block;
      margin-bottom: 24px;
      box-shadow: 0 0 30px rgba(239, 68, 68, 0.2);
    }}
    .qr-box svg {{
      width: 240px;
      height: 240px;
      display: block;
    }}
    .btn {{
      display: block;
      background: #ef4444;
      color: #ffffff;
      text-decoration: none;
      padding: 14px 20px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 13px;
      letter-spacing: 0.05em;
      transition: all 0.2s;
    }}
    .btn:hover {{
      background: #dc2626;
      transform: translateY(-1px);
    }}
    .repo-link {{
      display: block;
      margin-top: 16px;
      color: #64748b;
      font-size: 12px;
      text-decoration: none;
    }}
    .repo-link:hover {{
      color: #94a3b8;
    }}
  </style>
</head>
<body>
  <div class="card">
    <div class="badge">LIVE CANARY TOKEN // PUSSIBERAD</div>
    <h1>UMPAN DOKUMEN INTELIJEN</h1>
    <p>Arahkan kamera smartphone ke QR Code di bawah untuk mengunduh berkas <code>Rahasia_Dislokasi_Pasukan_2026.docx</code> langsung dari GitHub.</p>
    <div class="qr-box">
      {svg_content}
    </div>
    <a href="{download_url}" class="btn" target="_blank">UNDUH BERKAS DARI GITHUB</a>
    <a href="{repo_url}" class="repo-link" target="_blank">Kunjungi Repositori: ditogianto/file-internal &rarr;</a>
  </div>
</body>
</html>
"""

with open('E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/QR_DOWNLOAD_FILE_INTERNAL.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Successfully generated QR assets & HTML viewer!')
