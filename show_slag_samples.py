import os
import re

ROOT = r"e:\vscode\AI知識庫\數位佛堂\AI 總論"
samples = []
markers = [
    r'Source: "無"',
    r'title: 無',
    r'義理: 無原文依據',
    r'無法判斷.*?原文缺失',
    r'tags: \["未分類"\]'
]

for root, dirs, files in os.walk(ROOT):
    for f in files:
        if not f.endswith(".md"):
            continue
        path = os.path.join(root, f)
        try:
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
                for m in markers:
                    if re.search(m, content):
                        samples.append((path, content))
                        break
        except Exception:
            pass
        if len(samples) >= 3:
            break
    if len(samples) >= 3:
        break

print("--- AI 總論 礦渣樣本 (Top 3) ---")
for path, content in samples:
    print(f"\n[檔案]: {path}")
    print("-" * 20)
    print(content[:500] + "...")
    print("=" * 40)
