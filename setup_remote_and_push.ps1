# ==============================================================================
# PUSSIBERAD TNI AD - KARTIKA CYBER HACKATHON 2026
# Automated Git Remote Setup & Repository Publication Script
# ==============================================================================

param(
    [Parameter(Mandatory=$false)]
    [string]$RepoUrl = ""
)

Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "  NEXUS-TRAP // AUTOMATED GITHUB REPOSITORY PUBLISHER" -ForegroundColor Green
Write-Host "=================================================================" -ForegroundColor Cyan

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "[ERROR] Git tidak terdeteksi pada sistem. Harap install Git terlebih dahulu." -ForegroundColor Red
    exit 1
}

# Ensure inside repository directory
Set-Location -Path $PSScriptRoot

# Check current status
Write-Host "[1/4] Memeriksa status git lokal..." -ForegroundColor Yellow
git status --short

# Ask for Remote URL if not provided
if ([string]::IsNullOrWhiteSpace($RepoUrl)) {
    Write-Host "`nMasukkan URL repository GitHub/GitLab publik Anda" -ForegroundColor White
    Write-Host "(Contoh: https://github.com/username/nexus-trap-kch2026.git): " -NoNewline -ForegroundColor Green
    $RepoUrl = Read-Host
}

if ([string]::IsNullOrWhiteSpace($RepoUrl)) {
    Write-Host "[ABORT] URL Repository tidak boleh kosong." -ForegroundColor Red
    exit 1
}

# Configure or update origin remote
Write-Host "[2/4] Mengonfigurasi remote 'origin'..." -ForegroundColor Yellow
$existingRemote = git remote get-url origin 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "  Memperbarui origin yang sudah ada: $existingRemote -> $RepoUrl" -ForegroundColor Gray
    git remote set-url origin $RepoUrl
} else {
    Write-Host "  Menambahkan remote origin: $RepoUrl" -ForegroundColor Gray
    git remote add origin $RepoUrl
}

# Stage all files
Write-Host "[3/4] Menambahkan seluruh berkas dan artefak pembaruan..." -ForegroundColor Yellow
git add .
git commit -m "feat(kch2026): complete production-ready release with multi-target firewall export, hotkeys, and video storyboard" -q
if ($LASTEXITCODE -eq 0) {
    Write-Host "  Commit baru berhasil dibuat." -ForegroundColor Green
} else {
    Write-Host "  Semua perubahan telah ter-commit." -ForegroundColor Gray
}

# Push to remote
Write-Host "[4/4] Melakukan push ke branch utama remote origin..." -ForegroundColor Yellow
$currentBranch = (git branch --show-current).Trim()
if ([string]::IsNullOrWhiteSpace($currentBranch)) {
    $currentBranch = "master"
}

git push -u origin $currentBranch
if ($LASTEXITCODE -eq 0) {
    Write-Host "`n=================================================================" -ForegroundColor Green
    Write-Host "  [SUKSES] REPOSITORY BERHASIL DIPUBLIKASIKAN KE GITHUB!" -ForegroundColor Green
    Write-Host "  Tautan Publik : $RepoUrl" -ForegroundColor Cyan
    Write-Host "  Salin tautan di atas ke formulir submission platform Codepolitan!" -ForegroundColor Yellow
    Write-Host "=================================================================" -ForegroundColor Green
} else {
    Write-Host "`n[CATATAN] Push gagal atau membutuhkan otentikasi Git credential." -ForegroundColor Yellow
    Write-Host "Jalankan perintah manual: git push -u origin $currentBranch" -ForegroundColor Gray
}
