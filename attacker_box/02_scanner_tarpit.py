import time
import urllib.request
import threading
import sys

TARGET_URL = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8000/decoy-portal/api/"
WORDLIST = [
    "admin", "login", "config", "backup", "db", "scada", 
    "genset", "radar", "sisfopers", "telemetry", "firmware",
    "passwords", "users", "secret", "mabesad", "kodam"
]

print("=" * 65)
print(f"[*] PENYERANG / SCANNER TERMINAL: MULTI-THREAD DIRECTORY BRUTE-FORCE")
print(f"[*] Target Endpoint : {TARGET_URL}")
print(f"[*] Threads         : 8 Concurrent Scanning Workers")
print("=" * 65)

def worker(thread_id, word):
    url = TARGET_URL + word
    t0 = time.time()
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Gobuster/v3.5 (Scanning Worker)"}
        )
        print(f"[Thread-{thread_id}] Probing: /{word} ...")
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read(64)
            elapsed = time.time() - t0
            print(f"[Thread-{thread_id}] /{word} -> HTTP {resp.status} (Response time: {elapsed:.2f}s)")
    except Exception as e:
        elapsed = time.time() - t0
        print(f"[Thread-{thread_id}] /{word} -> MACET/TIMEOUT setelah {elapsed:.2f}s: {e}")

threads = []
for idx, word in enumerate(WORDLIST[:8]):
    t = threading.Thread(target=worker, args=(idx + 1, word))
    threads.append(t)
    t.start()
    time.sleep(0.15)

for t in threads:
    t.join()

print("[*] Pemindaian selesai.")
