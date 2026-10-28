import time
import urllib.request
import json
import sys

BACKEND_API = "http://127.0.0.1:8000/api/status"
TARGET_IP = "192.168.1.50"

print("=" * 65)
print(f"[*] PENYERANG MONITOR: KONEKSI INTRANET PANGKALAN (ICMP / PING)")
print(f"[*] Sasaran Komunikasi : {TARGET_IP} (Pangkalan TNI AD)")
print(f"[*] Tekan Ctrl+C untuk menghentikan pemantauan.")
print("=" * 65)

seq = 1
while True:
    try:
        # Check backend state
        req = urllib.request.Request(BACKEND_API, headers={"User-Agent": "AttackerProbe"})
        with urllib.request.urlopen(req, timeout=1.0) as resp:
            data = json.loads(resp.read().decode())
            is_isolated = data.get("adversary_dossier", {}).get("isolated", False)
            
            if is_isolated:
                print(f"[SEQ={seq}] Reply from {TARGET_IP}: Destination host unreachable. (ISOLATED)")
                print(f"[SEQ={seq+1}] Request timed out.")
                seq += 2
            else:
                print(f"[SEQ={seq}] Reply from {TARGET_IP}: bytes=32 time=0.84ms TTL=64 [CONNECTED]")
                seq += 1
    except Exception:
        print(f"[SEQ={seq}] Request timed out. Connection refused.")
        seq += 1
    time.sleep(1.0)
