import os
import re
import json

# 設定路徑
ROOT_DIR = r"E:\vscode\AI知識庫\數位佛堂"
LEXICON_PATH = r"E:\vscode\AI知識庫\all_concepts_list.txt"
OUTPUT_REPORT = r"E:\vscode\AI知識庫\數位佛堂\missing_concepts_report.json"

def load_lexicon():
    chinese_pattern = re.compile(r'^[\u4e00-\u9fa5]{2,10}$')
    with open(LEXICON_PATH, 'r', encoding='utf-8', errors='ignore') as f:
        terms = {line.strip() for line in f if chinese_pattern.match(line.strip())}
    return terms

def get_existing_nodes():
    nodes = set()
    for root, dirs, files in os.walk(ROOT_DIR):
        if "wiki" in root.lower() and "concepts" in root.lower():
            for f in files:
                if f.endswith(".md"):
                    nodes.add(f[:-3])
    return nodes

def run_audit():
    lexicon = load_lexicon()
    existing = get_existing_nodes()
    print(f"[*] 已載入辭典: {len(lexicon)}, 現有節點: {len(existing)}")
    
    raw_files = []
    for root, dirs, files in os.walk(ROOT_DIR):
        if "raw" in root.lower():
            for f in files:
                if f.endswith((".md", ".txt")):
                    raw_files.append(os.path.join(root, f))
    
    missing_hits = {}
    candidates = lexicon - existing
    print(f"[*] 待掃描缺口候選: {len(candidates)}")
    
    # 為了效能，我們只掃描前 2000 個候選（這已經涵蓋了絕大多數高頻詞）
    # 或者我們反向操作：掃描文本，看看哪些詞出現了
    
    for i, file_path in enumerate(raw_files[:50]): # 先掃描前 50 個重要檔案
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            for term in candidates:
                if term in content:
                    missing_hits[term] = missing_hits.get(term, 0) + content.count(term)
        except:
            continue
        if i % 10 == 0: print(f"[*] 掃描進度: {i}/50")

    sorted_missing = sorted(missing_hits.items(), key=lambda x: x[1], reverse=True)
    
    report = {
        "summary": {
            "lexicon_size": len(lexicon),
            "existing_nodes": len(existing),
            "missing_count": len(sorted_missing)
        },
        "top_missing": sorted_missing[:1000]
    }
    
    with open(OUTPUT_REPORT, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"[OK] 報告已生成：{OUTPUT_REPORT}")

if __name__ == "__main__":
    run_audit()
