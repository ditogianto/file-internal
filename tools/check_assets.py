import re

with open('E:/04_Webdev/59_Cyber-Hackathon/nexus-trap/presentasi.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = set(re.findall(r'(?:src|href)=[\'"]([^\'"]+\.(?:png|svg|jpg|jpeg|css|js|docx|html))[\'"]', text))
for m in sorted(matches):
    print(m)
