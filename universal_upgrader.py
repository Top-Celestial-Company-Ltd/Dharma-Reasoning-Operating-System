import os
import re

ROOT = r"e:\vscode\AI知識庫\數位佛堂"

def upgrade_node(content, lib_name):
    # Same logic as before
    yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    metadata = {}
    if yaml_match:
        yaml_content = yaml_match.group(1)
        for line in yaml_content.split("\n"):
            if ":" in line:
                parts = line.split(":", 1)
                metadata[parts[0].strip()] = parts[1].strip().strip('"').strip("'")
        content = content[yaml_match.end():].strip()
    
    if not yaml_match and "##- **層級**:" in content:
        content = re.sub(r'## 1\. (?:義理定義|義\[\[理定義\]\])\n(.*?)(?=\n##|\Z)', 
                         lambda m: f"> [!NOTE] 核心義理\n" + "\n".join([f"> {l}" if l.strip() else ">" for l in m.group(1).strip().split("\n")]), 
                         content, flags=re.DOTALL)
        content = re.sub(r'## 2\. (?:經文原句|經\[\[文原句\]\]|來源|ӷ)\n(.*?)(?=\n##|\Z)', 
                         lambda m: f"> [!QUOTE] 經文原句\n" + "\n".join([f"> {l}" if l.strip() else ">" for l in m.group(1).strip().split("\n")]), 
                         content, flags=re.DOTALL)
        return content

    layer = metadata.get("layer", "3")
    tags = metadata.get("tags", f'["{lib_name}"]')
    source = metadata.get("source", "未知來源")
    status = metadata.get("status", "extracted")
    
    if not tags.startswith("["): tags = f'["{tags}"]'
    header = f"##- **層級**: {layer}\n- **標籤**: {tags}\n- **來源**: {source}\n- **狀態**: {status}\n\n"
    
    content = re.sub(r'## 1\. (?:義理定義|義\[\[理定義\]\])\n(.*?)(?=\n##|\Z)', 
                     lambda m: f"> [!NOTE] 核心義理\n" + "\n".join([f"> {l}" if l.strip() else ">" for l in m.group(1).strip().split("\n")]), 
                     content, flags=re.DOTALL)
    content = re.sub(r'## 2\. (?:來源|ӷ|經文原句|經\[\[文原句\]\])\n(.*?)(?=\n##|\Z)', 
                     lambda m: f"> [!QUOTE] 經文原句\n" + "\n".join([f"> {l}" if l.strip() else ">" for l in m.group(1).strip().split("\n")]), 
                     content, flags=re.DOTALL)

    return header + content

total_processed = 0
# 動態搜尋所有 concepts 目錄
for root, dirs, files in os.walk(ROOT):
    if "concepts" in dirs:
        d = os.path.join(root, "concepts")
        lib_name = os.path.relpath(root, ROOT).split(os.sep)[0]
        print(f"Processing: {lib_name} ({d})")
        for filename in os.listdir(d):
            if not filename.endswith(".md"): continue
            path = os.path.join(d, filename)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = content.lstrip('\ufeff')
                new_content = upgrade_node(content, lib_name)
                with open(path, 'w', encoding='utf-8', newline='\n') as f:
                    f.write(new_content)
                total_processed += 1
            except Exception as e:
                pass

print(f"Total nodes upgraded to DROS 2.0: {total_processed}")
