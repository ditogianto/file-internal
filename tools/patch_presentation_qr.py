import re

pres_path = 'E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/presentasi.html'

with open(pres_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace image sources
html = html.replace(
    '''<img src="/api/canary/qr.svg" alt="QR Code Juri" style="width: 60px; height: 60px;" onerror="this.src='qr_download_file_internal.svg';">''',
    '''<img src="qr_download_file_internal.svg" alt="QR Code Juri" style="width: 60px; height: 60px; cursor: pointer;" onclick="toggleCanaryModal(true)">'''
)

html = html.replace(
    '''<img src="/api/canary/qr.svg" alt="QR Code Panggung" style="width: 56px; height: 56px;" onerror="this.src='qr_download_file_internal.svg';">''',
    '''<img src="qr_download_file_internal.svg" alt="QR Code Panggung" style="width: 56px; height: 56px; cursor: pointer;" onclick="toggleCanaryModal(true)">'''
)

# 2. Replace anchor links from /canary-qr to QR_DOWNLOAD_FILE_INTERNAL.html with onclick modal trigger
html = re.sub(
    r'<a\s+href="/canary-qr"\s+target="_blank"',
    r'<a href="QR_DOWNLOAD_FILE_INTERNAL.html" onclick="toggleCanaryModal(true); return false;" target="_blank"',
    html
)

# 3. Add modal HTML right before </body> if not already present
modal_html = """
  <!-- ========================================================================= -->
  <!-- MODAL: TACTICAL FULLSCREEN CANARY QR VIEWER                               -->
  <!-- ========================================================================= -->
  <div id="canary-modal" style="display: none; position: fixed; inset: 0; z-index: 99999; background: rgba(2, 6, 23, 0.92); backdrop-filter: blur(8px); align-items: center; justify-content: center;" onclick="if(event.target===this) toggleCanaryModal(false)">
    <div style="background: #0f172a; border: 1px solid #334155; border-radius: 16px; padding: 36px 40px; text-align: center; max-width: 460px; width: 90%; box-shadow: 0 25px 60px rgba(0,0,0,0.85); position: relative;" onclick="event.stopPropagation()">
      <button onclick="toggleCanaryModal(false)" style="position: absolute; top: 14px; right: 16px; background: transparent; border: none; color: #94a3b8; font-size: 26px; cursor: pointer; line-height: 1;" title="Tutup (Esc)">&times;</button>
      
      <div style="display: inline-block; background: rgba(239, 68, 68, 0.15); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.4); padding: 5px 14px; border-radius: 9999px; font-size: 11px; font-weight: 800; letter-spacing: 0.1em; margin-bottom: 16px;">
        LIVE CANARY TOKEN // PUSSIBERAD
      </div>
      
      <h3 style="font-size: 20px; font-weight: 800; margin: 0 0 8px 0; color: #ffffff;">UMPAN DOKUMEN INTELIJEN</h3>
      <p style="color: #94a3b8; font-size: 12.5px; line-height: 1.5; margin: 0 0 20px 0;">
        Pindai QR Code di bawah dengan kamera smartphone untuk mengunduh <code>Rahasia_Dislokasi_Pasukan_2026.docx</code> langsung dari GitHub.
      </p>
      
      <div style="background: #ffffff; padding: 18px; border-radius: 12px; display: inline-block; margin-bottom: 20px; box-shadow: 0 0 35px rgba(239, 68, 68, 0.25);">
        <img src="qr_download_file_internal.svg" alt="QR Code Unduh Berkas" style="width: 230px; height: 230px; display: block;">
      </div>
      
      <div style="display: flex; gap: 10px; justify-content: center;">
        <a href="https://github.com/ditogianto/file-internal/raw/master/Rahasia_Dislokasi_Pasukan_2026.docx" target="_blank" style="flex: 1; background: #ef4444; color: #ffffff; text-decoration: none; padding: 12px 16px; border-radius: 6px; font-weight: 700; font-size: 12px; letter-spacing: 0.05em; display: inline-block;">
          UNDUH BERKAS (.DOCX) ↗
        </a>
        <a href="QR_DOWNLOAD_FILE_INTERNAL.html" target="_blank" style="background: #1e293b; color: #cbd5e1; text-decoration: none; padding: 12px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; display: inline-block; border: 1px solid #334155;">
          TAB BARU ↗
        </a>
      </div>
    </div>
  </div>

  <script>
    function toggleCanaryModal(show) {
      const modal = document.getElementById('canary-modal');
      if (modal) {
        modal.style.display = show ? 'flex' : 'none';
      }
    }

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        toggleCanaryModal(false);
      }
    });
  </script>
"""

if 'id="canary-modal"' not in html:
    html = html.replace('</body>', modal_html + '\n</body>')

with open(pres_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Patch applied successfully!")
