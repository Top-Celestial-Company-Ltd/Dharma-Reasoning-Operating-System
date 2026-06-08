import os
import json
import time
from collections import deque

class AhoCorasick:
    def __init__(self):
        self.trie = [{'next': {}, 'fail': 0, 'output': []}]
        self.nodes_count = 1

    def add_pattern(self, pattern):
        node = 0
        for char in pattern:
            if char not in self.trie[node]['next']:
                self.trie.append({'next': {}, 'fail': 0, 'output': []})
                self.trie[node]['next'][char] = self.nodes_count
                self.nodes_count += 1
            node = self.trie[node]['next'][char]
        self.trie[node]['output'].append(pattern)

    def build_fail_links(self):
        queue = deque()
        for char, next_node in self.trie[0]['next'].items():
            queue.append(next_node)
        
        while queue:
            u = queue.popleft()
            for char, v in self.trie[u]['next'].items():
                fail = self.trie[u]['fail']
                while char not in self.trie[fail]['next'] and fail != 0:
                    fail = self.trie[fail]['fail']
                self.trie[v]['fail'] = self.trie[fail]['next'].get(char, 0)
                self.trie[v]['output'].extend(self.trie[self.trie[v]['fail']]['output'])
                queue.append(v)

    def search(self, text):
        node = 0
        results = []
        for i, char in enumerate(text):
            while char not in self.trie[node]['next'] and node != 0:
                node = self.trie[node]['fail']
            node = self.trie[node]['next'].get(char, 0)
            for pattern in self.trie[node]['output']:
                results.append((i - len(pattern) + 1, pattern))
        return results

def main():
    base_path = r"e:\vscode\AI知識庫\數位佛堂"
    manifest_path = os.path.join(base_path, "zhii_missing_concepts.json")
    raw_dir = os.path.join(base_path, "AI 智者", "raw")
    output_path = os.path.join(base_path, "zhii_para_map.json")

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    
    concepts = manifest.get("concepts", [])
    print(f"Building automaton for {len(concepts)} concepts...")
    
    start_time = time.time()
    ac = AhoCorasick()
    for concept in concepts:
        if concept:
            ac.add_pattern(concept)
    ac.build_fail_links()
    print(f"Automaton built in {time.time() - start_time:.2f}s")

    para_map = {}
    
    source_files = [
        "T1716_《妙法蓮華經玄義》.md",
        "T1717_《法華文句》.md",
        "T1911_《摩訶止觀》.md",
        "T1926_《法華經安樂行義》.md",
        "X0585_《法華經三大部讀教記》.md"
    ]

    for filename in source_files:
        file_path = os.path.join(raw_dir, filename)
        if not os.path.exists(file_path):
            print(f"Skipping missing file: {filename}")
            continue
        
        print(f"Scanning {filename}...")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        scan_start = time.time()
        hits = ac.search(content)
        print(f"  - Found {len(hits)} hits in {time.time() - scan_start:.2f}s")
        
        # Process hits into context snippets
        for start_idx, pattern in hits:
            # Get context (±500 chars)
            start_context = max(0, start_idx - 500)
            end_context = min(len(content), start_idx + len(pattern) + 500)
            snippet = content[start_context:end_context]
            
            if pattern not in para_map:
                para_map[pattern] = []
            
            # Limit to top 5 hits per pattern to save tokens
            if len(para_map[pattern]) < 5:
                para_map[pattern].append({
                    "sutra_id": filename.split("_")[0],
                    "source_file": filename,
                    "index": start_idx,
                    "snippet": snippet
                })

    print(f"Total concepts with hits: {len(para_map)}")
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(para_map, f, ensure_ascii=False, indent=2)
    
    print(f"Para map saved to {output_path}")

if __name__ == "__main__":
    main()
