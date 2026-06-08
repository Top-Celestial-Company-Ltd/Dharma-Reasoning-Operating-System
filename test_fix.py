import os
import re

TARGET_DIR = r"e:\vscode\AI知識庫\數位佛堂\AI 智者\wiki\concepts"
FILES = os.listdir(TARGET_DIR)[:10]

for filename in FILES:
    path = os.path.join(TARGET_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 嚴格修復：確保標籤後面緊跟換行，且義理區塊格式正確
    # 移除任何可能干擾正則的尾隨空格
    content = re.sub(r' +$', '', content, flags=re.MULTILINE)
    
    # 確保核心義理區塊格式
    content = re.sub(r'> \[\!NOTE\] 核心義理.*?\n', '> [!NOTE] 核心義理\n', content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Fixed 10 files: {FILES}")
