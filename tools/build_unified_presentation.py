import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
BAK_PRES_DIR = ROOT_DIR / "bak" / "presentasi_lama"
AWAM_PATH = BAK_PRES_DIR / "presentasi_awam.html"
TEKNIS_PATH = BAK_PRES_DIR / "presentasi_teknis.html"
OUTPUT_PATH = ROOT_DIR / "presentasi.html"

def generate_cover_awam_visual():
    return """
    <div class="cover-tactical-visual" style="position: relative; width: 100%; height: 100%; min-height: 420px; display: flex; align-items: center; justify-content: center;">
      <!-- Subtle Military Radar & Cyber Deception Hologram -->
      <svg viewBox="0 0 520 480" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: 100%; max-height: 460px; filter: drop-shadow(0 0 25px rgba(16, 185, 129, 0.08));">
        <defs>
          <radialGradient id="radarGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#10b981" stop-opacity="0.12"/>
            <stop offset="60%" stop-color="#06b6d4" stop-opacity="0.04"/>
            <stop offset="100%" stop-color="#05080e" stop-opacity="0"/>
          </radialGradient>
          <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#162c46"/>
            <stop offset="100%" stop-color="#0b1624"/>
          </linearGradient>
        </defs>

        <!-- Ambient Radar Glow Field -->
        <circle cx="260" cy="240" r="210" fill="url(#radarGlow)"/>

        <!-- Concentric Range Rings -->
        <circle cx="260" cy="240" r="200" stroke="#10b981" stroke-width="1.2" stroke-opacity="0.25" stroke-dasharray="3 6"/>
        <circle cx="260" cy="240" r="150" stroke="#1e3a5f" stroke-width="1" stroke-opacity="0.5"/>
        <circle cx="260" cy="240" r="100" stroke="#10b981" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="2 4"/>
        <circle cx="260" cy="240" r="50" stroke="#06b6d4" stroke-width="0.8" stroke-opacity="0.4"/>

        <!-- Crosshair Coordinate Reticles -->
        <line x1="40" y1="240" x2="480" y2="240" stroke="#1e3a5f" stroke-width="1" stroke-opacity="0.4" stroke-dasharray="4 4"/>
        <line x1="260" y1="20" x2="260" y2="460" stroke="#1e3a5f" stroke-width="1" stroke-opacity="0.4" stroke-dasharray="4 4"/>

        <!-- Azimuth Markings -->
        <text x="260" y="32" fill="#10b981" font-size="8.5" font-family="monospace" font-weight="bold" text-anchor="middle" opacity="0.6">000° UTARA [PUSSIBERAD]</text>
        <text x="470" y="244" fill="#06b6d4" font-size="8" font-family="monospace" text-anchor="end" opacity="0.6">090° TIMUR</text>
        <text x="260" y="454" fill="#64748b" font-size="8" font-family="monospace" text-anchor="middle" opacity="0.6">180° SELATAN</text>
        <text x="50" y="244" fill="#64748b" font-size="8" font-family="monospace" opacity="0.6">270° BARAT</text>

        <!-- Dynamic Radar Sweep Beam Line -->
        <line x1="260" y1="240" x2="400" y2="100" stroke="#10b981" stroke-width="1.5" stroke-opacity="0.6" stroke-linecap="round"/>
        <path d="M 260 240 L 400 100 A 198 198 0 0 0 360 80 Z" fill="#10b981" fill-opacity="0.08"/>

        <!-- Central Defense Shield / Garuda Cyber Insignia -->
        <path d="M 260 160 L 310 185 L 310 245 C 310 285 260 315 260 315 C 260 315 210 285 210 245 L 210 185 Z" fill="url(#shieldGrad)" stroke="#10b981" stroke-width="2" stroke-opacity="0.85"/>
        <!-- Star In Center -->
        <polygon points="260,195 264,208 277,208 266,216 270,229 260,221 250,229 254,216 243,208 256,208" fill="#f59e0b" opacity="0.9"/>
        <text x="260" y="252" fill="#a7f3d0" font-size="9" font-family="monospace" font-weight="900" text-anchor="middle" letter-spacing="1.5">TNI AD</text>
        <text x="260" y="266" fill="#38bdf8" font-size="7.5" font-family="monospace" font-weight="bold" text-anchor="middle" letter-spacing="1">PUSSIBERAD</text>

        <!-- Regional Satuan Teritorial Nodes & Arcs -->
        <!-- Node Aceh -->
        <circle cx="120" cy="140" r="4" fill="#10b981" opacity="0.8"/>
        <circle cx="120" cy="140" r="8" stroke="#10b981" stroke-width="0.8" opacity="0.4"/>
        <text x="120" y="128" fill="#94a3b8" font-size="7" font-family="monospace" text-anchor="middle">KODAM IM</text>
        <path d="M 124 140 Q 180 180 210 200" stroke="#10b981" stroke-width="0.8" stroke-dasharray="2 3" opacity="0.4"/>

        <!-- Node Surabaya / Jatim -->
        <circle cx="370" cy="300" r="4" fill="#10b981" opacity="0.8"/>
        <circle cx="370" cy="300" r="8" stroke="#10b981" stroke-width="0.8" opacity="0.4"/>
        <text x="370" y="316" fill="#94a3b8" font-size="7" font-family="monospace" text-anchor="middle">KODAM V/BRW</text>
        <path d="M 310 250 Q 340 270 366 298" stroke="#10b981" stroke-width="0.8" stroke-dasharray="2 3" opacity="0.4"/>

        <!-- Node IKN / Mulawarman -->
        <circle cx="360" cy="170" r="4.5" fill="#06b6d4" opacity="0.9"/>
        <circle cx="360" cy="170" r="9" stroke="#06b6d4" stroke-width="1" opacity="0.5"/>
        <text x="360" y="158" fill="#7dd3fc" font-size="7.5" font-family="monospace" font-weight="bold" text-anchor="middle">KODAM VI (IKN)</text>
        <path d="M 306 200 Q 330 185 356 172" stroke="#06b6d4" stroke-width="0.8" stroke-dasharray="2 3" opacity="0.5"/>

        <!-- Node Jayapura / Papua -->
        <circle cx="440" cy="220" r="4" fill="#10b981" opacity="0.8"/>
        <circle cx="440" cy="220" r="8" stroke="#10b981" stroke-width="0.8" opacity="0.4"/>
        <text x="440" y="208" fill="#94a3b8" font-size="7" font-family="monospace" text-anchor="middle">KODAM XVII/CEN</text>
        <path d="M 310 235 Q 380 230 436 222" stroke="#10b981" stroke-width="0.8" stroke-dasharray="2 3" opacity="0.4"/>

        <!-- Tactical Telemetry Overlay Badges -->
        <!-- Badge 1: Deception Status (Top-Right) -->
        <g transform="translate(340, 55)">
          <rect width="165" height="32" rx="4" fill="#080e18" fill-opacity="0.9" stroke="#10b981" stroke-width="1" stroke-opacity="0.6"/>
          <circle cx="14" cy="16" r="3.5" fill="#10b981"/>
          <text x="24" y="14" fill="#cbd5e1" font-size="7.5" font-family="monospace" font-weight="bold">STATUS DECEPTION:</text>
          <text x="24" y="24" fill="#34d399" font-size="8" font-family="monospace" font-weight="900">PERIMETER AKTIF [SIAGA]</text>
        </g>

        <!-- Badge 2: Decoy OT Genset (Bottom-Left) -->
        <g transform="translate(25, 360)">
          <rect width="175" height="32" rx="4" fill="#080e18" fill-opacity="0.9" stroke="#f59e0b" stroke-width="1" stroke-opacity="0.6"/>
          <circle cx="14" cy="16" r="3.5" fill="#f59e0b"/>
          <text x="24" y="14" fill="#cbd5e1" font-size="7.5" font-family="monospace" font-weight="bold">UMPAN OT GENSET 502:</text>
          <text x="24" y="24" fill="#fbbf24" font-size="8" font-family="monospace" font-weight="900">380V // 50Hz // BBM 85%</text>
        </g>

        <!-- Badge 3: Out-of-Band Canary (Bottom-Right) -->
        <g transform="translate(325, 380)">
          <rect width="180" height="32" rx="4" fill="#080e18" fill-opacity="0.9" stroke="#06b6d4" stroke-width="1" stroke-opacity="0.6"/>
          <circle cx="14" cy="16" r="3.5" fill="#06b6d4"/>
          <text x="24" y="14" fill="#cbd5e1" font-size="7.5" font-family="monospace" font-weight="bold">SUAR KLANDESTIN UDP 5053:</text>
          <text x="24" y="24" fill="#38bdf8" font-size="8" font-family="monospace" font-weight="900">DOCX TRACKING STANDBY</text>
        </g>
      </svg>
    </div>
    """

def generate_c4isr_preview_svg():
    return """
    <div class="c4isr-preview-container" style="position: relative; width: 100%; border-radius: 10px; background: #070d18; border: 1px solid #1e3a5f; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.6);">
      <!-- Window Titlebar -->
      <div style="background: #0f1c30; padding: 8px 14px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #1e293b;">
        <div style="display: flex; align-items: center; gap: 7px;">
          <span style="width: 8px; height: 8px; background: #ef4444; border-radius: 50%;"></span>
          <span style="width: 8px; height: 8px; background: #f59e0b; border-radius: 50%;"></span>
          <span style="width: 8px; height: 8px; background: #10b981; border-radius: 50%;"></span>
          <span style="margin-left: 8px; font-family: var(--master-mono); font-size: 11px; font-weight: 800; color: #94a3b8; letter-spacing: 0.5px;">C4ISR MEJA KOMANDO PUSSIBERAD // OPERASI NUSA GUARD 2026</span>
        </div>
        <div style="background: rgba(239, 68, 68, 0.2); border: 1px solid #ef4444; border-radius: 4px; padding: 2px 8px; font-family: var(--master-mono); font-size: 9.5px; font-weight: 900; color: #f87171;">
          DEFCON 1 SIAGA MERAH
        </div>
      </div>

      <!-- Map & Telemetry Grid Area -->
      <div style="padding: 14px 16px; position: relative;">
        <!-- SVG Map of NKRI with Satuan Nodes -->
        <svg viewBox="0 0 540 180" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: 165px; filter: drop-shadow(0 0 15px rgba(6, 182, 212, 0.1));">
          <!-- Grid Lines -->
          <line x1="0" y1="45" x2="540" y2="45" stroke="#102035" stroke-width="0.7" stroke-dasharray="3 3"/>
          <line x1="0" y1="90" x2="540" y2="90" stroke="#102035" stroke-width="0.7" stroke-dasharray="3 3"/>
          <line x1="0" y1="135" x2="540" y2="135" stroke="#102035" stroke-width="0.7" stroke-dasharray="3 3"/>
          <line x1="135" y1="0" x2="135" y2="180" stroke="#102035" stroke-width="0.7" stroke-dasharray="3 3"/>
          <line x1="270" y1="0" x2="270" y2="180" stroke="#102035" stroke-width="0.7" stroke-dasharray="3 3"/>
          <line x1="405" y1="0" x2="405" y2="180" stroke="#102035" stroke-width="0.7" stroke-dasharray="3 3"/>

          <!-- Stylized Archipelago Landmass Polygons -->
          <path d="M 40 50 L 90 20 L 140 85 L 115 130 L 70 80 Z" fill="#0d1b2e" stroke="#1e3a5f" stroke-width="1.2"/>
          <path d="M 145 135 L 245 140 L 260 155 L 150 150 Z" fill="#0d1b2e" stroke="#1e3a5f" stroke-width="1.2"/>
          <path d="M 200 45 L 270 35 L 285 95 L 210 100 Z" fill="#0d1b2e" stroke="#1e3a5f" stroke-width="1.2"/>
          <path d="M 295 50 L 330 35 L 320 85 L 335 125 L 305 110 Z" fill="#0d1b2e" stroke="#1e3a5f" stroke-width="1.2"/>
          <path d="M 410 70 L 490 55 L 515 115 L 440 135 Z" fill="#0d1b2e" stroke="#1e3a5f" stroke-width="1.2"/>

          <!-- Normal Kodam Nodes (Green) -->
          <circle cx="55" cy="35" r="3.5" fill="#10b981"/>
          <text x="55" y="27" fill="#64748b" font-size="7" font-family="monospace" text-anchor="middle">KODAM IM</text>

          <circle cx="240" cy="65" r="4" fill="#06b6d4"/>
          <text x="240" y="55" fill="#38bdf8" font-size="7.5" font-family="monospace" font-weight="bold" text-anchor="middle">IKN (MLW)</text>

          <circle cx="225" cy="142" r="3.5" fill="#10b981"/>
          <text x="225" y="160" fill="#64748b" font-size="7" font-family="monospace" text-anchor="middle">KODAM V</text>

          <circle cx="315" cy="85" r="3.5" fill="#10b981"/>
          <text x="315" y="75" fill="#64748b" font-size="7" font-family="monospace" text-anchor="middle">KODAM XIV</text>

          <circle cx="470" cy="95" r="3.5" fill="#10b981"/>
          <text x="470" y="85" fill="#64748b" font-size="7" font-family="monospace" text-anchor="middle">KODAM XVII</text>

          <!-- TARGET NODE INTRUDED: KODAM JAYA (Red Blinking Radar Reticle) -->
          <circle cx="160" cy="138" r="14" fill="rgba(239, 68, 68, 0.25)"/>
          <circle cx="160" cy="138" r="8" stroke="#ef4444" stroke-width="1.2" stroke-dasharray="2 3"/>
          <circle cx="160" cy="138" r="4" fill="#ef4444"/>
          <line x1="160" y1="120" x2="160" y2="156" stroke="#ef4444" stroke-width="0.8"/>
          <line x1="142" y1="138" x2="178" y2="138" stroke="#ef4444" stroke-width="0.8"/>
          
          <rect x="175" y="115" width="135" height="22" rx="3" fill="#090e18" stroke="#ef4444" stroke-width="1"/>
          <text x="182" y="129" fill="#fca5a5" font-size="8" font-family="monospace" font-weight="900">! KODAM JAYA // INTRUSI</text>
        </svg>

        <!-- Command Controls & Real-Time Dossier Split -->
        <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 12px; margin-top: 10px;">
          <!-- Left: Dossier Box -->
          <div style="background: #090e18; border: 1px solid #1e293b; border-radius: 6px; padding: 10px; font-family: var(--master-mono); font-size: 10.5px; line-height: 1.5;">
            <div style="color: #38bdf8; font-weight: 800; border-bottom: 1px solid #1e293b; padding-bottom: 3px; margin-bottom: 5px;">
              DOSSIER PENYERANG TERTANGKAP:
            </div>
            <div><span style="color: #64748b;">IP PELAKU :</span> <strong style="color: #f87171;">192.168.1.88</strong></div>
            <div><span style="color: #64748b;">CANARY OOB:</span> <span style="color: #fbbf24;">doc-991a.kodim-0501.lan</span></div>
            <div><span style="color: #64748b;">HARDWARE  :</span> <span style="color: #cbd5e1;">GPU-7b3a99e120fd9c48</span></div>
            <div><span style="color: #64748b;">STATUS    :</span> <span style="color: #f87171; font-weight: 800;">TERKUNCI DI SIAGA 1</span></div>
          </div>

          <!-- Right: Isolation Action Trigger -->
          <div style="background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.4); border-radius: 6px; padding: 10px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-family: var(--master-mono); font-size: 10px; font-weight: 800; color: #f87171; margin-bottom: 4px;">
                TINDAKAN PENANGGULANGAN:
              </div>
              <div style="font-size: 11px; line-height: 1.4; color: #cbd5e1;">
                Eksekusi isolasi host tersangka seketika tanpa kompromi.
              </div>
            </div>
            <div style="background: #ef4444; color: #ffffff; padding: 8px; border-radius: 4px; font-family: var(--master-mono); font-size: 11px; font-weight: 900; text-align: center; letter-spacing: 0.5px; box-shadow: 0 0 15px rgba(239, 68, 68, 0.4);">
              ⚡ ISOLIR HOST 1-KLIK
            </div>
          </div>
        </div>
      </div>

      <!-- Footer Bar -->
      <div style="background: #090e18; padding: 7px 16px; border-top: 1px solid #1e293b; display: flex; align-items: center; justify-content: space-between; font-family: var(--master-mono); font-size: 10px;">
        <span style="color: #10b981;">★ ANTI-FRIENDLY-FIRE: GATEWAY 100% AMAN</span>
        <span style="color: #64748b;">11 KODAM LIVE MONITOR // LATENSI &lt; 12MS</span>
      </div>
    </div>
    """

def get_native_stage_deck_slides(radar_visual=""):
    c4isr_preview = generate_c4isr_preview_svg()
    return f"""
    <!-- ========================================================================= -->
    <!-- SLIDE 1: COVER & EXECUTIVE VALUE PROPOSITION                              -->
    <!-- ========================================================================= -->
    <section class="slide active stage-slide" id="deck-slide-1">
      <div class="stage-slide-content">
        <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 36px; align-items: center; width: 100%;">
          <!-- Left Column: Executive Value Proposition -->
          <div>
            <div class="stage-eyebrow">
              <span>PUSSIBERAD TNI AD × KARTIKA CYBER HACKATHON 2026</span>
              <span class="stage-tag">KATEGORI: PENANGKALAN</span>
            </div>
            
            <h1 class="stage-h1" style="font-size: clamp(30px, 3.2vw, 54px); margin-bottom: 1.4vh;">
              NEXUS-TRAP<br>
              <span class="stage-hl-green">ACTIVE CYBER DECEPTION &amp; INTERDICTION</span>
            </h1>

            <p class="stage-lead" style="font-size: clamp(14px, 1.1vw, 17px); line-height: 1.55; margin-bottom: 2vh;">
              Platform Pertahanan Siber Asimetris, Kontra-Spionase Internal, dan Pelumpuh Otomatis Pemindai Lawan
              untuk Melindungi Jaringan Markas Satuan Teritorial Komando Daerah Militer (Kodam) Se-Indonesia.
            </p>

            <div class="stage-doctrine-quote" style="margin-bottom: 0;">
              <span class="quote-bar"></span>
              <div>
                <strong style="color: #fbbf24;">DOKTRIN UTAMA SUN TZU:</strong><br>
                <em style="color: #cbd5e1;">"Penyusup mengira sedang meretas fasilitas markas, padahal setiap langkah mereka sedang dijebak, dicatat, dan dilaporkan ke meja komando."</em>
              </div>
            </div>
          </div>

          <!-- Right Column: Tactical Radar Hologram Visual -->
          <div style="display: flex; align-items: center; justify-content: center;">
            {radar_visual}
          </div>
        </div>

        <!-- Full-Width Bottom 4 Executive Metric Cards -->
        <div class="stage-metrics-grid" style="margin-top: 2.5vh;">
          <div class="stage-metric-card border-green">
            <div class="metric-val text-green">100%</div>
            <div class="metric-title">AKURASI DETERMINISTIK</div>
            <div class="metric-sub">Zero False Positive by Design (Sekali ranjau disentuh = 100% musuh)</div>
          </div>
          <div class="stage-metric-card border-cyan">
            <div class="metric-val text-cyan">0 req/s</div>
            <div class="metric-title">TARPIT CHOKER INTERDICTION</div>
            <div class="metric-sub">Membekukan worker thread scanner otomatis &amp; soket penyerang</div>
          </div>
          <div class="stage-metric-card border-amber">
            <div class="metric-val text-amber">100%</div>
            <div class="metric-title">AIR-GAP ON-PREMISE</div>
            <div class="metric-sub">Kedaulatan total tanpa ketergantungan lisensi cloud vendor pihak ketiga</div>
          </div>
          <div class="stage-metric-card border-purple">
            <div class="metric-val text-purple">&lt; 1 DETIK</div>
            <div class="metric-title">SITREP RESMI SHA-256</div>
            <div class="metric-sub">Naskah dinas militer bersegel kriptografis sah untuk alat bukti POMAD</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- SLIDE 2: PARADOKS PERTAHANAN PASIF VS PERTAHANAN AKTIF                     -->
    <!-- ========================================================================= -->
    <section class="slide stage-slide" id="deck-slide-2">
      <div class="stage-slide-content">
        <div class="stage-eyebrow">01 // LATAR BELAKANG &amp; PARADOKS ANCAMAN SIBER</div>
        <h2 class="stage-h2">Penyusup Memakai <span class="stage-hl-red">Kredensial Sah Staf</span>. Firewall Konvensional Buta.</h2>
        
        <div class="stage-split-grid">
          <!-- Left: Dilema Pasif -->
          <div class="stage-card card-fail">
            <div class="card-tag tag-red">PARADOKS PERTAHANAN PASIF (FIREWALL / SIEM BIASA)</div>
            <h3 class="stage-h3" style="margin-bottom: 14px;">Kerapuhan Paradigma Penjaga Gerbang</h3>
            
            <div class="tile-item" style="border-left: 3px solid #ef4444;">
              <div class="tile-hdr text-red">01. TITIK BUTA INTERNAL (IDENTITY BLINDSPOT)</div>
              <div class="tile-desc">Staf tertipu phishing atau APK malware dinas. Penyerang masuk lewat pintu depan memakai kredensial sah prajurit (Living off the Land). Firewall gerbang tidak curiga.</div>
            </div>

            <div class="tile-item" style="border-left: 3px solid #ef4444;">
              <div class="tile-hdr text-red">02. BANJIR ALARM PALSU (ALARM FATIGUE)</div>
              <div class="tile-desc">SIEM konvensional memuntahkan 10.000+ log setiap hari. Tim analis siber kelelahan dan sinyal intrusi nyata tenggelam dalam tumpukan alarm palsu.</div>
            </div>

            <div class="tile-item" style="border-left: 3px solid #ef4444;">
              <div class="tile-hdr text-red">03. DWELL TIME FATAL (&gt; 200 HARI SADAR)</div>
              <div class="tile-desc">Rata-rata industri membutuhkan 200+ hari untuk menyadari penyusupan. Kebocoran baru diketahui setelah rahasia dislokasi pasukan dijual di Dark Web.</div>
            </div>

            <div style="margin-top: auto; padding-top: 10px; font-family: var(--master-mono); font-size: 11px; color: #f87171; font-weight: 800; border-top: 1px dashed rgba(239,68,68,0.3);">
              STATUS: TERLAMBAT DAN BUTA TOTAL DI DALAM PERIMETER
            </div>
          </div>

          <!-- Right: Solusi Aktif -->
          <div class="stage-card card-win">
            <div class="card-tag tag-green">DOKTRIN PERTAHANAN AKTIF (NEXUS-TRAP)</div>
            <h3 class="stage-h3" style="margin-bottom: 14px;">Memasang Ranjau Digital di Dalam Markas</h3>
            
            <div class="tile-item" style="border-left: 3px solid #10b981;">
              <div class="tile-hdr text-green">01. AKURASI DETERMINISTIK 100%</div>
              <div class="tile-desc">Dokumen umpan dan sensor genset tidak pernah disentuh personel normal. Siapa pun yang menyentuh umpan DIPASTIKAN 100% adalah musuh nyata.</div>
            </div>

            <div class="tile-item" style="border-left: 3px solid #10b981;">
              <div class="tile-hdr text-green">02. DETEKSI TEMBUS SANDBOX &amp; VM</div>
              <div class="tile-desc">Dokumen Word (.docx) menyisipkan suar DNS klandestin UDP 5053. Begitu file dibuka di komputer musuh di luar pangkalan, IP publik dan lokasinya terbongkar seketika.</div>
            </div>

            <div class="tile-item" style="border-left: 3px solid #10b981;">
              <div class="tile-hdr text-green">03. PENCEKIKAN SUMBER DAYA LAWAN (TARPIT)</div>
              <div class="tile-desc">Aliran data 1 byte/detik membekukan scanner Gobuster musuh di 0 req/s. Soket lawan macet total tanpa ada beban lalu lintas palsu di jaringan pangkalan.</div>
            </div>

            <div style="margin-top: auto; padding-top: 10px; font-family: var(--master-mono); font-size: 11px; color: #34d399; font-weight: 800; border-top: 1px dashed rgba(16,185,129,0.3);">
              STATUS: INTERSEPSI KILAT &lt; 1 DETIK TANPA ALARM PALSU
            </div>
          </div>
        </div>

        <div style="margin-top: 2.2vh; background: #090e18; border: 1px solid #1e293b; border-radius: 8px; padding: 12px 20px; display: flex; align-items: center; justify-content: space-between; font-family: var(--master-mono); font-size: 11.5px;">
          <span style="color: #94a3b8;">PERBANDINGAN KECEPATAN DETEKSI:</span>
          <span style="color: #ffffff; font-weight: 900;">200 HARI (PARADIKMA PASIF) <span style="color: var(--master-green);">&rarr; &lt; 1 DETIK (DOKTRIN AKTIF NEXUS-TRAP)</span></span>
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- SLIDE 3: FILOSOFI LONCENG ASIMETRIS & STEMPEL KRIPTOGRAFIS                 -->
    <!-- ========================================================================= -->
    <section class="slide stage-slide" id="deck-slide-3">
      <div class="stage-slide-content">
        <div class="stage-eyebrow">02 // LANDASAN TEORI &amp; SENI PERANG SUN TZU</div>
        <h2 class="stage-h2">Landasan Doktrin: <span class="stage-hl-green">Lonceng Asimetris</span> &amp; <span class="stage-hl-cyan">Stempel Digital</span></h2>
        
        <div class="stage-cards-3">
          <div class="stage-card">
            <div class="card-icon-round icon-green">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
              </svg>
            </div>
            <h3 class="stage-h3">Stratagem 33: Memancing di Air Keruh</h3>
            <div class="stage-stratagem-sub">Doktrin Umpan Berpelacak Klandestin</div>
            
            <div style="font-size: 12.5px; line-height: 1.55; color: #cbd5e1; display: flex; flex-direction: column; gap: 8px; margin: 10px 0 16px 0;">
              <div><strong style="color: #6ee7b7;">MEKANISME:</strong> Menanam dokumen Word (.docx) berelasi tersembunyi di folder staf.</div>
              <div><strong style="color: #6ee7b7;">TRIGER MUSUH:</strong> Musuh mencuri file dan membukanya di komputer luar markas.</div>
              <div><strong style="color: #6ee7b7;">DAMPAK TEMPUR:</strong> Suar DNS 5053 berdering seketika, membongkar IP publik lawan.</div>
            </div>

            <div class="stage-stat-pill" style="margin-top: auto;">Deteksi OOB DNS UDP 5053</div>
          </div>

          <div class="stage-card">
            <div class="card-icon-round icon-cyan">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#06b6d4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path>
                <path d="M2 12h20"></path>
              </svg>
            </div>
            <h3 class="stage-h3">Stratagem 25: Menukar Balok Kayu Lapuk</h3>
            <div class="stage-stratagem-sub">Doktrin Tarpit Anti-Reconnaissance</div>
            
            <div style="font-size: 12.5px; line-height: 1.55; color: #cbd5e1; display: flex; flex-direction: column; gap: 8px; margin: 10px 0 16px 0;">
              <div><strong style="color: #7dd3fc;">MEKANISME:</strong> Mengalirkan respons chunk TCP tak berujung 1 byte per detik.</div>
              <div><strong style="color: #7dd3fc;">TRIGER MUSUH:</strong> Alat pemindai (Gobuster/dirsearch) mencoba scanning direktori markas.</div>
              <div><strong style="color: #7dd3fc;">DAMPAK TEMPUR:</strong> Worker thread musuh terkunci pada 0 req/s, terminal lawan macet total.</div>
            </div>

            <div class="stage-stat-pill" style="margin-top: auto;">Throttling 1 Byte/s RFC 9309</div>
          </div>

          <div class="stage-card">
            <div class="card-icon-round icon-purple">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
                <polyline points="10 9 9 9 8 9"></polyline>
              </svg>
            </div>
            <h3 class="stage-h3">Stempel Integritas: Validitas POMAD</h3>
            <div class="stage-stratagem-sub">Rantai Bukti Forensik Tak Terbantahkan</div>
            
            <div style="font-size: 12.5px; line-height: 1.55; color: #cbd5e1; display: flex; flex-direction: column; gap: 8px; margin: 10px 0 16px 0;">
              <div><strong style="color: #d8b4fe;">MEKANISME:</strong> Menyegel setiap log intrusi dalam rantai HMAC-SHA256 SQLite.</div>
              <div><strong style="color: #d8b4fe;">TRIGER MUSUH:</strong> Setiap upaya akses ilegal terekam sidik jari GPU dan IP sumbernya.</div>
              <div><strong style="color: #d8b4fe;">DAMPAK TEMPUR:</strong> Terbit Naskah Dinas SITREP resmi sah untuk peradilan militer POMAD.</div>
            </div>

            <div class="stage-stat-pill" style="margin-top: auto;">Rantai Integritas HMAC-SHA256</div>
          </div>
        </div>

        <div style="margin-top: 2.6vh; background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.35); border-radius: 8px; padding: 12px 20px; font-family: var(--master-mono); font-size: 11.5px; color: #a7f3d0; text-align: center;">
          ★ DOKTRIN AKTIF: BUKAN MENGEJAR PENYUSUP DI RATUSAN KOMPUTER SATUAN, MELAINKAN MEMASANG UMPAN DETERMINISTIK BERSTEMPEL HUKUM POMAD
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- SLIDE 4: 4 PILAR ARSITEKTUR TEKNIS                                        -->
    <!-- ========================================================================= -->
    <section class="slide stage-slide" id="deck-slide-4">
      <div class="stage-slide-content">
        <div class="stage-eyebrow">03 // ARSITEKTUR SISTEM &amp; REKAYASA TEKNIS</div>
        <h2 class="stage-h2">Empat Pilar Pertahanan Asimetris <span class="stage-hl-green">NEXUS-TRAP</span></h2>

        <div class="stage-cards-4">
          <div class="stage-pillar-card p-green">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
              <div class="pillar-num">01</div>
              <span class="pillar-layer-badge">ICS/SCADA LAYER</span>
            </div>
            <h3 class="pillar-title">OT GENSET DECOY</h3>
            <div class="pillar-proto">Modbus/TCP Port 502 / 5020</div>
            <p class="pillar-desc">
              Meniru register daya genset cadangan pangkalan (380V, 50Hz, BBM 85%).
              Merespons paket pemindai ICS/SCADA industri tanpa membahayakan genset fisik pangkalan.
            </p>
            <div class="pillar-telemetry-box">
              <span class="telem-label">TELEMETRI KELUARAN:</span><br>
              40001: 380V | 40002: 50Hz | 40003: 85% BBM
            </div>
            <div class="pillar-badge" style="margin-top: 10px;">Transisi Siaga Kuning</div>
          </div>

          <div class="stage-pillar-card p-cyan">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
              <div class="pillar-num">02</div>
              <span class="pillar-layer-badge">L4/L7 TRAFFIC LAYER</span>
            </div>
            <h3 class="pillar-title">TCP TARPIT CHOKER</h3>
            <div class="pillar-proto">HTTP Endless Chunk Stream</div>
            <p class="pillar-desc">
              Menjebak alat otomatis (Gobuster/Dirbuster) dengan aliran data tak berujung 1 byte per detik.
              Membekukan worker thread scanner penyerang pada kecepatan 0 req/s.
            </p>
            <div class="pillar-telemetry-box">
              <span class="telem-label">THROTTLING RATE:</span><br>
              0.00 kb/s | 1 Byte/s | Thread Musuh Macet Total
            </div>
            <div class="pillar-badge" style="margin-top: 10px;">RFC 9309 FCrDNS Guard</div>
          </div>

          <div class="stage-pillar-card p-amber">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
              <div class="pillar-num">03</div>
              <span class="pillar-layer-badge">OOB THREAT INTEL</span>
            </div>
            <h3 class="pillar-title">CANARY TOKEN DNS</h3>
            <div class="pillar-proto">Out-of-Band UDP Port 5053</div>
            <p class="pillar-desc">
              Umpan dokumen Word (.docx) menyisipkan relasi template klandestin.
              Membongkar IP publik &amp; geolokasi penyerang bahkan saat dibuka di lingkungan Sandbox/VM terisolasi.
            </p>
            <div class="pillar-telemetry-box">
              <span class="telem-label">OOB DNS RESOLVER:</span><br>
              doc-991a.kodim-0501.canary.lan &rarr; IP Terlacak
            </div>
            <div class="pillar-badge" style="margin-top: 10px;">Transisi Siaga 1 Merah</div>
          </div>

          <div class="stage-pillar-card p-purple">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
              <div class="pillar-num">04</div>
              <span class="pillar-layer-badge">C4ISR DECISION LAYER</span>
            </div>
            <h3 class="pillar-title">AUTO-SITREP &amp; ISOLASI</h3>
            <div class="pillar-proto">SHA-256 &amp; Multi-Firewall L3</div>
            <p class="pillar-desc">
              Pemutusan koneksi 1-klik dengan Anti-Friendly-Fire gateway pangkalan.
              Menghasilkan naskah dinas resmi PUSSIBERAD dan aturan firewall (iptables, MikroTik, Cisco ACL).
            </p>
            <div class="pillar-telemetry-box">
              <span class="telem-label">RANTAI BUKTI SHA-256:</span><br>
              1178D8418DBADC3F... [Sah untuk POMAD]
            </div>
            <div class="pillar-badge" style="margin-top: 10px;">&lt; 1 Detik Terbit Otomatis</div>
          </div>
        </div>

        <div style="margin-top: 2.5vh; background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 12px 20px; font-family: var(--master-mono); font-size: 11.5px; color: #a7f3d0; text-align: center;">
          ★ SELURUH 4 PILAR BERJALAN TERISOLASI SECARA ZERO-IMPACT TANPA MEMBEBANI JARINGAN UTAMA SATUAN
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- SLIDE 5: KOREOGRAFI LIVE DEMO 10 MENIT                                    -->
    <!-- ========================================================================= -->
    <section class="slide stage-slide" id="deck-slide-5">
      <div class="stage-slide-content">
        <div class="stage-eyebrow">04 // SKENARIO PANGGUNG &amp; UJI PENJURIAN</div>
        <h2 class="stage-h2">Koreografi Demonstrasi Langsung <span class="stage-hl-green">(10 Menit di Layar Kaca)</span></h2>

        <div style="margin-bottom: 1.6vh; display: flex; align-items: center; justify-content: space-between; background: rgba(15, 23, 42, 0.6); border: 1px solid #1e293b; border-radius: 6px; padding: 10px 18px; font-family: var(--master-mono); font-size: 11px;">
          <span style="color: #64748b;">TOTAL DURASI DEMO PENJURIAN: <strong style="color: #ffffff;">10 MENIT</strong></span>
          <span style="color: #38bdf8; font-weight: 800;">5 FASE RESPON AKTIF // DARI INFILTRASI HINGGA ISOLASI HUKUM</span>
        </div>

        <div class="stage-choreography-grid">
          <div class="choreo-step">
            <div class="choreo-time">00:00 - 02:30</div>
            <div class="choreo-status st-green">SIAGA 3 HIJAU</div>
            <h4 class="choreo-title">Baseline Normal Pangkalan</h4>
            <p class="choreo-desc">
              Dashboard memantau 11 Kodam aktif. Sensor Modbus genset dan suar Canary dalam status siaga tanpa beban lalu lintas palsu.
            </p>
          </div>

          <div class="choreo-step">
            <div class="choreo-time">02:30 - 04:30</div>
            <div class="choreo-status st-amber">SIAGA 2 KUNING</div>
            <h4 class="choreo-title">Pengintaian Modbus OT</h4>
            <p class="choreo-desc">
              Penyerang memindai port 502 genset markas. Umpan membalas 380V/50Hz. Dashboard membunyikan Siaga Kuning dan mencatat IP pelaku.
            </p>
          </div>

          <div class="choreo-step">
            <div class="choreo-time">04:30 - 07:00</div>
            <div class="choreo-status st-cyan">TARPIT TRAPPED</div>
            <h4 class="choreo-title">Pembekuan Terminal Musuh</h4>
            <p class="choreo-desc">
              Penyerang meluncurkan Gobuster scanner. Tarpit Choker mengunci worker thread lawan ke 0 req/s. Terminal musuh macet total.
            </p>
          </div>

          <div class="choreo-step">
            <div class="choreo-time">07:00 - 09:00</div>
            <div class="choreo-status st-red">SIAGA 1 MERAH</div>
            <h4 class="choreo-title">Detonasi Dokumen Canary</h4>
            <p class="choreo-desc">
              Musuh membuka file rahasia curian di luar markas. Suar DNS 5053 meledak, pin Kodam di peta menyala merah, geolokasi musuh tertangkap.
            </p>
          </div>

          <div class="choreo-step">
            <div class="choreo-time">09:00 - 10:00</div>
            <div class="choreo-status st-purple">NETRALISASI</div>
            <h4 class="choreo-title">1-Klik Isolasi &amp; SITREP</h4>
            <p class="choreo-desc">
              Komandan menekan 1 tombol isolasi host. Naskah Dinas SITREP berstempel hash SHA-256 terbit seketika untuk Danpussiberad.
            </p>
          </div>
        </div>

        <!-- Live Demo Operational Metrics Strip -->
        <div class="stage-demo-strip">
          <div class="demo-metric-item">
            <span class="m-lbl">LATENSI INTERSEPSI:</span>
            <span class="m-val">&lt; 12 ms</span>
          </div>
          <div class="demo-metric-item">
            <span class="m-lbl">ANTI-FRIENDLY-FIRE:</span>
            <span class="m-val text-green">AKTIF (GATEWAY 100% AMAN)</span>
          </div>
          <div class="demo-metric-item">
            <span class="m-lbl">INTEGRITAS BUKTI HUKUM:</span>
            <span class="m-val text-cyan">HMAC-SHA256 LENGKAP</span>
          </div>
          <div class="demo-metric-item">
            <span class="m-lbl">TARGET PENINDAKAN:</span>
            <span class="m-val text-amber">1-KLIK QUARANTINE HOST</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- SLIDE 6: PURWARUPA C4ISR & BUKTI HUKUM POMAD                              -->
    <!-- ========================================================================= -->
    <section class="slide stage-slide" id="deck-slide-6">
      <div class="stage-slide-content">
        <div class="stage-eyebrow">05 // PURWARUPA SISTEM &amp; VALIDITAS HUKUM</div>
        <h2 class="stage-h2">Layar Komando C4ISR &amp; <span class="stage-hl-green">Naskah Dinas Bersegel SHA-256</span></h2>

        <div class="stage-split-grid">
          <!-- Left: Real SVG Wireframe Prototype of Dashboard -->
          <div class="stage-card">
            <div class="card-tag tag-cyan">INTERFACE MEJA KOMANDO PUSSIBERAD</div>
            <h3 class="stage-h3" style="margin-bottom: 12px;">Dashboard C4ISR 1-Layar Zero-Scroll</h3>
            {c4isr_preview}
          </div>

          <!-- Right: Official SITREP Document Prototype -->
          <div class="stage-card">
            <div class="card-tag tag-purple">STANDAR NASKAH DINAS MILITER TNI AD</div>
            <h3 class="stage-h3" style="margin-bottom: 12px;">Integritas Forensik Berstandar POMAD</h3>
            
            <div class="sitrep-preview-box">
              <div class="sitrep-hdr">KOP: MARKAS BESAR ANGKATAN DARAT // PUSAT SIBER TNI AD</div>
              <div class="sitrep-line">NOMOR: R/SITREP-20261027-091/PUSSIBERAD | KLASIFIKASI: RAHASIA</div>
              <div class="sitrep-body">
                1. DASAR: Doktrin Pertahanan Siber Semesta TNI AD Kep/44/XII/2025.<br>
                2. FAKTA: Intersepsi Dokumen Umpan Satuan KODAM JAYA / KOREM 051.<br>
                3. PENINDAKAN: Host 192.168.1.88 Diisolir. Aturan Firewall Terpasang.<br>
                4. SEKTOR: Hardware/GPU Fingerprint 7b3a99e120fd9c48 Tercatat.
              </div>
              <div class="sitrep-seal">
                ★ SEGEL SHA-256: 1178D8418DBADC3F4D9085AC98EFB76378A86C459D115C6B... [VALID]
              </div>
            </div>

            <div style="margin-top: 14px; background: rgba(168, 85, 247, 0.08); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 6px; padding: 12px 14px; font-family: var(--master-mono); font-size: 11px; color: #d8b4fe; display: flex; align-items: center; justify-content: space-between;">
              <span>STATUS RANTAI BUKTI:</span>
              <span style="font-weight: 800;">100% UNTAMPERED // ALAT BUKTI SAH PERADILAN MILITER</span>
            </div>
            
            <div style="margin-top: auto; padding-top: 12px; font-family: var(--master-mono); font-size: 10.5px; color: #64748b; line-height: 1.4;">
              * Laporan otomatis diekspor dalam format resmi militer siap cetak dan diverifikasi stempel hash kriptografis oleh Oditur Militer.
            </div>
          </div>
        </div>

        <div style="margin-top: 2.2vh; background: #090e18; border: 1px solid #1e293b; border-radius: 8px; padding: 12px 18px; display: flex; align-items: center; justify-content: space-between; font-family: var(--master-mono); font-size: 11.5px;">
          <div style="display: flex; align-items: center; gap: 8px; color: #a7f3d0;">
            <span style="display: inline-block; width: 7px; height: 7px; background: #10b981; border-radius: 50%; box-shadow: 0 0 6px #10b981;"></span>
            <span>SOP KESIAPAN MILITER: DARI DETEKSI RAW HINGGA PERINTAH ISOLASI TERLAKSANA DALAM SATU TAMPILAN</span>
          </div>
          <div style="color: #64748b;">PUSSIBERAD TNI AD // 2026</div>
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- SLIDE 7: KESIMPULAN & KEDAULATAN PERTAHANAN SIBER NKRI                     -->
    <!-- ========================================================================= -->
    <section class="slide stage-slide" id="deck-slide-7">
      <div class="stage-slide-content">
        <div class="stage-eyebrow">06 // KESIMPULAN STRATEGIS &amp; KESIAPAN GELAR</div>
        <h2 class="stage-h2">100% Mandiri, <span class="stage-hl-green">Kedaulatan Penuh</span>, Siap Gelar di Jajaran Kodam</h2>

        <div class="stage-cards-3">
          <div class="stage-card">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
              <div class="card-icon-round icon-green" style="margin-bottom: 0;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
                </svg>
              </div>
              <span class="stage-stat-giant text-green">Rp 0,-</span>
            </div>
            
            <h3 class="stage-h3">Efisiensi Anggaran Negara</h3>
            <div class="stage-stratagem-sub">Nol Rupiah Lisensi Vendor Asing</div>
            <p class="stage-text">
              Didesain khusus untuk berjalan di komputer pangkalan biasa tanpa perlu membeli server atau lisensi vendor luar negeri bernilai miliaran rupiah.
            </p>
            <div class="stage-stat-pill" style="margin-top: auto;">100% Mandiri Finansial</div>
          </div>

          <div class="stage-card">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
              <div class="card-icon-round icon-cyan" style="margin-bottom: 0;">
                <svg width="24" height="20" viewBox="0 0 24 20" fill="none" style="filter: drop-shadow(0 0 6px rgba(239,68,68,0.3));">
                  <rect x="0.5" y="0.5" width="23" height="19" rx="3.5" stroke="#06b6d4" stroke-width="1"/>
                  <rect x="1" y="1" width="22" height="9" fill="#ef4444" rx="3 3 0 0"/>
                  <rect x="1" y="10" width="22" height="9" fill="#f8fafc" rx="0 0 3 3"/>
                </svg>
              </div>
              <span class="stage-stat-giant text-cyan">100%</span>
            </div>

            <h3 class="stage-h3">Kedaulatan &amp; Kemandirian</h3>
            <div class="stage-stratagem-sub">Air-Gapped Standalone &amp; Zero-Backdoor</div>
            <p class="stage-text">
              100% karya mandiri talenta nasional. Bebas dari risiko backdoor atau spyware pihak asing yang dapat membocorkan rahasia militer Indonesia.
            </p>
            <div class="stage-stat-pill" style="margin-top: auto;">Kebal Embargo Teknologi</div>
          </div>

          <div class="stage-card">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
              <div class="card-icon-round icon-purple" style="margin-bottom: 0;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                  <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
                </svg>
              </div>
              <span class="stage-stat-giant text-purple">&lt; 1 Menit</span>
            </div>

            <h3 class="stage-h3">Gelar Instan Satuan Kodim</h3>
            <div class="stage-stratagem-sub">Hot-Plug Teritorial Nusantara</div>
            <p class="stage-text">
              Mekanisme hot-plug generator satuan memungkinkan pendaftaran Kodim baru dalam 1 klik tanpa perlu kompilasi ulang kode atau restart server.
            </p>
            <div class="stage-stat-pill" style="margin-top: auto;">Hot-Plug Zero-Recompile</div>
          </div>
        </div>

        <div class="stage-final-banner">
          <div class="banner-quote">
            "KITA TIDAK MENUNGGU DISERANG. KITA YANG MENYIAPKAN PANGGUNGNYA."
          </div>
          <div class="banner-sub">
            PUSSIBERAD TNI AD × KARTIKA CYBER HACKATHON 2026 // DOKTRIN PERTAHANAN SIBER AKTIF
          </div>
        </div>
      </div>
    </section>
    """

    return """
    <!-- ========================================================================= -->
    <!-- SLIDE 1: COVER & EXECUTIVE VALUE PROPOSITION                              -->
    <!-- ========================================================================= -->
    <section class="slide active stage-slide" id="deck-slide-1">
      <div class="stage-slide-content">
        <div class="stage-eyebrow">
          <span>PUSSIBERAD TNI AD × KARTIKA CYBER HACKATHON 2026</span>
          <span class="stage-tag">KATEGORI: PENANGKALAN</span>
        </div>
        
        <h1 class="stage-h1">
          NEXUS-TRAP<br>
          <span class="stage-hl-green">ACTIVE CYBER DECEPTION &amp; INTERDICTION</span>
        </h1>

        <p class="stage-lead">
          Platform Pertahanan Siber Asimetris, Kontra-Spionase Internal, dan Pelumpuh Otomatis Pemindai Lawan
          untuk Melindungi Jaringan Markas &amp; Satuan Teritorial Komando Daerah Militer (Kodam) Se-Indonesia.
        </p>

        <div class="stage-doctrine-quote">
          <span class="quote-bar"></span>
          <div>
            <strong>DOKTRIN UTAMA SUN TZU:</strong>
            <em>"Penyusup mengira sedang meretas fasilitas pangkalan, padahal setiap langkah mereka sedang ditahan, dicatat, dan dilaporkan ke meja komando."</em>
          </div>
        </div>

        <div class="stage-metrics-grid">
          <div class="stage-metric-card border-green">
            <div class="metric-val text-green">100%</div>
            <div class="metric-title">AKURASI DETERMINISTIK</div>
            <div class="metric-sub">Zero False Positive by Design (Hanya bereaksi saat ranjau disentuh)</div>
          </div>
          <div class="stage-metric-card border-cyan">
            <div class="metric-val text-cyan">0 req/s</div>
            <div class="metric-title">TARPIT CHOKER INTERDICTION</div>
            <div class="metric-sub">Membekukan worker thread scanner otomatis &amp; soket penyerang</div>
          </div>
          <div class="stage-metric-card border-amber">
            <div class="metric-val text-amber">100%</div>
            <div class="metric-title">AIR-GAP ON-PREMISE</div>
            <div class="metric-sub">Kedaulatan total tanpa ketergantungan lisensi cloud pihak ketiga</div>
          </div>
          <div class="stage-metric-card border-purple">
            <div class="metric-val text-purple">&lt; 1 DETIK</div>
            <div class="metric-title">SITREP RESMI SHA-256</div>
            <div class="metric-sub">Naskah dinas militer bersegel kriptografis sah untuk POMAD</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- SLIDE 2: PARADOKS PERTAHANAN PASIF VS PERTAHANAN AKTIF                     -->
    <!-- ========================================================================= -->
    <section class="slide stage-slide" id="deck-slide-2">
      <div class="stage-slide-content">
        <div class="stage-eyebrow">01 // LATAR BELAKANG &amp; PARADOKS ANCAMAN SIBER</div>
        <h2 class="stage-h2">Penyusup Memakai <span class="stage-hl-red">Kredensial Sah Staf</span>. Firewall Konvensional Buta.</h2>
        
        <div class="stage-split-grid">
          <!-- Left: Dilema Pasif -->
          <div class="stage-card card-fail">
            <div class="card-tag tag-red">PARADOKS PERTAHANAN PASIF (FIREWALL / SIEM BIASA)</div>
            <h3 class="stage-h3">Kerapuhan Paradigma Penjaga Gerbang</h3>
            <ul class="stage-list list-red">
              <li><strong>Titik Buta Internal:</strong> Begitu penyerang memperoleh akun staf (melalui phishing atau APK malware), ia bergerak bebas tanpa dicurigai firewall.</li>
              <li><strong>Banjir Alarm Palsu (Alarm Fatigue):</strong> SIEM konvensional menghasilkan ribuan log setiap hari sehingga sinyal intrusi nyata tenggelam.</li>
              <li><strong>Rata-rata Waktu Sadar &gt; 200 Hari:</strong> Kebocoran baru disadari setelah data personel dan rahasia dislokasi pasukan dijual di Dark Web.</li>
              <li><strong>Biaya Lisensi Vendor Asing Tinggi:</strong> Membebani anggaran negara ratusan juta rupiah per tahun tanpa jaminan kedaulatan.</li>
            </ul>
          </div>

          <!-- Right: Solusi Aktif -->
          <div class="stage-card card-win">
            <div class="card-tag tag-green">DOKTRIN PERTAHANAN AKTIF (NEXUS-TRAP)</div>
            <h3 class="stage-h3">Memasang Ranjau Digital di Dalam Markas</h3>
            <ul class="stage-list list-green">
              <li><strong>Deterministik 100%:</strong> Sistem asli tidak pernah disentuh personel biasa. Siapa pun yang menyentuh umpan dipastikan adalah musuh.</li>
              <li><strong>Deteksi Menembus Sandbox &amp; VM:</strong> Dokumen Canary memicu suar DNS Out-of-Band saat file dibuka di komputer luar mana pun.</li>
              <li><strong>Pencekikan Sumber Daya Penyerang:</strong> Modul Tarpit Choker menahan koneksi musuh pada 0 req/s, menguras kuota dan soket mereka.</li>
              <li><strong>100% Karya Mandiri:</strong> Berjalan di komputer pangkalan biasa tanpa lisensi asing, siap digelar di seluruh Kodim terluar.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- SLIDE 3: FILOSOFI LONCENG ASIMETRIS & STEMPEL KRIPTOGRAFIS                 -->
    <!-- ========================================================================= -->
    <section class="slide stage-slide" id="deck-slide-3">
      <div class="stage-slide-content">
        <div class="stage-eyebrow">02 // LANDASAN TEORI &amp; SENI PERANG SUN TZU</div>
        <h2 class="stage-h2">Landasan Doktrin: <span class="stage-hl-green">Lonceng Asimetris</span> &amp; <span class="stage-hl-cyan">Stempel Digital</span></h2>
        
        <div class="stage-cards-3">
          <div class="stage-card">
            <div class="card-icon-round icon-green">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
              </svg>
            </div>
            <h3 class="stage-h3">Stratagem 33: Memancing di Air Keruh</h3>
            <div class="stage-stratagem-sub">Doktrin Umpan Berpelacak Klandestin</div>
            <p class="stage-text">
              Alih-alih bersusah payah mengejar penyusup di antara ribuan komputer pangkalan, kita sediakan dokumen umpan yang tampak sangat rahasia.
              Saat dibuka di laptop penyerang, suar DNS otomatis berdering di Meja Komando PUSSIBERAD.
            </p>
            <div class="stage-stat-pill" style="margin-top: auto;">Deteksi OOB DNS UDP 5053</div>
          </div>

          <div class="stage-card">
            <div class="card-icon-round icon-cyan">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#06b6d4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path>
                <path d="M2 12h20"></path>
              </svg>
            </div>
            <h3 class="stage-h3">Stratagem 25: Menukar Balok Kayu Lapuk</h3>
            <div class="stage-stratagem-sub">Doktrin Tarpit Anti-Reconnaissance</div>
            <p class="stage-text">
              Penyerang mengira berhasil menemukan celah direktori server. Kenyataannya, mereka terjerat aliran chunk TCP tak berujung (0 req/s).
              Sumber daya pemindai musuh terkunci dan membeku sementara markas tetap aman.
            </p>
            <div class="stage-stat-pill" style="margin-top: auto;">Throttling 1 Byte/s RFC 9309</div>
          </div>

          <div class="stage-card">
            <div class="card-icon-round icon-purple">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
                <polyline points="10 9 9 9 8 9"></polyline>
              </svg>
            </div>
            <h3 class="stage-h3">Stempel Integritas: Validitas POMAD</h3>
            <div class="stage-stratagem-sub">Rantai Bukti Forensik Tak Terbantahkan</div>
            <p class="stage-text">
              Setiap jejak, geolokasi IP, dan sidik jari perangkat penyerang langsung disegel dalam rantai HMAC-SHA256.
              Laporan Naskah Dinas SITREP terbit seketika dan sah sebagai alat bukti hukum peradilan militer.
            </p>
            <div class="stage-stat-pill" style="margin-top: auto;">Rantai Integritas HMAC-SHA256</div>
          </div>
        </div>

        <div style="margin-top: 2.6vh; background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.35); border-radius: 8px; padding: 12px 20px; font-family: var(--master-mono); font-size: 11.5px; color: #a7f3d0; text-align: center;">
          ★ DOKTRIN AKTIF: BUKAN MENGEJAR PENYUSUP DI RATUSAN KOMPUTER SATUAN, MELAINKAN MEMASANG UMPAN DETERMINISTIK BERSTEMPEL HUKUM POMAD
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- SLIDE 4: 4 PILAR ARSITEKTUR TEKNIS                                        -->
    <!-- ========================================================================= -->
    <section class="slide stage-slide" id="deck-slide-4">
      <div class="stage-slide-content">
        <div class="stage-eyebrow">03 // ARSITEKTUR SISTEM &amp; REKAYASA TEKNIS</div>
        <h2 class="stage-h2">Empat Pilar Pertahanan Asimetris <span class="stage-hl-green">NEXUS-TRAP</span></h2>

        <div class="stage-cards-4">
          <div class="stage-pillar-card p-green">
            <div class="pillar-num">01</div>
            <h3 class="pillar-title">OT GENSET DECOY</h3>
            <div class="pillar-proto">Modbus/TCP Port 502 / 5020</div>
            <p class="pillar-desc">
              Meniru register daya genset cadangan pangkalan (380V, 50Hz, BBM 85%).
              Merespons paket pemindai ICS/SCADA industri tanpa membahayakan genset fisik pangkalan.
            </p>
            <div class="pillar-telemetry-box">
              <span class="telem-label">TELEMETRI KELUARAN:</span><br>
              40001: 380V | 40002: 50Hz | 40003: 85% BBM
            </div>
            <div class="pillar-badge" style="margin-top: 10px;">Transisi Siaga Kuning</div>
          </div>

          <div class="stage-pillar-card p-cyan">
            <div class="pillar-num">02</div>
            <h3 class="pillar-title">TCP TARPIT CHOKER</h3>
            <div class="pillar-proto">HTTP Endless Chunk Stream</div>
            <p class="pillar-desc">
              Menjebak alat otomatis (Gobuster/Dirbuster) dengan aliran data tak berujung 1 byte per detik.
              Membekukan worker thread scanner penyerang pada kecepatan 0 req/s.
            </p>
            <div class="pillar-telemetry-box">
              <span class="telem-label">THROTTLING RATE:</span><br>
              0.00 kb/s | 1 Byte/s | Thread Musuh Macet Total
            </div>
            <div class="pillar-badge" style="margin-top: 10px;">RFC 9309 FCrDNS Guard</div>
          </div>

          <div class="stage-pillar-card p-amber">
            <div class="pillar-num">03</div>
            <h3 class="pillar-title">CANARY TOKEN DNS</h3>
            <div class="pillar-proto">Out-of-Band UDP Port 5053</div>
            <p class="pillar-desc">
              Umpan dokumen Word (.docx) menyisipkan relasi template klandestin.
              Membongkar IP publik &amp; geolokasi penyerang bahkan saat dibuka di lingkungan Sandbox/VM terisolasi.
            </p>
            <div class="pillar-telemetry-box">
              <span class="telem-label">OOB DNS RESOLVER:</span><br>
              doc-991a.kodim-0501.canary.lan &rarr; IP Terlacak
            </div>
            <div class="pillar-badge" style="margin-top: 10px;">Transisi Siaga 1 Merah</div>
          </div>

          <div class="stage-pillar-card p-purple">
            <div class="pillar-num">04</div>
            <h3 class="pillar-title">AUTO-SITREP &amp; ISOLASI</h3>
            <div class="pillar-proto">SHA-256 &amp; Multi-Firewall L3</div>
            <p class="pillar-desc">
              Pemutusan koneksi 1-klik dengan Anti-Friendly-Fire gateway pangkalan.
              Menghasilkan naskah dinas resmi PUSSIBERAD dan aturan firewall (iptables, MikroTik, Cisco ACL).
            </p>
            <div class="pillar-telemetry-box">
              <span class="telem-label">RANTAI BUKTI SHA-256:</span><br>
              1178D8418DBADC3F... [Sah untuk POMAD]
            </div>
            <div class="pillar-badge" style="margin-top: 10px;">&lt; 1 Detik Terbit Otomatis</div>
          </div>
        </div>

        <div style="margin-top: 2.5vh; background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 12px 20px; font-family: var(--master-mono); font-size: 11.5px; color: #a7f3d0; text-align: center;">
          ★ SELURUH 4 PILAR BERJALAN TERISOLASI SECARA ZERO-IMPACT TANPA MEMBEBANI JARINGAN UTAMA SATUAN
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- SLIDE 5: KOREOGRAFI LIVE DEMO 10 MENIT                                    -->
    <!-- ========================================================================= -->
    <section class="slide stage-slide" id="deck-slide-5">
      <div class="stage-slide-content">
        <div class="stage-eyebrow">04 // SKENARIO PANGGUNG &amp; UJI PENJURIAN</div>
        <h2 class="stage-h2">Koreografi Demonstrasi Langsung <span class="stage-hl-green">(10 Menit di Layar Kaca)</span></h2>

        <div style="margin-bottom: 1.6vh; display: flex; align-items: center; justify-content: space-between; background: rgba(15, 23, 42, 0.6); border: 1px solid #1e293b; border-radius: 6px; padding: 10px 18px; font-family: var(--master-mono); font-size: 11px;">
          <span style="color: #64748b;">TOTAL DURASI DEMO PENJURIAN: <strong style="color: #ffffff;">10 MENIT</strong></span>
          <span style="color: #38bdf8; font-weight: 800;">5 FASE RESPON AKTIF // DARI INFILTRASI HINGGA ISOLASI HUKUM</span>
        </div>

        <div class="stage-choreography-grid">
          <div class="choreo-step">
            <div class="choreo-time">00:00 - 02:30</div>
            <div class="choreo-status st-green">SIAGA 3 HIJAU</div>
            <h4 class="choreo-title">Baseline Normal Pangkalan</h4>
            <p class="choreo-desc">
              Dashboard memantau 11 Kodam aktif. Sensor Modbus genset dan suar Canary dalam status siaga tanpa beban lalu lintas palsu.
            </p>
          </div>

          <div class="choreo-step">
            <div class="choreo-time">02:30 - 04:30</div>
            <div class="choreo-status st-amber">SIAGA 2 KUNING</div>
            <h4 class="choreo-title">Pengintaian Modbus OT</h4>
            <p class="choreo-desc">
              Penyerang memindai port 502 genset markas. Umpan membalas 380V/50Hz. Dashboard membunyikan Siaga Kuning dan mencatat IP pelaku.
            </p>
          </div>

          <div class="choreo-step">
            <div class="choreo-time">04:30 - 07:00</div>
            <div class="choreo-status st-cyan">TARPIT TRAPPED</div>
            <h4 class="choreo-title">Pembekuan Terminal Musuh</h4>
            <p class="choreo-desc">
              Penyerang meluncurkan Gobuster scanner. Tarpit Choker mengunci worker thread lawan ke 0 req/s. Terminal musuh macet total.
            </p>
          </div>

          <div class="choreo-step">
            <div class="choreo-time">07:00 - 09:00</div>
            <div class="choreo-status st-red">SIAGA 1 MERAH</div>
            <h4 class="choreo-title">Detonasi Dokumen Canary</h4>
            <p class="choreo-desc">
              Musuh membuka file rahasia curian di luar markas. Suar DNS 5053 meledak, pin Kodam di peta menyala merah, geolokasi musuh tertangkap.
            </p>
          </div>

          <div class="choreo-step">
            <div class="choreo-time">09:00 - 10:00</div>
            <div class="choreo-status st-purple">NETRALISASI</div>
            <h4 class="choreo-title">1-Klik Isolasi &amp; SITREP</h4>
            <p class="choreo-desc">
              Komandan menekan 1 tombol isolasi host. Naskah Dinas SITREP berstempel hash SHA-256 terbit seketika untuk Danpussiberad.
            </p>
          </div>
        </div>

        <!-- Live Demo Operational Metrics Strip -->
        <div class="stage-demo-strip">
          <div class="demo-metric-item">
            <span class="m-lbl">LATENSI INTERSEPSI:</span>
            <span class="m-val">&lt; 12 ms</span>
          </div>
          <div class="demo-metric-item">
            <span class="m-lbl">ANTI-FRIENDLY-FIRE:</span>
            <span class="m-val text-green">AKTIF (GATEWAY 100% AMAN)</span>
          </div>
          <div class="demo-metric-item">
            <span class="m-lbl">INTEGRITAS BUKTI HUKUM:</span>
            <span class="m-val text-cyan">HMAC-SHA256 LENGKAP</span>
          </div>
          <div class="demo-metric-item">
            <span class="m-lbl">TARGET PENINDAKAN:</span>
            <span class="m-val text-amber">1-KLIK QUARANTINE HOST</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- SLIDE 6: PURWARUPA C4ISR & BUKTI HUKUM POMAD                              -->
    <!-- ========================================================================= -->
    <section class="slide stage-slide" id="deck-slide-6">
      <div class="stage-slide-content">
        <div class="stage-eyebrow">05 // PURWARUPA SISTEM &amp; VALIDITAS HUKUM</div>
        <h2 class="stage-h2">Layar Komando C4ISR &amp; <span class="stage-hl-green">Naskah Dinas Bersegel SHA-256</span></h2>

        <div class="stage-split-grid">
          <div class="stage-card">
            <div class="card-tag tag-cyan">INTERFACE MEJA KOMANDO PUSSIBERAD</div>
            <h3 class="stage-h3">Dashboard C4ISR 1-Layar Zero-Scroll</h3>
            <ul class="stage-list list-cyan">
              <li><strong>Peta Operasi NKRI:</strong> Menampilkan sebaran sensor 11 Kodam dan titik satelit Kodim teritorial secara real-time.</li>
              <li><strong>Papan Defcon Status:</strong> Lampu siaga Hijau, Kuning, Merah yang mudah dipahami perwira jaga pangkalan.</li>
              <li><strong>Intelligence Dossier:</strong> Merekam alamat IP luar, hardware hash, vector intrusi, dan nama file yang bocor.</li>
              <li><strong>Tombol Isolasi Kilat:</strong> 1 detik memutus hak akses host terdampak dengan proteksi Anti-Friendly-Fire gateway.</li>
            </ul>
            <div style="margin-top: auto; padding-top: 14px; border-top: 1px solid #1e293b; display: flex; align-items: center; justify-content: space-between; font-family: var(--master-mono); font-size: 11px;">
              <span style="color: #64748b;">MEJA TELEMETRI:</span>
              <span style="color: #38bdf8; font-weight: 800;">11 KODAM AKTIF // DEFCON MONITOR // ZERO-RELOAD</span>
            </div>
          </div>

          <div class="stage-card">
            <div class="card-tag tag-purple">STANDAR NASKAH DINAS MILITER TNI AD</div>
            <h3 class="stage-h3">Integritas Forensik Berstandar POMAD</h3>
            <div class="sitrep-preview-box">
              <div class="sitrep-hdr">KOP: MARKAS BESAR ANGKATAN DARAT // PUSSIBERAD</div>
              <div class="sitrep-line">NOMOR: R/SITREP-20261027-091/PUSSIBERAD | KLASIFIKASI: RAHASIA</div>
              <div class="sitrep-body">
                1. DASAR: Doktrin Pertahanan Siber Semesta TNI AD Kep/44/XII/2025.<br>
                2. FAKTA: Intersepsi Dokumen Umpan Satuan KODAM JAYA / KOREM 051.<br>
                3. PENINDAKAN: Host 192.168.1.88 Diisolir. Aturan Firewall Terpasang.<br>
                4. SEKTOR: Hardware/GPU Fingerprint 7b3a99e120fd9c48 Tercatat.
              </div>
              <div class="sitrep-seal">
                ★ SEGAL SHA-256: 1178D8418DBADC3F4D9085AC98EFB76378A86C459D115C6B... [VALID]
              </div>
            </div>
            <div style="margin-top: 12px; background: rgba(168, 85, 247, 0.08); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 6px; padding: 10px 14px; font-family: var(--master-mono); font-size: 11px; color: #d8b4fe; display: flex; align-items: center; justify-content: space-between;">
              <span>STATUS RANTAI BUKTI:</span>
              <span style="font-weight: 800;">100% UNTAMPERED // ALAT BUKTI SAH</span>
            </div>
          </div>
        </div>

        <div style="margin-top: 2.2vh; background: #090e18; border: 1px solid #1e293b; border-radius: 8px; padding: 12px 18px; display: flex; align-items: center; justify-content: space-between; font-family: var(--master-mono); font-size: 11.5px;">
          <div style="display: flex; align-items: center; gap: 8px; color: #a7f3d0;">
            <span style="display: inline-block; width: 7px; height: 7px; background: #10b981; border-radius: 50%; box-shadow: 0 0 6px #10b981;"></span>
            <span>SOP KESIAPAN MILITER: DARI DETEKSI RAW HINGGA PERINTAH ISOLASI TERLAKSANA DALAM SATU TAMPILAN</span>
          </div>
          <div style="color: #64748b;">PUSSIBERAD TNI AD // 2026</div>
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- SLIDE 7: KESIMPULAN & KEDAULATAN PERTAHANAN SIBER NKRI                     -->
    <!-- ========================================================================= -->
    <section class="slide stage-slide" id="deck-slide-7">
      <div class="stage-slide-content">
        <div class="stage-eyebrow">06 // KESIMPULAN STRATEGIS &amp; KESIAPAN GELAR</div>
        <h2 class="stage-h2">100% Mandiri, <span class="stage-hl-green">Kedaulatan Penuh</span>, Siap Gelar di Jajaran Kodam</h2>

        <div class="stage-cards-3">
          <div class="stage-card">
            <div class="card-icon-round icon-green">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
              </svg>
            </div>
            <h3 class="stage-h3">Efisiensi Anggaran Negara</h3>
            <p class="stage-text">
              Didesain khusus untuk berjalan di komputer pangkalan biasa tanpa perlu membeli server atau lisensi vendor luar negeri bernilai miliaran rupiah.
            </p>
            <div class="stage-stat-pill">0 Rupiah Lisensi Vendor Asing</div>
          </div>

          <div class="stage-card">
            <div class="card-icon-round icon-cyan">
              <svg width="24" height="20" viewBox="0 0 24 20" fill="none" style="filter: drop-shadow(0 0 6px rgba(239,68,68,0.3));">
                <rect x="0.5" y="0.5" width="23" height="19" rx="3.5" stroke="#06b6d4" stroke-width="1"/>
                <rect x="1" y="1" width="22" height="9" fill="#ef4444" rx="3 3 0 0"/>
                <rect x="1" y="10" width="22" height="9" fill="#f8fafc" rx="0 0 3 3"/>
              </svg>
            </div>
            <h3 class="stage-h3">Kedaulatan &amp; Kemandirian</h3>
            <p class="stage-text">
              100% karya mandiri talenta nasional. Bebas dari risiko backdoor atau spyware pihak asing yang dapat membocorkan rahasia negara.
            </p>
            <div class="stage-stat-pill">100% Air-Gapped Standalone</div>
          </div>

          <div class="stage-card">
            <div class="card-icon-round icon-purple">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
              </svg>
            </div>
            <h3 class="stage-h3">Gelar Instan Satuan Kodim</h3>
            <p class="stage-text">
              Mekanisme hot-plug generator satuan memungkinkan pendaftaran Kodim baru dalam 1 klik tanpa perlu kompilasi ulang kode atau restart server.
            </p>
            <div class="stage-stat-pill">Hot-Plug Zero-Recompile</div>
          </div>
        </div>

        <div class="stage-final-banner">
          <div class="banner-quote">
            "KITA TIDAK MENUNGGU DISERANG. KITA YANG MENYIAPKAN PANGGUNGNYA."
          </div>
          <div class="banner-sub">
            PUSSIBERAD TNI AD × KARTIKA CYBER HACKATHON 2026 // DOKTRIN PERTAHANAN SIBER AKTIF
          </div>
        </div>
      </div>
    </section>
    """

def get_stage_deck_styles():
    return """
    /* New Revamped Styles for Stage Deck */
    .tile-item {
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 8px;
      padding: 11px 14px;
      margin-bottom: 9px;
    }
    .tile-hdr {
      font-family: var(--master-mono);
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.5px;
      margin-bottom: 4px;
    }
    .tile-desc {
      font-size: 12.5px;
      line-height: 1.5;
      color: var(--master-muted);
    }
    .pillar-layer-badge {
      font-family: var(--master-mono);
      font-size: 9.5px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid #273b56;
      color: #7dd3fc;
    }
    .stage-stat-giant {
      font-family: var(--master-mono);
      font-size: clamp(32px, 3.2vw, 48px);
      font-weight: 900;
      line-height: 1;
    }

    /* ========================================================================= */
    /* STAGE DECK NATIVE RESPONSIVE 16:9 VIEWPORT STYLES                         */
    /* ========================================================================= */
    #view-deck {
      display: none;
      width: 100vw;
      height: calc(100vh - 58px);
      position: absolute;
      top: 0;
      left: 0;
      background: radial-gradient(circle at 50% 20%, #0d1726 0%, #05080e 80%);
      overflow: hidden;
      align-items: center;
      justify-content: center;
    }
    #view-deck.active {
      display: flex;
    }

    #view-awam .slide.active,
    #view-teknis .slide.active,
    #view-deck .stage-slide.active {
      display: flex !important;
      opacity: 1 !important;
      visibility: visible !important;
      transform: none !important;
    }

    .stage-slide {
      display: none;
      width: 100%;
      height: 100%;
      max-width: 1560px;
      margin-left: auto;
      margin-right: auto;
      padding: 3.5vh 3.5vw 4vh 3.5vw;
      box-sizing: border-box;
      flex-direction: column;
      justify-content: center;
      animation: stageFadeIn 0.24s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .stage-slide.active {
      display: flex;
    }

    @keyframes stageFadeIn {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .stage-slide-content {
      display: flex;
      flex-direction: column;
      height: 100%;
      justify-content: center;
    }

    .stage-eyebrow {
      font-family: var(--master-mono);
      font-size: clamp(12px, 0.95vw, 14px);
      font-weight: 800;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--master-green);
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 1.2vh;
    }
    .stage-eyebrow::before {
      content: "";
      width: 9px;
      height: 9px;
      background: var(--master-green);
      border-radius: 50%;
      box-shadow: 0 0 10px var(--master-green);
    }

    .stage-tag {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #6ee7b7;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 11px;
    }

    .stage-h1 {
      font-size: clamp(34px, 3.8vw, 62px);
      font-weight: 900;
      line-height: 1.1;
      letter-spacing: -0.02em;
      color: #ffffff;
      margin-bottom: 1.8vh;
    }

    .stage-h2 {
      font-size: clamp(26px, 2.8vw, 44px);
      font-weight: 900;
      line-height: 1.18;
      letter-spacing: -0.015em;
      color: #ffffff;
      margin-bottom: 2.2vh;
    }

    .stage-h3 {
      font-size: clamp(17px, 1.35vw, 22px);
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 10px;
    }

    .stage-hl-green {
      color: var(--master-green);
    }
    .stage-hl-cyan {
      color: var(--master-cyan);
    }
    .stage-hl-red {
      color: var(--master-red);
    }

    .stage-lead {
      font-size: clamp(16px, 1.25vw, 21px);
      line-height: 1.6;
      color: #cbd5e1;
      max-width: 82ch;
      margin-bottom: 2.5vh;
    }

    .stage-doctrine-quote {
      display: flex;
      align-items: center;
      gap: 16px;
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 14px 20px;
      max-width: 90ch;
      margin-bottom: 3.5vh;
      font-size: clamp(13px, 1.05vw, 16px);
      color: #e2e8f0;
    }

    .quote-bar {
      width: 4px;
      height: 38px;
      background: var(--master-amber);
      border-radius: 2px;
      flex-shrink: 0;
    }

    .stage-metrics-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
    }

    .stage-metric-card {
      background: #090e18;
      border: 1px solid #1e293b;
      border-radius: 10px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      position: relative;
      overflow: hidden;
    }
    .stage-metric-card::before {
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0; height: 3px;
    }
    .border-green::before { background: var(--master-green); }
    .border-cyan::before { background: var(--master-cyan); }
    .border-amber::before { background: var(--master-amber); }
    .border-purple::before { background: var(--master-purple); }

    .metric-val {
      font-size: clamp(26px, 2.5vw, 38px);
      font-weight: 900;
      font-family: var(--master-mono);
      line-height: 1.1;
    }
    .text-green { color: #34d399; }
    .text-cyan { color: #38bdf8; }
    .text-amber { color: #fbbf24; }
    .text-purple { color: #c084fc; }

    .metric-title {
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 0.8px;
      color: #f8fafc;
    }
    .metric-sub {
      font-size: 12px;
      color: var(--master-muted);
      line-height: 1.45;
    }

    /* Split Grids */
    .stage-split-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      flex: 1;
    }

    .stage-card {
      background: #090e18;
      border: 1px solid #1e293b;
      border-radius: 12px;
      padding: 26px 22px;
      display: flex;
      flex-direction: column;
    }

    .card-fail {
      border-color: rgba(239, 68, 68, 0.4);
      background: linear-gradient(180deg, rgba(239, 68, 68, 0.05) 0%, #090e18 100%);
    }
    .card-win {
      border-color: rgba(16, 185, 129, 0.5);
      background: linear-gradient(180deg, rgba(16, 185, 129, 0.06) 0%, #090e18 100%);
    }

    .card-tag {
      font-family: var(--master-mono);
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 1px;
      margin-bottom: 12px;
      display: inline-block;
    }
    .tag-red { color: #f87171; }
    .tag-green { color: #34d399; }
    .tag-cyan { color: #38bdf8; }
    .tag-purple { color: #c084fc; }

    .stage-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 14px;
      font-size: clamp(13.5px, 1.05vw, 16px);
      line-height: 1.55;
      color: #cbd5e1;
      margin-top: 10px;
    }
    .stage-list li {
      position: relative;
      padding-left: 20px;
    }
    .stage-list li::before {
      content: "";
      position: absolute;
      left: 0;
      top: 9px;
      width: 7px;
      height: 7px;
      border-radius: 50%;
    }
    .list-red li::before { background: #ef4444; }
    .list-green li::before { background: #10b981; }
    .list-cyan li::before { background: #06b6d4; }

    /* 3 Cards Layout */
    .stage-cards-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 22px;
      margin-top: 1vh;
    }

    .card-icon-round {
      width: 48px;
      height: 48px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      margin-bottom: 16px;
    }
    .icon-green { background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.4); }
    .icon-cyan { background: rgba(6, 182, 212, 0.15); border: 1px solid rgba(6, 182, 212, 0.4); }
    .icon-purple { background: rgba(168, 85, 247, 0.15); border: 1px solid rgba(168, 85, 247, 0.4); }

    .stage-stratagem-sub {
      font-size: 12px;
      font-family: var(--master-mono);
      color: var(--master-green);
      font-weight: 700;
      margin-bottom: 12px;
    }
    .stage-text {
      font-size: clamp(13px, 1vw, 15px);
      line-height: 1.6;
      color: #cbd5e1;
    }
    .stage-stat-pill {
      margin-top: 20px;
      display: inline-block;
      font-family: var(--master-mono);
      font-size: 11.5px;
      font-weight: 800;
      padding: 6px 12px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid #273b56;
      border-radius: 6px;
      color: #7dd3fc;
    }

    /* 4 Pillars Layout */
    .stage-cards-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
      margin-top: 1vh;
    }

    .stage-pillar-card {
      background: #090e18;
      border: 1px solid #1e293b;
      border-radius: 12px;
      padding: 24px 20px;
      display: flex;
      flex-direction: column;
      position: relative;
    }
    .p-green { border-color: rgba(16, 185, 129, 0.4); }
    .p-cyan { border-color: rgba(6, 182, 212, 0.4); }
    .p-amber { border-color: rgba(245, 158, 11, 0.4); }
    .p-purple { border-color: rgba(168, 85, 247, 0.4); }

    .pillar-num {
      font-family: var(--master-mono);
      font-size: 26px;
      font-weight: 900;
      color: #334155;
      margin-bottom: 8px;
    }
    .pillar-title {
      font-size: 16px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 4px;
    }
    .pillar-proto {
      font-size: 11.5px;
      font-family: var(--master-mono);
      color: var(--master-green);
      font-weight: 700;
      margin-bottom: 12px;
    }
    .pillar-desc {
      font-size: 12.5px;
      line-height: 1.55;
      color: var(--master-muted);
      flex: 1;
      margin-bottom: 16px;
    }
    .pillar-badge {
      font-family: var(--master-mono);
      font-size: 10.5px;
      font-weight: 800;
      padding: 4px 8px;
      border-radius: 4px;
      background: #141f32;
      color: #e2e8f0;
      text-align: center;
    }

    /* Telemetry Box in Slide 4 Pillars */
    .pillar-telemetry-box {
      background: #06090e;
      border: 1px solid #1e293b;
      border-radius: 6px;
      padding: 8px 10px;
      font-family: var(--master-mono);
      font-size: 10.5px;
      line-height: 1.4;
      color: #94a3b8;
      margin-top: auto;
      margin-bottom: 10px;
      word-break: break-all;
    }
    .telem-label {
      color: #64748b;
      font-size: 9.5px;
      font-weight: 800;
      letter-spacing: 0.5px;
      display: inline-block;
      margin-bottom: 2px;
    }

    /* Choreography Layout */
    .stage-choreography-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 14px;
      margin-top: 1.5vh;
    }

    .choreo-step {
      background: #090e18;
      border: 1px solid #1e293b;
      border-radius: 10px;
      padding: 20px 16px;
      display: flex;
      flex-direction: column;
      gap: 7px;
    }
    .choreo-time {
      font-family: var(--master-mono);
      font-size: 11px;
      font-weight: 800;
      color: #64748b;
    }
    .choreo-status {
      font-family: var(--master-mono);
      font-size: 10.5px;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 4px;
      display: inline-block;
      margin-bottom: 4px;
    }
    .st-green { background: rgba(16, 185, 129, 0.2); color: #34d399; }
    .st-amber { background: rgba(245, 158, 11, 0.2); color: #fbbf24; }
    .st-cyan { background: rgba(6, 182, 212, 0.2); color: #38bdf8; }
    .st-red { background: rgba(239, 68, 68, 0.25); color: #f87171; }
    .st-purple { background: rgba(168, 85, 247, 0.2); color: #c084fc; }

    .choreo-title {
      font-size: 13.5px;
      font-weight: 800;
      color: #ffffff;
    }
    .choreo-desc {
      font-size: 11.5px;
      line-height: 1.45;
      color: var(--master-muted);
    }

    /* Slide 5 Live Demo Operational Metrics Strip */
    .stage-demo-strip {
      margin-top: 2.2vh;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
      background: #090e18;
      border: 1px solid #1e293b;
      border-radius: 10px;
      padding: 12px 16px;
    }
    .demo-metric-item {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .m-lbl {
      font-family: var(--master-mono);
      font-size: 10px;
      font-weight: 800;
      color: #64748b;
      letter-spacing: 0.8px;
    }
    .m-val {
      font-family: var(--master-mono);
      font-size: 13.5px;
      font-weight: 900;
      color: #ffffff;
      letter-spacing: 0.3px;
    }

    /* SITREP Preview Card */
    .sitrep-preview-box {
      background: #06090e;
      border: 1px solid #20314a;
      border-radius: 8px;
      padding: 14px;
      font-family: var(--master-mono);
      font-size: 11px;
      line-height: 1.6;
      color: #cbd5e1;
      margin-top: 10px;
    }
    .sitrep-hdr {
      color: var(--master-green);
      font-weight: 900;
      border-bottom: 1px dashed #1e293b;
      padding-bottom: 4px;
      margin-bottom: 6px;
    }
    .sitrep-line {
      color: #94a3b8;
      font-size: 10px;
      margin-bottom: 6px;
    }
    .sitrep-body {
      font-size: 11px;
      line-height: 1.6;
      color: #cbd5e1;
      margin-bottom: 8px;
    }
    .sitrep-seal {
      margin-top: 10px;
      background: rgba(16, 185, 129, 0.1);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #6ee7b7;
      padding: 6px;
      border-radius: 4px;
      font-size: 10px;
      font-weight: 800;
      word-break: break-all;
    }

    /* Final Banner */
    .stage-final-banner {
      margin-top: 3vh;
      background: radial-gradient(circle at 50% 50%, rgba(16, 185, 129, 0.12) 0%, rgba(10, 16, 26, 0.8) 100%);
      border: 1px solid rgba(16, 185, 129, 0.4);
      border-radius: 12px;
      padding: 24px;
      text-align: center;
    }
    .banner-quote {
      font-size: clamp(20px, 1.8vw, 30px);
      font-weight: 900;
      letter-spacing: 0.5px;
      color: #ffffff;
      margin-bottom: 6px;
    }
    .banner-sub {
      font-family: var(--master-mono);
      font-size: 12px;
      color: var(--master-green);
      font-weight: 700;
      letter-spacing: 1.5px;
    }
    """

def build():
    awam_raw = AWAM_PATH.read_text(encoding="utf-8")
    teknis_raw = TEKNIS_PATH.read_text(encoding="utf-8")

    # Extract Awam styles & body slides
    awam_css = re.search(r'<style>(.*?)</style>', awam_raw, re.DOTALL).group(1)
    awam_css_cleaned = re.sub(r'html,\s*body\s*\{[^}]*\}', '', awam_css)
    awam_slides = re.search(r'<main class="deck"[^>]*>(.*?)</main>', awam_raw, re.DOTALL).group(1)

    # 1. Update Cover Awam (Slide 1) with 2-Column Layout & Subtle Tactical Radar Artwork
    radar_visual = generate_cover_awam_visual()
    old_slide_1 = re.search(r'(<!-- SLIDE 1: COVER.*?<section class="slide active"[^>]*>)(.*?)(</section>)', awam_slides, re.DOTALL)
    if old_slide_1:
        s1_head = old_slide_1.group(1)
        s1_content = old_slide_1.group(2)
        s1_tail = old_slide_1.group(3)
        
        new_slide_1_inner = f"""
  <div style="display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 32px; align-items: center; width: 100%; height: 100%;">
    <!-- Left Column: Content -->
    <div style="display: flex; flex-direction: column; justify-content: center;">
      <div class="eyebrow">PUSSIBERAD TNI AD × KARTIKA CYBER HACKATHON 2026 // KATEGORI PENANGKALAN</div>
      <h1 style="font-size: clamp(32px, 3.2vw, 54px); line-height: 1.15; letter-spacing: -0.02em;">
        NEXUS-TRAP<br><span class="hl">Ranjau Umpan Digital</span><br>Penjaga Rahasia Markas
      </h1>
      <p class="lead" style="margin-top: 2vh; max-width: 58ch; text-wrap: balance; line-height: 1.6; font-size: clamp(17px, 1.35vw, 21px);">
        Penyusup boleh saja berhasil menembus perimeter jaringan satuan kita. Namun yang ia sentuh hanyalah <strong>sarana tipuan</strong>, dan saat itu juga <strong>sarang musuh terbongkar seketika</strong>.
      </p>
      <div style="margin-top: 3.2vh; display: flex; flex-wrap: wrap; gap: 12px;">
        <div style="background: var(--surface); border: 1px solid var(--brand); padding: 10px 18px; border-radius: 8px; font-family: ui-monospace, monospace; font-size: 12.5px; font-weight: 700; color: #6ee7b7; box-shadow: 0 4px 14px rgba(16,185,129,0.15);">
          ★ DOKTRIN PERTAHANAN SIBER AKTIF
        </div>
        <div style="background: var(--surface); border: 1px solid #0284c7; padding: 10px 18px; border-radius: 8px; font-family: ui-monospace, monospace; font-size: 12.5px; font-weight: 700; color: #7dd3fc; box-shadow: 0 4px 14px rgba(56,189,248,0.15);">
          ★ 100% AIR-GAPPED ON-PREMISE
        </div>
        <div style="background: var(--surface); border: 1px solid #d97706; padding: 10px 18px; border-radius: 8px; font-family: ui-monospace, monospace; font-size: 12.5px; font-weight: 700; color: #fde68a; box-shadow: 0 4px 14px rgba(245,158,11,0.15);">
          ★ ZERO FALSE POSITIVE BY DESIGN
        </div>
      </div>
      <div style="margin-top: 2.5vh; display: flex; align-items: center; gap: 10px; font-family: ui-monospace, monospace; font-size: 11px; color: var(--dim);">
        <span style="display: inline-block; width: 7px; height: 7px; background: #10b981; border-radius: 50%; box-shadow: 0 0 8px #10b981;"></span>
        <span>GELAR TERITORIAL AKTIF // 11 KODAM DI BAWAH PENGAWASAN PUSSIBERAD</span>
      </div>
    </div>

    <!-- Right Column: Context-Relevant Tactical Deception Radar & Shield Hologram -->
    {radar_visual}
  </div>
"""
        awam_slides = awam_slides.replace(old_slide_1.group(0), f"{s1_head}{new_slide_1_inner}{s1_tail}")

    # Extract Teknis styles & body slides
    teknis_css = re.search(r'<style>(.*?)</style>', teknis_raw, re.DOTALL).group(1)
    teknis_css_cleaned = re.sub(r'html,\s*body\s*\{[^}]*\}', '', teknis_css)
    teknis_slides = re.search(r'<main class="deck"[^>]*>(.*?)</main>', teknis_raw, re.DOTALL).group(1)

    # 2. Native Stage Deck Slides & Styles
    stage_deck_slides = get_native_stage_deck_slides(radar_visual=radar_visual)
    stage_deck_styles = get_stage_deck_styles()

    # Drawer Cards for Stage Deck
    drawer_cards = """
      <div class="drawer-card" onclick="goToSlide(0)">
        <div class="drawer-card-num">01</div>
        <div>
          <div class="title">Cover &amp; Value Proposition</div>
          <div class="subtitle">NEXUS-TRAP Active Cyber Deception</div>
        </div>
      </div>
      <div class="drawer-card" onclick="goToSlide(1)">
        <div class="drawer-card-num">02</div>
        <div>
          <div class="title">Paradoks Pertahanan Pasif</div>
          <div class="subtitle">Ancaman Kredensial Asli Staf</div>
        </div>
      </div>
      <div class="drawer-card" onclick="goToSlide(2)">
        <div class="drawer-card-num">03</div>
        <div>
          <div class="title">Filosofi Lonceng &amp; Stempel</div>
          <div class="subtitle">Doktrin Stratagem 33 &amp; 25 Sun Tzu</div>
        </div>
      </div>
      <div class="drawer-card" onclick="goToSlide(3)">
        <div class="drawer-card-num">04</div>
        <div>
          <div class="title">4 Pilar Arsitektur Asimetris</div>
          <div class="subtitle">OT Genset, Tarpit, Canary &amp; SITREP</div>
        </div>
      </div>
      <div class="drawer-card" onclick="goToSlide(4)">
        <div class="drawer-card-num">05</div>
        <div>
          <div class="title">Koreografi Live Demo 10 Menit</div>
          <div class="subtitle">Skenario Intersepsi Hijau-Kuning-Merah</div>
        </div>
      </div>
      <div class="drawer-card" onclick="goToSlide(5)">
        <div class="drawer-card-num">06</div>
        <div>
          <div class="title">Purwarupa C4ISR &amp; Bukti POMAD</div>
          <div class="subtitle">Naskah Dinas Laporan Bersegel SHA-256</div>
        </div>
      </div>
      <div class="drawer-card" onclick="goToSlide(6)">
        <div class="drawer-card-num">07</div>
        <div>
          <div class="title">Kedaulatan &amp; Gelar Nusantara</div>
          <div class="subtitle">100% Mandiri Tanpa Lisensi Asing</div>
        </div>
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
    /* UNIVERSAL HORIZONTAL & VIEWPORT CENTERING (BALANCED ACROSS RESOLUTIONS)   */
    /* ========================================================================= */
    #view-awam, #view-teknis, #view-deck {{
      align-items: center;
      justify-content: center;
    }}

    #view-awam .deck, #view-teknis .deck, #view-deck .deck-viewport {{
      width: 100vw;
      height: calc(100vh - 58px);
      position: absolute;
      top: 0;
      left: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      padding: 0;
    }}

    #view-awam .slide,
    #view-teknis .slide,
    #view-deck .stage-slide {{
      max-width: 1560px !important;
      width: min(1560px, 92vw) !important;
      left: 0 !important;
      right: 0 !important;
      margin-left: auto !important;
      margin-right: auto !important;
      box-sizing: border-box;
    }}

    /* ========================================================================= */
    /* 2. PORTAL HOME VIEW (MODE SELECTOR)                                       */
    /* ========================================================================= */
    #view-home {{
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      padding: 3.5vh 4vw 2.5vh 4vw;
      background: radial-gradient(circle at 50% 12%, #0e1c32 0%, #05080e 72%);
      z-index: 100;
    }}

    .home-header {{
      text-align: center;
      max-width: 1020px;
    }}

    .home-eyebrow {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-family: var(--master-mono);
      font-size: clamp(11.5px, 0.9vw, 13px);
      font-weight: 800;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--master-green);
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.35);
      padding: 6px 18px;
      border-radius: 999px;
      margin-bottom: 1.4vh;
    }}

    .home-eyebrow::before {{
      content: "";
      width: 8px;
      height: 8px;
      background: var(--master-green);
      border-radius: 50%;
      box-shadow: 0 0 10px var(--master-green);
    }}

    /* Anti-breakage for Title */
    .home-title {{
      font-size: clamp(26px, 3.1vw, 48px);
      font-weight: 900;
      letter-spacing: -0.02em;
      line-height: 1.18;
      color: #ffffff;
      margin-bottom: 1vh;
    }}

    .title-line-1 {{
      display: block;
      color: #ffffff;
    }}

    .title-line-2 {{
      display: inline-block;
      white-space: nowrap;
      background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .home-desc {{
      font-size: clamp(13.5px, 1.1vw, 16px);
      color: var(--master-muted);
      max-width: 80ch;
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
      margin: 1.5vh 0;
    }}

    .home-card {{
      background: #090e18;
      border: 1px solid var(--master-border);
      border-radius: 14px;
      padding: 26px 24px 22px 24px;
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
      margin-bottom: 16px;
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
      margin-bottom: 10px;
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
      font-size: clamp(18px, 1.35vw, 22px);
      font-weight: 800;
      color: #ffffff;
      line-height: 1.2;
    }}

    .card-subtitle {{
      font-size: 12px;
      font-weight: 600;
      color: var(--master-dim);
      margin-bottom: 14px;
    }}

    .card-desc {{
      font-size: 13px;
      color: #cbd5e1;
      line-height: 1.55;
      margin-bottom: 16px;
      flex-grow: 1;
    }}

    .card-points {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 7px;
      margin-bottom: 22px;
      font-size: 12px;
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
      padding: 12px 16px;
      border-radius: 8px;
      font-family: var(--master-font);
      font-size: 13px;
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
      padding-top: 12px;
      border-top: 1px solid #141f32;
      font-size: 11.5px;
      color: var(--master-dim);
    }}

    .home-shortcuts {{
      display: flex;
      align-items: center;
      gap: 16px;
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
      font-size: 12px;
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
      font-size: 11px;
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

    /* Drawer Styles */
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
      font-size: 13.5px;
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
      gap: 10px;
      overflow-y: auto;
      flex: 1;
      padding-right: 4px;
    }}

    .drawer-card {{
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 10px 14px;
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

    .drawer-card-num {{
      font-family: var(--master-mono);
      font-size: 16px;
      font-weight: 900;
      color: #38bdf8;
      width: 24px;
      text-align: center;
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
    /* 4. SCOPED STYLES FOR AWAM, TEKNIS & STAGE DECK                            */
    /* ========================================================================= */
    {awam_css_cleaned}
    {teknis_css_cleaned}
    {stage_deck_styles}
  </style>
</head>
<body>

  <!-- ========================================================================= -->
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
            Format visual 16:9 responsive widescreen definisi tinggi tanpa blok teks padat.
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
    <main class="deck-viewport" id="deck-viewport" style="width: 100vw; height: calc(100vh - 58px); display: flex; align-items: center; justify-content: center;">
      {stage_deck_slides}
    </main>

    <!-- Drawer Slider for Stage Deck -->
    <div id="deck-drawer" class="drawer">
      <div class="drawer-header">
        <span class="drawer-title">LACI SLIDE STAGE DECK</span>
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
      if (mode === 'deck') return Array.from(document.querySelectorAll('#view-deck .stage-slide'));
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

    window.addEventListener('hashchange', initFromHash);
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
