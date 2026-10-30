import os
import math
from PIL import Image, ImageDraw

def create_svg_mark():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <linearGradient id="shieldBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b132b"/>
      <stop offset="50%" stop-color="#050811"/>
      <stop offset="100%" stop-color="#020408"/>
    </linearGradient>
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="50%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="innerGrid" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#06b6d4" stop-opacity="0.2"/>
    </linearGradient>
    <radialGradient id="coreGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#06b6d4" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#06b6d4" stop-opacity="0"/>
    </radialGradient>
    <filter id="glowEffect" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Base Hexagonal Fortress Plate -->
  <polygon points="256,16 480,132 480,380 256,496 32,380 32,132" fill="url(#shieldBg)" stroke="url(#borderGrad)" stroke-width="8" stroke-linejoin="round"/>
  
  <!-- Inner Tactical Inset -->
  <polygon points="256,40 456,144 456,368 256,472 56,368 56,144" fill="none" stroke="#1e293b" stroke-width="3" stroke-dasharray="8 6"/>

  <!-- Radar Trap Grid Circles -->
  <circle cx="256" cy="256" r="170" fill="none" stroke="#0e2238" stroke-width="2"/>
  <circle cx="256" cy="256" r="120" fill="none" stroke="#0e2238" stroke-width="2.5"/>
  <circle cx="256" cy="256" r="70" fill="none" stroke="#10b981" stroke-width="2" stroke-opacity="0.5"/>

  <!-- Crosshair Coordinates -->
  <line x1="256" y1="60" x2="256" y2="452" stroke="#06b6d4" stroke-width="2" stroke-opacity="0.4" stroke-dasharray="12 8"/>
  <line x1="76" y1="256" x2="436" y2="256" stroke="#06b6d4" stroke-width="2" stroke-opacity="0.4" stroke-dasharray="12 8"/>
  
  <!-- Diagonal Trap Web Interlinks (Deception Matrix) -->
  <line x1="120" y1="120" x2="392" y2="392" stroke="#10b981" stroke-width="1.5" stroke-opacity="0.3"/>
  <line x1="392" y1="120" x2="120" y2="392" stroke="#10b981" stroke-width="1.5" stroke-opacity="0.3"/>

  <!-- Concentric Decoy Nodes -->
  <polygon points="256,136 360,196 360,316 256,376 152,316 152,196" fill="none" stroke="url(#innerGrid)" stroke-width="3"/>
  
  <!-- Glowing Core Focal Nexus -->
  <circle cx="256" cy="256" r="50" fill="url(#coreGlow)"/>
  <polygon points="256,206 298,256 256,306 214,256" fill="#10b981" filter="url(#glowEffect)"/>
  <polygon points="256,224 282,256 256,288 230,256" fill="#ffffff"/>

  <!-- Apex Tripwire Warning Beacon (Canary Sensor) -->
  <circle cx="256" cy="74" r="14" fill="#ef4444" filter="url(#glowEffect)"/>
  <circle cx="256" cy="74" r="6" fill="#ffffff"/>
  
  <!-- Subtle Tactical Corner Brackets -->
  <path d="M 90 150 L 90 130 L 115 130" fill="none" stroke="#10b981" stroke-width="4"/>
  <path d="M 422 150 L 422 130 L 397 130" fill="none" stroke="#10b981" stroke-width="4"/>
  <path d="M 90 362 L 90 382 L 115 382" fill="none" stroke="#06b6d4" stroke-width="4"/>
  <path d="M 422 362 L 422 382 L 397 382" fill="none" stroke="#06b6d4" stroke-width="4"/>
</svg>"""

def create_svg_favicon():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="favShield" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b132b"/>
      <stop offset="100%" stop-color="#030712"/>
    </linearGradient>
  </defs>
  <!-- Background Shield Plate -->
  <polygon points="32,2 60,16 60,48 32,62 4,48 4,16" fill="url(#favShield)" stroke="#10b981" stroke-width="3"/>
  <!-- Crosshairs -->
  <line x1="32" y1="8" x2="32" y2="56" stroke="#06b6d4" stroke-width="1.5" stroke-opacity="0.6"/>
  <line x1="10" y1="32" x2="54" y2="32" stroke="#06b6d4" stroke-width="1.5" stroke-opacity="0.6"/>
  <!-- Central Diamond -->
  <polygon points="32,22 41,32 32,42 23,32" fill="#10b981"/>
  <polygon points="32,26 37,32 32,38 27,32" fill="#ffffff"/>
  <!-- Top Beacon Dot -->
  <circle cx="32" cy="11" r="3.5" fill="#ef4444"/>
</svg>"""

def create_svg_full_logo():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 220" width="100%" height="100%">
  <defs>
    <linearGradient id="logoBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070c18"/>
      <stop offset="100%" stop-color="#03050a"/>
    </linearGradient>
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="60%" stop-color="#e2e8f0"/>
      <stop offset="100%" stop-color="#94a3b8"/>
    </linearGradient>
    <linearGradient id="greenAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#06b6d4"/>
    </linearGradient>
    <filter id="logoGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Left Emblem (Icon Mark 180x180 at 20, 20) -->
  <g transform="translate(24, 18) scale(0.36)">
    <!-- Hexagon Outer -->
    <polygon points="256,16 480,132 480,380 256,496 32,380 32,132" fill="#0b132b" stroke="url(#greenAccent)" stroke-width="12"/>
    <!-- Inset -->
    <polygon points="256,44 452,146 452,366 256,468 60,366 60,146" fill="none" stroke="#1e293b" stroke-width="5" stroke-dasharray="14 10"/>
    <!-- Radar Rings -->
    <circle cx="256" cy="256" r="160" fill="none" stroke="#0e2238" stroke-width="4"/>
    <circle cx="256" cy="256" r="100" fill="none" stroke="#10b981" stroke-width="4" stroke-opacity="0.5"/>
    <!-- Crosshairs -->
    <line x1="256" y1="60" x2="256" y2="452" stroke="#06b6d4" stroke-width="4" stroke-opacity="0.6"/>
    <line x1="60" y1="256" x2="452" y2="256" stroke="#06b6d4" stroke-width="4" stroke-opacity="0.6"/>
    <!-- Diamond Core -->
    <polygon points="256,186 316,256 256,326 196,256" fill="#10b981" filter="url(#logoGlow)"/>
    <polygon points="256,216 286,256 256,296 226,256" fill="#ffffff"/>
    <!-- Top Beacon -->
    <circle cx="256" cy="74" r="20" fill="#ef4444" filter="url(#logoGlow)"/>
    <circle cx="256" cy="74" r="8" fill="#ffffff"/>
  </g>

  <!-- Divider Line -->
  <line x1="230" y1="36" x2="230" y2="184" stroke="#1e293b" stroke-width="2"/>

  <!-- Right Typography Section -->
  <!-- Top Eyebrow Tag -->
  <g transform="translate(254, 46)">
    <rect x="0" y="0" width="310" height="24" rx="4" fill="rgba(16, 185, 129, 0.12)" stroke="rgba(16, 185, 129, 0.35)" stroke-width="1"/>
    <circle cx="12" cy="12" r="4" fill="#10b981"/>
    <text x="24" y="16" fill="#34d399" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, monospace" font-size="11" font-weight="800" letter-spacing="1.5">PUSSIBERAD TNI AD // ACTIVE DEFENSE</text>
  </g>

  <!-- Main Wordmark -->
  <text x="254" y="124" fill="url(#textGrad)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="52" font-weight="900" letter-spacing="-1">
    NEXUS<tspan fill="#10b981">-</tspan><tspan fill="#06b6d4">TRAP</tspan>
  </text>

  <!-- Tagline / Subtitle -->
  <text x="256" y="156" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" font-weight="600" letter-spacing="0.5">
    Autonomous Network Deception, Sticky Tarpit &amp; C4ISR Counter-Espionage
  </text>

  <!-- Security Badges -->
  <g transform="translate(256, 172)">
    <text x="0" y="12" fill="#64748b" font-family="ui-monospace, monospace" font-size="11" font-weight="700">
      <tspan fill="#10b981">●</tspan> ZERO FALSE POSITIVE   <tspan fill="#06b6d4">●</tspan> 100% AIR-GAPPED ON-PREMISE   <tspan fill="#a855f7">●</tspan> POMAD SHA-256 SEAL
    </text>
  </g>
</svg>"""

def render_png_favicon(output_path, size=64):
    # Supersampled rendering for ultra-crisp output
    scale = 4
    w, h = size * scale, size * scale
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)

    # Coordinates
    center_x, center_y = w / 2, h / 2
    r_outer = w * 0.46

    # Hexagon outer
    hex_pts = []
    for i in range(6):
        angle = math.radians(60 * i - 30)
        hex_pts.append((center_x + r_outer * math.cos(angle), center_y + r_outer * math.sin(angle)))

    draw.polygon(hex_pts, fill=(11, 19, 43, 255), outline=(16, 185, 129, 255), width=int(3 * scale))

    # Crosshairs
    draw.line([(center_x, w * 0.12), (center_x, w * 0.88)], fill=(6, 182, 212, 160), width=int(1.5 * scale))
    draw.line([(w * 0.12, center_y), (w * 0.88, center_y)], fill=(6, 182, 212, 160), width=int(1.5 * scale))

    # Core Diamond
    r_core = w * 0.18
    core_pts = [
        (center_x, center_y - r_core),
        (center_x + r_core, center_y),
        (center_x, center_y + r_core),
        (center_x - r_core, center_y),
    ]
    draw.polygon(core_pts, fill=(16, 185, 129, 255))
    
    # Inner white diamond
    r_inner = r_core * 0.5
    inner_pts = [
        (center_x, center_y - r_inner),
        (center_x + r_inner, center_y),
        (center_x, center_y + r_inner),
        (center_x - r_inner, center_y),
    ]
    draw.polygon(inner_pts, fill=(255, 255, 255, 255))

    # Top Beacon Dot
    r_beacon = w * 0.05
    beacon_y = w * 0.18
    draw.ellipse([
        center_x - r_beacon, beacon_y - r_beacon,
        center_x + r_beacon, beacon_y + r_beacon
    ], fill=(239, 68, 68, 255))

    # Downsample with Lanczos filter for razor-sharp antialiasing
    final_im = im.resize((size, size), Image.Resampling.LANCZOS)
    final_im.save(output_path, "PNG")

def main():
    targets = [
        'E:/04_Webdev/59_Cyber-Hackathon/nexus-trap',
        'E:/04_Webdev/59_Cyber-Hackathon/web_presentation'
    ]

    svg_mark = create_svg_mark()
    svg_favicon = create_svg_favicon()
    svg_logo = create_svg_full_logo()

    for base in targets:
        if not os.path.exists(base):
            continue
        
        # Save SVG Mark
        with open(os.path.join(base, 'nexus_trap_mark.svg'), 'w', encoding='utf-8') as f:
            f.write(svg_mark)
        
        # Save SVG Favicon
        with open(os.path.join(base, 'favicon.svg'), 'w', encoding='utf-8') as f:
            f.write(svg_favicon)

        # Save SVG Full Logo
        with open(os.path.join(base, 'nexus_trap_logo.svg'), 'w', encoding='utf-8') as f:
            f.write(svg_logo)

        # Generate raster PNG favicons
        render_png_favicon(os.path.join(base, 'favicon.png'), size=32)
        render_png_favicon(os.path.join(base, 'apple-touch-icon.png'), size=180)
        
        print(f"Generated brand assets for {base}")

if __name__ == '__main__':
    main()
