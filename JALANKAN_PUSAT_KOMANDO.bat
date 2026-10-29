@echo off
chcp 65001 >nul
title PUSSIBERAD - MEJA KOMANDO C4ISR NEXUS-TRAP
color 0B
cls
echo ===============================================================================
echo      PUSSIBERAD TNI AD // KARTIKA CYBER HACKATHON 2026
echo      NEXUS-TRAP C4ISR WAR ROOM PUSAT KOMANDO
echo ===============================================================================
echo.
echo   [*] Menjalankan Backend Deception & C4ISR Listener:
echo       - FastAPI REST & WebSocket Server (Port 8000)
echo       - OT Modbus Industrial Honeypot (Port 5020)
echo       - Klandestin Canary UDP DNS Listener (Port 5053)
echo.
echo   [*] Menjalankan Frontend C4ISR War Room (Port 3000)...
echo.
echo ===============================================================================

REM Panggil start_all.ps1 via PowerShell
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0start_all.ps1"

pause
