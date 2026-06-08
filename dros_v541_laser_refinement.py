import os
import re
import glob

# 核心路徑
path = r'e:\vscode\AI知識庫\DROS_GitHub_Release_v5.2\core'

# 1. 激進清理正則
RE_CODE_POLLUTION = re.compile(r"putchar|printf|scanf|\\n\\n|#include", re.IGNORECASE)
RE_CLEAN_PATH = re.compile(r"\*[0-9]{2}-p\*|]]\s*]]|\[\[\s*\[\[")
RE_EMPTY_MARK = re.compile(r"\(無\)|無原文依據|無資料|無內容|文中並未直接提供")

def refine_soul_v541(content):
    modified = False
    lines = content.splitlines()
    new_lines = []
    
    in_polluted_block = False
    
    for i, line in enumerate(lines):
        # A. 程式碼殘留偵測
        if RE_CODE_POLLUTION.search(line) and (">" in line or "##" in line):
            modified = True
            continue
            
        # B. 雙括號與路徑殘留 (激進替換)
        original_line = line
        line = line.replace("]] ]]", "]]").replace("[[ [[", "[[")
        line = re.sub(r"\]\]\s*\]\]", "]]", line)
        line = re.sub(r"\[\[\s*\[\[", "[[", line)
        line = re.sub(r"\*[0-9]{2}-p\*", "", line)
        line = re.sub(r"_\s*\[\[", "[[", line)
        line = re.sub(r"\]\]\s*_", "]]", line)
        
        # C. 修復重複經名 (解深密經解深密經 -> 解深密經)
        # 匹配 4 個字以上的重複字串
        line = re.sub(r"(.{4,})\1", r"\1", line)
        
        if line != original_line:
            modified = True
            
        # D. 空區塊抑制
        if line.startswith("> [!"):
            if i + 1 < len(lines) and RE_EMPTY_MARK.search(lines[i+1]):
                in_polluted_block = True
                modified = True
                continue
        
        if in_polluted_block:
            if line.startswith(">"):
                continue
            else:
                in_polluted_block = False
        
        # E. 標點平滑化 (針對經文原句)
        if line.startswith(">"):
            # 將 [[爾時]]。[[世尊]]。 轉為 [[爾時]]、[[世尊]]。
            line = line.replace("]]。", "]]、").replace("]]，", "]]、")
            if line.endswith("]]、"): line = line[:-1] + "]]。"
            if line != original_line: modified = True
            
        new_lines.append(line)
        
    final_content = "\n".join(new_lines)
    
    # 強制重置狀態
    if modified:
        # 不論原本是什麼，統一改為 Refined-v5.4
        final_content = re.sub(r"\*\*狀態\*\*.*", "**狀態**: Refined-v5.4 (Diamond Soul)", final_content)
        
    return final_content, modified

print(f"[INFO] Diamond Soul v5.4.1 (Laser) Started...")
all_files = glob.glob(os.path.join(path, "**", "*.md"), recursive=True)
count = 0

for fp in all_files:
    try:
        with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        new_content, modified = refine_soul_v541(content)
        
        if modified:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
    except: continue

print(f"[DONE] Diamond Soul v5.4.1 Refined: {count}")
