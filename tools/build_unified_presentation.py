import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
AWAM_PATH = ROOT_DIR / "presentasi_awam.html"
TEKNIS_PATH = ROOT_DIR / "presentasi_teknis.html"
DECK_PATH = ROOT_DIR / "presentation_deck.html"
OUTPUT_PATH = ROOT_DIR / "presentasi.html"

def build():
    awam_raw = AWAM_PATH.read_text(encoding="utf-8")
    teknis_raw = TEKNIS_PATH.read_text(encoding="utf-8")
    deck_raw = DECK_PATH.read_text(encoding="utf-8")

    # Extract Awam styles & body slides
    awam_css = re.search(r'<style>(.*?)</style>', awam_raw, re.DOTALL).group(1)
    # Strip html, body, and .deck global rules from awam_css so they don't leak to global
    awam_css_cleaned = re.sub(r'html,\s*body\s*\{[^}]*\}', '', awam_css)
    awam_slides = re.search(r'<main class="deck"[^>]*>(.*?)</main>', awam_raw, re.DOTALL).group(1)

    # Extract Teknis styles & body slides
    teknis_css = re.search(r'<style>(.*?)</style>', teknis_raw, re.DOTALL).group(1)
    teknis_css_cleaned = re.sub(r'html,\s*body\s*\{[^}]*\}', '', teknis_css)
    teknis_slides = re.search(r'<main class="deck"[^>]*>(.*?)</main>', teknis_raw, re.DOTALL).group(1)

    # Extract Deck slides & drawer
    deck_slides = re.search(r'<div id="deck-container">(.*?)</div>', deck_raw, re.DOTALL).group(1)
    
    drawer_cards = """
      <div class="drawer-card" onclick="goToSlide(0)">
        <img src="screenshots/slide_01.png" alt="Slide 1">
        <div class="title">01 // Cover Eksekutif</div>
        <div class="subtitle">Doktrin Pertahanan Aktif</div>
      </div>
      <div class="drawer-card" onclick="goToSlide(1)">
        <img src="screenshots/slide_02.png" alt="Slide 2">
        <div class="title">02 // Paradoks Pondasi</div>
        <div class="subtitle">Ancaman Asimetris Modern</div>
      </div>
      <div class="drawer-card" onclick="goToSlide(2)">
        <img src="screenshots/slide_03.png" alt="Slide 3">
        <div class="title">03 // Lonceng & Stempel</div>
        <div class="subtitle">Filosofi Inti Sistem</div>
      </div>
      <div class="drawer-card" onclick="goToSlide(3)">
        <img src="screenshots/slide_04.png" alt="Slide 4">
        <div class="title">04 // Arsitektur 4 Pilar</div>
        <div class="subtitle">OT, Tarpit, Canary & SITREP</div>
      </div>
      <div class="drawer-card" onclick="goToSlide(4)">
        <img src="screenshots/slide_05.png" alt="Slide 5">
        <div class="title">05 // Koreografi Demo</div>
        <div class="subtitle">Skenario Intersepsi 10 Menit</div>
      </div>
      <div class="drawer-card" onclick="goToSlide(5)">
        <img src="screenshots/slide_06.png" alt="Slide 6">
        <div class="title">06 // Purwarupa C4ISR</div>
        <div class="subtitle">Laporan Kedinasan PUSSIBERAD</div>
      </div>
      <div class="drawer-card" onclick="goToSlide(6)">
        <img src="screenshots/slide_07.png" alt="Slide 7">
        <div class="title">07 // Kedaulatan Digital</div>
        <div class="subtitle">Kesiapan Gelar Kodam Se-NKRI</div>
      </div>
    """

    master_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NEXUS-TRAP // Master Presentation Portal (PUSSIBERAD TNI AD)</title>
  
  <style>
    /* ========================================================================= */
    /* 1. MASTER UNIFIED THEME & RESET                                           */
    /* ========================================================================= */
    :root {{
      --master-bg: #05080e;
      --master-surface: #0a101d;
      --master-card: #0f172a;
      --master-border: #1e293b;
      --master-border-glow: #2d4263;
      --master-text: #f8fafc;
      --master-muted: #94a3b8;
      --master-dim: #64748b;
      --master-green: #10b981;
      --master-green-glow: rgba(16, 185, 129, 0.25);
      --master-cyan: #06b6d4;
      --master-cyan-glow: rgba(6, 182, 212, 0.25);
      --master-amber: #f59e0b;
      --master-red: #ef4444;
      --master-purple: #a855f7;
      --master-font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      --master-mono: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html, body {{
      width: 100%;
      height: 100%;
      background-color: var(--master-bg);
      color: var(--master-text);
      font-family: var(--master-font);
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
    }}

    /* Viewport Containers */
    .view-container {{
      position: absolute;
      inset: 0;
      display: none;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
    }}

    .view-container.active {{
      display: flex;
    }}

    /* ========================================================================= */
    /* 2. PORTAL HOME VIEW (MODE SELECTOR)                                       */
    /* ========================================================================= */
    #view-home {{
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      padding: 3.5vh 4vw 3vh 4vw;
      background: radial-gradient(circle at 50% 15%, #0c182b 0%, #05080e 70%);
      z-index: 100;
    }}

    .home-header {{
      text-align: center;
      max-width: 980px;
    }}

    .home-eyebrow {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-family: var(--master-mono);
      font-size: clamp(11.5px, 0.9vw, 13.5px);
      font-weight: 800;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--master-green);
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 6px 18px;
      border-radius: 999px;
      margin-bottom: 1.6vh;
    }}

    .home-eyebrow::before {{
      content: "";
      width: 8px;
      height: 8px;
      background: var(--master-green);
      border-radius: 50%;
      box-shadow: 0 0 10px var(--master-green);
    }}

    .home-title {{
      font-size: clamp(28px, 3.2vw, 50px);
      font-weight: 900;
      letter-spacing: -0.02em;
      line-height: 1.15;
      color: #ffffff;
      margin-bottom: 1vh;
    }}

    .home-title span.hl-green {{
      background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .home-desc {{
      font-size: clamp(14px, 1.15vw, 17px);
      color: var(--master-muted);
      max-width: 78ch;
      margin: 0 auto;
      line-height: 1.55;
    }}

    /* 3 Main Choice Cards */
    .home-cards-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      width: 100%;
      max-width: 1460px;
      margin: 2vh 0;
    }}

    .home-card {{
      background: #090e18;
      border: 1px solid var(--master-border);
      border-radius: 14px;
      padding: 28px 24px 24px 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      cursor: pointer;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
    }}

    .home-card::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: transparent;
      transition: background 0.25s ease;
    }}

    .home-card:hover {{
      transform: translateY(-5px);
      border-color: var(--card-hover-border, var(--master-green));
      box-shadow: 0 16px 36px var(--card-hover-glow, rgba(16, 185, 129, 0.15));
      background: #0d1524;
    }}

    /* Card Variants */
    .card-awam {{
      --card-hover-border: var(--master-green);
      --card-hover-glow: rgba(16, 185, 129, 0.2);
    }}
    .card-awam::before {{
      background: var(--master-green);
    }}

    .card-teknis {{
      --card-hover-border: var(--master-cyan);
      --card-hover-glow: rgba(6, 182, 212, 0.2);
    }}
    .card-teknis::before {{
      background: var(--master-cyan);
    }}

    .card-deck {{
      --card-hover-border: var(--master-purple);
      --card-hover-glow: rgba(168, 85, 247, 0.2);
    }}
    .card-deck::before {{
      background: var(--master-purple);
    }}

    .card-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 18px;
    }}

    .card-badge {{
      font-family: var(--master-mono);
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 1.2px;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--master-border);
    }}

    .badge-green {{ color: #6ee7b7; border-color: rgba(16, 185, 129, 0.4); background: rgba(16, 185, 129, 0.1); }}
    .badge-cyan {{ color: #7dd3fc; border-color: rgba(6, 182, 212, 0.4); background: rgba(6, 182, 212, 0.1); }}
    .badge-purple {{ color: #d8b4fe; border-color: rgba(168, 85, 247, 0.4); background: rgba(168, 85, 247, 0.1); }}

    .card-key-shortcut {{
      font-family: var(--master-mono);
      font-size: 11px;
      font-weight: 800;
      background: #1e293b;
      color: #cbd5e1;
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid #334155;
    }}

    .card-icon-title {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 12px;
    }}

    .card-icon {{
      width: 44px;
      height: 44px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      background: #141f32;
      border: 1px solid #20314b;
    }}

    .card-title {{
      font-size: clamp(19px, 1.4vw, 22px);
      font-weight: 800;
      color: #ffffff;
      line-height: 1.2;
    }}

    .card-subtitle {{
      font-size: 12.5px;
      font-weight: 600;
      color: var(--master-dim);
      margin-bottom: 16px;
    }}

    .card-desc {{
      font-size: 13.5px;
      color: #cbd5e1;
      line-height: 1.6;
      margin-bottom: 20px;
      flex-grow: 1;
    }}

    .card-points {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-bottom: 24px;
      font-size: 12.5px;
      color: var(--master-muted);
    }}

    .card-points li {{
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }}

    .card-points li span.bullet {{
      font-weight: 900;
    }}

    .btn-card-launch {{
      width: 100%;
      padding: 13px 18px;
      border-radius: 8px;
      font-family: var(--master-font);
      font-size: 13.5px;
      font-weight: 800;
      letter-spacing: 0.5px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      border: 1px solid transparent;
      transition: all 0.2s ease;
    }}

    .btn-green {{
      background: #059669;
      color: #ffffff;
    }}
    .btn-green:hover {{
      background: #10b981;
      box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4);
    }}

    .btn-cyan {{
      background: #0891b2;
      color: #ffffff;
    }}
    .btn-cyan:hover {{
      background: #06b6d4;
      box-shadow: 0 4px 14px rgba(6, 182, 212, 0.4);
    }}

    .btn-purple {{
      background: #9333ea;
      color: #ffffff;
    }}
    .btn-purple:hover {{
      background: #a855f7;
      box-shadow: 0 4px 14px rgba(168, 85, 247, 0.4);
    }}

    /* Home Footer Strip */
    .home-footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      max-width: 1460px;
      padding-top: 14px;
      border-top: 1px solid #141f32;
      font-size: 12px;
      color: var(--master-dim);
    }}

    .home-shortcuts {{
      display: flex;
      align-items: center;
      gap: 18px;
      font-family: var(--master-mono);
    }}

    .shortcut-pill {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .kbd {{
      background: #141f32;
      border: 1px solid #283e5e;
      color: #94a3b8;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 700;
    }}

    /* ========================================================================= */
    /* 3. SLIDE VIEW CONTAINERS & HUD BAR                                        */
    /* ========================================================================= */
    .deck-viewport {{
      width: 100vw;
      height: calc(100vh - 58px);
      position: absolute;
      top: 0;
      left: 0;
      overflow: hidden;
    }}

    /* Unified Floating HUD Bar */
    .unified-hud {{
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100vw;
      height: 58px;
      background: #080d17;
      border-top: 1px solid #1a273b;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      z-index: 50;
    }}

    .hud-left {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .hud-btn {{
      background: #0f1827;
      border: 1px solid #22344f;
      color: #cbd5e1;
      padding: 7px 14px;
      border-radius: 6px;
      font-size: 12.5px;
      font-weight: 700;
      font-family: var(--master-font);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }}

    .hud-btn:hover {{
      background: #1e2c42;
      color: #ffffff;
      border-color: #3b557b;
    }}

    .hud-btn-home {{
      background: rgba(16, 185, 129, 0.1);
      border-color: rgba(16, 185, 129, 0.4);
      color: #34d399;
    }}

    .hud-btn-home:hover {{
      background: rgba(16, 185, 129, 0.2);
      border-color: #10b981;
      color: #ffffff;
    }}

    .hud-divider {{
      width: 1px;
      height: 24px;
      background: #1a273b;
    }}

    .mode-pills {{
      display: flex;
      align-items: center;
      background: #0a111e;
      padding: 3px;
      border-radius: 7px;
      border: 1px solid #19263a;
      gap: 3px;
    }}

    .pill-btn {{
      background: transparent;
      border: none;
      color: #94a3b8;
      padding: 5px 12px;
      border-radius: 5px;
      font-size: 11.5px;
      font-weight: 700;
      font-family: var(--master-mono);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }}

    .pill-btn:hover {{
      color: #f8fafc;
      background: rgba(255, 255, 255, 0.05);
    }}

    .pill-btn.active {{
      background: #182840;
      color: #ffffff;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
    }}

    .pill-btn.active.mode-awam-pill {{
      background: rgba(16, 185, 129, 0.2);
      color: #6ee7b7;
      border: 1px solid rgba(16, 185, 129, 0.4);
    }}

    .pill-btn.active.mode-teknis-pill {{
      background: rgba(6, 182, 212, 0.2);
      color: #7dd3fc;
      border: 1px solid rgba(6, 182, 212, 0.4);
    }}

    .pill-btn.active.mode-deck-pill {{
      background: rgba(168, 85, 247, 0.2);
      color: #d8b4fe;
      border: 1px solid rgba(168, 85, 247, 0.4);
    }}

    .hud-center {{
      flex: 1;
      max-width: 380px;
      margin: 0 24px;
    }}

    .hud-progress-wrap {{
      width: 100%;
      height: 4px;
      background: #141f30;
      border-radius: 2px;
      overflow: hidden;
    }}

    .hud-progress-bar {{
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #10b981, #06b6d4);
      transition: width 0.2s ease;
    }}

    .hud-right {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .hud-counter {{
      font-family: var(--master-mono);
      font-size: 13px;
      font-weight: 800;
      color: #cbd5e1;
      min-width: 64px;
      text-align: center;
    }}

    .hud-btn-next {{
      background: #047857;
      border-color: #059669;
      color: #ffffff;
    }}

    .hud-btn-next:hover {{
      background: #10b981;
      border-color: #34d399;
    }}

    /* ========================================================================= */
    /* 4. MODE 3: STAGE DECK 16:9 VIEW SPECIFICS                                 */
    /* ========================================================================= */
    #view-deck {{
      align-items: center;
      justify-content: center;
      background-color: var(--master-bg);
    }}

    #view-deck .slide {{
      display: none;
      width: 100%;
      height: 100%;
      max-width: 100vw;
      max-height: calc(100vh - 58px);
      object-fit: contain;
      aspect-ratio: 16 / 9;
      box-shadow: 0 0 50px rgba(0, 0, 0, 0.85);
      animation: fadeInDeck 0.25s ease-out;
    }}

    #view-deck .slide.active {{
      display: block;
    }}

    @keyframes fadeInDeck {{
      from {{ opacity: 0.6; transform: scale(0.995); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}

    /* Thumbnail Drawer */
    .drawer {{
      position: absolute;
      top: 0;
      right: 0;
      width: 360px;
      height: calc(100vh - 58px);
      background: #0b121e;
      border-left: 1px solid #1e293b;
      transform: translateX(100%);
      transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 80;
      display: flex;
      flex-direction: column;
      padding: 20px;
      box-shadow: -10px 0 30px rgba(0, 0, 0, 0.6);
    }}

    .drawer.open {{
      transform: translateX(0);
    }}

    .drawer-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 12px;
    }}

    .drawer-title {{
      font-size: 14px;
      font-weight: 800;
      letter-spacing: 1px;
      color: #ffffff;
      font-family: var(--master-mono);
    }}

    .drawer-close {{
      background: transparent;
      border: none;
      color: var(--master-muted);
      font-size: 18px;
      cursor: pointer;
    }}

    .drawer-grid {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      overflow-y: auto;
      flex: 1;
      padding-right: 4px;
    }}

    .drawer-card {{
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 10px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      gap: 12px;
      align-items: center;
    }}

    .drawer-card:hover {{
      border-color: var(--master-green);
      transform: translateX(-3px);
      background: #142036;
    }}

    .drawer-card img {{
      width: 100px;
      aspect-ratio: 16 / 9;
      object-fit: cover;
      border-radius: 4px;
      border: 1px solid #334155;
    }}

    .drawer-card .title {{
      font-size: 12.5px;
      font-weight: 700;
      color: #f8fafc;
    }}

    .drawer-card .subtitle {{
      font-size: 11px;
      color: var(--master-muted);
    }}

    /* ========================================================================= */
    /* 5. SCOPED STYLES FOR AWAM & TEKNIS SLIDES                                 */
    /* ========================================================================= */
    {awam_css_cleaned}
    {teknis_css_cleaned}
  </style>
</head>
<body>

  <!-- ========================================================================= -->
  <!-- VIEW 1: HOME PORTAL SELECTOR                                              -->
  <!-- ========================================================================= -->
  <div id="view-home" class="view-container active">
    <header class="home-header">
      <div class="home-eyebrow">PUSSIBERAD TNI AD × KARTIKA CYBER HACKATHON 2026 // DOKTRIN PERTAHANAN SIBER AKTIF</div>
      <h1 class="home-title">PORTAL PRESENTASI RESMI <span class="hl-green">NEXUS-TRAP</span></h1>
      <p class="home-desc">
        Sistem Pertahanan Aktif Siber, Deception Teritorial Klandestin, dan Kontra-Spionase Mandiri.
        Pilih format presentasi di bawah ini sesuai profil audiens dan alokasi waktu evaluasi panggung.
      </p>
    </header>

    <!-- 3 Mode Cards -->
    <div class="home-cards-grid">
      
      <!-- Card 1: Non-Tech (Awam) -->
      <div class="home-card card-awam" onclick="switchMode('awam')">
        <div>
          <div class="card-top">
            <span class="card-badge badge-green">11 SLIDE // DOKTRIN AWAM</span>
            <span class="card-key-shortcut">[1] AWAM</span>
          </div>
          <div class="card-icon-title">
            <div class="card-icon">🛡️</div>
            <div>
              <h2 class="card-title">Doktrin &amp; Alur Cerita Awam</h2>
              <div class="card-subtitle">Untuk Pimpinan, Komandan, &amp; Juri Non-Teknis</div>
            </div>
          </div>
          <p class="card-desc">
            Penyampaian doktrin pertahanan aktif dengan analogi taktis dunia nyata tanpa istilah teknis rumit.
            Membalikkan anggapan bahwa pertahanan siber harus pasif menunggu diserang.
          </p>
          <ul class="card-points">
            <li><span class="bullet" style="color: #10b981;">✓</span> Analogi Umpan Tank Kayu, Lem Tikus Digital, &amp; Koper Ber-GPS</li>
            <li><span class="bullet" style="color: #10b981;">✓</span> Doktrin 36 Stratagem Sun Tzu (Stratagem 33 &amp; 25 Terbukti)</li>
            <li><span class="bullet" style="color: #10b981;">✓</span> Peta Alur Operasi 5 Tahap dari Masuk hingga Pelumpuhan 1-Klik</li>
            <li><span class="bullet" style="color: #10b981;">✓</span> Logika Perlindungan Markas Sendiri (Anti-Friendly-Fire)</li>
          </ul>
        </div>
        <button class="btn-card-launch btn-green">
          <span>Buka Presentasi Awam (Non-Tech)</span>
          <span>→</span>
        </button>
      </div>

      <!-- Card 2: Tech (Teknis) -->
      <div class="home-card card-teknis" onclick="switchMode('teknis')">
        <div>
          <div class="card-top">
            <span class="card-badge badge-cyan">11 SLIDE // DEEP-DIVE TEKNIS</span>
            <span class="card-key-shortcut">[2] TEKNIS</span>
          </div>
          <div class="card-icon-title">
            <div class="card-icon">⚡</div>
            <div>
              <h2 class="card-title">Arsitektur &amp; Rekayasa Sistem</h2>
              <div class="card-subtitle">Untuk Tim Juri Teknis, Red Team &amp; Cyber Engineers</div>
            </div>
          </div>
          <p class="card-desc">
            Spesifikasi rekayasa mendalam: integrasi 3-subnet terisolasi, emulasi SCADA OT Modbus port 502,
            penjeratan scanner Tarpit berkecepatan 0 req/s, dan suar DNS klandestin UDP 5053.
          </p>
          <ul class="card-points">
            <li><span class="bullet" style="color: #06b6d4;">✓</span> Topologi 3 Subnet (VLAN 10 Pangkalan, 20 Trap, 30 Komando)</li>
            <li><span class="bullet" style="color: #06b6d4;">✓</span> Modbus/TCP 502 Holding Register Genset Pangkalan Asli</li>
            <li><span class="bullet" style="color: #06b6d4;">✓</span> Tarpit Choker RFC 9309 FCrDNS Anti-Bot Discrimination</li>
            <li><span class="bullet" style="color: #06b6d4;">✓</span> Rantai Integritas HMAC-SHA256 &amp; Ekspor Multi-Firewall L3</li>
          </ul>
        </div>
        <button class="btn-card-launch btn-cyan">
          <span>Buka Presentasi Teknis (Tech)</span>
          <span>→</span>
        </button>
      </div>

      <!-- Card 3: Stage Pitch Deck (16:9) -->
      <div class="home-card card-deck" onclick="switchMode('deck')">
        <div>
          <div class="card-top">
            <span class="card-badge badge-purple">7 SLIDE // 16:9 PITCH DECK</span>
            <span class="card-key-shortcut">[3] STAGE DECK</span>
          </div>
          <div class="card-icon-title">
            <div class="card-icon">🖥️</div>
            <div>
              <h2 class="card-title">Executive Stage Pitch Deck</h2>
              <div class="card-subtitle">Untuk Sesi Panggung Proyektor &amp; Live Demo 10 Menit</div>
            </div>
          </div>
          <p class="card-desc">
            Format visual vektor murni 1920x1080 rasio 16:9 tanpa blok teks padat.
            Dirancang presisi untuk presentasi panggung berkecepatan tinggi dengan navigasi thumbnail instan.
          </p>
          <ul class="card-points">
            <li><span class="bullet" style="color: #a855f7;">✓</span> Tampilan Vektor 16:9 Zero-Scroll Definisi Tinggi</li>
            <li><span class="bullet" style="color: #a855f7;">✓</span> Panduan Koreografi Live Demo 10 Menit di Layar Kaca</li>
            <li><span class="bullet" style="color: #a855f7;">✓</span> Naskah Dinas SITREP Resmi SHA-256 PUSSIBERAD</li>
            <li><span class="bullet" style="color: #a855f7;">✓</span> Laci Visual Thumbnail Cepat Navigasi Lintas Bab</li>
          </ul>
        </div>
        <button class="btn-card-launch btn-purple">
          <span>Buka Stage Pitch Deck (16:9)</span>
          <span>→</span>
        </button>
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
        NEXUS-TRAP // 100% AIR-GAPPED STANDALONE • KARTIKA CYBER HACKATHON 2026
      </div>
    </footer>
  </div>

  <!-- ========================================================================= -->
  <!-- VIEW 2: NON-TECH (AWAM) SLIDES                                            -->
  <!-- ========================================================================= -->
  <div id="view-awam" class="view-container">
    <main class="deck" id="deck-awam" style="height: calc(100vh - 58px);">
      {awam_slides}
    </main>
  </div>

  <!-- ========================================================================= -->
  <!-- VIEW 3: TECH (TEKNIS) SLIDES                                              -->
  <!-- ========================================================================= -->
  <div id="view-teknis" class="view-container">
    <main class="deck" id="deck-teknis" style="height: calc(100vh - 58px);">
      {teknis_slides}
    </main>
  </div>

  <!-- ========================================================================= -->
  <!-- VIEW 4: STAGE DECK (16:9) SLIDES                                          -->
  <!-- ========================================================================= -->
  <div id="view-deck" class="view-container">
    <div id="deck-container" style="width: 100vw; height: calc(100vh - 58px); display: flex; align-items: center; justify-content: center;">
      {deck_slides}
    </div>

    <!-- Drawer Slider for Stage Deck -->
    <div id="deck-drawer" class="drawer">
      <div class="drawer-header">
        <span class="drawer-title">DAFTAR SLIDE STAGE DECK</span>
        <button class="drawer-close" onclick="toggleDrawer()">✕</button>
      </div>
      <div class="drawer-grid">
        {drawer_cards}
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- UNIFIED FLOATING HUD BAR (Visible in all presentation modes)              -->
  <!-- ========================================================================= -->
  <footer id="unified-hud" class="unified-hud" style="display: none;">
    <!-- Left Section -->
    <div class="hud-left">
      <button class="hud-btn hud-btn-home" onclick="switchMode('home')" title="Kembali ke Portal Seleksi (Esc / H)">
        <span>🏠 BERANDA [ESC]</span>
      </button>
      <div class="hud-divider"></div>
      <!-- Mode Switching Quick-Pills -->
      <div class="mode-pills">
        <button id="pill-awam" class="pill-btn mode-awam-pill" onclick="switchMode('awam')" title="Beralih ke Format Awam (Tekan 1)">
          🌱 AWAM (NON-TECH)
        </button>
        <button id="pill-teknis" class="pill-btn mode-teknis-pill" onclick="switchMode('teknis')" title="Beralih ke Format Teknis (Tekan 2)">
          ⚡ TEKNIS (TECH)
        </button>
        <button id="pill-deck" class="pill-btn mode-deck-pill" onclick="switchMode('deck')" title="Beralih ke Stage Deck (Tekan 3)">
          🖥️ STAGE DECK (16:9)
        </button>
      </div>
    </div>

    <!-- Center Section: Progress Bar -->
    <div class="hud-center">
      <div class="hud-progress-wrap">
        <div id="hud-progress-bar" class="hud-progress-bar"></div>
      </div>
    </div>

    <!-- Right Section: Navigation Controls -->
    <div class="hud-right">
      <button class="hud-btn" onclick="prevSlide()" title="Slide Sebelumnya (←)">
        ← SEBELUMNYA
      </button>
      <span id="hud-counter" class="hud-counter">1 / 11</span>
      <button class="hud-btn hud-btn-next" onclick="nextSlide()" title="Slide Berikutnya (→)">
        SELANJUTNYA →
      </button>
      <button id="btn-toggle-drawer" class="hud-btn" onclick="toggleDrawer()" title="Laci Thumbnail Slide (L)" style="display: none;">
        📑 LACI SLIDE
      </button>
      <button class="hud-btn" onclick="toggleFullscreen()" title="Layar Penuh (F)">
        ⛶
      </button>
    </div>
  </footer>

  <!-- ========================================================================= -->
  <!-- MASTER ORCHESTRATION JAVASCRIPT                                           -->
  <!-- ========================================================================= -->
  <script>
    const state = {{
      mode: 'home', // 'home' | 'awam' | 'teknis' | 'deck'
      indices: {{
        awam: 0,
        teknis: 0,
        deck: 0
      }}
    }};

    const views = {{
      home: document.getElementById('view-home'),
      awam: document.getElementById('view-awam'),
      teknis: document.getElementById('view-teknis'),
      deck: document.getElementById('view-deck')
    }};

    const hud = document.getElementById('unified-hud');
    const pbar = document.getElementById('hud-progress-bar');
    const counter = document.getElementById('hud-counter');
    const drawerBtn = document.getElementById('btn-toggle-drawer');
    const drawer = document.getElementById('deck-drawer');

    const pills = {{
      awam: document.getElementById('pill-awam'),
      teknis: document.getElementById('pill-teknis'),
      deck: document.getElementById('pill-deck')
    }};

    function getSlides(mode) {{
      if (mode === 'awam') return Array.from(document.querySelectorAll('#view-awam .slide'));
      if (mode === 'teknis') return Array.from(document.querySelectorAll('#view-teknis .slide'));
      if (mode === 'deck') return Array.from(document.querySelectorAll('#view-deck .slide'));
      return [];
    }}

    function updateSlideVisibility() {{
      if (state.mode === 'home') {{
        hud.style.display = 'none';
        return;
      }}

      hud.style.display = 'flex';
      const slides = getSlides(state.mode);
      const idx = state.indices[state.mode];

      slides.forEach((s, i) => {{
        s.classList.toggle('active', i === idx);
        s.setAttribute('aria-hidden', i !== idx);
      }});

      // Update HUD counter & progress
      const total = slides.length;
      counter.textContent = `${{idx + 1}} / ${{total}}`;
      pbar.style.width = `${{((idx + 1) / total) * 100}}%`;

      // Update pills
      Object.keys(pills).forEach(m => {{
        pills[m].classList.toggle('active', m === state.mode);
      }});

      // Show drawer button only in stage deck
      drawerBtn.style.display = state.mode === 'deck' ? 'inline-flex' : 'none';

      // Update URL hash without breaking history
      history.replaceState(null, '', `#${{state.mode}}:${{idx + 1}}`);
    }}

    function switchMode(newMode) {{
      if (!views[newMode]) return;
      state.mode = newMode;

      // Close drawer if open
      if (drawer) drawer.classList.remove('open');

      Object.keys(views).forEach(m => {{
        views[m].classList.toggle('active', m === newMode);
      }});

      if (newMode === 'home') {{
        hud.style.display = 'none';
        history.replaceState(null, '', '#home');
      }} else {{
        updateSlideVisibility();
      }}
    }}

    function goToSlide(n) {{
      if (state.mode === 'home') return;
      const slides = getSlides(state.mode);
      state.indices[state.mode] = Math.min(Math.max(n, 0), slides.length - 1);
      updateSlideVisibility();
      if (drawer) drawer.classList.remove('open');
    }}

    function nextSlide() {{
      if (state.mode === 'home') return;
      goToSlide(state.indices[state.mode] + 1);
    }}

    function prevSlide() {{
      if (state.mode === 'home') return;
      goToSlide(state.indices[state.mode] - 1);
    }}

    function toggleDrawer() {{
      if (drawer) drawer.classList.toggle('open');
    }}

    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen?.();
      }} else {{
        document.exitFullscreen?.();
      }}
    }}

    // Master Keyboard Handling
    document.addEventListener('keydown', (e) => {{
      const key = e.key;

      // If user presses Escape or H -> Go Home
      if (key === 'Escape' || key === 'h' || key === 'H') {{
        switchMode('home');
        return;
      }}

      // Numerical shortcuts: 1 (Awam), 2 (Teknis), 3 (Deck)
      if (key === '1' && !['INPUT', 'TEXTAREA'].includes(e.target.tagName)) {{
        switchMode('awam');
        return;
      }}
      if (key === '2' && !['INPUT', 'TEXTAREA'].includes(e.target.tagName)) {{
        switchMode('teknis');
        return;
      }}
      if (key === '3' && !['INPUT', 'TEXTAREA'].includes(e.target.tagName)) {{
        switchMode('deck');
        return;
      }}

      // Drawer toggle in deck mode
      if ((key === 'l' || key === 'L') && state.mode === 'deck') {{
        toggleDrawer();
        return;
      }}

      // Fullscreen shortcut
      if (key === 'f' || key === 'F') {{
        toggleFullscreen();
        return;
      }}

      // Arrow navigation
      if (state.mode !== 'home') {{
        if (['ArrowRight', 'PageDown', ' '].includes(key)) {{
          e.preventDefault();
          nextSlide();
        }} else if (['ArrowLeft', 'PageUp'].includes(key)) {{
          e.preventDefault();
          prevSlide();
        }} else if (key === 'Home') {{
          goToSlide(0);
        }} else if (key === 'End') {{
          goToSlide(getSlides(state.mode).length - 1);
        }}
      }}
    }});

    // Parse URL on Load (#awam:2, #tech, #deck:5, #home)
    function initFromHash() {{
      const hash = location.hash.replace('#', '').toLowerCase();
      if (!hash || hash === 'home') {{
        switchMode('home');
        return;
      }}

      const [modePart, slidePart] = hash.split(':');
      let targetMode = 'home';
      if (modePart.includes('awam') || modePart.includes('non-tech')) targetMode = 'awam';
      else if (modePart.includes('teknis') || modePart.includes('tech')) targetMode = 'teknis';
      else if (modePart.includes('deck') || modePart.includes('stage')) targetMode = 'deck';

      if (slidePart) {{
        const slideIdx = parseInt(slidePart, 10) - 1;
        if (!isNaN(slideIdx) && slideIdx >= 0) {{
          state.indices[targetMode] = slideIdx;
        }}
      }}

      switchMode(targetMode);
    }}

    initFromHash();
  </script>
</body>
</html>
"""

    OUTPUT_PATH.write_text(master_html, encoding="utf-8")
    print(f"[+] Berhasil membuat Master Presentation: {OUTPUT_PATH}")
    print(f"    Ukuran Berkas: {len(master_html):,} bytes")

if __name__ == "__main__":
    build()
