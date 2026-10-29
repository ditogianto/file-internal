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
  const [exportFormat, setExportFormat] = useState('iptables');

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

  const handleFirewallDownload = (fmt) => {
    const targetFmt = fmt || exportFormat;
    setExportFormat(targetFmt);
    if (onExportFirewall) {
      onExportFirewall(targetFmt);
    }
  };

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
          title="Hotkey: Tekan [T]"
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
          <div className="flex items-center gap-1.5">
            <span className="text-[9px] text-slate-500 font-mono">[T]</span>
            <span className={`text-[9px] px-1.5 py-0.5 rounded ${tarpitActive ? 'bg-amber-500 text-black font-extrabold' : 'bg-slate-800 text-slate-400'}`}>
              {tarpitActive ? 'LOCKING' : 'OFF'}
            </span>
          </div>
        </button>

        {/* Button 2: 1-Click Host Isolation */}
        <button
          onClick={handleIsolateClick}
          disabled={loadingIsolate || isIsolated}
          title="Hotkey: Tekan [K]"
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
          <div className="flex items-center gap-1.5">
            <span className="text-[9px] text-slate-500 font-mono">[K]</span>
            <span className="text-[9px] px-1.5 py-0.5 rounded bg-black/40 text-slate-200">
              {isIsolated ? 'QUARANTINED' : '1-KLIK'}
            </span>
          </div>
        </button>

        {/* Button 3: AI Military Sitrep Generator */}
        <button
          onClick={onOpenSitrep}
          title="Hotkey: Tekan [S]"
          className="w-full py-2 px-3 rounded bg-cyan-950/60 border border-cyan-500 text-cyan-200 hover:bg-cyan-900/60 text-xs font-bold tracking-wider flex items-center justify-between transition-all"
        >
          <div className="flex items-center gap-2">
            <FileText className="w-4 h-4 text-cyan-400" />
            <span>GENERATE AI MILITARY SITREP</span>
          </div>
          <div className="flex items-center gap-1.5">
            <span className="text-[9px] text-slate-500 font-mono">[S]</span>
            <span className="text-[9px] px-1.5 py-0.5 rounded bg-cyan-900 text-cyan-200">TNI AD</span>
          </div>
        </button>

        {/* Button 4: Multi-Target Export Threat Intel Firewall Rules */}
        <div className="rounded bg-slate-900/90 border border-slate-700/80 p-2">
          <div className="flex items-center justify-between mb-1.5">
            <div className="flex items-center gap-1.5 text-[11px] font-bold text-slate-300">
              <span className="text-emerald-400">🛡</span>
              <span>EKSPOR SENTRAL BLACKLIST</span>
            </div>
            <span className="text-[8px] bg-slate-800 text-emerald-400 px-1 py-0.5 rounded font-mono">
              ROUTER / SWITCH L3
            </span>
          </div>
          <div className="grid grid-cols-4 gap-1">
            <button
              onClick={() => handleFirewallDownload('iptables')}
              title="Linux iptables bash script"
              className={`py-1 px-1 text-[9px] font-bold rounded border transition-all ${
                exportFormat === 'iptables'
                  ? 'bg-emerald-900/60 border-emerald-500 text-emerald-300'
                  : 'bg-slate-800/80 border-slate-700 text-slate-400 hover:text-slate-200'
              }`}
            >
              IPTABLES
            </button>
            <button
              onClick={() => handleFirewallDownload('windows_netsh')}
              title="Windows Advanced Firewall batch script"
              className={`py-1 px-1 text-[9px] font-bold rounded border transition-all ${
                exportFormat === 'windows_netsh'
                  ? 'bg-blue-900/60 border-blue-500 text-blue-300'
                  : 'bg-slate-800/80 border-slate-700 text-slate-400 hover:text-slate-200'
              }`}
            >
              NETSH
            </button>
            <button
              onClick={() => handleFirewallDownload('mikrotik')}
              title="MikroTik RouterOS script (.rsc)"
              className={`py-1 px-1 text-[9px] font-bold rounded border transition-all ${
                exportFormat === 'mikrotik'
                  ? 'bg-amber-900/60 border-amber-500 text-amber-300'
                  : 'bg-slate-800/80 border-slate-700 text-slate-400 hover:text-slate-200'
              }`}
            >
              MIKROTIK
            </button>
            <button
              onClick={() => handleFirewallDownload('cisco')}
              title="Cisco IOS Access Control List (.cfg)"
              className={`py-1 px-1 text-[9px] font-bold rounded border transition-all ${
                exportFormat === 'cisco'
                  ? 'bg-cyan-900/60 border-cyan-500 text-cyan-300'
                  : 'bg-slate-800/80 border-slate-700 text-slate-400 hover:text-slate-200'
              }`}
            >
              CISCO
            </button>
          </div>
        </div>
      </div>

      {/* Button 5: Reset Demo State */}
      <div className="pt-2 border-t border-tactical-border/60 mt-2 flex items-center justify-between">
        <button
          onClick={onReset}
          title="Hotkey: Tekan [R]"
          className="flex-1 py-1 text-[10px] text-slate-400 hover:text-slate-200 bg-slate-900 hover:bg-slate-800 rounded border border-slate-800 flex items-center justify-center gap-1.5"
        >
          <RotateCcw className="w-3 h-3" />
          <span>RESET STATUS PURWARUPA (0 DETIK)</span>
        </button>
        <span className="text-[9px] text-slate-500 font-mono ml-2">[R]</span>
      </div>
    </div>
  );
}
