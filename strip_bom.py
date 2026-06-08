import os

TARGET_DIR = r"e:\vscode\AI知識庫\數位佛堂\AI 智者\wiki\concepts"

for filename in os.listdir(TARGET_DIR):
    if not filename.endswith(".md"): continue
    path = os.path.join(TARGET_DIR, filename)
    
    # 使用 utf-8-sig 讀取 (會自動去掉 BOM)
    with open(path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    # 使用 utf-8 寫回 (純 UTF-8，無 BOM)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)

print("All files converted to Pure UTF-8 (No BOM).")
