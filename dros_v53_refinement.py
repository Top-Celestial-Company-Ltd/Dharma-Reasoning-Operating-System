import os
import re
import shutil
import io
import sys

# 強制輸出為 UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# DROS v5.3 "Land of Purity" Refinement Script
# 針對 NotebookLM 審計報告進行全庫數據淨化 (No-Emoji Edition)

RELEASE_DIR = r"E:\vscode\AI知識庫\DROS_GitHub_Release_v5.2"
CORE_DIR = os.path.join(RELEASE_DIR, "core")
SANDBOX_DIR = os.path.join(RELEASE_DIR, "pavilion", "Pavilion_Sandbox")

# Ensure Sandbox exists
if not os.path.exists(SANDBOX_DIR):
    os.makedirs(SANDBOX_DIR)

# 1. 正則表達式準備
REGEX_LEVEL = re.compile(r"\* \*\*層級\*\* : (\d+)")
REGEX_CBETA_NOISE = [
    re.compile(r"sutra_id:.*"),
    re.compile(r"title:.*《.*》.*"),
    re.compile(r"edition:.*"),
    re.compile(r"status:.*Auto-Validated.*"),
    re.compile(r"//【經文資訊】.*"),
    re.compile(r"//【版本記錄】.*"),
    re.compile(r"發行日期：.*")
]
EMPTY_SHELL_KEYWORDS = ["未出現對.*的明確定義", "並無直接定義", "無法從該段落中提取明確的義理定義", "並無獨立的明確義理定義"]

def refine_node(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except:
        return None, False
    
    new_lines = []
    quarantine = False
    sectarian_tag = None
    
    # 根據資料夾判斷宗派
    if "天台" in file_path: sectarian_tag = "天台宗"
    elif "唯識" in file_path: sectarian_tag = "唯識宗"
    elif "中觀" in file_path or "龍樹" in file_path: sectarian_tag = "中觀學派"
    
    for line in lines:
        # A. 修正層級異常
        match_lv = REGEX_LEVEL.search(line)
        if match_lv:
            lv_val = int(match_lv.group(1))
            if lv_val > 5 or lv_val == 0:
                line = "* **層級** : 3 (Auto-Corrected)\n"
        
        # B. 剔除 CBETA 噪音
        is_noise = any(noise.search(line) for noise in REGEX_CBETA_NOISE)
        if is_noise: continue
        
        # C. 檢查空殼關鍵字
        if any(kw in line for kw in EMPTY_SHELL_KEYWORDS):
            quarantine = True
            
        # D. 檢查 legacy_stub
        if "legacy_stub" in line:
            quarantine = True
            
        # E. 補全缺失的宗派標籤
        if sectarian_tag and "* **宗派** :" in line:
            stripped = line.strip()
            if stripped.endswith(":") or "未知" in line:
                line = f"* **宗派** : {sectarian_tag} (Auto-Tagged)\n"
            
        new_lines.append(line)
        
    return "".join(new_lines), quarantine

def main():
    print("[INFO] DROS v5.3 Purification Started...")
    count_refined = 0
    count_quarantined = 0
    
    for root, dirs, files in os.walk(CORE_DIR):
        for f in files:
            if f.endswith(".md"):
                file_path = os.path.join(root, f)
                new_content, should_quarantine = refine_node(file_path)
                
                if new_content is None: continue
                
                if should_quarantine:
                    # 隔離至沙盒
                    target_path = os.path.join(SANDBOX_DIR, f)
                    try:
                        shutil.move(file_path, target_path)
                        count_quarantined += 1
                    except: pass
                else:
                    # 更新內容
                    with open(file_path, 'w', encoding='utf-8') as out:
                        out.write(new_content)
                    count_refined += 1
                    
    print(f"\n[DONE] Refined Nodes: {count_refined}")
    print(f"[DONE] Quarantined (Sandbox): {count_quarantined}")

if __name__ == "__main__":
    main()
