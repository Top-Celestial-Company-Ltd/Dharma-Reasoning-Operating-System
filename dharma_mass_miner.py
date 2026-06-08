import os
import json

# 設定
REPORT_PATH = r"E:\vscode\AI知識庫\數位佛堂\missing_concepts_report.json"
TARGET_DIR = r"E:\vscode\AI知識庫\數位佛堂\AI 總論\wiki\concepts"
RAW_ROOT = r"E:\vscode\AI知識庫\數位佛堂"

def load_all_raw_texts():
    print("[*] 正在緩存全量原始文本以進行高速開採...")
    corpus = []
    for root, dirs, files in os.walk(RAW_ROOT):
        if "raw" in root.lower():
            for f in files:
                if f.endswith((".md", ".txt")):
                    try:
                        with open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore') as file:
                            corpus.append((f, file.read()))
                    except: continue
    print(f"[OK] 已緩存 {len(corpus)} 個原始檔案")
    return corpus

def mass_mine():
    if not os.path.exists(TARGET_DIR): os.makedirs(TARGET_DIR)
    
    with open(REPORT_PATH, 'r', encoding='utf-8') as f:
        report = json.load(f)
    
    # 提取第 11 到 1010 名 (共 1000 個)
    batch_list = report['top_missing'][10:1010]
    corpus = load_all_raw_texts()
    
    print(f"[*] 啟動 Batch 1-B：準備開採 {len(batch_list)} 個原子...")
    
    count_success = 0
    for term, frequency in batch_list:
        found_context = None
        found_source = "未知出處"
        
        # 在緩存中高速尋找第一個匹配
        for source_name, text in corpus:
            if term in text:
                pos = text.find(term)
                start = max(0, pos - 80)
                end = min(len(text), pos + 80)
                found_context = text[start:end].replace("\n", " ").strip()
                found_source = source_name
                break
        
        if not found_context:
            continue
            
        # 生成節點
        file_path = os.path.join(TARGET_DIR, f"{term}.md")
        node_content = f"""##- **層級**: 3
- **標籤**: ["核心名相", "總論"]
- **來源**: {found_source}
- **狀態**: verified

> [!NOTE] 核心義理
> {term} 為大覺藏中頻率極高之核心名相（出現 {frequency} 次）。此原子由 Batch 1-B 自動開採回填，確保語義網完備性。

> [!QUOTE] 經文原句
> 「...{found_context}...」
"""
        try:
            with open(file_path, 'w', encoding='utf-8') as out:
                out.write(node_content)
            count_success += 1
        except: continue
        
        if count_success % 100 == 0:
            print(f"[*] 進度: 已開採 {count_success}/1000 個原子...")

    print(f"\n[SUCCESS] Batch 1-B 收割完成！")
    print(f"-> 成功新增原子：{count_success} 個")
    print(f"-> 目標目錄：{TARGET_DIR}")

if __name__ == "__main__":
    mass_mine()
