import os

files_to_update = [
    'E:/04_Webdev/59_Cyber-Hackathon/presentation_hackathon/index.html',
    'E:/04_Webdev/59_Cyber-Hackathon/presentation_hackathon/presentasi.html',
    'E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/presentasi.html'
]

for file_path in files_to_update:
    if not os.path.exists(file_path):
        print(f"Skipping missing: {file_path}")
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update home footer
    content = content.replace(
        'NEXUS-TRAP // 100% AIR-GAPPED STANDALONE • KARTIKA CYBER HACKATHON 2026',
        'NEXUS-TRAP // 100% AIR-GAPPED STANDALONE • KARTIKA CYBER HACKATHON 2026 • PENGEMBANG: DITOGIANTO'
    )

    # 2. Add ditogianto tag in unified-hud right before button prevSlide
    hud_author_tag = '''<div class="hud-author" style="font-family: var(--master-mono); font-size: 11px; color: #10b981; font-weight: 800; letter-spacing: 0.08em; padding: 4px 10px; background: rgba(16, 185, 129, 0.1); border-radius: 4px; border: 1px solid rgba(16, 185, 129, 0.3); margin-right: 6px;">
        👤 DITOGIANTO
      </div>'''

    if '👤 DITOGIANTO' not in content:
        content = content.replace(
            '<div class="hud-right">\n      <button class="hud-btn" onclick="prevSlide()"',
            f'<div class="hud-right">\n      {hud_author_tag}\n      <button class="hud-btn" onclick="prevSlide()"'
        )
        # Also try CRLF
        content = content.replace(
            '<div class="hud-right">\r\n      <button class="hud-btn" onclick="prevSlide()"',
            f'<div class="hud-right">\r\n      {hud_author_tag}\r\n      <button class="hud-btn" onclick="prevSlide()"'
        )

    # 3. Add Author tag to Stage Cover Eyebrow if not present
    stage_cover_target = '<span class="stage-tag">KATEGORI: PENANGKALAN</span>\n            </div>'
    stage_cover_replacement = '<span class="stage-tag">KATEGORI: PENANGKALAN</span>\n              <span style="color: #10b981; font-weight: 800; font-family: var(--master-mono); font-size: 12px; letter-spacing: 0.08em; margin-left: 12px;">PENGEMBANG: DITOGIANTO</span>\n            </div>'
    content = content.replace(stage_cover_target, stage_cover_replacement)

    stage_cover_target_crlf = '<span class="stage-tag">KATEGORI: PENANGKALAN</span>\r\n            </div>'
    stage_cover_replacement_crlf = '<span class="stage-tag">KATEGORI: PENANGKALAN</span>\r\n              <span style="color: #10b981; font-weight: 800; font-family: var(--master-mono); font-size: 12px; letter-spacing: 0.08em; margin-left: 12px;">PENGEMBANG: DITOGIANTO</span>\r\n            </div>'
    content = content.replace(stage_cover_target_crlf, stage_cover_replacement_crlf)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated footer in {file_path}")

print("All footers updated with 'ditogianto'!")
