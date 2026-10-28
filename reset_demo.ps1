# NEXUS-TRAP: Instant Demo Reset Tool
Write-Host "[*] Mengirim sinyal RESET STATE ke Pusat Kendali NEXUS-TRAP..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "http://localhost:8000/api/reset" -Method Post
    Write-Host "[+] SUKSES: Status sistem kembali ke SIAGA HIJAU (Normal)." -ForegroundColor Green
    Write-Host "    - False Positive: $($response.state.metrics.false_positive_rate)" -ForegroundColor Cyan
    Write-Host "    - Tarpit Threads: $($response.state.metrics.locked_threads)" -ForegroundColor Cyan
    Write-Host "    - Status Buronan: $($response.state.adversary_dossier.status)" -ForegroundColor Cyan
} catch {
    Write-Host "[-] Gagal terhubung ke backend http://localhost:8000. Pastikan backend aktif." -ForegroundColor Red
}
