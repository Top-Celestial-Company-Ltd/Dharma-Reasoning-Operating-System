import os
import json
import subprocess

# Configuration
BASE_PATH = r"e:\vscode\AI知識庫\數位佛堂"
ZHII_RAW_PATH = os.path.join(BASE_PATH, "AI 智者", "raw")
REPORT_FILE = os.path.join(BASE_PATH, "missing_concepts_report.json")
ZHII_GAPS_FILE = os.path.join(BASE_PATH, "zhii_missing_concepts.json")

def main():
    if not os.path.exists(REPORT_FILE):
        print("Report file not found. Please run dharma_gap_analyzer.py first.")
        return

    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        report = json.load(f)

    # Combine all missing terms from all indices
    all_missing = set()
    for source in report["gaps"].values():
        all_missing.update(source["all_missing"])
    
    print(f"Total unique missing concepts: {len(all_missing)}")

    # We want to find which of these missing terms appear in Zhiyi's raw texts.
    # To speed up, we'll use 'ripgrep' (rg) if available, or 'grep'.
    # Since I don't know if 'rg' is in the path, I'll use a simpler approach:
    # Read the most important Tiantai texts into memory as a single blob.
    
    important_files = [
        "T1716_《妙法蓮華經玄義》.md",
        "T1717_《法華文句》.md",
        "T1911_《摩訶止觀》.md",
        "T1926_《法華經安樂行義》.md",
        "X0585_《法華經三大部讀教記》.md"
    ]
    
    print("Loading core Tiantai texts for matching...")
    blob = ""
    for fname in important_files:
        fpath = os.path.join(ZHII_RAW_PATH, fname)
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                blob += f.read()
    
    print(f"Text blob size: {len(blob)} characters.")

    zhii_confirmed_gaps = []
    print("Filtering missing concepts by Tiantai context...")
    
    # Sort terms by length (longest first) to avoid partial matches if needed, 
    # but here we just want to know if it exists.
    count = 0
    total = len(all_missing)
    for term in sorted(list(all_missing)):
        count += 1
        if count % 1000 == 0:
            print(f"Processed {count}/{total} terms...")
        
        # Simple existence check
        if term in blob:
            zhii_confirmed_gaps.append(term)

    print(f"Found {len(zhii_confirmed_gaps)} missing concepts that appear in core Tiantai texts.")

    # Save the positive list
    with open(ZHII_GAPS_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "summary": {
                "source_texts": important_files,
                "total_confirmed_gaps": len(zhii_confirmed_gaps)
            },
            "concepts": sorted(zhii_confirmed_gaps)
        }, f, ensure_ascii=False, indent=2)

    print(f"Tiantai positive list saved to: {ZHII_GAPS_FILE}")

if __name__ == "__main__":
    main()
