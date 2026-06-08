import os
import re
import json

# Configuration
BASE_PATH = r"e:\vscode\AI知識庫\數位佛堂"
PILLARS = ["AI 智者", "AI 總論", "AI 龍樹", "AI 彌勒", "AI 惠能", "AI 善導"]

INDEX_FILES = {
    "Foguang": os.path.join(BASE_PATH, "00_黃金索引庫", "0-佛光辭典索引.md"),
    "Faxiang": os.path.join(BASE_PATH, "00_黃金索引庫", "0-法相辭典索引.md")
}

OUTPUT_FILE = os.path.join(BASE_PATH, "missing_concepts_report.json")

def get_existing_concepts():
    existing = set()
    for pillar in PILLARS:
        path = os.path.join(BASE_PATH, pillar, "wiki", "concepts")
        if os.path.exists(path):
            print(f"Scanning {pillar} concepts...")
            for filename in os.listdir(path):
                if filename.endswith(".md"):
                    concept = filename[:-3]
                    existing.add(concept)
    return existing

def extract_terms_from_index(file_path):
    terms = set()
    if not os.path.exists(file_path):
        print(f"Warning: Index file not found: {file_path}")
        return terms
    
    # Pattern: 【[[SOURCE#TERM|TERM]]】
    pattern = re.compile(r"【\[\[.*?#(.*?)\|.*?\]\]】")
    
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                term = match.group(1).strip()
                # Filter out numbers and common noise
                if term and not term.isdigit():
                    terms.add(term)
    return terms

def main():
    print("Scanning existing concepts...")
    existing = get_existing_concepts()
    print(f"Found {len(existing)} existing concepts across all pillars.")

    report = {
        "summary": {
            "total_existing": len(existing),
            "pillars_scanned": PILLARS
        },
        "gaps": {}
    }

    for name, path in INDEX_FILES.items():
        print(f"Processing {name} index...")
        source_terms = extract_terms_from_index(path)
        missing = source_terms - existing
        
        report["gaps"][name] = {
            "total_source_terms": len(source_terms),
            "total_missing": len(missing),
            "missing_samples": sorted(list(missing))[:100],
            "all_missing": sorted(list(missing))
        }
        
        print(f"  - Source terms: {len(source_terms)}")
        print(f"  - Missing: {len(missing)}")

    # Special logic for Tiantai/Zhiyi: 
    # Terms found in "Tiantai" related source indices but missing in Wiki.
    # For now, we'll just output the missing list and let the user review.

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\nReport generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
