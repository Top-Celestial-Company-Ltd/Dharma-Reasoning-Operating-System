import os
import re
import shutil
import io
import sys

# 強制輸出為 UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

RELEASE_DIR = r"E:\vscode\AI知識庫\DROS_GitHub_Release_v5.2"
CORE_DIR = os.path.join(RELEASE_DIR, "core")
SANDBOX_DIR = os.path.join(RELEASE_DIR, "pavilion", "Pavilion_Sandbox")

# 1. 精準清洗規則 (v5.3.3)
REGEX_LEVEL_BROAD = re.compile(r".*層級.*[:：]\s*(\d+)")
REGEX_NESTED_LINK = re.compile(r"\[\[([^\[\]]*?)\[\[([^\[\]]*?)\]\]([^\[\]]*?)\]\]")
REGEX_CBETA_HEAD = re.compile(r"(--- sutra_id:.*|//【經文資訊】.*|//【版本記錄】.*|//【編輯說明】.*|發行日期：.*|edition:.*|status:.*Auto-Validated.*|--- title:.*)")
REGEX_YAML_BLOCK = re.compile(r"^---[\s\S]*?---", re.MULTILINE) # 針對大寶積這種整塊 YAML 的
REGEX_NULL_VALUE = re.compile(r"\b(null|無資料內容|無明確定義|無法從該段落中提取明確的義理定義)\b", re.IGNORECASE)

# 2. AI 幻覺關鍵字 (隔離名單)
QUARANTINE_KEYWORDS = [
    "文中並未直接提供", "未對.*進行具體解釋", "未直接找到支持", "無法從提供的文字中提取", 
    "核心義理 (無)", "legacy_stub", "試驗性數據"
]

def ultra_purify(content):
    modified = False
    original_content = content
    
    # A. 移除 YAML/CBETA 標頭 (針對經文原句內的滲透)
    # 我們只在 [!QUOTE] 區塊內或內容開頭執行此操作，避免誤刪 Metadata
    if "--- sutra_id:" in content or "//【" in content:
        content = REGEX_CBETA_HEAD.sub("", content)
        content = REGEX_YAML_BLOCK.sub("", content)
        modified = True

    # B. 修復層級 (103, 85, 83 -> 3)
    lines = content.splitlines()
    new_lines = []
    for line in lines:
        match_lv = REGEX_LEVEL_BROAD.search(line)
        if match_lv:
            lv_val = int(match_lv.group(1))
            if lv_val > 5 or lv_val == 0:
                new_lines.append("* **層級** : 3 (Refined)")
                modified = True
                continue
        
        # C. 狀態重置 (符合閣主建議)
        if "status: Auto-Validated" in line and modified:
            new_lines.append("- **狀態**: Refined-v5.3")
            continue
            
        new_lines.append(line)
    
    content = "\n".join(new_lines)
    
    # D. 嵌套連結與 NULL 處理
    while REGEX_NESTED_LINK.search(content):
        content = REGEX_NESTED_LINK.sub(r"[[\1\2\3]]", content)
        modified = True
        
    if REGEX_NULL_VALUE.search(content):
        content = REGEX_NULL_VALUE.sub("(無資料內容)", content)
        modified = True
        
    return content, modified

def main():
    print("[INFO] DROS v5.3.3 Final Purifier Started...")
    count_refined = 0
    count_quarantined = 0
    
    for root, dirs, files in os.walk(CORE_DIR):
        for f in files:
            if f.endswith(".md"):
                file_path = os.path.join(root, f)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f_in:
                        content = f_in.read()
                except: continue
                
                # 判斷是否需要隔離 (AI 幻覺或 stub)
                if any(kw in content for kw in QUARANTINE_KEYWORDS):
                    target_path = os.path.join(SANDBOX_DIR, f)
                    try:
                        shutil.move(file_path, target_path)
                        count_quarantined += 1
                        continue
                    except: pass
                
                # 執行淨化
                new_content, was_modified = ultra_purify(content)
                
                if was_modified:
                    with open(file_path, 'w', encoding='utf-8') as out:
                        out.write(new_content)
                    count_refined += 1
                    
    print(f"\n[DONE] Final Refined: {count_refined}")
    print(f"[DONE] Final Quarantined: {count_quarantined}")

if __name__ == "__main__":
    main()
