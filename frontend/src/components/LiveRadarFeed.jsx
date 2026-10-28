import React, { useRef, useEffect, useState } from 'react';
import { Terminal, Shield, AlertTriangle, AlertOctagon, Info, Filter } from 'lucide-react';

export default function LiveRadarFeed({ logs }) {
  const bottomRef = useRef(null);
  const [filterTag, setFilterTag] = useState('ALL');

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [logs]);

  const filteredLogs = logs?.filter(item => {
    if (filterTag === 'ALL') return true;
    return item.tag?.toUpperCase().includes(filterTag);
  });

  const getLevelBadge = (level) => {
    switch (level) {
      case 'ALERT':
        return {
          icon: AlertOctagon,
          style: 'bg-red-950 text-red-400 border-red-700/60'
        };
      case 'WARN':
        return {
          icon: AlertTriangle,
          style: 'bg-amber-950 text-amber-400 border-amber-700/60'
        };
      case 'INFO':
      default:
        return {
          icon: Info,
          style: 'bg-slate-900 text-slate-400 border-slate-700/60'
        };
    }
  };

  return (
    <div className="rounded bg-tactical-card border border-tactical-border p-3 flex flex-col h-full overflow-hidden">
      <div className="flex items-center justify-between border-b border-tactical-border pb-2 mb-2">
        <div className="flex items-center gap-2">
          <Terminal className="w-3.5 h-3.5 text-cyan-400" />
          <span className="text-[11px] font-bold tracking-wider text-slate-200">RADAR TELEMETRI & LOG WAKTU NYATA</span>
        </div>
        
        {/* Quick Filter Pills */}
        <div className="flex items-center gap-1 text-[9px]">
          {['ALL', 'OT_DECOY', 'TARPIT', 'CANARY'].map(tag => (
            <button
              key={tag}
              onClick={() => setFilterTag(tag)}
              className={`px-1.5 py-0.5 rounded border transition-all ${
                filterTag === tag 
                  ? 'bg-cyan-950 border-cyan-500 text-cyan-300 font-bold' 
                  : 'bg-slate-900/60 border-slate-800 text-slate-500 hover:text-slate-300'
              }`}
            >
              {tag === 'ALL' ? 'SEMUA' : tag}
            </button>
          ))}
          <span className="text-slate-600 pl-1">({filteredLogs?.length || 0})</span>
        </div>
      </div>

      {/* Log Feed Table */}
      <div className="flex-1 overflow-y-auto space-y-1.5 pr-1 font-mono text-[11px]">
        {filteredLogs?.map((item, idx) => {
          const badge = getLevelBadge(item.level);
          const Icon = badge.icon;
          return (
            <div
              key={idx}
              className="p-1.5 rounded bg-tactical-dark/80 border border-slate-900 hover:border-slate-800 flex items-start gap-2.5 transition-colors"
            >
              <div className="text-slate-500 text-[10px] shrink-0 pt-0.5">{item.timestamp}</div>
              <div className={`px-1.5 py-0.2 rounded border text-[9px] font-bold shrink-0 flex items-center gap-1 ${badge.style}`}>
                <Icon className="w-2.5 h-2.5" />
                <span>{item.tag || item.level}</span>
              </div>
              <div className="text-slate-300 flex-1 leading-snug break-all">
                {item.message}
              </div>
              {item.source_ip && item.source_ip !== '-' && (
                <div className="text-[9px] text-slate-500 shrink-0 font-semibold px-1 rounded bg-slate-900 border border-slate-800">
                  {item.source_ip}
                </div>
              )}
            </div>
          );
        })}
        <div ref={bottomRef} />
      </div>
    </div>
  );
}
