import os
import shutil

src_dir = 'E:/04_Webdev/59_Cyber-Hackathon/nexus-trap'
dest_dir = 'E:/04_Webdev/59_Cyber-Hackathon/web_presentation'

os.makedirs(dest_dir, exist_ok=True)

files_to_copy = [
    ('presentasi.html', 'index.html'),
    ('presentasi.html', 'presentasi.html'),
    ('qr_download_file_internal.svg', 'qr_download_file_internal.svg'),
    ('qr_download_file_internal.png', 'qr_download_file_internal.png'),
    ('qr_github_repo.png', 'qr_github_repo.png'),
    ('QR_DOWNLOAD_FILE_INTERNAL.html', 'QR_DOWNLOAD_FILE_INTERNAL.html'),
    ('Rahasia_Dislokasi_Pasukan_2026.docx', 'Rahasia_Dislokasi_Pasukan_2026.docx'),
]

for src_name, dest_name in files_to_copy:
    src_file = os.path.join(src_dir, src_name)
    dest_file = os.path.join(dest_dir, dest_name)
    if os.path.exists(src_file):
        shutil.copy2(src_file, dest_file)
        print(f"Copied: {src_name} -> {dest_name}")
    else:
        print(f"WARNING: Source file not found: {src_file}")

print("Folder setup complete!")
