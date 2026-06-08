import os
import re

ROOT = r"e:\vscode\AI知識庫\數位佛堂"
results = {}
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
                        rel = os.path.relpath(root, ROOT)
                        lib = rel.split(os.sep)[0] if rel != "." else "ROOT"
                        if lib not in results: results[lib] = []
                        results[lib].append(path)
                        break
        except Exception:
            pass

mapping = {
    "AI 智者": "AI 智者 (天台)",
    "AI 總論": "AI 總論",
    "AI 禪修": "AI 禪修",
    "AI 阿含": "AI 阿含",
    "AI 般若": "AI 般若",
    "AI 維摩": "AI 維摩",
    "AI 禪法": "AI 禪法"
}

print("--- 礦渣（Data Slag）詳細清單 ---")
for lib, paths in sorted(results.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"\n圖書館: {lib} ({len(paths)} 個)")
    for p in paths[:5]: # Show 5 samples
        print(f"  - {p}")
