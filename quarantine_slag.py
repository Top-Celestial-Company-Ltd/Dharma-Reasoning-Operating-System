import os
import shutil

ROOT = r"e:\vscode\AI知識庫\數位佛堂"
SLAG_DIR = os.path.join(ROOT, "_slag_archive_")
if not os.path.exists(SLAG_DIR):
    os.makedirs(SLAG_DIR)

markers = [
    r'無原文依據',
    r'無法判斷.*?原文缺失',
    r'title: 無',
    r'Source: "無"',
    r'來源[:：]\s*無'
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
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    is_slag = False
                    for m in markers:
                        if re.search(m, content):
                            is_slag = True
                            break
                    
                    if is_slag:
                        # Move to slag archive
                        dest = os.path.join(SLAG_DIR, f"{os.path.basename(root)}_{filename}")
                        shutil.move(path, dest)
                        slag_count += 1
            except Exception:
                pass

import re # Added missing import

print(f"Total Slag nodes quarantined to _slag_archive_: {slag_count}")
