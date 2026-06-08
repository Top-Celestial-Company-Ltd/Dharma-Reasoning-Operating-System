import os

ROOT = r"e:\vscode\AI知識庫\數位佛堂"
LEXICON_PATH = r"e:\vscode\AI知識庫\all_concepts_list.txt"

# 1. 載入當前 Wiki 所有節點
wiki_nodes = set()
for root, dirs, files in os.walk(ROOT):
    if "concepts" in root: # 確保在 concepts 目錄下
        for f in files:
            if f.endswith(".md"):
                wiki_nodes.add(f[:-3])

print(f"[*] 當前 Wiki 實體節點數: {len(wiki_nodes)}")

# 2. 載入辭典 (黃金名相清單)
with open(LEXICON_PATH, 'r', encoding='utf-8') as f:
    lexicon = {line.strip() for line in f if line.strip()}

print(f"[*] 黃金辭典總量: {len(lexicon)}")

# 3. 計算缺口
gaps = lexicon - wiki_nodes
print(f"[*] 發現缺口數 (辭典有但 Wiki 沒有): {len(gaps)}")

# 4. 輸出前 100 個缺口樣本供檢視
sorted_gaps = sorted(list(gaps))
print("\n--- 缺口樣本 (Top 100) ---")
for i in range(min(100, len(sorted_gaps))):
    print(f"{i+1}. {sorted_gaps[i]}")
