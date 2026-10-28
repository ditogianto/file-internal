import socket
import sys
import time

TARGET_HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
TARGET_PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 5020  # Default dev port; 502 in standard deployment

print("=" * 60)
print(f"[*] PENYERANG / SCANNER TERMINAL: PENGINTAIAN FASILITAS OT (MODBUS)")
print(f"[*] Target : {TARGET_HOST}:{TARGET_PORT}")
print("=" * 60)

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5.0)
    sock.connect((TARGET_HOST, TARGET_PORT))
    print(f"[+] Koneksi TCP Handshake ke Port {TARGET_PORT} BERHASIL.")
    
    # Send Modbus Function 0x03 (Read Holding Registers: TransId=1, Unit=1, Func=3, Start=0, Count=3)
    modbus_request = b"\x00\x01\x00\x00\x00\x06\x01\x03\x00\x00\x00\x03"
    print(f"[>] Mengirim Probe Modbus Read Holding Registers (Function 0x03)...")
    sock.sendall(modbus_request)
    
    response = sock.recv(1024)
    if response and len(response) >= 9:
        func = response[7]
        byte_count = response[8]
        print(f"[+] Respons Modbus Diterima (Function 0x{func:02X}, Length: {byte_count} bytes):")
        if len(response) >= 15:
            reg0 = int.from_bytes(response[9:11], "big")
            reg1 = int.from_bytes(response[11:13], "big")
            reg2 = int.from_bytes(response[13:15], "big")
            print(f"    - Register 40001 (Tegangan Genset) : {reg0} V")
            print(f"    - Register 40002 (Frekuensi Daya)  : {reg1} Hz")
            print(f"    - Register 40003 (Level Tangki BBM): {reg2} %")
            print(f"[!] Target dikonfirmasi sebagai PLC Fasilitas Genset Pangkalan!")
    sock.close()
except Exception as e:
    print(f"[-] Gagal terhubung ke Modbus ({e}). Pastikan backend NEXUS-TRAP sudah aktif.")
