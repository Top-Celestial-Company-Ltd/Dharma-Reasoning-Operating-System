import os

ROOT = r"e:\vscode\AI知識庫\數位佛堂"
concept_dirs = []

for root, dirs, files in os.walk(ROOT):
    if "concepts" in dirs:
        concept_dirs.append(os.path.join(root, "concepts"))

print("--- 發現所有 Concepts 目錄 ---")
for d in concept_dirs:
    count = len([f for f in os.listdir(d) if f.endswith(".md")])
    print(f"路徑: {d:60} | 節點數: {count}")
