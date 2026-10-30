import re

targets = [
    'E:/04_Webdev/59_Cyber-Hackathon/web_presentation/index.html',
    'E:/04_Webdev/59_Cyber-Hackathon/web_presentation/presentasi.html',
    'E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/presentasi.html'
]

# Additional CSS for Audience Hero Boxes
css_to_add = """
    /* ========================================================================= */
    /* AUDIENCE HERO & DIFFERENTIATOR CARD STYLING                               */
    /* ========================================================================= */
    .target-audience-box {
      background: rgba(0, 0, 0, 0.4);
      border-radius: 8px;
      padding: 14px 16px;
      margin-bottom: 14px;
      border: 1px solid rgba(255, 255, 255, 0.07);
    }
    .audience-label {
      display: inline-block;
      font-family: var(--master-mono);
      font-size: 10px;
      font-weight: 900;
      letter-spacing: 1.5px;
      padding: 3px 8px;
      border-radius: 4px;
      margin-bottom: 8px;
    }
    .tag-green { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.35); }
    .tag-cyan { background: rgba(6, 182, 212, 0.15); color: #38bdf8; border: 1px solid rgba(6, 182, 212, 0.35); }
    .tag-purple { background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.35); }

    .audience-title {
      font-size: clamp(16px, 1.15vw, 19px);
      font-weight: 900;
      line-height: 1.25;
      letter-spacing: -0.01em;
      margin-bottom: 4px;
    }
    .title-green { color: #ffffff; text-shadow: 0 0 14px rgba(16, 185, 129, 0.4); }
    .title-cyan { color: #ffffff; text-shadow: 0 0 14px rgba(6, 182, 212, 0.4); }
    .title-purple { color: #ffffff; text-shadow: 0 0 14px rgba(168, 85, 247, 0.4); }

    .audience-sub {
      font-size: 11.5px;
      color: #94a3b8;
      font-weight: 600;
      line-height: 1.4;
    }

    .card-divider {
      height: 1px;
      background: linear-gradient(90deg, rgba(255, 255, 255, 0.08), transparent);
      margin-bottom: 12px;
    }

    .format-header {
      margin-bottom: 10px;
    }
    .format-badge-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 4px;
    }
    .format-code {
      font-family: var(--master-mono);
      font-size: 10px;
      font-weight: 800;
      color: #64748b;
      letter-spacing: 0.5px;
    }
    .format-title {
      font-size: 15px;
      font-weight: 800;
      color: #e2e8f0;
      line-height: 1.3;
    }

    .format-desc {
      font-size: 12.5px;
      line-height: 1.5;
      color: #94a3b8;
      margin-bottom: 14px;
      flex-grow: 1;
    }

    .format-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 18px;
    }
    .format-pill {
      font-family: var(--master-mono);
      font-size: 10.5px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
    }
    .pill-green { color: #a7f3d0; border: 1px solid rgba(16, 185, 129, 0.25); background: rgba(16, 185, 129, 0.05); }
    .pill-cyan { color: #bae6fd; border: 1px solid rgba(6, 182, 212, 0.25); background: rgba(6, 182, 212, 0.05); }
    .pill-purple { color: #e9d5ff; border: 1px solid rgba(168, 85, 247, 0.25); background: rgba(168, 85, 247, 0.05); }
"""

# New HTML for View Home
new_view_home_content = """  <!-- ========================================================================= -->
  <!-- VIEW 1: HOME PORTAL SELECTOR                                              -->
  <!-- ========================================================================= -->
  <div id="view-home" class="view-container active">
    <header class="home-header">
      <div class="home-eyebrow">PUSSIBERAD TNI AD × KARTIKA CYBER HACKATHON 2026 // DOKTRIN PERTAHANAN SIBER AKTIF</div>
      <h1 class="home-title">
        <span class="title-line-1">PORTAL PRESENTASI RESMI</span>
        <span class="title-line-2">NEXUS-TRAP</span>
      </h1>
      <p class="home-desc">
        Pilih salah satu dari <strong>3 format presentasi</strong> di bawah ini sesuai profil target Dewan Juri:
      </p>
    </header>

    <!-- 3 Audience-Driven Presentation Modes -->
    <div class="home-cards-grid">
      
      <!-- Card 1: Non-Tech / Eksekutif -->
      <div class="home-card card-awam" onclick="switchMode('awam')">
        <div style="display: flex; flex-direction: column; height: 100%;">
          
          <!-- Audience Hero Header -->
          <div class="target-audience-box">
            <span class="audience-label tag-green">TARGET AUDIENS</span>
            <div class="audience-title title-green">DEWAN JURI NON-TEKNIS &amp; PIMPINAN</div>
            <div class="audience-sub">Perwira Tinggi, Komandan Satuan, &amp; Penilai Eksekutif</div>
          </div>

          <div class="card-divider"></div>

          <!-- Format Spec -->
          <div class="format-header">
            <div class="format-badge-row">
              <span class="format-code">OPSI 01 // FORMAT AWAM</span>
              <span class="card-key-shortcut">[1] AWAM</span>
            </div>
            <h2 class="format-title">Doktrin &amp; Alur Cerita Asimetris</h2>
          </div>

          <p class="format-desc">
            Penyampaian doktrin pertahanan aktif asimetris menggunakan <strong>analogi taktis dunia nyata</strong> (Tank Kayu, Lem Tikus, &amp; Koper Berpelacak) tanpa istilah teknis rumit. Membalikkan persepsi bahwa pertahanan siber harus pasif menunggu diserang.
          </p>

          <!-- Highlights / Metrics -->
          <div class="format-pills">
            <span class="format-pill pill-green">✓ 11 Slide Naratif</span>
            <span class="format-pill pill-green">✓ Bahasa Awam &amp; Bebas Jargon</span>
            <span class="format-pill pill-green">✓ Efisiensi Biaya Rp 0,-</span>
          </div>

          <!-- Action Button -->
          <button class="btn-card-launch btn-green" style="margin-top: auto;">
            <span>PILIH FORMAT NON-TEKNIS</span>
            <span style="font-family: var(--master-mono); font-size: 11px; opacity: 0.85;">[TEKAN 1] →</span>
          </button>
        </div>
      </div>

      <!-- Card 2: Deep-Dive Teknis -->
      <div class="home-card card-teknis" onclick="switchMode('teknis')">
        <div style="display: flex; flex-direction: column; height: 100%;">
          
          <!-- Audience Hero Header -->
          <div class="target-audience-box">
            <span class="audience-label tag-cyan">TARGET AUDIENS</span>
            <div class="audience-title title-cyan">DEWAN JURI TEKNIS &amp; RED TEAM</div>
            <div class="audience-sub">Cyber Security Engineers, Praktisi Forensik, &amp; Pentester</div>
          </div>

          <div class="card-divider"></div>

          <!-- Format Spec -->
          <div class="format-header">
            <div class="format-badge-row">
              <span class="format-code">OPSI 02 // DEEP-DIVE TEKNIS</span>
              <span class="card-key-shortcut">[2] TEKNIS</span>
            </div>
            <h2 class="format-title">Arsitektur &amp; Rekayasa Sistem</h2>
          </div>

          <p class="format-desc">
            Bedah rekayasa mendalam: spesifikasi <strong>emulasi SCADA OT Modbus 502</strong>, algoritma <em>slow-drip</em> Sticky Tarpit (0 req/s), suar klandestin DNS UDP 5053 tembus isolasi VM, dan rantai integritas HMAC-SHA256 untuk barang bukti POMAD.
          </p>

          <!-- Highlights / Metrics -->
          <div class="format-pills">
            <span class="format-pill pill-cyan">✓ 11 Slide Spesifikasi</span>
            <span class="format-pill pill-cyan">✓ RFC 9309 &amp; FCrDNS Verification</span>
            <span class="format-pill pill-cyan">✓ SQLite HMAC-SHA256 Seal</span>
          </div>

          <!-- Action Button -->
          <button class="btn-card-launch btn-cyan" style="margin-top: auto;">
            <span>PILIH FORMAT TEKNIS</span>
            <span style="font-family: var(--master-mono); font-size: 11px; opacity: 0.85;">[TEKAN 2] →</span>
          </button>
        </div>
      </div>

      <!-- Card 3: Stage Pitch Deck (16:9) -->
      <div class="home-card card-deck" onclick="switchMode('deck')">
        <div style="display: flex; flex-direction: column; height: 100%;">
          
          <!-- Audience Hero Header -->
          <div class="target-audience-box">
            <span class="audience-label tag-purple">TARGET AUDIENS</span>
            <div class="audience-title title-purple">SESI PANGGUNG &amp; LIVE DEMO</div>
            <div class="audience-sub">Presentasi Proyektor 16:9, Dewan Juri Utama, &amp; Penonton</div>
          </div>

          <div class="card-divider"></div>

          <!-- Format Spec -->
          <div class="format-header">
            <div class="format-badge-row">
              <span class="format-code">OPSI 03 // MASTER STAGE DECK</span>
              <span class="card-key-shortcut">[3] STAGE DECK</span>
            </div>
            <h2 class="format-title">Executive Stage Pitch Deck (16:9)</h2>
          </div>

          <p class="format-desc">
            Format sinematik 16:9 widescreen <em>zero-scroll</em> yang dirancang khusus untuk <strong>evaluasi panggung berdurasi 10 menit</strong>. Dilengkapi koreografi insiden panggung, wireframe GUI C4ISR, dan <strong>widget QR interaktif</strong> yang dapat diuji langsung oleh juri.
          </p>

          <!-- Highlights / Metrics -->
          <div class="format-pills">
            <span class="format-pill pill-purple">✓ 7 Slide Sinematik 16:9</span>
            <span class="format-pill pill-purple">✓ Live Audience QR Detonation</span>
            <span class="format-pill pill-purple">✓ Naskah Dinas SITREP Kasad</span>
          </div>

          <!-- Action Button -->
          <button class="btn-card-launch btn-purple" style="margin-top: auto;">
            <span>PILIH STAGE DECK (16:9)</span>
            <span style="font-family: var(--master-mono); font-size: 11px; opacity: 0.85;">[TEKAN 3] →</span>
          </button>
        </div>
      </div>

    </div>

    <!-- Home Bottom Status Strip -->
    <footer class="home-footer">
      <div class="home-shortcuts">
        <div class="shortcut-pill"><span class="kbd">1</span> Awam</div>
        <div class="shortcut-pill"><span class="kbd">2</span> Teknis</div>
        <div class="shortcut-pill"><span class="kbd">3</span> Stage Deck</div>
        <div class="shortcut-pill"><span class="kbd">Esc</span> Beranda</div>
        <div class="shortcut-pill"><span class="kbd">F</span> Fullscreen</div>
        <div class="shortcut-pill"><span class="kbd">← / →</span> Pindah Slide</div>
      </div>
      <div>
        NEXUS-TRAP // 100% AIR-GAPPED STANDALONE • KARTIKA CYBER HACKATHON 2026 • PENGEMBANG: DITOGIANTO
      </div>
    </footer>
  </div>"""

for path in targets:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add CSS if not present
    if '.target-audience-box' not in html:
        html = html.replace('</style>', f'{css_to_add}\n  </style>')

    # 2. Replace entire view-home
    pattern = r'<!-- ========================================================================= -->\s*<!-- VIEW 1: HOME PORTAL SELECTOR.*?</div>\s*<!-- ========================================================================= -->\s*<!-- VIEW 2: NON-TECH'
    replacement = f'{new_view_home_content}\n\n  <!-- ========================================================================= -->\n  <!-- VIEW 2: NON-TECH'
    
    new_html = re.sub(pattern, replacement, html, flags=re.DOTALL)
    if new_html == html:
        print(f"Warning: Regex pattern didn't match for {path}, trying fallback replacement...")
        # Fallback using view-home tag
        start_idx = html.find('<div id="view-home"')
        end_idx = html.find('<div id="view-awam"')
        if start_idx != -1 and end_idx != -1:
            header_prefix = '  <!-- ========================================================================= -->\n  <!-- VIEW 1: HOME PORTAL SELECTOR                                              -->\n  <!-- ========================================================================= -->\n'
            # find where previous section ended
            prev_comment = html.rfind('<!-- ===', 0, start_idx)
            if prev_comment != -1:
                new_html = html[:prev_comment] + new_view_home_content + '\n\n' + html[end_idx:]
            else:
                new_html = html[:start_idx] + new_view_home_content + '\n\n' + html[end_idx:]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print(f"Redesigned Home Portal applied to: {path}")

print("All targets successfully updated with the clean, audience-driven layout!")
