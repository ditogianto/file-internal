import re

with open('E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/presentasi.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="view-deck"')
end = text.find('id="unified-hud"')
deck_html = text[start:end]

sections = re.findall(r'<section\s+class="slide[^"]*"[^>]*>(.*?)</section>', deck_html, re.DOTALL)
print(f"Total sections in view-deck: {len(sections)}")

for i, sec in enumerate(sections):
    h2 = re.search(r'<h[12][^>]*>(.*?)</h[12]>', sec, re.DOTALL)
    h2_text = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else "No Title"
    eyebrow = re.search(r'class="stage-eyebrow"[^>]*>(.*?)</div>', sec, re.DOTALL)
    eb_text = re.sub(r'<[^>]+>', '', eyebrow.group(1)).strip() if eyebrow else "No Eyebrow"
    print(f"\n--- STAGE DECK SLIDE {i+1} ---")
    print(f"Eyebrow: {eb_text}")
    print(f"Title: {h2_text}")
    
    # Check for any code or commands
    codes = re.findall(r'<code[^>]*>(.*?)</code>', sec, re.DOTALL)
    if codes:
        print("  Codes in <code>:")
        for c in codes:
            clean_c = re.sub(r'<[^>]+>', '', c).strip()
            print(f"    - {clean_c}")
