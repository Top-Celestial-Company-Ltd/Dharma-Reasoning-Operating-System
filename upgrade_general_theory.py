import os
import re

TARGET_DIR = r"e:\vscode\AI知識庫\數位佛堂\AI 總論\wiki\concepts"

def upgrade_node(content):
    # 1. 處理 YAML Frontmatter
    yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    metadata = {}
    if yaml_match:
        yaml_content = yaml_match.group(1)
        # 簡單解析 YAML
        for line in yaml_content.split("\n"):
            if ":" in line:
                key, val = line.split(":", 1)
                metadata[key.strip()] = val.strip().strip('"').strip("'")
        
        # 移除 YAML 區塊
        content = content[yaml_match.end():].strip()
    
    # 2. 構建 DROS 2.0 標頭
    # 預設值
    layer = metadata.get("layer", "3")
    tags = metadata.get("tags", '["總論"]')
    source = metadata.get("source", "未知來源")
    status = metadata.get("status", "extracted")
    
    # 格式化 tags (如果是 ["a", "b"] 字串)
    if not tags.startswith("["):
        tags = f'["{tags}"]'
        
    header = f"##- **層級**: {layer}\n"
    header += f"- **標籤**: {tags}\n"
    header += f"- **來源**: {source}\n"
    header += f"- **狀態**: {status}\n\n"
    
    # 3. 轉換區塊標題
    # 義理定義 -> [!NOTE] 核心義理
    content = re.sub(r'## 1\. (?:義理定義|義\[\[理定義\]\])\n(.*?)(?=\n##|\Z)', 
                     lambda m: f"> [!NOTE] 核心義理\n" + "\n".join([f"> {l}" if l.strip() else ">" for l in m.group(1).strip().split("\n")]), 
                     content, flags=re.DOTALL)
    
    # 來源 -> [!QUOTE] 經文原句 (暫時將舊的來源描述放入 QUOTE 區塊，等待後續重採集補強)
    content = re.sub(r'## 2\. (?:來源|ӷ)\n(.*?)(?=\n##|\Z)', 
                     lambda m: f"> [!QUOTE] 經文原句\n" + "\n".join([f"> {l}" if l.strip() else ">" for l in m.group(1).strip().split("\n")]), 
                     content, flags=re.DOTALL)

    return header + content

if not os.path.exists(TARGET_DIR):
    print(f"Error: Directory not found: {TARGET_DIR}")
else:
    count = 0
    for filename in os.listdir(TARGET_DIR):
        if not filename.endswith(".md"): continue
        path = os.path.join(TARGET_DIR, filename)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 移除 BOM
            content = content.lstrip('\ufeff')
            
            # 執行升級
            new_content = upgrade_node(content)
            
            with open(path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(new_content)
            count += 1
        except Exception as e:
            print(f"Failed to process {filename}: {e}")

    print(f"Successfully upgraded {count} nodes in General Theory to DROS 2.0 Structure.")
