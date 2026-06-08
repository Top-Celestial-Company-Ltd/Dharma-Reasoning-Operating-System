import os
import shutil
import sys
import io

# 強制輸出為 UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 設定
WIKI_ROOT = r"E:\vscode\AI知識庫\數位佛堂"
QUARANTINE_DIR = os.path.join(WIKI_ROOT, "Pavilion_Sandbox", "wiki", "quarantine")
DIGITAL_DIR = os.path.join(WIKI_ROOT, "Pavilion_Digital", "wiki", "mapping")

def purify():
    print("="*50)
    print("[DROS v5.2] - FINAL PURIFICATION START")
    print("="*50)
    
    if not os.path.exists(QUARANTINE_DIR): os.makedirs(QUARANTINE_DIR)
    if not os.path.exists(DIGITAL_DIR): os.makedirs(DIGITAL_DIR)
    
    count_tagged = 0
    count_quarantined = 0
    count_digital = 0
    
    for root, dirs, files in os.walk(WIKI_ROOT):
        # 排除備份與已隔離目錄
        if "Backup" in root or "quarantine" in root or "mapping" in root or "Pavilion_Sandbox" in root or "Pavilion_Digital" in root:
            continue
            
        for f in files:
            if f.endswith(".md"):
                file_path = os.path.join(root, f)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                    
                    # 1. 識別數位映射 (Digital Mapping)
                    if "來源: 數位佛堂 v4.0" in content or any(x in f for x in ["AI", "LLM", "模型", "資料庫"]):
                        shutil.move(file_path, os.path.join(DIGITAL_DIR, f))
                        count_digital += 1
                        continue
                    
                    # 2. 識別遺留孤點 (Quarantine)
                    if "狀態: legacy_stub" in content or "來源: 無原文依據" in content:
                        shutil.move(file_path, os.path.join(QUARANTINE_DIR, f))
                        count_quarantined += 1
                        continue
                    
                    # 3. 義理分流標籤 (Panjiao Tagging)
                    new_tags = []
                    if any(x in content for x in ["瑜伽師地論", "成唯識論", "五位百法"]):
                        new_tags.append("唯識")
                    if any(x in content for x in ["大智度論", "中論", "龍樹", "空性"]):
                        new_tags.append("中觀")
                    if any(x in content for x in ["法華經", "天台", "一念三千", "智者"]):
                        new_tags.append("天台")
                    
                    if new_tags:
                        tag_str = "- **宗派**: [" + ", ".join([f'"{t}"' for t in new_tags]) + "]\n"
                        if "- **標籤**:" in content and "- **宗派**:" not in content:
                            new_content = content.replace("- **標籤**:", tag_str + "- **標籤**:")
                            with open(file_path, 'w', encoding='utf-8') as out:
                                out.write(new_content)
                            count_tagged += 1
                except Exception as e:
                    # 忽略已移走的檔案錯誤
                    if not os.path.exists(file_path): continue
                    print(f"  [ERROR] 處理 {f} 失敗: {e}")

    print("\n" + "="*50)
    print("[SUCCESS] PURIFICATION COMPLETE")
    print(f"-> Tagged: {count_tagged} nodes")
    print(f"-> Quarantined: {count_quarantined} nodes")
    print(f"-> Digital Separated: {count_digital} nodes")
    print("="*50)

if __name__ == "__main__":
    purify()
