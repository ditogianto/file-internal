$chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$base = "E:\04_Webdev\59_Cyber-Hackathon\nexus-trap\screenshots"

$slides = @(
    "slide_01_cover.svg",
    "slide_02_paradoks_pondasi.svg",
    "slide_03_filosofi_lonceng_stempel.svg",
    "slide_04_arsitektur_4_pilar.svg",
    "slide_05_koreografi_live_demo.svg",
    "slide_06_purwarupa_c4isr_sitrep.svg",
    "slide_07_kesimpulan_kedaulatan.svg"
)

$idx = 1
foreach ($s in $slides) {
    $num = "{0:d2}" -f $idx
    $svgPath = Join-Path $base $s
    $pngPath = Join-Path $base ("slide_" + $num + ".png")
    $url = "file:///" + $svgPath.Replace("\", "/")
    Write-Host "Rendering $s to slide_$num.png..."
    Start-Process -FilePath $chrome -ArgumentList @("--headless=new", "--disable-gpu", "--window-size=1920,1080", "--screenshot=$pngPath", $url) -Wait
    $idx++
}

Write-Host "Render Complete!"
Get-ChildItem -Path $base -Filter "slide_*.png" | Select-Object Name, Length, LastWriteTime
