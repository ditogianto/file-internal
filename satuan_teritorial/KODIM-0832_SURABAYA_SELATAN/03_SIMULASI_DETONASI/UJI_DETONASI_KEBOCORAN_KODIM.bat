@echo off
chcp 65001 >nul
title SIMULASI DETONASI KEBOCORAN - Kodim 0832/Surabaya Selatan
color 0C
cls
echo ========================================================================
echo   PUSSIBERAD TNI AD // SIMULASI DETONASI CANARY TOKEN
echo   Satuan : Kodim 0832/Surabaya Selatan
echo   Induk  : Kodam V/Brawijaya
echo   Token  : doc-0832a.kodim-0832.canary.lan
echo ========================================================================
echo.
echo [*] Mensimulasikan dokumen rahasia dibuka di komputer peretas luar...
echo [*] Mengirimkan paket Out-of-Band UDP DNS Query ke NEXUS-TRAP (Port 5053)...
echo.
powershell -Command "Resolve-DnsName -Name 'doc-0832a.kodim-0832.canary.lan' -Server 127.0.0.1 -Port 5053 -Type A"
echo.
echo ========================================================================
echo [+] DETONASI BERHASIL DIKIRIM!
echo [*] Silakan periksa layar C4ISR Meja Komando (http://localhost:3000):
echo     1. Status bertransisi ke SIAGA 1 MERAH
echo     2. Pin Kodam V/Brawijaya di Peta Operasi NKRI berkedip merah
echo     3. Banner menampilkan: INTERSEPSI AKTIF: Kodim 0832/Surabaya Selatan
echo ========================================================================
echo.
pause
