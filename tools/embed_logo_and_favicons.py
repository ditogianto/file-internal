import os

html_files = [
    'E:/04_Webdev/59_Cyber-Hackathon/web_presentation/index.html',
    'E:/04_Webdev/59_Cyber-Hackathon/web_presentation/presentasi.html',
    'E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/presentasi.html',
]

favicon_tags = """  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="favicon.png">
  <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">"""

logo_banner = """      <div style="margin-bottom: 22px; display: flex; justify-content: center;">
        <img src="nexus_trap_logo.svg" alt="NEXUS-TRAP Military Brandmark" style="height: 76px; max-width: 92%; filter: drop-shadow(0 4px 25px rgba(16, 185, 129, 0.2));">
      </div>"""

hud_logo_icon = """<img src="nexus_trap_mark.svg" alt="Nexus-Trap" style="width: 22px; height: 22px; vertical-align: middle; margin-right: 6px; filter: drop-shadow(0 0 6px rgba(16,185,129,0.5));">"""

for p in html_files:
    if not os.path.exists(p):
        continue
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add Favicons if not present
    if 'rel="icon"' not in content:
        content = content.replace('<head>', f'<head>\n{favicon_tags}')

    # 2. Add Logo Banner above home-title in home-header if not present
    if 'nexus_trap_logo.svg' not in content:
        target = '<h1 class="home-title">'
        replacement = f'{logo_banner}\n      <h1 class="home-title">'
        content = content.replace(target, replacement)

    # 3. Add Tactical Mark Icon in unified-hud before "BERANDA [ESC]"
    if 'nexus_trap_mark.svg' not in content:
        content = content.replace('<span>🏠 BERANDA [ESC]</span>', f'<span>{hud_logo_icon} BERANDA [ESC]</span>')

    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated brand elements in: {p}")

# Also update QR viewer HTML files
qr_files = [
    'E:/04_Webdev/59_Cyber-Hackathon/web_presentation/QR_DOWNLOAD_FILE_INTERNAL.html',
    'E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/QR_DOWNLOAD_FILE_INTERNAL.html'
]

for qp in qr_files:
    if not os.path.exists(qp):
        continue
    with open(qp, 'r', encoding='utf-8') as f:
        q_content = f.read()
    if 'rel="icon"' not in q_content:
        q_content = q_content.replace('<head>', f'<head>\n{favicon_tags}')
    with open(qp, 'w', encoding='utf-8') as f:
        f.write(q_content)
    print(f"Updated favicons in: {qp}")

print("Brand embedding completed successfully!")
