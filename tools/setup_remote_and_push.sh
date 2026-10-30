#!/usr/bin/env bash
# ==============================================================================
# PUSSIBERAD TNI AD - KARTIKA CYBER HACKATHON 2026
# Automated Git Remote Setup & Repository Publication Script (Linux / macOS)
# ==============================================================================

set -e

REPO_URL="$1"

echo "================================================================="
echo "  NEXUS-TRAP // AUTOMATED GITHUB REPOSITORY PUBLISHER"
echo "================================================================="

if ! command -v git &> /dev/null; then
    echo "[ERROR] Git tidak terinstal. Harap pasang git terlebih dahulu."
    exit 1
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." >/dev/null 2>&1 && pwd )"
cd "$DIR"

echo "[1/4] Memeriksa status git lokal..."
git status --short

if [ -z "$REPO_URL" ]; then
    echo ""
    read -p "Masukkan URL repository GitHub/GitLab publik Anda (cth: https://github.com/user/nexus-trap.git): " REPO_URL
fi

if [ -z "$REPO_URL" ]; then
    echo "[ABORT] URL Repository tidak boleh kosong."
    exit 1
fi

echo "[2/4] Mengonfigurasi remote 'origin'..."
if git remote get-url origin > /dev/null 2>&1; then
    git remote set-url origin "$REPO_URL"
else
    git remote add origin "$REPO_URL"
fi

echo "[3/4] Menambahkan seluruh berkas dan artefak pembaruan..."
git add .
git commit -m "feat(kch2026): complete production-ready release with multi-target firewall export, hotkeys, and video storyboard" || true

echo "[4/4] Melakukan push ke branch utama remote origin..."
CURRENT_BRANCH=$(git branch --show-current)
if [ -z "$CURRENT_BRANCH" ]; then
    CURRENT_BRANCH="master"
fi

git push -u origin "$CURRENT_BRANCH" || {
    echo "[CATATAN] Harap lakukan push manual dengan kredensial Anda: git push -u origin $CURRENT_BRANCH"
    exit 0
}

echo "================================================================="
echo "  [SUKSES] REPOSITORY BERHASIL DIPUBLIKASIKAN KE GITHUB!"
echo "  Tautan Publik : $REPO_URL"
echo "================================================================="
