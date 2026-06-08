import os
import re

# Paths to the wiki concept directories
BASE_DIR = r"e:\vscode\AI知識庫\數位佛堂"
DIRS_TO_SCAN = [
    os.path.join(BASE_DIR, "AI 智者", "wiki", "concepts"),
    os.path.join(BASE_DIR, "AI 總論", "wiki", "concepts")
]

DRY_RUN = False  # Set to False to actually delete files

def should_delete(filepath, content):
    # Check for "Ghost Node" patterns in YAML and Content
    
    # YAML patterns (case-insensitive for safety)
    yaml_header_match = re.search(r'---\s*(.*?)\s*---', content, re.DOTALL)
    if yaml_header_match:
        yaml_content = yaml_header_match.group(1).lower()
        
        # Criteria 1: status is unverified
        if "status: 待印證" in yaml_content:
            return True, "status: 待印證"
            
        # Criteria 2: source is missing
        if 'source: "無"' in yaml_content or 'source: 無' in yaml_content:
            return True, 'source: "無"'
            
        # Criteria 3: title is missing
        if 'title: 無' in yaml_content:
            return True, 'title: 無'
            
        # Criteria 4: interpretation_standpoint is missing or "None"
        if "interpretation_standpoint:" in yaml_content:
            if 'interpretation_standpoint: "無"' in yaml_content or 'interpretation_standpoint: 無' in yaml_content:
                return True, 'standpoint: 無'
        # Note: We don't delete just because standpoint is missing yet, 
        # unless it's in AI 智者 where it's mandatory.
        # But for now, status and source are stronger indicators.

    # Criteria 5: Content contains "No evidence" markers
    if "無原文依據" in content or "無法判斷" in content:
        return True, "Content: 無原文依據"

    return False, ""

def run_exorcism():
    total_scanned = 0
    total_to_delete = 0
    deleted_files = []

    print(f"Starting DROS Zero-Noise Cleanup (DRY_RUN={DRY_RUN})...")
    
    for directory in DIRS_TO_SCAN:
        if not os.path.exists(directory):
            print(f"Directory not found: {directory}")
            continue
            
        print(f"Scanning: {directory}")
        for filename in os.listdir(directory):
            if filename.endswith(".md"):
                total_scanned += 1
                filepath = os.path.join(directory, filename)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    to_delete, reason = should_delete(filepath, content)
                    
                    if to_delete:
                        total_to_delete += 1
                        if DRY_RUN:
                            try:
                                print(f"[DRY-RUN] To Delete: {filename} (Reason: {reason})")
                            except UnicodeEncodeError:
                                print(f"[DRY-RUN] To Delete: (Encoding Error) (Reason: {reason})")
                        else:
                            os.remove(filepath)
                            try:
                                print(f"[DELETED] {filename} (Reason: {reason})")
                            except UnicodeEncodeError:
                                print(f"[DELETED] (Encoding Error) (Reason: {reason})")
                        deleted_files.append((filename, reason))
                        
                except Exception as e:
                    try:
                        print(f"Error processing {filename}: {e}")
                    except UnicodeEncodeError:
                        print(f"Error processing a file due to encoding: {e}")

    print("\n" + "="*40)
    print(f"Cleanup Summary:")
    print(f"Total Scanned: {total_scanned}")
    print(f"Nodes Identified for Cleanup: {total_to_delete}")
    print(f"Target Nodes Remaining: {total_scanned - total_to_delete}")
    print("="*40)
    
    if not DRY_RUN:
        with open(os.path.join(BASE_DIR, "deleted_nodes_log.txt"), 'w', encoding='utf-8') as log_f:
            for item in deleted_files:
                log_f.write(f"{item[0]} | {item[1]}\n")
        print(f"\nList of deleted files saved to deleted_nodes_log.txt")

    if DRY_RUN:
        print("\nThis was a DRY RUN. No files were actually deleted.")
        print("To proceed with deletion, set DRY_RUN = False in the script.")

if __name__ == "__main__":
    run_exorcism()
