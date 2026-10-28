#!/usr/bin/env bash
# NEXUS-TRAP: 1-Click Startup Launcher (Linux/macOS)
set -e

echo -e "\033[0;32m=================================================================\033[0m"
echo -e "\033[0;36m [!] MEMULAI NEXUS-TRAP C4ISR PLATFORM (PUSSIBERAD TNI AD)     \033[0m"
echo -e "\033[0;32m=================================================================\033[0m"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# 1. Start Backend
echo -e "\n\033[0;33m[1/3] Menyiapkan Backend Engine (FastAPI, OT Decoy, DNS Canary)...\033[0m"
cd "$DIR/backend"
pip install -r requirements.txt
python run_backend.py &
BACKEND_PID=$!
echo -e "\033[0;32m    -> Backend running with PID $BACKEND_PID\033[0m"

# 2. Start Frontend
echo -e "\n\033[0;33m[2/3] Menyiapkan Frontend C4ISR UI (React + Vite)...\033[0m"
cd "$DIR/frontend"
npm install
npm run dev -- --host &
FRONTEND_PID=$!
echo -e "\033[0;32m    -> Frontend running with PID $FRONTEND_PID\033[0m"

# 3. Ready notification
sleep 3
echo -e "\n\033[0;32m=================================================================\033[0m"
echo -e "\033[0;32m [*] SELURUH LAYANAN AKTIF. Buka http://localhost:3000\033[0m"
echo -e "\033[0;36m [*] Untuk simulasi penyerang, jalankan skrip di folder attacker_box/\033[0m"
echo -e "\033[0;32m=================================================================\033[0m"

wait
