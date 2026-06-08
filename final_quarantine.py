import os
import shutil

ROOT = r"e:\vscode\AI知識庫\數位佛堂"
SLAG_DIR = os.path.join(ROOT, "_slag_archive_")
if not os.path.exists(SLAG_DIR):
    os.makedirs(SLAG_DIR)

# 這些是我們定義為「礦渣」的特徵字串
MARKERS = [
    "無原文依據",
    "無法判斷，原文缺失",
    "Source: \"無\"",
    "title: 無"
]

slag_count = 0
for root, dirs, files in os.walk(ROOT):
    if "_slag_archive_" in root: continue
    if "concepts" in dirs:
        d = os.path.join(root, "concepts")
        for filename in os.listdir(d):
            if not filename.endswith(".md"): continue
            path = os.path.join(d, filename)
            try:
                # 使用 utf-8-sig 處理 BOM，避免匹配失敗
                with open(path, "r", encoding="utf-8-sig") as f:
                    content = f.read()
                    found = False
                    for m in MARKERS:
                        if m in content:
                            found = True
                            break
                    
                    if found:
                        # 執行隔離
                        rel_path = os.path.relpath(root, ROOT).replace(os.sep, "_")
                        dest_name = f"{rel_path}_{filename}"
                        shutil.move(path, os.path.join(SLAG_DIR, dest_name))
                        slag_count += 1
            except Exception as e:
                print(f"Error moving {filename}: {e}")

print(f"DONE: Quarantined {slag_count} slag nodes.")
