import os
import re
import shutil
import io
import sys

# 強制輸出為 UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# DROS v5.3.1 "Land of Purity" Ultra-Refinement
# 針對 LM 深度掃描報告，修復：嵌套括號、底線補白、Null 值溢出

RELEASE_DIR = r"E:\vscode\AI知識庫\DROS_GitHub_Release_v5.2"
CORE_DIR = os.path.join(RELEASE_DIR, "core")
SANDBOX_DIR = os.path.join(RELEASE_DIR, "pavilion", "Pavilion_Sandbox")

# 1. 精準過濾器
REGEX_LEVEL = re.compile(r"\* \*\*層級\*\* : (\d+)")
REGEX_NESTED_LINK = re.compile(r"\[\[([^\[\]]*?)\[\[([^\[\]]*?)\]\]([^\[\]]*?)\]\]") # 匹配 [[A[[B]]C]]
REGEX_PADDING_NOISE = re.compile(r"[_]{3,}[-]{3,}.*") # 匹配 ___----------
REGEX_NULL_VALUE = re.compile(r"\bnull\b", re.IGNORECASE)

EMPTY_SHELL_KEYWORDS = ["未出現對.*的明確定義", "並無直接定義", "無法從該段落中提取明確的義理定義", "並無獨立的明確義理定義", "核心義理 (無)"]

def ultra_refine(content):
    # A. 修復嵌套括號 (遞迴處理直到沒有嵌套)
    while REGEX_NESTED_LINK.search(content):
        content = REGEX_NESTED_LINK.sub(r"[[\1\2\3]]", content)
    
    # B. 掃除底線與補白噪音
    content = REGEX_PADDING_NOISE.sub("", content)
    
    # C. 封殺 null 文本
    content = REGEX_NULL_VALUE.sub("(無資料內容)", content)
    
    return content

def refine_line_logic(line, sectarian_tag):
    # D. 修正層級異常
    match_lv = REGEX_LEVEL.search(line)
    if match_lv:
        lv_val = int(match_lv.group(1))
        if lv_val > 5 or lv_val == 0:
            return "* **層級** : 3 (Auto-Corrected)\n"
    
    # E. 補全宗派標籤
    if sectarian_tag and "* **宗派** :" in line:
        stripped = line.strip()
        if stripped.endswith(":") or "未知" in line:
            return f"* **宗派** : {sectarian_tag} (Auto-Tagged)\n"
            
    return line

def main():
    print("[INFO] DROS v5.3.1 Ultra-Refinement Started...")
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
                
                # 執行全局超微過濾
                new_content = ultra_refine(content)
                
                # 執行逐行邏輯
                sectarian_tag = None
                if "天台" in file_path: sectarian_tag = "天台宗"
                elif "唯識" in file_path: sectarian_tag = "唯識宗"
                elif "中觀" in file_path or "龍樹" in file_path: sectarian_tag = "中觀學派"
                
                lines = new_content.splitlines(keepends=True)
                final_lines = []
                should_quarantine = False
                
                for line in lines:
                    line = refine_line_logic(line, sectarian_tag)
                    # 檢查隔離條件
                    if any(kw in line for kw in EMPTY_SHELL_KEYWORDS) or "legacy_stub" in line:
                        should_quarantine = True
                    final_lines.append(line)
                
                final_content = "".join(final_lines)
                
                if should_quarantine:
                    target_path = os.path.join(SANDBOX_DIR, f)
                    try:
                        shutil.move(file_path, target_path)
                        count_quarantined += 1
                    except: pass
                else:
                    with open(file_path, 'w', encoding='utf-8') as out:
                        out.write(final_content)
                    count_refined += 1
                    
    print(f"\n[DONE] Ultra-Refined Nodes: {count_refined}")
    print(f"[DONE] Quarantined to Sandbox: {count_quarantined}")

if __name__ == "__main__":
    main()
