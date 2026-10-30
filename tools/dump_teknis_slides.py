import re

with open('E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/presentasi.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="view-teknis"')
end = text.find('id="view-deck"')
teknis_html = text[start:end]

sections = re.findall(r'<section\s+class="slide[^"]*"[^>]*>(.*?)</section>', teknis_html, re.DOTALL)

for i in [1, 2, 3, 4, 5, 6, 7, 9]:  # 0-indexed: slides 2, 3, 4, 5, 6, 7, 8, 10
    sec = sections[i]
    clean_text = re.sub(r'<style.*?</style>', '', sec, flags=re.DOTALL)
    clean_text = re.sub(r'<[^>]+>', ' ', clean_text)
    clean_text = ' '.join(clean_text.split())
    print(f"\n==================== TEKNIS SLIDE {i+1} ====================")
    print(clean_text[:500] + "...")
