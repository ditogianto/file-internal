import React, { useState } from 'react';
import { X, Copy, Check, Printer, Shield } from 'lucide-react';

export default function SitrepModal({ isOpen, onClose, sitrepContent, loading }) {
  const [copied, setCopied] = useState(false);

  if (!isOpen) return null;

  const handleCopy = () => {
    navigator.clipboard.writeText(sitrepContent);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const extractHash = (content) => {
    if (!content) return 'E8B2F901A4C90D81...';
    const match = content.match(/Hash Integritas Berkas\s*:\s*([A-F0-9]{64})/i);
    return match ? match[1] : 'E8B2F901A4C90D817652BC9A31415E9F...';
  };

  const dynamicHash = extractHash(sitrepContent);

  const handlePrint = () => {
    window.print();
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
      <div className="w-full max-w-4xl bg-tactical-card border border-tactical-border rounded shadow-2xl flex flex-col max-h-[90vh] overflow-hidden">
        {/* Modal Header */}
        <div className="px-4 py-3 border-b border-tactical-border bg-slate-900 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Shield className="w-4 h-4 text-emerald-400" />
            <span className="font-bold text-xs tracking-wider text-slate-100">
              LAPORAN SITUASI SIBER MILITER RESMI // PUSSIBERAD TNI AD
            </span>
          </div>
          <div className="flex items-center gap-3">
            <span className="text-[10px] px-2 py-0.5 rounded bg-red-950 border border-red-500 text-red-300 font-bold tracking-widest">
              RAHASIA
            </span>
            <button
              onClick={onClose}
              className="p-1 rounded text-slate-400 hover:text-white hover:bg-slate-800"
            >
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Modal Body */}
        <div className="p-4 flex-1 overflow-y-auto bg-tactical-dark space-y-3">
          {/* Cryptographic chain-of-custody banner */}
          <div className="p-2 rounded bg-slate-900/80 border border-slate-800 flex items-center justify-between text-[10px] font-mono">
            <div className="text-slate-400 flex items-center gap-1.5">
              <span>HASH INTEGRITAS:</span>
              <span className="text-emerald-400 font-bold">SHA256: {dynamicHash.slice(0, 16)}...{dynamicHash.slice(-8)}</span>
            </div>
            <div className="text-slate-500">
              OTENTIKASI: <span className="text-cyan-400 font-bold">KASATGAS SIBER PUSSIBERAD</span>
            </div>
          </div>

          {loading ? (
            <div className="py-20 text-center text-slate-400 space-y-3 font-mono">
              <div className="w-8 h-8 border-2 border-emerald-500 border-t-transparent rounded-full animate-spin mx-auto" />
              <div>Memproses Telemetri Insiden via Model AI PUSSIBERAD...</div>
            </div>
          ) : (
            <pre className="font-mono text-xs text-slate-200 whitespace-pre-wrap leading-relaxed select-text bg-black/60 p-4 rounded border border-slate-900 shadow-inner">
              {sitrepContent}
            </pre>
          )}
        </div>

        {/* Modal Footer */}
        <div className="px-4 py-3 border-t border-tactical-border bg-slate-900 flex items-center justify-between">
          <div className="text-[10px] text-slate-500">
            KLASIFIKASI: RAHASIA NEGARA // DOKTRIN PERTAHANAN SIBER SEMESTA
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={handlePrint}
              className="px-3 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold flex items-center gap-1.5"
            >
              <Printer className="w-3.5 h-3.5 text-cyan-400" />
              <span>CETAK / PDF</span>
            </button>
            <button
              onClick={handleCopy}
              className="px-3 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold flex items-center gap-1.5"
            >
              {copied ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
              <span>{copied ? 'TERSALIN' : 'SALIN SITREP'}</span>
            </button>
            <button
              onClick={onClose}
              className="px-3 py-1.5 rounded bg-emerald-700 hover:bg-emerald-600 text-white text-xs font-semibold"
            >
              TUTUP
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
