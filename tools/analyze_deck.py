import re

with open('E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/presentasi.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find view containers
view_awam = re.search(r'<div\s+id="view-awam".*?(?=<div\s+id="view-teknis")', html, re.DOTALL)
view_teknis = re.search(r'<div\s+id="view-teknis".*?(?=<div\s+id="view-deck")', html, re.DOTALL)
view_deck = re.search(r'<div\s+id="view-deck".*?(?=<footer\s+id="unified-hud")', html, re.DOTALL)

def count_sections(content):
    if not content:
        return 0, []
    matches = re.findall(r'<section\s+class="slide[^"]*"(\s+id="[^"]*")?', content.group(0))
    return len(matches), matches

c_awam, m_awam = count_sections(view_awam)
c_tek, m_tek = count_sections(view_teknis)
c_deck, m_deck = count_sections(view_deck)

print(f"Awam Slides Count: {c_awam}")
print(f"Teknis Slides Count: {c_tek}")
print(f"Deck Slides Count: {c_deck}")

# Check slide headers and claims in Stage Deck
deck_titles = re.findall(r'<h[12][^>]*>(.*?)</h[12]>', view_deck.group(0) if view_deck else "")
print("\n--- STAGE DECK TITLES ---")
for i, t in enumerate(deck_titles[:15]):
    clean_t = re.sub(r'<[^>]+>', '', t).strip()
    print(f"Slide {i+1}: {clean_t}")

# Check Awam deck titles
awam_titles = re.findall(r'<h[12][^>]*>(.*?)</h[12]>', view_awam.group(0) if view_awam else "")
print("\n--- AWAM DECK TITLES ---")
for i, t in enumerate(awam_titles[:15]):
    clean_t = re.sub(r'<[^>]+>', '', t).strip()
    print(f"Slide {i+1}: {clean_t}")

# Check Teknis deck titles
tek_titles = re.findall(r'<h[12][^>]*>(.*?)</h[12]>', view_teknis.group(0) if view_teknis else "")
print("\n--- TEKNIS DECK TITLES ---")
for i, t in enumerate(tek_titles[:15]):
    clean_t = re.sub(r'<[^>]+>', '', t).strip()
    print(f"Slide {i+1}: {clean_t}")
