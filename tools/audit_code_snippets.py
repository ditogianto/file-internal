import re

with open('E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/presentasi.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find code tags
code_tags = re.findall(r'<code[^>]*>(.*?)</code>', text, re.DOTALL)
print(f"Total <code> tags: {len(code_tags)}")

# Search for technical code snippets, terminal displays, command lines
tech_slide_blocks = re.findall(r'<!--\s*SLIDE\s*\d+:\s*(?:INTI TEKNIS|TEKNIS|ARSITEKTUR).*?-->.*?(?=<!--\s*SLIDE|\Z)', text, re.DOTALL)
print(f"Technical slides found: {len(tech_slide_blocks)}")

# Search for any potential leaks:
leak_patterns = [
    (r'(?:api[_-]?key|secret|password|passwd|auth_token|token)\s*[:=]\s*["\']([^"\']+)["\']', "Potential Secret/Token"),
    (r'(?:192\.168\.\d+\.\d+|10\.\d+\.\d+\.\d+|172\.(?:1[6-9]|2\d|3[01])\.\d+\.\d+)', "RFC 1918 Private IP"),
    (r'(?:[1-9]\d{0,2}\.){3}[1-9]\d{0,2}', "Any IP Address"),
    (r'BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY', "Private Key Header"),
    (r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', "Email Address"),
]

for pattern, desc in leak_patterns:
    matches = set(re.findall(pattern, text, re.IGNORECASE))
    print(f"\n[LEAK SCAN] {desc}: {len(matches)} distinct occurrences")
    for m in list(matches)[:10]:
        print(f"   -> {m}")

# Inspect content of technical slides (Mode Teknis)
view_teknis = re.search(r'<div\s+id="view-teknis".*?(?=<div\s+id="view-deck")', text, re.DOTALL)
if view_teknis:
    slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]*)">(.*?)</section>', view_teknis.group(0), re.DOTALL)
    print(f"\n=== INSPECTING {len(slides)} TECHNICAL SLIDES ===")
    for s_id, s_content in slides:
        h2 = re.search(r'<h2[^>]*>(.*?)</h2>', s_content)
        title = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else s_id
        # extract any code or terminal snippets
        snippets = re.findall(r'(?:<code[^>]*>|<div[^>]*font-family:\s*(?:var\(--master-mono\)|monospace)[^>]*>)(.*?)(?:</code>|</div>)', s_content, re.DOTALL)
        clean_snips = [re.sub(r'<[^>]+>', '', snip).strip() for snip in snippets if len(re.sub(r'<[^>]+>', '', snip).strip()) > 15]
        print(f"\n[{s_id}] {title}")
        print(f"   Snippets found: {len(clean_snips)}")
        for cs in clean_snips[:3]:
            first_line = cs.split('\n')[0][:80]
            print(f"      • {first_line}")
