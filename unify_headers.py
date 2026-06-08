import os
import re

TARGET_DIR = r"e:\vscode\AI知識庫\數位佛堂\AI 智者\wiki\concepts"

for filename in os.listdir(TARGET_DIR):
    if not filename.endswith(".md"): continue
    path = os.path.join(TARGET_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 轉換 ## 1. 義理定義 為 > [!NOTE] 核心義理
    pattern = r'## 1\. (?:義理定義|義\[\[理定義\]\])\n(.*?)(?=\n##|\Z)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        def_body = match.group(1).strip()
        quoted_body = "\n".join([f"> {line}" if line.strip() else ">" for line in def_body.split("\n")])
        new_block = f"> [!NOTE] 核心義理\n{quoted_body}"
        content = content.replace(match.group(0), new_block)

    # 順便把 ## 2. 經文原句 轉換為 > [!QUOTE] 經文原句
    pattern = r'## 2\. (?:經文原句|經\[\[文原句\]\])\n(.*?)(?=\n##|\Z)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        quote_body = match.group(1).strip()
        quoted_body = "\n".join([f"> {line}" if line.strip() else ">" for line in quote_body.split("\n")])
        new_block = f"> [!QUOTE] 經文原句\n{quoted_body}"
        content = content.replace(match.group(0), new_block)
            
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)

print("Unified headers to DROS 2.0 Callout style.")
