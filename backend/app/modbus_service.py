import asyncio
from app.config import settings
from app.telemetry import telemetry

class ModbusDecoyServer:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.server = None

    async def handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        client_addr = writer.get_extra_info('peername')
        client_ip = client_addr[0] if client_addr else "UNKNOWN"
        
        # Trigger Yellow Alert
        if telemetry.system_status == "SIAGA_HIJAU":
            await telemetry.set_status("SIAGA_KUNING")
        
        await telemetry.register_threat_actor(
            ip=client_ip,
            vector=f"MODBUS_TCP_SCAN_PORT_{self.port}",
            severity="HIGH",
            unit="GENSET-RADAR-01",
            notes=f"Pemindaian unauthorized pada Modbus TCP port {self.port}"
        )
        
        await telemetry.update_dossier({
            "status": "PENGINTAIAN FASILITAS VITAL OT TERDETEKSI",
            "attacker_ip": client_ip,
            "breach_vector": f"Intersepsi Modbus TCP (Port {self.port}) - Genset Markas"
        })
        
        await telemetry.add_log(
            level="WARN",
            tag="OT_DECOY",
            message=f"Penyusup memindai protokol industri Modbus TCP Port {self.port} (Genset/Radar Pangkalan).",
            source_ip=client_ip
        )

        try:
            while True:
                data = await reader.read(1024)
                if not data:
                    break

                # Parse MBAP Header (Modbus TCP)
                # Bytes 0-1: Transaction ID
                # Bytes 2-3: Protocol ID (0 = Modbus)
                # Bytes 4-5: Length
                # Byte 6: Unit ID
                # Byte 7: Function Code
                if len(data) >= 8:
                    trans_id = data[0:2]
                    unit_id = data[6:7]
                    func_code = data[7]
                    
                    # Simulated PLC Registers (Genset Pangkalan: 380V, 50Hz, 85% Fuel)
                    # Function 0x03: Read Holding Registers
                    if func_code == 0x03:
                        # Construct realistic Modbus reply:
                        # Byte count: 6 bytes (3 registers x 2 bytes)
                        # Reg 1 (380V): 0x017C
                        # Reg 2 (50Hz): 0x0032
                        # Reg 3 (85%):  0x0055
                        payload = bytes([func_code, 0x06, 0x01, 0x7C, 0x00, 0x32, 0x00, 0x55])
                        length = len(payload) + 1
                        header = trans_id + b"\x00\x00" + length.to_bytes(2, "big") + unit_id
                        writer.write(header + payload)
                        await writer.drain()
                    else:
                        # Echo back generic acknowledge
                        writer.write(data)
                        await writer.drain()
                else:
                    # Echo raw response to satisfy Nmap probe
                    writer.write(b"\x00\x01\x00\x00\x00\x06\x01\x03\x02\x01\x7c")
                    await writer.drain()
        except Exception:
            pass
        finally:
            writer.close()
            await writer.wait_closed()

    async def start(self):
        try:
            self.server = await asyncio.start_server(
                self.handle_client,
                self.host,
                self.port
            )
            await telemetry.add_log(
                level="INFO",
                tag="OT_DECOY",
                message=f"Emulasi Modbus TCP (Genset/Radar Pangkalan) aktif di port {self.port}.",
                source_ip="0.0.0.0"
            )
        except PermissionError:
            await telemetry.add_log(
                level="WARN",
                tag="OT_DECOY",
                message=f"Port Modbus {self.port} butuh izin root/admin.",
                source_ip="0.0.0.0"
            )
        except Exception as e:
            await telemetry.add_log(
                level="WARN",
                tag="OT_DECOY",
                message=f"Gagal memulai Modbus Server: {str(e)}",
                source_ip="0.0.0.0"
            )

async def start_modbus_service():
    modbus_server = ModbusDecoyServer(settings.MODBUS_HOST, settings.MODBUS_PORT)
    await modbus_server.start()
    return modbus_server
