import re

with open(r'E:\vscode\AI知識庫\數位佛堂\dros_academic_paper_draft.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Locate the parts
pattern = r'(進行強型別約束。)\s*(<div class="full-width" style="page-break-before: always;">.*?</div>)\s*(【圖 2：DROS 執行契約編譯器工作管線與認識論路由】\s*系統將推論邊界物理劃分為三個平行宇宙：.*?不會污染底層知識庫。)'

def replacer(match):
    part1 = match.group(1) # 進行強型別約束。
    part2 = match.group(2) # <div ...>...</div>
    part3 = match.group(3) # 【圖 2...不會污染底層知識庫。
    
    # We want: part1 -> part3 (except the Figure caption) -> part2 -> Figure caption
    # Wait, the Figure caption usually goes under the figure.
    # So we want:
    # part1
    # text about 3 universes
    # part2 (the diagram)
    # Figure 2 caption
    
    text_3_universes = match.group(3).replace('【圖 2：DROS 執行契約編譯器工作管線與認識論路由】\n\n', '')
    caption = '【圖 2：DROS 執行契約編譯器工作管線與認識論路由】'
    
    return f"{part1}\n\n{text_3_universes}\n\n{part2}\n\n{caption}"

new_text = re.sub(pattern, replacer, text, flags=re.DOTALL)

with open(r'E:\vscode\AI知識庫\數位佛堂\dros_academic_paper_draft.md', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Text moved successfully!")
