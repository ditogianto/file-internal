import React, { useState, useEffect, useRef } from 'react';
import TopNav from './components/TopNav';
import MetricsGrid from './components/MetricsGrid';
import TacticalMap from './components/TacticalMap';
import ActionConsole from './components/ActionConsole';
import LiveRadarFeed from './components/LiveRadarFeed';
import AdversaryDossier from './components/AdversaryDossier';
import SitrepModal from './components/SitrepModal';
import { playRadarBeep, playRedAlertSiren } from './utils/audioAlerts';

const HOSTNAME = typeof window !== 'undefined' && window.location.hostname ? window.location.hostname : 'localhost';
const API_BASE = `http://${HOSTNAME}:8000`;
const WS_BASE = `ws://${HOSTNAME}:8000/ws/telemetry`;

export default function App() {
  const [operatorKey, setOperatorKey] = useState(() => {
    if (typeof window !== 'undefined') {
      return sessionStorage.getItem('c4isr_operator_key') || 'PUSSIBERAD-C4ISR-COMMAND-KEY';
    }
    return 'PUSSIBERAD-C4ISR-COMMAND-KEY';
  });

  const getAuthHeaders = () => ({
    'Content-Type': 'application/json',
    'X-C4ISR-Auth': operatorKey
  });

  const [systemStatus, setSystemStatus] = useState('SIAGA_HIJAU');
  const [tarpitActive, setTarpitActive] = useState(false);
  const [metrics, setMetrics] = useState(null);
  const [adversaryDossier, setAdversaryDossier] = useState(null);
  const [eventLogs, setEventLogs] = useState([]);
  const [compromisedUnit, setCompromisedUnit] = useState(null);
  const [wsConnected, setWsConnected] = useState(false);

  // Modal State
  const isSitrepParam = new URLSearchParams(window.location.search).get('modal') === 'sitrep';
  const defaultInitialSitrep = `================================================================================
MARKAS BESAR ANGKATAN DARAT
PUSAT SIBER ANGKATAN DARAT (PUSSIBERAD)
================================================================================
KLASIFIKASI  : RAHASIA (SECRET)
NOMOR SURAT  : R/SITREP-20261027-091/PUSSIBERAD
DARI         : KASATGAS SIBER KODAM JAYA / PUSSIBERAD
KEPADA       : DANPUSSIBERAD / ASINTEL KASAD
PERIHAL      : LAPORAN PENINDAKAN NEXUS-TRAP (NETWORK DECEPTION & ACTIVE TARPIT)
================================================================================

1. DASAR OPERASI:
   a. Doktrin Pertahanan Siber Semesta TNI AD Nomor Kep/44/XII/2025.
   b. Telemetri Aktif Sistem Deception NEXUS-TRAP Titik Sensor Satuan Teritorial.

2. FAKTA KEJADIAN:
   a. Waktu Intersepsi  : 27 Oktober 2026, Pukul 19:30:10 WIB.
   b. Satuan Terdampak  : KODAM JAYA / KOREM 051/WKT
   c. Host Terkompromi  : PC-ADMIN-LOGISTIK-04 (IP: 192.168.1.88)
   d. Status Ancaman    : SIAGA 1 (MERAH) - NETRALISASI SELESAI

3. KRONOLOGI INSIDEN:
   a. PENGINTAIAN FASILITAS VITAL (OT/ICS):
      Pelaku memindai Port 502 Modbus TCP (Telemetri Genset/Radar Komando).
      Sistem NEXUS-TRAP menyerap paket pengintaian dan membunyikan Siaga Kuning.
   b. PELUMPUHAN INSTRUMEN LAWAN (TARPIT):
      Penyerang meluncurkan scanner otomatis. Modul Tarpit Crasher mengunci
      worker thread pemindai musuh hingga proses penyerang macet total (0 req/s).
   c. PENCURIAN DOKUMEN & IDENTIFIKASI ATRIBUSI:
      Dokumen umpan (Rahasia_Dislokasi_Pasukan_2026.docx) diekstraksi ke VM.
      Suar DNS Klandestin (UDP 5053) menembus isolasi VM, membongkar:
      - Hardware/GPU Fingerprint : 7b3a99e120fd9c48... [ANGLE Intel UHD]
      - L4/L7 CLI Signature (JA4): t13d1516h2_8da6530 (Gobuster/v3.5)
      - Resolver Node Eksternal  : doc-991a.kodam-jaya.canary.nexustrap.mil.id

4. TINDAKAN PENINDAKAN:
   a. Menjalankan isolasi jaringan 1-klik (Quarantine) terhadap IP 192.168.1.88.
   b. Memasukkan sidik jari hardware pelaku ke Blacklist Sentral PUSSIBERAD.
   c. Mengamankan integritas register OT pangkalan tetap dalam batas normal.

                                                JAKARTA, 27 OKTOBER 2026
                                                KASATGAS OPERASI SIBER NEXUS-TRAP
================================================================================`;

  const [sitrepModalOpen, setSitrepModalOpen] = useState(isSitrepParam);
  const [sitrepContent, setSitrepContent] = useState(isSitrepParam ? defaultInitialSitrep : '');
  const [sitrepLoading, setSitrepLoading] = useState(false);

  const prevStatusRef = useRef(systemStatus);

  // WebSocket Connection
  useEffect(() => {
    let ws = null;
    let reconnectTimer = null;

    const connectWebSocket = () => {
      const wsUrl = `${WS_BASE}?token=${encodeURIComponent(operatorKey)}`;
      ws = new WebSocket(wsUrl);

      ws.onopen = () => {
        setWsConnected(true);
      };

      ws.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          if (data.system_status) {
            setSystemStatus(data.system_status);
            // Trigger tactical audio effects on status transitions
            if (data.system_status === 'SIAGA_KUNING' && prevStatusRef.current !== 'SIAGA_KUNING') {
              playRadarBeep();
            } else if (data.system_status === 'SIAGA_MERAH' && prevStatusRef.current !== 'SIAGA_MERAH') {
              playRedAlertSiren();
            }
            prevStatusRef.current = data.system_status;
          }
          if (data.tarpit_active !== undefined) setTarpitActive(data.tarpit_active);
          if (data.metrics) setMetrics(data.metrics);
          if (data.adversary_dossier) setAdversaryDossier(data.adversary_dossier);
          if (data.event_logs) setEventLogs(data.event_logs);
          if (data.compromised_unit !== undefined) setCompromisedUnit(data.compromised_unit);
        } catch (e) {}
      };

      ws.onclose = () => {
        setWsConnected(false);
        reconnectTimer = setTimeout(connectWebSocket, 2000);
      };

      ws.onerror = () => {
        ws.close();
      };
    };

    connectWebSocket();

    return () => {
      if (ws) ws.close();
      if (reconnectTimer) clearTimeout(reconnectTimer);
    };
  }, [operatorKey]);

  // Action Handlers
  const handleToggleTarpit = async (active) => {
    try {
      const resp = await fetch(`${API_BASE}/api/tarpit/toggle`, {
        method: 'POST',
        headers: getAuthHeaders(),
        body: JSON.stringify({ active })
      });
      const data = await resp.json();
      setTarpitActive(data.tarpit_active);
    } catch (e) {}
  };

  const handleIsolateHost = async (ip) => {
    try {
      await fetch(`${API_BASE}/api/isolate`, {
        method: 'POST',
        headers: getAuthHeaders(),
        body: JSON.stringify({ ip })
      });
    } catch (e) {}
  };

  const handleOpenSitrep = async () => {
    setSitrepModalOpen(true);
    setSitrepLoading(true);
    try {
      const resp = await fetch(`${API_BASE}/api/sitrep/generate`, {
        method: 'POST',
        headers: getAuthHeaders()
      });
      const data = await resp.json();
      setSitrepContent(data.sitrep || 'Laporan Sitrep tidak tersedia.');
    } catch (e) {
      setSitrepContent('Gagal memproses Laporan Intelijen Sitrep.');
    } finally {
      setSitrepLoading(false);
    }
  };

  const handleReset = async () => {
    try {
      await fetch(`${API_BASE}/api/reset`, {
        method: 'POST',
        headers: getAuthHeaders()
      });
    } catch (e) {}
  };

  const handleExportFirewall = async (format = 'iptables') => {
    try {
      const res = await fetch(`${API_BASE}/api/threat-intel/export-firewall?format=${format}`, {
        headers: getAuthHeaders()
      });
      if (res.ok) {
        const text = await res.text();
        const blob = new Blob([text], { type: 'text/plain' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        let filename = 'pussiberad_firewall_rules.sh';
        if (format === 'windows_netsh') filename = 'pussiberad_firewall_rules.bat';
        else if (format === 'mikrotik') filename = 'pussiberad_firewall_rules.rsc';
        else if (format === 'cisco') filename = 'pussiberad_cisco_acl.cfg';
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        a.remove();
        window.URL.revokeObjectURL(url);
      }
    } catch (err) {
      console.error('Export failed:', err);
    }
  };

  // Keyboard Shortcuts for High-Tempo Stage Presentation
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;

      const key = e.key.toLowerCase();
      if (key === 'r') {
        e.preventDefault();
        handleReset();
      } else if (key === 't') {
        e.preventDefault();
        handleToggleTarpit(!tarpitActive);
      } else if (key === 'k') {
        e.preventDefault();
        handleIsolateHost(adversaryDossier?.attacker_ip || '192.168.1.88');
      } else if (key === 's') {
        e.preventDefault();
        handleOpenSitrep();
      } else if (key === 'q') {
        e.preventDefault();
        window.open(`http://${HOSTNAME}:8000/canary-qr`, '_blank');
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [tarpitActive, adversaryDossier, operatorKey]);

  return (
    <div className="h-screen w-screen flex flex-col bg-tactical-dark text-slate-100 overflow-hidden">
      {/* Top Navigation Bar */}
      <TopNav systemStatus={systemStatus} wsConnected={wsConnected} />

      {/* Main Single-Screen C4ISR War Room Body */}
      <main className="flex-1 p-3 flex flex-col gap-3 overflow-hidden">
        {/* KPI Metrics Ribbon */}
        <MetricsGrid metrics={metrics} tarpitActive={tarpitActive} />

        {/* Central Operations Split: Tactical Map & Action Console */}
        <div className="grid grid-cols-12 gap-3 h-[42%] min-h-[200px]">
          <div className="col-span-8 h-full">
            <TacticalMap systemStatus={systemStatus} compromisedUnit={compromisedUnit} />
          </div>
          <div className="col-span-4 h-full">
            <ActionConsole
              tarpitActive={tarpitActive}
              onToggleTarpit={handleToggleTarpit}
              onIsolate={handleIsolateHost}
              onOpenSitrep={handleOpenSitrep}
              onReset={handleReset}
              onExportFirewall={handleExportFirewall}
              adversaryDossier={adversaryDossier}
            />
          </div>
        </div>

        {/* Bottom Operations Split: Live Event Stream & Adversary Dossier */}
        <div className="grid grid-cols-12 gap-3 flex-1 min-h-[180px] overflow-hidden">
          <div className="col-span-7 h-full overflow-hidden">
            <LiveRadarFeed logs={eventLogs} />
          </div>
          <div className="col-span-5 h-full overflow-hidden">
            <AdversaryDossier dossier={adversaryDossier} />
          </div>
        </div>
      </main>

      {/* Pop-up Tactical Military Sitrep Modal */}
      <SitrepModal
        isOpen={sitrepModalOpen}
        onClose={() => setSitrepModalOpen(false)}
        sitrepContent={sitrepContent}
        loading={sitrepLoading}
      />
    </div>
  );
}
