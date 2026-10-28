import React, { useState } from 'react';
import { Lock, Unlock, ShieldBan, FileText, RotateCcw } from 'lucide-react';
import { playLockSuccessChime } from '../utils/audioAlerts';

export default function ActionConsole({
  tarpitActive,
  onToggleTarpit,
  onIsolate,
  onOpenSitrep,
  onReset,
  onExportFirewall,
  adversaryDossier
}) {
  const [loadingTarpit, setLoadingTarpit] = useState(false);
  const [loadingIsolate, setLoadingIsolate] = useState(false);

  const handleTarpitClick = async () => {
    setLoadingTarpit(true);
    await onToggleTarpit(!tarpitActive);
    playLockSuccessChime();
    setLoadingTarpit(false);
  };

  const handleIsolateClick = async () => {
    setLoadingIsolate(true);
    const targetIp = adversaryDossier?.attacker_ip || '192.168.1.88';
    await onIsolate(targetIp);
    playLockSuccessChime();
    setLoadingIsolate(false);
  };

  const isIsolated = adversaryDossier?.isolated;

  return (
    <div className="rounded bg-tactical-card border border-tactical-border p-3 flex flex-col justify-between h-full">
      <div className="border-b border-tactical-border pb-2 mb-2 flex items-center justify-between">
        <span className="text-[11px] font-bold tracking-wider text-slate-200">KONSOL KENDALI TAKTIS</span>
        <span className="text-[9px] bg-slate-800 text-slate-400 px-1.5 py-0.5 rounded">PUSSIBERAD AUTHORIZED</span>
      </div>

      <div className="space-y-2 flex-1 flex flex-col justify-center">
        {/* Button 1: Tarpit Crasher Switch */}
        <button
          onClick={handleTarpitClick}
          disabled={loadingTarpit}
          className={`w-full py-2 px-3 rounded border text-xs font-bold tracking-wider flex items-center justify-between transition-all ${
            tarpitActive
              ? 'bg-amber-600/30 border-amber-500 text-amber-200 hover:bg-amber-600/40 glow-amber'
              : 'bg-slate-900 border-slate-700 text-slate-300 hover:bg-slate-800'
          }`}
        >
          <div className="flex items-center gap-2">
            {tarpitActive ? <Lock className="w-4 h-4 text-amber-400 animate-spin" style={{ animationDuration: '3s' }} /> : <Unlock className="w-4 h-4 text-slate-400" />}
            <span>{tarpitActive ? 'TARPIT CRASHER: AKTIF' : 'AKTIFKAN TARPIT CRASHER'}</span>
          </div>
          <span className={`text-[9px] px-1.5 py-0.5 rounded ${tarpitActive ? 'bg-amber-500 text-black font-extrabold' : 'bg-slate-800 text-slate-400'}`}>
            {tarpitActive ? 'LOCKING' : 'OFF'}
          </span>
        </button>

        {/* Button 2: 1-Click Host Isolation */}
        <button
          onClick={handleIsolateClick}
          disabled={loadingIsolate || isIsolated}
          className={`w-full py-2 px-3 rounded border text-xs font-bold tracking-wider flex items-center justify-between transition-all ${
            isIsolated
              ? 'bg-emerald-950/60 border-emerald-500 text-emerald-300 cursor-not-allowed'
              : 'bg-red-950/70 border-red-600 text-red-200 hover:bg-red-900/80 glow-red'
          }`}
        >
          <div className="flex items-center gap-2">
            <ShieldBan className="w-4 h-4 text-red-400" />
            <span>{isIsolated ? 'HOST TELAH TERISOLASI' : 'ISOLASI HOST TERINFEKSI'}</span>
          </div>
          <span className="text-[9px] px-1.5 py-0.5 rounded bg-black/40 text-slate-200">
            {isIsolated ? 'QUARANTINED' : '1-KLIK'}
          </span>
        </button>

        {/* Button 3: AI Military Sitrep Generator */}
        <button
          onClick={onOpenSitrep}
          className="w-full py-2 px-3 rounded bg-cyan-950/60 border border-cyan-500 text-cyan-200 hover:bg-cyan-900/60 text-xs font-bold tracking-wider flex items-center justify-between transition-all"
        >
          <div className="flex items-center gap-2">
            <FileText className="w-4 h-4 text-cyan-400" />
            <span>GENERATE AI MILITARY SITREP</span>
          </div>
          <span className="text-[9px] px-1.5 py-0.5 rounded bg-cyan-900 text-cyan-200">TNI AD</span>
        </button>

        {/* Button 4: Export Threat Intel Firewall Rules */}
        <button
          onClick={() => onExportFirewall && onExportFirewall('iptables')}
          className="w-full py-1.5 px-3 rounded bg-slate-900 border border-slate-700 text-slate-300 hover:text-emerald-300 hover:border-emerald-600 text-[11px] font-bold tracking-wider flex items-center justify-between transition-all"
        >
          <div className="flex items-center gap-2">
            <span className="text-emerald-400">🛡</span>
            <span>EKSPOR FIREWALL BLACKLIST</span>
          </div>
          <span className="text-[9px] px-1.5 py-0.5 rounded bg-slate-800 text-emerald-400">IPTABLES</span>
        </button>
      </div>

      {/* Button 4: Reset Demo State */}
      <div className="pt-2 border-t border-tactical-border/60 mt-2">
        <button
          onClick={onReset}
          className="w-full py-1 text-[10px] text-slate-400 hover:text-slate-200 bg-slate-900 hover:bg-slate-800 rounded border border-slate-800 flex items-center justify-center gap-1.5"
        >
          <RotateCcw className="w-3 h-3" />
          <span>RESET STATUS PURWARUPA (0 DETIK)</span>
        </button>
      </div>
    </div>
  );
}
