import os
import re
import shutil
import io
import sys

# 強制輸出為 UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# DROS v5.3.2 "Nirvana Shield" Full Coverage Refinement
# 針對所有變體的層級異常、檔名噪音、文本殘留進行全庫大清掃

RELEASE_DIR = r"E:\vscode\AI知識庫\DROS_GitHub_Release_v5.2"
CORE_DIR = os.path.join(RELEASE_DIR, "core")
SANDBOX_DIR = os.path.join(RELEASE_DIR, "pavilion", "Pavilion_Sandbox")

# 1. 激進正則準備 (不限格式)
# 匹配任何包含 "層級" 二字且後接數字的行
REGEX_LEVEL_BROAD = re.compile(r".*層級.*[:：]\s*(\d+)")
REGEX_NESTED_LINK = re.compile(r"\[\[([^\[\]]*?)\[\[([^\[\]]*?)\]\]([^\[\]]*?)\]\]")
REGEX_PADDING_NOISE = re.compile(r"[_]{2,}[-]{2,}.*")
REGEX_CBETA_HEAD = re.compile(r"(--- sutra_id:.*|//【經文資訊】.*|//【版本記錄】.*|發行日期：.*|edition:.*|status:.*Auto-Validated.*)")
REGEX_NULL_VALUE = re.compile(r"\bnull\b", re.IGNORECASE)

EMPTY_SHELL_KEYWORDS = ["未出現對.*的明確定義", "並無直接定義", "無法從該段落中提取明確的義理定義", "核心義理 (無)"]

def ultra_refine_content(content):
    # A. 修復嵌套括號
    while REGEX_NESTED_LINK.search(content):
        content = REGEX_NESTED_LINK.sub(r"[[\1\2\3]]", content)
    
    # B. 掃除文本內的補白噪音與 CBETA 標頭
    content = REGEX_PADDING_NOISE.sub("", content)
    content = REGEX_CBETA_HEAD.sub("", content)
    
    # C. 封殺 null 文本
    content = REGEX_NULL_VALUE.sub("(無資料內容)", content)
    
    return content

def refine_line_logic(line):
    # D. 激進修正層級
    match_lv = REGEX_LEVEL_BROAD.search(line)
    if match_lv:
        lv_val = int(match_lv.group(1))
        if lv_val > 5 or lv_val == 0:
            # 統一重寫為標準格式
            return "* **層級** : 3 (Auto-Corrected)\n"
    return line

def main():
    print("[INFO] DROS v5.3.2 Full Coverage Refinement Started...")
    count_refined = 0
    count_quarantined = 0
    count_renamed = 0
    
    for root, dirs, files in os.walk(CORE_DIR):
        for f in files:
            if f.endswith(".md"):
                file_path = os.path.join(root, f)
                
                # 1. 檔名清洗 (File Renaming)
                new_filename = REGEX_PADDING_NOISE.sub("", f)
                if new_filename != f:
                    new_file_path = os.path.join(root, new_filename)
                    try:
                        os.rename(file_path, new_file_path)
                        file_path = new_file_path
                        count_renamed += 1
                    except: pass
                
                # 2. 內容清洗
                try:
                    with open(file_path, 'r', encoding='utf-8') as f_in:
                        content = f_in.read()
                except: continue
                
                content = ultra_refine_content(content)
                lines = content.splitlines(keepends=True)
                final_lines = []
                should_quarantine = False
                
                for line in lines:
                    line = refine_line_logic(line)
                    if any(kw in line for kw in EMPTY_SHELL_KEYWORDS) or "legacy_stub" in line:
                        should_quarantine = True
                    final_lines.append(line)
                
                final_content = "".join(final_lines)
                
                if should_quarantine:
                    target_path = os.path.join(SANDBOX_DIR, os.path.basename(file_path))
                    try:
                        shutil.move(file_path, target_path)
                        count_quarantined += 1
                    except: pass
                else:
                    with open(file_path, 'w', encoding='utf-8') as out:
                        out.write(final_content)
                    count_refined += 1
                    
    print(f"\n[DONE] Full-Refined Nodes: {count_refined}")
    print(f"[DONE] Files Renamed (Cleaned): {count_renamed}")
    print(f"[DONE] Quarantined to Sandbox: {count_quarantined}")

if __name__ == "__main__":
    main()
