import os
import math

# 設定
WIKI_ROOT = r"E:\vscode\AI知識庫\數位佛堂"
OUTPUT_DIR = r"E:\vscode\AI知識庫\數位佛堂_LM_Upload_V5"
CHUNKS_COUNT = 50

def pack_for_lm():
    if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)
    
    # 收集所有節點
    all_nodes = []
    for root, dirs, files in os.walk(WIKI_ROOT):
        if "wiki" in root.lower() and "concepts" in root.lower():
            for f in files:
                if f.endswith(".md"):
                    all_nodes.append(os.path.join(root, f))
                    
    total_nodes = len(all_nodes)
    print(f"[*] 發現總節點數：{total_nodes}")
    
    nodes_per_chunk = math.ceil(total_nodes / CHUNKS_COUNT)
    print(f"[*] 每個分包預計包含：{nodes_per_chunk} 個節點")
    
    for i in range(CHUNKS_COUNT):
        chunk_nodes = all_nodes[i*nodes_per_chunk : (i+1)*nodes_per_chunk]
        if not chunk_nodes: break
        
        output_file = os.path.join(OUTPUT_DIR, f"DROS_V5_Chunk_{i+1:02d}.txt")
        with open(output_file, 'w', encoding='utf-8') as out:
            for node_path in chunk_nodes:
                try:
                    with open(node_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        node_name = os.path.basename(node_path)[:-3]
                        out.write(f"\n\n=== NODE: {node_name} ===\n")
                        out.write(content)
                        out.write("\n--- END OF NODE ---\n")
                except: continue
        
        print(f"[OK] 已打包：{output_file} ({len(chunk_nodes)} nodes)")

    print(f"\n[SUCCESS] 打包完成！請至 {OUTPUT_DIR} 提取 50 個檔案上傳至 NotebookLM。")

if __name__ == "__main__":
    pack_for_lm()
