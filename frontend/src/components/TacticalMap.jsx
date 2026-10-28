import React from 'react';
import { MapPin, AlertCircle, ShieldAlert } from 'lucide-react';

export default function TacticalMap({ systemStatus, compromisedUnit }) {
  const isRedAlert = systemStatus === 'SIAGA_MERAH';
  const isYellowAlert = systemStatus === 'SIAGA_KUNING';

  // Strategically distributed nodes with alternating label offsets to eliminate text collisions
  const nodes = [
    { id: 'KODAM_IM', name: 'Kodam IM (Aceh)', x: 65, y: 65, labelDy: -12, status: 'NORMAL' },
    { id: 'KODAM_I', name: 'Kodam I/BB (Medan)', x: 125, y: 95, labelDy: -12, status: 'NORMAL' },
    { id: 'KODAM_II', name: 'Kodam II/Swj (Plg)', x: 195, y: 155, labelDy: -12, status: 'NORMAL' },
    { 
      id: 'KODAM_JAYA', 
      name: 'Kodam Jaya (Jakarta)', 
      x: 245, 
      y: 200, 
      labelDy: -14,
      status: isRedAlert ? 'BREACHED' : isYellowAlert ? 'WARNING' : 'NORMAL' 
    },
    { id: 'KODAM_III', name: 'Kodam III/Slw (Bdg)', x: 280, y: 228, labelDy: 16, status: 'NORMAL' },
    { id: 'KODAM_IV', name: 'Kodam IV/Dip (Smg)', x: 335, y: 202, labelDy: -13, status: 'NORMAL' },
    { id: 'KODAM_V', name: 'Kodam V/Brw (Sby)', x: 395, y: 228, labelDy: 16, status: 'NORMAL' },
    { id: 'KODAM_IX', name: 'Kodam IX/Udy (Dps)', x: 460, y: 236, labelDy: 16, status: 'NORMAL' },
    { id: 'KODAM_VI', name: 'Kodam VI/Mlw (IKN)', x: 380, y: 125, labelDy: -12, status: 'NORMAL' },
    { id: 'KODAM_XIV', name: 'Kodam XIV/Hsn (Mks)', x: 480, y: 160, labelDy: -12, status: 'NORMAL' },
    { id: 'KODAM_XVII', name: 'Kodam XVII/Cen (Jyp)', x: 645, y: 155, labelDy: -12, status: 'NORMAL' }
  ];

  return (
    <div className="rounded bg-tactical-card border border-tactical-border p-3 flex flex-col h-full">
      <div className="flex items-center justify-between border-b border-tactical-border pb-2 mb-2">
        <div className="flex items-center gap-2">
          <MapPin className="w-3.5 h-3.5 text-emerald-400" />
          <span className="text-[11px] font-bold tracking-wider text-slate-200">SEBARAN SENSOR DECEPTION KODAM</span>
        </div>
        <div className="text-[10px] text-slate-400">
          Target Utama: <span className="text-amber-400 font-semibold">{compromisedUnit || 'JARINGAN TERITORIAL'}</span>
        </div>
      </div>

      {/* SVG Canvas Map Display */}
      <div className="relative flex-1 bg-tactical-dark/90 rounded border border-slate-900/80 overflow-hidden flex items-center justify-center">
        {/* Radar concentric tactical rings */}
        <div className="absolute inset-0 flex items-center justify-center opacity-15 pointer-events-none">
          <div className="w-[320px] h-[320px] rounded-full border border-emerald-500/40 animate-ping" style={{ animationDuration: '7s' }} />
          <div className="w-[220px] h-[220px] rounded-full border border-emerald-500/30 absolute" />
          <div className="w-[120px] h-[120px] rounded-full border border-emerald-500/40 absolute" />
        </div>

        <svg viewBox="0 0 740 270" className="w-full h-full max-h-[220px]">
          {/* Stylized Archipelago Landmass Silhouettes (Sumatera, Jawa, Kalimantan, Sulawesi, Papua) */}
          <g fill="#13202e" stroke="#1e3a4c" strokeWidth="1" opacity="0.65">
            {/* Sumatera */}
            <polygon points="50,45 85,35 155,115 220,185 185,190 120,110 50,45" />
            {/* Jawa */}
            <polygon points="225,200 425,215 420,230 220,220" />
            {/* Kalimantan */}
            <polygon points="310,75 390,65 415,120 385,160 325,150 300,105" />
            {/* Sulawesi */}
            <polygon points="450,110 495,100 485,140 505,170 465,195 455,145" />
            {/* Nusa Tenggara */}
            <polygon points="440,230 520,235 520,242 440,238" />
            {/* Maluku */}
            <polygon points="530,120 560,115 550,165 525,160" />
            {/* Papua */}
            <polygon points="585,140 685,130 705,210 655,205 605,175" />
          </g>

          {/* Grid coordinates and range circles */}
          <line x1="20" y1="135" x2="720" y2="135" stroke="#162231" strokeWidth="0.8" strokeDasharray="4 4" />
          <line x1="370" y1="20" x2="370" y2="250" stroke="#162231" strokeWidth="0.8" strokeDasharray="4 4" />

          {/* Node Render */}
          {nodes.map((node) => {
            const isBreached = node.status === 'BREACHED';
            const isWarn = node.status === 'WARNING';
            return (
              <g key={node.id} className="cursor-pointer group">
                {/* Outer ring */}
                {isBreached ? (
                  <>
                    <circle cx={node.x} cy={node.y} r="16" fill="none" stroke="#ef4444" strokeWidth="2" className="animate-ping" />
                    <circle cx={node.x} cy={node.y} r="9" fill="#ef4444" fillOpacity="0.4" />
                    <circle cx={node.x} cy={node.y} r="4.5" fill="#ef4444" />
                  </>
                ) : isWarn ? (
                  <>
                    <circle cx={node.x} cy={node.y} r="13" fill="none" stroke="#f59e0b" strokeWidth="2" className="animate-ping" />
                    <circle cx={node.x} cy={node.y} r="8" fill="#f59e0b" fillOpacity="0.3" />
                    <circle cx={node.x} cy={node.y} r="4" fill="#f59e0b" />
                  </>
                ) : (
                  <>
                    <circle cx={node.x} cy={node.y} r="3.5" fill="#10b981" />
                    <circle cx={node.x} cy={node.y} r="7" fill="none" stroke="#059669" strokeWidth="0.8" opacity="0.5" />
                  </>
                )}

                {/* Leader line connecting node to label */}
                <line
                  x1={node.x}
                  y1={node.y}
                  x2={node.x}
                  y2={node.y + (node.labelDy > 0 ? 8 : -8)}
                  stroke={isBreached ? '#ef4444' : isWarn ? '#f59e0b' : '#334155'}
                  strokeWidth="0.8"
                />

                {/* Label text with dark backdrop badge */}
                <rect
                  x={node.x - 42}
                  y={node.y + node.labelDy - 6}
                  width="84"
                  height="12"
                  fill="#080c13"
                  fillOpacity="0.9"
                  stroke={isBreached ? '#ef4444' : isWarn ? '#f59e0b' : '#1e293b'}
                  strokeWidth="0.6"
                  rx="2"
                />
                <text
                  x={node.x}
                  y={node.y + node.labelDy + 3}
                  textAnchor="middle"
                  fill={isBreached ? '#fca5a5' : isWarn ? '#fde68a' : '#cbd5e1'}
                  fontSize="7.5"
                  fontWeight={isBreached || isWarn ? 'bold' : '600'}
                  fontFamily="monospace"
                >
                  {node.name}
                </text>
              </g>
            );
          })}
        </svg>

        {/* Breach Alert Pill Overlay */}
        {isRedAlert && (
          <div className="absolute top-2 left-2 bg-red-950/90 border border-red-500 text-red-200 text-[10px] px-2 py-1 rounded flex items-center gap-1.5 animate-bounce">
            <ShieldAlert className="w-3.5 h-3.5 text-red-400" />
            <span>INTERSEPSI AKTIF: KODAM JAYA / KOREM 051</span>
          </div>
        )}
      </div>
    </div>
  );
}
