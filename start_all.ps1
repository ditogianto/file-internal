# NEXUS-TRAP: 1-Click Startup Launcher (Windows PowerShell)
$ErrorActionPreference = "Stop"

Write-Host "=================================================================" -ForegroundColor Green
Write-Host " [!] MEMULAI NEXUS-TRAP C4ISR PLATFORM (PUSSIBERAD TNI AD)     " -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Green

$RootPath = $PSScriptRoot

# 1. Inisialisasi Backend
Write-Host "`n[1/3] Menyiapkan Backend Engine (FastAPI, OT Decoy, DNS Canary)..." -ForegroundColor Yellow
$BackendPath = Join-Path $RootPath "backend"

# Jalankan backend di window powershell terpisah
$BackendJob = Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$BackendPath'; pip install -r requirements.txt; python run_backend.py" -PassThru
Write-Host "    -> Backend PID: $($BackendJob.Id) berjalan di port 8000 (Modbus: 5020, DNS: 5053)" -ForegroundColor Green

# 2. Inisialisasi Frontend
Write-Host "`n[2/3] Menyiapkan Frontend C4ISR UI (React + Vite + TailwindCSS)..." -ForegroundColor Yellow
$FrontendPath = Join-Path $RootPath "frontend"

$FrontendJob = Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$FrontendPath'; npm install; npm run dev" -PassThru
Write-Host "    -> Frontend PID: $($FrontendJob.Id) berjalan di http://localhost:3000" -ForegroundColor Green

# 3. Tunggu dan buka browser
Start-Sleep -Seconds 3
Write-Host "`n[3/3] Membuka Antarmuka Komando di Browser..." -ForegroundColor Yellow
Start-Process "http://localhost:3000"

Write-Host "`n=================================================================" -ForegroundColor Green
Write-Host " [*] SELURUH LAYANAN AKTIF. SIAP UNTUK LIVE DEMO PANGGUNG!" -ForegroundColor Green
Write-Host " [*] Untuk menguji skenario serangan, buka folder: attacker_box/" -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Green
