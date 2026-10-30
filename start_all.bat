@echo off
chcp 65001 >nul
title PUSSIBERAD - NEXUS-TRAP C4ISR PLATFORM
color 0A
cls
echo ===============================================================================
echo      PUSSIBERAD TNI AD // KARTIKA CYBER HACKATHON 2026
echo      NEXUS-TRAP PLATFORM PERTAHANAN SIBER AKTIF
echo ===============================================================================
echo.
echo   [*] Menjalankan Backend Deception Engine ^& Frontend C4ISR War Room...
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0start_all.ps1"
