import re

with open('E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/presentasi.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="view-teknis"')
end = text.find('id="view-deck"')
teknis_html = text[start:end]

sections = re.findall(r'<section\s+class="slide[^"]*"[^>]*>(.*?)</section>', teknis_html, re.DOTALL)
print(f"Total sections in view-teknis: {len(sections)}")

for i, sec in enumerate(sections):
    h2 = re.search(r'<h2[^>]*>(.*?)</h2>', sec, re.DOTALL)
    h2_text = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else "No H2"
    eyebrow = re.search(r'class="eyebrow"[^>]*>(.*?)</div>', sec, re.DOTALL)
    eb_text = re.sub(r'<[^>]+>', '', eyebrow.group(1)).strip() if eyebrow else "No Eyebrow"
    print(f"\n--- TEKNIS SLIDE {i+1} ---")
    print(f"Eyebrow: {eb_text}")
    print(f"Title: {h2_text}")
    
    # Check for any code or commands in this slide
    codes = re.findall(r'<code[^>]*>(.*?)</code>', sec, re.DOTALL)
    if codes:
        print("  Codes in <code>:")
        for c in codes:
            clean_c = re.sub(r'<[^>]+>', '', c).strip()
            print(f"    - {clean_c}")
            
    # Check for any terminal or monospace blocks
    monos = re.findall(r'font-family:\s*(?:var\(--master-mono\)|monospace)[^>]*>(.*?)</div>', sec, re.DOTALL)
    if monos:
        print("  Monospace snippets:")
        for m in monos:
            clean_m = re.sub(r'<[^>]+>', '', m).strip()
            if len(clean_m) > 10 and '\n' in clean_m:
                print("    [Multiline block]:")
                for line in clean_m.split('\n')[:4]:
                    print(f"      {line[:80]}")
