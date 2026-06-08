import os
import re
import sys
import io
import glob

# Force UTF-8 for terminal output
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = r'e:\vscode\AI知識庫\DROS_GitHub_Release_v5.2\core'
count = 0

# 匹配 狀態: verified 的各種變體 (包括 Big5 亂碼)
re_status = re.compile(r"[-*]\s*\*\*.*?\*\*.*?[:：]\s*verified", re.IGNORECASE)
re_level = re.compile(r".*層級.*[:：]\s*(\d+)")

# 使用 glob 進行全域搜索
print(f"[INFO] Scanning {path} for .md files...")
all_files = glob.glob(os.path.join(path, "**", "*.md"), recursive=True)
print(f"[INFO] Found {len(all_files)} files. Starting refinement...")

for fp in all_files:
    try:
        # 1. 讀取原始二進位
        with open(fp, 'rb') as f_bin:
            raw = f_bin.read()
        
        # 2. 優先嘗試 UTF-8，失敗則嘗試 CP950
        try:
            content = raw.decode('utf-8')
        except UnicodeDecodeError:
            content = raw.decode('cp950', errors='ignore')
        
        # 3. 執行替換
        modified = False
        
        # 替換狀態
        if re_status.search(content):
            content = re_status.sub("- **狀態**: Refined-v5.3 (Diamond Purified)", content)
            modified = True
        
        # 替換層級
        lines = content.splitlines()
        new_lines = []
        for line in lines:
            match_lv = re_level.search(line)
            if match_lv:
                lv = int(match_lv.group(1))
                if lv > 5 or lv == 0:
                    new_lines.append("* **層級** : 3 (Diamond Corrected)")
                    modified = True
                    continue
            new_lines.append(line)
        
        if modified:
            content = "\n".join(new_lines)
            with open(fp, 'w', encoding='utf-8') as f_out:
                f_out.write(content)
            count += 1
            
    except Exception as e:
        # 這裡不列印具體檔名，避免編碼崩潰，只記錄錯誤數
        pass

print(f"Final Standardized Nodes: {count}")
