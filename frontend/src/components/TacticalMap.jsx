import React from 'react';
import { MapPin, ShieldAlert, Radio } from 'lucide-react';

function isNodeTargeted(nodeId, unitStr) {
  if (!unitStr) return nodeId === 'KODAM_JAYA';
  const u = unitStr.toUpperCase().replace(/[-_]/g, ' ');
  
  if (nodeId === 'KODAM_IM' && (u.includes('IM') || u.includes('ISKANDAR') || u.includes('ACEH') || u.includes('0101'))) return true;
  if (nodeId === 'KODAM_I' && (u.includes('KODAM I ') || u.includes('KODAM I/') || u.includes('BUKIT') || u.includes('MEDAN') || u.includes('0201'))) return true;
  if (nodeId === 'KODAM_II' && (u.includes('KODAM II') || u.includes('SRIWIJAYA') || u.includes('PALEMBANG') || u.includes('0418'))) return true;
  if (nodeId === 'KODAM_JAYA' && (u.includes('JAYA') || u.includes('JAKARTA') || u.includes('0501') || u.includes('0502') || u.includes('0503') || u.includes('0504') || u.includes('0505') || u.includes('0506') || u.includes('0507') || u.includes('0508') || u.includes('0509') || u.includes('0510'))) return true;
  if (nodeId === 'KODAM_III' && (u.includes('KODAM III') || u.includes('SILIWANGI') || u.includes('BANDUNG') || u.includes('0618') || u.includes('JABAR'))) return true;
  if (nodeId === 'KODAM_IV' && (u.includes('KODAM IV') || u.includes('DIPONEGORO') || u.includes('SEMARANG') || u.includes('0733') || u.includes('JATENG'))) return true;
  if (nodeId === 'KODAM_V' && (u.includes('KODAM V') || u.includes('BRAWIJAYA') || u.includes('SURABAYA') || u.includes('0832') || u.includes('JATIM'))) return true;
  if (nodeId === 'KODAM_IX' && (u.includes('KODAM IX') || u.includes('UDAYANA') || u.includes('BALI') || u.includes('DENPASAR') || u.includes('1611'))) return true;
  if (nodeId === 'KODAM_VI' && (u.includes('KODAM VI') || u.includes('MULAWARMAN') || u.includes('BALIKPAPAN') || u.includes('SAMARINDA') || u.includes('IKN') || u.includes('0901'))) return true;
  if (nodeId === 'KODAM_XIV' && (u.includes('KODAM XIV') || u.includes('HASANUDDIN') || u.includes('MAKASSAR') || u.includes('1408'))) return true;
  if (nodeId === 'KODAM_XVII' && (u.includes('KODAM XVII') || u.includes('CENDERAWASIH') || u.includes('JAYAPURA') || u.includes('PAPUA') || u.includes('1701'))) return true;

  // Fallback: Default to Kodam Jaya if unit is not mapped to another Kodam
  return nodeId === 'KODAM_JAYA';
}

export default function TacticalMap({ systemStatus, compromisedUnit }) {
  const isRedAlert = systemStatus === 'SIAGA_MERAH';
  const isYellowAlert = systemStatus === 'SIAGA_KUNING';

  // 11 Kodam Sensor Nodes anchored accurately onto Indonesian provinces
  const baseNodes = [
    { id: 'KODAM_IM', name: 'Kodam IM (Aceh)', x: 55, y: 55, labelDy: -16 },
    { id: 'KODAM_I', name: 'Kodam I/BB (Medan)', x: 92, y: 82, labelDy: -15 },
    { id: 'KODAM_II', name: 'Kodam II/Swj (Plg)', x: 178, y: 158, labelDy: -15 },
    { id: 'KODAM_JAYA', name: 'Kodam Jaya (Jakarta)', x: 242, y: 198, labelDy: -18 },
    { id: 'KODAM_III', name: 'Kodam III/Slw (Bdg)', x: 262, y: 216, labelDy: 18 },
    { id: 'KODAM_IV', name: 'Kodam IV/Dip (Smg)', x: 318, y: 205, labelDy: -16 },
    { id: 'KODAM_V', name: 'Kodam V/Brw (Sby)', x: 378, y: 212, labelDy: 18 },
    { id: 'KODAM_IX', name: 'Kodam IX/Udy (Dps)', x: 436, y: 223, labelDy: 18 },
    { id: 'KODAM_VI', name: 'Kodam VI/Mlw (IKN)', x: 408, y: 138, labelDy: -18 },
    { id: 'KODAM_XIV', name: 'Kodam XIV/Hsn (Mks)', x: 448, y: 178, labelDy: 18 },
    { id: 'KODAM_XVII', name: 'Kodam XVII/Cen (Jyp)', x: 742, y: 142, labelDy: -18 }
  ];

  const nodes = baseNodes.map(n => {
    const isTarget = isNodeTargeted(n.id, compromisedUnit);
    return {
      ...n,
      status: (isRedAlert && isTarget) ? 'BREACHED' : (isYellowAlert && isTarget) ? 'WARNING' : 'NORMAL'
    };
  });

  return (
    <div className="rounded bg-tactical-card border border-tactical-border p-3 flex flex-col h-full">
      <div className="flex items-center justify-between border-b border-tactical-border pb-2 mb-2">
        <div className="flex items-center gap-2">
          <MapPin className="w-3.5 h-3.5 text-emerald-400" />
          <span className="text-[11px] font-bold tracking-wider text-slate-200">
            SEBARAN SENSOR DECEPTION KODAM // PETA OPERASI NKRI
          </span>
        </div>
        <div className="flex items-center gap-3 text-[10px]">
          <span className="text-slate-400 flex items-center gap-1">
            <Radio className="w-3 h-3 text-emerald-400 animate-pulse" /> 11 KODAM AKTIF
          </span>
          <span className="text-slate-400">
            Target Utama: <span className="text-amber-400 font-semibold">{compromisedUnit || 'JARINGAN TERITORIAL'}</span>
          </span>
        </div>
      </div>

      {/* SVG Canvas Tactical Map Display */}
      <div className="relative flex-1 bg-tactical-dark/95 rounded border border-slate-900/80 overflow-hidden flex items-center justify-center">
        {/* Radar concentric tactical rings centered around central Archipelago */}
        <div className="absolute inset-0 flex items-center justify-center opacity-15 pointer-events-none">
          <div className="w-[340px] h-[340px] rounded-full border border-emerald-500/40 animate-ping" style={{ animationDuration: '8s' }} />
          <div className="w-[240px] h-[240px] rounded-full border border-emerald-500/30 absolute" />
          <div className="w-[140px] h-[140px] rounded-full border border-emerald-500/40 absolute" />
        </div>

        <svg viewBox="0 0 800 280" className="w-full h-full max-h-[240px] select-none">
          <defs>
            {/* Tactical Landmass Gradient */}
            <linearGradient id="tacticalLandGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#14263b" />
              <stop offset="100%" stopColor="#091421" />
            </linearGradient>
          </defs>

          {/* Tactical Grid & Meridian Navigation Lines */}
          <g stroke="#142638" strokeWidth="0.8" strokeDasharray="3 4">
            {/* Equator / Katulistiwa */}
            <line x1="15" y1="135" x2="785" y2="135" stroke="#1c3e5e" strokeWidth="1.2" />
            {/* Meridians */}
            <line x1="105" y1="15" x2="105" y2="265" />
            <line x1="290" y1="15" x2="290" y2="265" />
            <line x1="465" y1="15" x2="465" y2="265" />
            <line x1="615" y1="15" x2="615" y2="265" />
            <line x1="755" y1="15" x2="755" y2="265" />
          </g>

          {/* Coordinates & Tactical Navigation Markings */}
          <g fill="#477aa3" fontSize="7" fontFamily="monospace" fontWeight="bold">
            <text x="24" y="131" fontSize="6.5">[0° KATULISTIWA / EQUATOR]</text>
            <text x="108" y="28">100°BT</text>
            <text x="293" y="28">110°BT</text>
            <text x="468" y="28">120°BT</text>
            <text x="618" y="28">130°BT</text>
            <text x="758" y="28">140°BT</text>
          </g>

          {/* ALKI Maritime Corridors (Archipelagic Sea Lanes of Indonesia) */}
          <g stroke="#0f4559" strokeWidth="1" strokeDasharray="2 4" fill="none" opacity="0.65">
            {/* ALKI I */}
            <path d="M 215 260 L 212 195 L 230 115 L 245 25" />
            <text x="248" y="45" fill="#14b8a6" fontSize="6" fontFamily="monospace" fontWeight="bold">ALKI I</text>
            {/* ALKI II */}
            <path d="M 445 260 L 442 220 L 428 140 L 436 25" />
            <text x="440" y="45" fill="#14b8a6" fontSize="6" fontFamily="monospace" fontWeight="bold">ALKI II</text>
            {/* ALKI III */}
            <path d="M 580 260 L 565 185 L 535 115 L 540 25" />
            <text x="544" y="45" fill="#14b8a6" fontSize="6" fontFamily="monospace" fontWeight="bold">ALKI III</text>
          </g>

          {/* ========================================================================= */}
          {/* REALISTIC ARCHIPELAGO OF INDONESIA (NKRI) ACCURATE CARTOGRAPHY            */}
          {/* ========================================================================= */}
          <g fill="url(#tacticalLandGrad)" stroke="#326792" strokeWidth="1.3" strokeLinejoin="round">
            
            {/* 1. SUMATERA & SURROUNDING ISLANDS */}
            <circle cx="48" cy="42" r="2.8" /> {/* Sabang */}
            <path d="
              M 48 48 
              C 56 46, 68 58, 86 78 
              C 102 92, 118 108, 134 122 
              C 152 136, 172 152, 188 164
              C 202 174, 214 182, 216 190
              C 214 195, 206 195, 198 188
              C 186 180, 172 168, 156 156
              C 142 166, 126 162, 114 148
              C 100 134, 88 116, 76 96
              C 64 80, 52 64, 44 54
              Z
            " />
            <ellipse cx="72" cy="112" rx="4.5" ry="9" transform="rotate(-30 72 112)" /> {/* Nias */}
            <path d="M 104 148 C 112 158, 118 174, 116 178 C 112 178, 106 164, 104 148 Z" /> {/* Mentawai */}
            <path d="M 194 135 C 204 132, 208 144, 205 152 C 198 156, 192 146, 194 135 Z" /> {/* Bangka */}
            <circle cx="225" cy="154" r="5" /> {/* Belitung */}
            <circle cx="152" cy="102" r="3" /> {/* Batam */}
            <circle cx="160" cy="106" r="3.5" /> {/* Bintan */}
            <ellipse cx="236" cy="48" rx="4" ry="6" /> {/* Natuna */}

            {/* 2. JAWA, MADURA */}
            <path d="
              M 215 196
              C 225 194, 238 196, 248 198
              C 268 200, 290 201, 315 203
              C 340 205, 365 208, 388 210
              C 406 212, 418 214, 422 216
              C 420 220, 412 222, 396 221
              C 376 220, 352 222, 326 223
              C 298 222, 272 221, 248 215
              C 232 212, 218 206, 215 196
              Z
            " />
            <ellipse cx="396" cy="204" rx="15" ry="4.5" transform="rotate(-5 396 204)" /> {/* Madura */}

            {/* 3. KALIMANTAN (BORNEO - INDONESIAN TERRITORY) */}
            <path d="
              M 272 98
              C 285 88, 315 82, 345 74
              C 370 70, 395 64, 414 58
              C 418 68, 416 85, 422 96
              C 428 104, 424 116, 416 128
              C 412 142, 404 154, 392 164
              C 382 172, 368 180, 350 180
              C 330 182, 305 180, 290 172
              C 276 162, 268 145, 270 125
              C 270 110, 268 102, 272 98
              Z
            " />
            <ellipse cx="388" cy="172" rx="4" ry="7" /> {/* Pulau Laut */}
            <circle cx="418" cy="54" r="3" /> {/* Tarakan */}

            {/* 4. SULAWESI (THE FAMOUS 4-ARMED K-SHAPE) */}
            <path d="
              M 452 128
              C 455 115, 470 105, 492 98
              C 512 92, 528 84, 534 88
              C 525 96, 505 105, 488 112
              C 475 118, 468 126, 466 132
              C 478 132, 498 136, 510 142
              C 505 146, 485 146, 470 142
              C 468 148, 475 160, 485 170
              C 492 178, 488 192, 482 188
              C 475 180, 468 165, 460 152
              C 456 160, 452 175, 448 188
              C 442 190, 440 180, 444 162
              C 446 148, 448 136, 452 128
              Z
            " />
            <ellipse cx="488" cy="192" rx="4" ry="7" /> {/* Buton */}
            <circle cx="480" cy="186" r="3" /> {/* Muna */}

            {/* 5. KEPULAUAN NUSA TENGGARA (LESSER SUNDA) */}
            <path d="M 430 219 C 438 217, 444 220, 442 226 C 436 228, 428 224, 430 219 Z" /> {/* Bali */}
            <ellipse cx="456" cy="223" rx="6" ry="5" /> {/* Lombok */}
            <path d="M 472 221 C 490 220, 506 222, 512 226 C 500 230, 480 228, 472 221 Z" /> {/* Sumbawa */}
            <path d="M 522 221 C 545 220, 566 222, 578 224 C 565 228, 535 228, 522 221 Z" /> {/* Flores */}
            <ellipse cx="538" cy="242" rx="12" ry="5" transform="rotate(-10 538 242)" /> {/* Sumba */}
            <path d="M 586 242 C 598 238, 614 232, 624 228 C 618 236, 602 245, 586 242 Z" /> {/* West Timor */}
            <circle cx="580" cy="250" r="3" /> {/* Rote */}

            {/* 6. KEPULAUAN MALUKU */}
            <path d="
              M 548 95
              C 552 86, 560 90, 558 98
              C 564 102, 572 104, 570 108
              C 562 110, 556 108, 554 114
              C 556 122, 552 126, 548 122
              C 546 114, 544 104, 548 95
              Z
            " /> {/* Halmahera */}
            <circle cx="558" cy="80" r="3" /> {/* Morotai */}
            <ellipse cx="535" cy="158" rx="8" ry="6" /> {/* Buru */}
            <path d="M 558 152 C 580 150, 602 154, 610 158 C 595 162, 570 160, 558 152 Z" /> {/* Seram */}
            <circle cx="568" cy="164" r="2.8" /> {/* Ambon */}
            <ellipse cx="625" cy="195" rx="4" ry="8" /> {/* Aru */}
            <ellipse cx="638" cy="205" rx="5" ry="10" /> {/* Kei */}

            {/* 7. TANAH PAPUA (IRIAN JAYA) */}
            <path d="
              M 626 126
              C 635 118, 650 116, 662 120
              C 672 126, 668 136, 664 142
              C 678 140, 698 138, 718 136
              C 738 135, 752 136, 755 138
              L 755 232
              C 744 236, 732 238, 720 232
              C 705 220, 692 200, 678 185
              C 660 178, 642 165, 634 152
              C 630 142, 622 135, 626 126
              Z
            " />
            <ellipse cx="678" cy="114" rx="7" ry="4" transform="rotate(-15 678 114)" /> {/* Biak */}
            <ellipse cx="682" cy="128" rx="10" ry="3" /> {/* Yapen */}
            <ellipse cx="734" cy="236" rx="8" ry="7" /> {/* Pulau Dolok */}
          </g>

          {/* Satellite Radar Range Sweep Background */}
          <g opacity="0.25">
            <circle cx="408" cy="138" r="175" fill="none" stroke="#10b981" strokeWidth="1" strokeDasharray="4 6" />
            <circle cx="408" cy="138" r="95" fill="none" stroke="#10b981" strokeWidth="0.8" />
            <circle cx="408" cy="138" r="35" fill="none" stroke="#10b981" strokeWidth="0.6" />
          </g>

          {/* ========================================================================= */}
          {/* 11 KODAM SENSOR NODES RENDERING                                            */}
          {/* ========================================================================= */}
          {nodes.map((node) => {
            const isBreached = node.status === 'BREACHED';
            const isWarn = node.status === 'WARNING';
            return (
              <g key={node.id} className="cursor-pointer group">
                {/* Node Target Rings */}
                {isBreached ? (
                  <>
                    <circle cx={node.x} cy={node.y} r="18" fill="none" stroke="#ef4444" strokeWidth="2.2" className="animate-ping" />
                    <circle cx={node.x} cy={node.y} r="10" fill="#ef4444" fillOpacity="0.4" />
                    <circle cx={node.x} cy={node.y} r="5" fill="#ef4444" />
                  </>
                ) : isWarn ? (
                  <>
                    <circle cx={node.x} cy={node.y} r="14" fill="none" stroke="#f59e0b" strokeWidth="2" className="animate-ping" />
                    <circle cx={node.x} cy={node.y} r="8" fill="#f59e0b" fillOpacity="0.3" />
                    <circle cx={node.x} cy={node.y} r="4" fill="#f59e0b" />
                  </>
                ) : (
                  <>
                    <circle cx={node.x} cy={node.y} r="4" fill="#10b981" />
                    <circle cx={node.x} cy={node.y} r="8" fill="none" stroke="#059669" strokeWidth="0.9" opacity="0.6" />
                  </>
                )}

                {/* Leader line connecting node to tactical label */}
                <line
                  x1={node.x}
                  y1={node.y}
                  x2={node.x}
                  y2={node.y + (node.labelDy > 0 ? 10 : -10)}
                  stroke={isBreached ? '#ef4444' : isWarn ? '#f59e0b' : '#334155'}
                  strokeWidth="0.9"
                />

                {/* Tactical Label Badge Box */}
                <rect
                  x={node.x - 42}
                  y={node.y + node.labelDy - 6}
                  width="84"
                  height="12"
                  fill="#080c13"
                  fillOpacity="0.95"
                  stroke={isBreached ? '#ef4444' : isWarn ? '#f59e0b' : '#1e293b'}
                  strokeWidth={isBreached || isWarn ? '1' : '0.6'}
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
          <div className="absolute top-2 left-2 bg-red-950/90 border border-red-500 text-red-200 text-[10px] px-2.5 py-1 rounded flex items-center gap-1.5 animate-bounce shadow-lg shadow-red-950/50">
            <ShieldAlert className="w-3.5 h-3.5 text-red-400" />
            <span className="font-bold tracking-wider">INTERSEPSI AKTIF: {compromisedUnit || 'KODAM JAYA / KOREM 051'}</span>
          </div>
        )}
      </div>
    </div>
  );
}
