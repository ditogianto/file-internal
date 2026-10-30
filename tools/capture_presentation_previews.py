import os
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
HTML_PATH = ROOT / "presentasi.html"
SHOTS_DIR = ROOT / "screenshots"
SHOTS_DIR.mkdir(exist_ok=True)

def main():
    target_url = f"file:///{HTML_PATH.as_posix()}"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        # 1. Home
        print("[*] Capturing Home...")
        page.goto(target_url, wait_until="networkidle")
        time.sleep(0.5)
        page.screenshot(path=str(SHOTS_DIR / "preview_01_home.png"))

        # 2. Awam Cover (Slide 1)
        print("[*] Capturing Cover Awam (Slide 1)...")
        page.goto(f"{target_url}#awam:1", wait_until="networkidle")
        time.sleep(0.5)
        page.screenshot(path=str(SHOTS_DIR / "preview_02_cover_awam.png"))

        # 3. Awam Slide 2
        print("[*] Capturing Awam Slide 2...")
        page.goto(f"{target_url}#awam:2", wait_until="networkidle")
        time.sleep(0.5)
        page.screenshot(path=str(SHOTS_DIR / "preview_awam_02.png"))

        # 4. Stage Deck Slide 1
        print("[*] Capturing Stage Deck Slide 1...")
        page.goto(f"{target_url}#deck:1", wait_until="networkidle")
        time.sleep(0.5)
        page.screenshot(path=str(SHOTS_DIR / "preview_deck_01.png"))

        # 5. Stage Deck Slide 2
        print("[*] Capturing Stage Deck Slide 2...")
        page.goto(f"{target_url}#deck:2", wait_until="networkidle")
        time.sleep(0.5)
        page.screenshot(path=str(SHOTS_DIR / "preview_deck_02.png"))

        # 6. Stage Deck Slide 3
        print("[*] Capturing Stage Deck Slide 3...")
        page.goto(f"{target_url}#deck:3", wait_until="networkidle")
        time.sleep(0.5)
        page.screenshot(path=str(SHOTS_DIR / "preview_deck_03.png"))

        # 7. Stage Deck Slide 4
        print("[*] Capturing Stage Deck Slide 4...")
        page.goto(f"{target_url}#deck:4", wait_until="networkidle")
        time.sleep(0.5)
        page.screenshot(path=str(SHOTS_DIR / "preview_deck_04.png"))

        # 8. Stage Deck Slide 5
        print("[*] Capturing Stage Deck Slide 5...")
        page.goto(f"{target_url}#deck:5", wait_until="networkidle")
        time.sleep(0.5)
        page.screenshot(path=str(SHOTS_DIR / "preview_deck_05.png"))

        # 9. Stage Deck Slide 6
        print("[*] Capturing Stage Deck Slide 6...")
        page.goto(f"{target_url}#deck:6", wait_until="networkidle")
        time.sleep(0.5)
        page.screenshot(path=str(SHOTS_DIR / "preview_deck_06.png"))

        # 10. Stage Deck Slide 7
        print("[*] Capturing Stage Deck Slide 7...")
        page.goto(f"{target_url}#deck:7", wait_until="networkidle")
        time.sleep(0.5)
        page.screenshot(path=str(SHOTS_DIR / "preview_deck_07.png"))

        browser.close()
        print("[+] All screenshots captured successfully!")

if __name__ == "__main__":
    main()
