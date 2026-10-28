import React from 'react';
import { Target, ShieldCheck, Lock, Cpu } from 'lucide-react';

export default function MetricsGrid({ metrics, tarpitActive }) {
  const cards = [
    {
      title: 'TINGKAT AKURASI',
      value: metrics?.accuracy_score || '100.0%',
      sub: 'Deterministik Mutlak',
      icon: Target,
      color: 'text-emerald-400',
      border: 'border-emerald-500/30'
    },
    {
      title: 'FALSE POSITIVE RATE',
      value: metrics?.false_positive_rate || '0.0%',
      sub: 'Nol Alarm Palsu',
      icon: ShieldCheck,
      color: 'text-emerald-400',
      border: 'border-emerald-500/30'
    },
    {
      title: 'NODE UMPAN AKTIF',
      value: metrics?.active_decoys || 64,
      sub: 'IT/OT Sensor Se-Kodam',
      icon: Cpu,
      color: 'text-cyan-400',
      border: 'border-cyan-500/30'
    },
    {
      title: 'THREAD LAWAN TERKUNCI',
      value: metrics?.locked_threads || 0,
      sub: tarpitActive ? 'Tarpit Crasher AKTIF' : 'Standby / Mode Silent',
      icon: Lock,
      color: metrics?.locked_threads > 0 ? 'text-amber-400 animate-pulse' : 'text-slate-400',
      border: metrics?.locked_threads > 0 ? 'border-amber-500/60 bg-amber-950/20' : 'border-slate-800'
    }
  ];

  return (
    <div className="grid grid-cols-4 gap-3">
      {cards.map((card, idx) => {
        const Icon = card.icon;
        return (
          <div
            key={idx}
            className={`p-3 rounded bg-tactical-card border ${card.border} flex items-center justify-between transition-all`}
          >
            <div>
              <div className="text-[10px] text-slate-400 font-semibold tracking-wider">{card.title}</div>
              <div className={`text-xl font-extrabold tracking-tight mt-0.5 ${card.color}`}>
                {card.value}
              </div>
              <div className="text-[9px] text-slate-500 mt-0.5">{card.sub}</div>
            </div>
            <div className="p-2 rounded bg-slate-900/80 border border-slate-800/80 text-slate-400">
              <Icon className="w-4 h-4" />
            </div>
          </div>
        );
      })}
    </div>
  );
}
