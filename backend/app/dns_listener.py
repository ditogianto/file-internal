import asyncio
from typing import Optional
from dnslib import DNSRecord, DNSHeader, RR, A, QTYPE
from app.config import settings
from app.telemetry import telemetry

class CanaryDNSProtocol(asyncio.DatagramProtocol):
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data: bytes, addr: tuple):
        try:
            request = DNSRecord.parse(data)
            qname = str(request.q.qname).lower().rstrip(".")
            client_ip = addr[0]

            # Detect if this is a canary beacon query
            if "canary" in qname or "doc-" in qname or settings.CANARY_DOMAIN in qname:
                asyncio.create_task(self.handle_canary_hit(qname, client_ip))

            # Build standard valid reply to satisfy client resolver
            reply = DNSRecord(
                DNSHeader(id=request.header.id, qr=1, aa=1, ra=1),
                q=request.q
            )
            reply.add_answer(RR(request.q.qname, QTYPE.A, rdata=A("127.0.0.1"), ttl=60))
            self.transport.sendto(reply.pack(), addr)
        except Exception as e:
            pass

    async def handle_canary_hit(self, qname: str, client_ip: str):
        # Extract doc id and unit from qname
        parts = qname.split(".")
        doc_id = parts[0].upper() if parts else "DOC-991A"
        unit_target = parts[1].upper() if len(parts) > 1 else "KODAM JAYA"
        
        telemetry.metrics["canary_triggers"] += 1
        telemetry.compromised_unit = "KODAM JAYA"
        await telemetry.set_status("SIAGA_MERAH")
        
        await telemetry.register_threat_actor(
            ip=client_ip,
            vector="CANARY_DNS_OUT_OF_BAND",
            severity="CRITICAL",
            fingerprint=f"DNS_QNAME: {qname}",
            unit=unit_target,
            notes=f"Dokumen rahasia {doc_id} dilarikan dan di-resolve melalui DNS eksternal"
        )
        
        await telemetry.update_dossier({
            "status": "INTRUSI KRITIS (DOKUMEN DIBUKA DI VM ASING)",
            "attacker_ip": client_ip,
            "workstation_host": "PC-ADMIN-LOGISTIK-04",
            "compromised_doc": f"Rahasia_Dislokasi_Pasukan_2026.docx ({doc_id})",
            "breach_vector": "Out-of-Band DNS Canary Triggered (Isolasi VM Terbongkar)"
        })
        
        await telemetry.add_log(
            level="ALERT",
            tag="CANARY_DNS",
            message=f"SUAR DNS AKTIF! Dokumen {doc_id} dibuka dari lingkungan luar. DNS Query: {qname}",
            source_ip=client_ip
        )

async def start_dns_listener() -> Optional[asyncio.DatagramTransport]:
    """Starts the Canary DNS UDP listener on configured host/port."""
    loop = asyncio.get_running_loop()
    try:
        transport, _ = await loop.create_datagram_endpoint(
            lambda: CanaryDNSProtocol(),
            local_addr=(settings.DNS_HOST, settings.DNS_PORT)
        )
        await telemetry.add_log(
            level="INFO",
            tag="DNS_CANARY",
            message=f"DNS Canary Listener berjalan di UDP port {settings.DNS_PORT}.",
            source_ip="0.0.0.0"
        )
        return transport
    except PermissionError:
        await telemetry.add_log(
            level="WARN",
            tag="DNS_CANARY",
            message=f"Port {settings.DNS_PORT} butuh hak administrator. Jalankan di port non-privileged.",
            source_ip="0.0.0.0"
        )
    except Exception as e:
        await telemetry.add_log(
            level="WARN",
            tag="DNS_CANARY",
            message=f"DNS Listener gagal inisialisasi: {str(e)}",
            source_ip="0.0.0.0"
        )
    return None
