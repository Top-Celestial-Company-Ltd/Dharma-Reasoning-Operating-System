import os
import re

WIKI_DIR = r"E:\vscode\AI知識庫\數位佛堂\AI 智者\wiki\concepts"
LEXICON_FILE = r"E:\vscode\AI知識庫\all_concepts_list.txt"

def load_lexicon():
    with open(LEXICON_FILE, 'r', encoding='utf-8') as f:
        concepts = {line.strip() for line in f if line.strip()}
    return concepts

def auto_link(content, lexicon_set, current_title):
    # 分離 Meta 和正文
    if content.startswith('##- **層級**:'):
        parts = content.split('\n\n# ', 1)
        if len(parts) == 2:
            meta = parts[0]
            body = "\n# " + parts[1]
        else:
            return content
    else:
        meta = ""
        body = content

    # 1. 移除 body 中所有的現有 [[ ]]，進行乾淨重新連結
    body = re.sub(r'\[\[(.*?)\]\]', r'\1', body)
    
    # 2. 提取文中的潛在詞彙
    found_concepts = set()
    for length in range(15, 1, -1):
        for i in range(len(body) - length + 1):
            term = body[i:i+length]
            if term in lexicon_set:
                if term != current_title:
                    found_concepts.add(term)
    
    if not found_concepts:
        return meta + body
        
    candidates = sorted(list(found_concepts), key=len, reverse=True)
    
    # 3. 執行替換 (嚴格跳過所有 Markdown 語法標籤)
    for concept in candidates:
        # 排除清單：不連動這些容易造成噪音的通用詞
        if concept in ["核心", "義理", "來源", "狀態", "標籤", "層級", "經文", "經典", "原句"]:
            continue
            
        # 正則：只在普通文字中替換，不替換已經有 [[ 的，也不替換 [!NOTE] 標題
        pattern = rf'(?<!\[\[)(?<!\!NOTE\] )(?<!\!QUOTE\] ){re.escape(concept)}(?!\]\])'
        body = re.sub(pattern, f'[[{concept}]]', body, count=1)
            
    return meta + body

def fix_format(content, filename):
    # 1. 徹底清除所有舊 Meta 和 YAML
    clean_content = content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            clean_content = parts[2].strip()
    
    # 移除任何 ##- **層級** 到 狀態: verified 的區塊
    clean_content = re.sub(r'##- \*\*層級\*\*.*?\n- \*\*狀態\*\*: verified\n', '', clean_content, flags=re.DOTALL)
    clean_content = clean_content.strip()

    # 2. 構造絕對純淨的 Metadata
    md_meta = f"""##- **層級**: 3
- **標籤**: ["天台宗"]
- **來源**: 天台三大部
- **狀態**: verified"""

    # 3. 確保 核心義理 標題 絕對不含鏈接
    # 先把可能存在的 [[核心]][[義理]] 還原
    clean_content = clean_content.replace('[[核心]]', '核心').replace('[[義理]]', '義理')
    clean_content = re.sub(r'> \[\!NOTE\] .*?核心義理.*?\n', '> [!NOTE] 核心義理\n', clean_content)
    clean_content = re.sub(r'> \[\!QUOTE\] .*?經文原句.*?\n', '> [!QUOTE] 經文原句\n', clean_content)

    return md_meta + "\n\n" + clean_content

def process_all():
    lexicon_set = load_lexicon()
    print(f"[*] 載入辭典：{len(lexicon_set)} 筆")
    
    all_files = [f for f in os.listdir(WIKI_DIR) if f.endswith(".md")]
    total = len(all_files)
    modified = 0
    
    for i, filename in enumerate(all_files):
        file_path = os.path.join(WIKI_DIR, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            new_content = fix_format(content, filename)
            new_content = auto_link(new_content, lexicon_set, os.path.splitext(filename)[0])
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                modified += 1
        except Exception as e:
            print(f"[!] 處理 {filename} 出錯: {e}")
            
        if i % 100 == 0:
            print(f"[*] 已處理 {i}/{total}...")

    print(f"[OK] 處理完成！共修改 {modified}/{total} 個檔案。")

if __name__ == "__main__":
    process_all()
