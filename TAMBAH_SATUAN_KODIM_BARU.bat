@echo off
chcp 65001 >nul
title PUSSIBERAD - GENERATOR SATUAN KODIM BARU
color 0A
cls
echo ===============================================================================
echo      PUSSIBERAD TNI AD // KARTIKA CYBER HACKATHON 2026
echo      NEXUS-TRAP: SISTEM PERTAHANAN AKTIF & DECEPTION BERKAS
echo ===============================================================================
echo.
echo   [!] Modul ini membuat paket berkas umpan resmi dan mendaftarkan Satuan
echo       Kodim baru ke dalam Pusat Komando secara OTOMATIS TANPA COMPILE ULANG.
echo.
echo ===============================================================================
echo.

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Python tidak ditemukan di PATH sistem.
    echo Pastikan Python 3 sudah terpasang.
    pause
    exit /b 1
)

python tools\generator_satuan_kodim.py

echo.
echo ===============================================================================
echo  Paket berkas umpan tersimpan di folder:
echo  - \satuan_teritorial\
echo.
echo  Anda dapat membuka folder satuan tersebut dan menjalankan skrip simulasi:
echo  - TEST_DETONASI_XXXX.bat
echo ===============================================================================
echo.
pause
