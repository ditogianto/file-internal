import React, { useState, useEffect } from 'react';
import { Shield, Radio, Activity, Clock, QrCode } from 'lucide-react';

export default function TopNav({ systemStatus, wsConnected }) {
  const [currentTime, setCurrentTime] = useState('');

  useEffect(() => {
    const updateClock = () => {
      const now = new Date();
      setCurrentTime(now.toLocaleTimeString('id-ID', { hour12: false }) + ' WIB');
    };
    updateClock();
    const timer = setInterval(updateClock, 1000);
    return () => clearInterval(timer);
  }, []);

  const getStatusBadge = () => {
    switch (systemStatus) {
      case 'SIAGA_MERAH':
        return {
          text: 'SIAGA 1 (MERAH) // INTRUSI DOKUMEN AKTIF',
          bg: 'bg-red-950/80 border-red-500 text-red-400 animate-pulse glow-red'
        };
      case 'SIAGA_KUNING':
        return {
          text: 'SIAGA 2 (KUNING) // PENGINTAIAN OT TERDETEKSI',
          bg: 'bg-amber-950/80 border-amber-500 text-amber-400 animate-pulse glow-amber'
        };
      case 'SIAGA_HIJAU':
      default:
        return {
          text: 'SIAGA 3 (HIJAU) // PERIMETER AMAN',
          bg: 'bg-emerald-950/80 border-emerald-500 text-emerald-400 glow-green'
        };
    }
  };

  const badge = getStatusBadge();

  return (
    <header className="h-14 border-b border-tactical-border bg-tactical-card px-4 flex items-center justify-between">
      {/* Insignia & Program Title */}
      <div className="flex items-center gap-3">
        <div className="w-9 h-9 rounded bg-emerald-900/40 border border-emerald-500/60 flex items-center justify-center text-emerald-400 shadow-md">
          <Shield className="w-5 h-5" />
        </div>
        <div>
          <div className="flex items-center gap-2">
            <span className="font-bold tracking-wider text-sm text-slate-100">NEXUS-TRAP</span>
            <span className="text-[10px] bg-slate-800 text-slate-300 px-1.5 py-0.5 rounded border border-slate-700">v2.0-MIL</span>
          </div>
          <div className="text-[10px] text-slate-400 tracking-tight">
            NETWORK DECEPTION &amp; ACTIVE TARPIT // PUSSIBERAD TNI AD
          </div>
        </div>
      </div>

      {/* Central Threat Level Defcon Indicator */}
      <div className={`px-4 py-1.5 rounded-full border text-xs font-bold tracking-wider flex items-center gap-2 transition-all duration-300 ${badge.bg}`}>
        <Radio className="w-3.5 h-3.5 animate-spin" style={{ animationDuration: '4s' }} />
        <span>{badge.text}</span>
      </div>

      {/* Military Time, QR Demo & Telemetry Status */}
      <div className="flex items-center gap-3 text-xs">
        <a
          href={`http://${typeof window !== 'undefined' && window.location.hostname ? window.location.hostname : '127.0.0.1'}:8000/canary-qr`}
          target="_blank"
          rel="noreferrer"
          title="Buka QR Code agar dewan juri / audiens dapat mengunduh dokumen umpan di HP mereka"
          className="flex items-center gap-1.5 px-2.5 py-1 rounded bg-amber-500/10 border border-amber-500/40 text-amber-300 text-[11px] font-semibold hover:bg-amber-500/20 transition-all cursor-pointer"
        >
          <QrCode className="w-3.5 h-3.5" />
          <span>QR DEMO JURI</span>
        </a>

        <div className="flex items-center gap-1.5 text-slate-300">
          <Clock className="w-3.5 h-3.5 text-slate-400" />
          <span className="font-semibold">{currentTime}</span>
        </div>
        <div className="flex items-center gap-1.5 px-2.5 py-1 rounded bg-slate-900 border border-slate-800 text-[11px]">
          <span className={`w-2 h-2 rounded-full ${wsConnected ? 'bg-emerald-400 animate-pulse' : 'bg-red-500'}`} />
          <span className="text-slate-400">{wsConnected ? 'LIVE FEED' : 'OFFLINE'}</span>
        </div>
      </div>
    </header>
  );
}
