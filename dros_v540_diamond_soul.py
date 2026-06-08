import os
import re
import glob

# 核心路徑
path = r'e:\vscode\AI知識庫\DROS_GitHub_Release_v5.2\core'

# 正則表達式設計
# 1. 程式碼殘留清理 (putchar, \n\n\n, 重複 ASCII)
RE_CODE_POLLUTION = re.compile(r"(putchar\s*){3,}|(\\n\s*){5,}|([a-zA-Z0-9_\(\)]\s*){20,}")

# 2. 空值與無意義佔位符清理
RE_EMPTY_CONTENT = re.compile(r"(\(無\)|\(無資料內容\)|無原文依據|文中並未直接提供|無資料|無)$")

# 3. 雙括號連結重複與路徑殘留修復
# 修正 [[ [[ ... ]] ]] 或 [[ ... ]] ]]
RE_NESTED_BRACKETS = re.compile(r"\[\[\s*\[\[(.*?)\]\]\s*\]\]")
RE_TRAILING_BRACKETS = re.compile(r"\]\]\s*\]\]")
# 修正路徑疊加 (重複的書名)
def fix_repetitive_path(text):
    # 找尋重複的經名，如 解深密經解深密經
    match = re.search(r"(\w{4,})\1", text)
    if match:
        return text.replace(match.group(0), match.group(1))
    return text

# 4. IDS 拆字式規範化 (癡[穀-(一/禾)+(夕*ㄗ)] -> 癡【穀-(一/禾)+(夕*ㄗ)】)
RE_IDS = re.compile(r"\[([^\]]{3,})\]")

# 5. 標點過度碎裂修復 (。、， 過多)
def smooth_punctuation(text):
    # 如果兩字內就出現標點，且連續出現 3 次以上，則移除中間的標點
    # 例如：爾時。世尊。從右脅。 -> 爾時世尊從右脅。
    pattern = re.compile(r"(\w{1,2})([。，、])(\w{1,2})([。，、])")
    return pattern.sub(r"\1\3\4", text)

def diamond_soul_process(content):
    modified = False
    lines = content.splitlines()
    new_lines = []
    
    skip_next_block = False
    
    for i, line in enumerate(lines):
        # A. 程式碼殘留清理
        if RE_CODE_POLLUTION.search(line):
            modified = True
            continue # 直接刪除該行
            
        # B. 處理 Markdown 區塊 (Quote/Note)
        if line.startswith("> [!"):
            # 檢查下一行是否為空值或佔位符
            if i + 1 < len(lines):
                next_line = lines[i+1].strip()
                if RE_EMPTY_CONTENT.search(next_line) or next_line == ">" or next_line == "":
                    skip_next_block = True # 標記為跳過整個區塊
                    modified = True
                    continue
            
        if skip_next_block:
            if line.startswith(">"):
                continue
            else:
                skip_next_block = False
        
        # C. 修復路徑疊加與括號
        line = RE_NESTED_BRACKETS.sub(r"[[\1]]", line)
        line = RE_TRAILING_BRACKETS.sub(r"]]", line)
        line = fix_repetitive_path(line)
        line = line.replace("*01-p*", "").replace("*02-p*", "").replace("*03-p*", "")
        
        # D. IDS 規範化
        line = RE_IDS.sub(r"【\1】", line)
        
        # E. 標點平滑化 (僅針對 Quote 內容)
        if line.startswith(">"):
             line = smooth_punctuation(line)
             
        new_lines.append(line)
        
    final_content = "\n".join(new_lines)
    if len(new_lines) != len(lines): modified = True
    
    # 最終標註
    if modified:
        final_content = final_content.replace("Refined-v5.3", "Refined-v5.4 (Diamond Soul)")
        
    return final_content, modified

# 執行全庫掃描
print(f"[INFO] Diamond Soul Purification Started...")
all_files = glob.glob(os.path.join(path, "**", "*.md"), recursive=True)
count = 0

for fp in all_files:
    try:
        with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        new_content, modified = diamond_soul_process(content)
        
        if modified:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
    except: continue

print(f"[DONE] Diamond Soul Refined: {count}")
