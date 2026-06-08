import os
import re

ROOT = r"e:\vscode\AI知識庫\數位佛堂"
MARKERS = ["無原文依據", "無法判斷，原文缺失", "Source: \"無\"", "title: 無"]

results = {}

for root, dirs, files in os.walk(ROOT):
    if "_slag_archive_" in root: continue
    if "concepts" in dirs:
        d = os.path.join(root, "concepts")
        for filename in os.listdir(d):
            if not filename.endswith(".md"): continue
            path = os.path.join(d, filename)
            try:
                with open(path, "r", encoding="utf-8-sig") as f:
                    content = f.read()
                    for m in MARKERS:
                        if m in content:
                            lib = os.path.relpath(root, ROOT).split(os.sep)[0]
                            if lib not in results: results[lib] = 0
                            results[lib] += 1
                            break
            except:
                pass

print("--- 礦渣（Slag）統計報告 ---")
total = 0
for lib, count in results.items():
    print(f"圖書館: {lib:20} | 礦渣數: {count}")
    total += count
print(f"\n總計應移除節點: {total}")
