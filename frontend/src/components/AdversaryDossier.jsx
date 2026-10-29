import React from 'react';
import { UserX, Fingerprint, HardDrive, FileWarning, ShieldCheck, Cpu } from 'lucide-react';

export default function AdversaryDossier({ dossier }) {
  const isIdentified = dossier?.status && dossier.status !== 'TIDAK TERDETEKSI';

  return (
    <div className="rounded bg-tactical-card border border-tactical-border p-3 flex flex-col h-full overflow-hidden">
      <div className="flex items-center justify-between border-b border-tactical-border pb-2 mb-2">
        <div className="flex items-center gap-2">
          <UserX className="w-3.5 h-3.5 text-amber-400" />
          <span className="text-[11px] font-bold tracking-wider text-slate-200">DOSSIER ATRIBUSI BURONAN SIBER</span>
        </div>
        <span
          className={`text-[9px] px-2 py-0.5 rounded font-bold border ${
            isIdentified
              ? 'bg-amber-950/80 border-amber-600 text-amber-300'
              : 'bg-slate-900 border-slate-800 text-slate-500'
          }`}
        >
          {dossier?.status || 'STANDBY'}
        </span>
      </div>

      <div className="flex-1 space-y-2 overflow-y-auto pr-1 text-[11px]">
        {/* Attacker Identity Items */}
        <div className="grid grid-cols-2 gap-2">
          <div className="p-2 rounded bg-tactical-dark border border-slate-900">
            <div className="text-[9px] text-slate-500 flex items-center gap-1">
              <HardDrive className="w-3 h-3 text-slate-400" /> WORKSTATION TERINFEKSI
            </div>
            <div className="font-semibold text-slate-200 mt-0.5 truncate">
              {dossier?.workstation_host || '-'}
            </div>
          </div>

          <div className="p-2 rounded bg-tactical-dark border border-slate-900">
            <div className="text-[9px] text-slate-500 flex items-center gap-1">
              <UserX className="w-3 h-3 text-slate-400" /> IP SUMBER PENYERANG
            </div>
            <div className="font-semibold text-amber-400 mt-0.5 truncate">
              {dossier?.attacker_ip || '-'}
            </div>
          </div>
        </div>

        {/* Dual Fingerprinting: L4/L7 JA4 & Hardware Hash */}
        <div className="p-2 rounded bg-tactical-dark border border-slate-900 space-y-1.5">
          <div>
            <div className="text-[9px] text-slate-500 flex items-center gap-1">
              <Cpu className="w-3 h-3 text-cyan-400" /> SIGNATURE CLI / SCANNER (JA4)
            </div>
            <div className="text-[10px] font-mono text-cyan-300 truncate">
              {dossier?.cli_signature && dossier.cli_signature !== '-' ? dossier.cli_signature : 'Menunggu pemindaian scanner...'}
            </div>
          </div>

          <div>
            <div className="text-[9px] text-slate-500 flex items-center gap-1">
              <Fingerprint className="w-3 h-3 text-emerald-400" /> SIDIK JARI HARDWARE (GPU / CANVAS)
            </div>
            <div className="text-[10px] font-mono text-emerald-300 truncate">
              {dossier?.hardware_hash && dossier.hardware_hash !== '-' ? `${dossier.hardware_hash} [${dossier.gpu_vendor || 'UNKNOWN'}]` : '-'}
            </div>
          </div>
        </div>

        {/* Breached Document */}
        <div className="p-2 rounded bg-tactical-dark border border-slate-900">
          <div className="text-[9px] text-slate-500 flex items-center gap-1">
            <FileWarning className="w-3 h-3 text-red-400" /> DOKUMEN UMPAN TEREKSTRAKSI
          </div>
          <div className="text-[10px] font-semibold text-red-300 mt-0.5 truncate">
            {dossier?.compromised_doc || '-'}
          </div>
        </div>

        {/* Executive Incident Correlation Context Box */}
        <div className="p-2 rounded bg-slate-900/90 border border-emerald-900/40 text-[10px] text-slate-400 leading-relaxed">
          <div className="text-emerald-400 font-bold mb-0.5 flex items-center gap-1">
            <ShieldCheck className="w-3 h-3" /> ANALISA HULU INSIDEN:
          </div>
          {isIdentified ? (
            <p className="text-slate-300">
              Kredensial dinas bocor via malware <em>Infostealer</em> pada workstation staf akibat APK ilegal. Penyerang melakukan <em>Lateral Movement</em> ke port Modbus OT dan memicu suar DNS dokumen rahasia.
            </p>
          ) : (
            <p className="text-slate-500 italic">
              Sensor aktif memantau lalu lintas internal pangkalan. Belum ada aktivitas klandestin atau pelanggaran ranjau siber.
            </p>
          )}
        </div>
      </div>
    </div>
  );
}
