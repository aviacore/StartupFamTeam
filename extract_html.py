import os
os.chdir('C:\\Users\\User\\Desktop\\CraftStack')

with open('project\\ceo\\ceo-20260528-202537.md', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('```html\n')
if start < 0:
    start = text.find('```html\r\n')
    
end = text.find('\n```', start + 8)
if end < 0:
    end = len(text)

html = text[start+8:end].strip()
print(f'Extracted {len(html)} chars')
print('Has </html>:', '</html>' in html)

with open('project\\ai-hub.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Saved to project/ai-hub.html')
