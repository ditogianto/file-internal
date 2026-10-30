@echo off
chcp 65001 >nul
title [ATTACKER SIMULATOR] SIMULASI SERANGAN SIBER TERHADAP NEXUS-TRAP
color 0C
cls
echo ===============================================================================
echo   [!] SIMULATOR SERANGAN PENYUSUP (ATTACKER BOX - PERSPEKTIF MUSUH)
echo   Target: PUSAT KOMANDO NEXUS-TRAP C4ISR
echo ===============================================================================
echo.
echo   Pastikan Pusat Komando NEXUS-TRAP sudah aktif di browser (http://localhost:3000)
echo   Siapkan perekam layar Anda (Tekan Win + Alt + R untuk rekam)
echo.
echo   Tekan sembarang tombol untuk MEMULAI RENTETAN SERANGAN (Scene 2 s/d 5)...
pause >nul

echo.
echo [*] Memeriksa ketersediaan WSL Ubuntu...
wsl -e uname -a >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [+] WSL Ubuntu terdeteksi. Menjalankan simulasi serangan lintas subnet...
    for /f "tokens=3" %%i in ('wsl ip route ^| findstr default') do set WIN_GATEWAY=%%i
    echo [+] Menyerang Gateway Windows di IP: %WIN_GATEWAY%
    wsl python3 /mnt/e/04_Webdev/59_Cyber-Hackathon/nexus-trap/attacker_box/run_full_accident_scenario.py %WIN_GATEWAY% 5020 5053
) else (
    echo [!] WSL tidak terdeteksi, menjalankan simulasi via Python lokal...
    python "%~dp0attacker_box\run_full_accident_scenario.py" 127.0.0.1 5020 5053
)

echo.
echo ===============================================================================
echo   [SELESAI] Simulasi serangan Scene 2 s/d 5 selesai!
echo   Tekan Win + Alt + R lagi untuk menghentikan perekaman layar.
echo ===============================================================================
pause
