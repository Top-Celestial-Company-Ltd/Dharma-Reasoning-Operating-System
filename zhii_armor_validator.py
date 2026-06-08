import os
import re
import yaml

VAULT_ROOT = r'E:\vscode\AI知識庫\數位佛堂'
PILLAR_PATH = os.path.join(VAULT_ROOT, "AI 智者")
INBOX_DIR = os.path.join(PILLAR_PATH, "wiki", "inbox")
CONCEPTS_DIR = os.path.join(PILLAR_PATH, "wiki", "concepts")

def validate_and_move():
    if not os.path.exists(INBOX_DIR):
        print(f"[!] Inbox directory not found: {INBOX_DIR}")
        return

    if not os.path.exists(CONCEPTS_DIR):
        os.makedirs(CONCEPTS_DIR)

    files = [f for f in os.listdir(INBOX_DIR) if f.endswith(".md") and f != "README.md"]
    print(f"[*] Validating {len(files)} nodes in inbox...")

    passed = 0
    failed = 0

    for filename in files:
        src_path = os.path.join(INBOX_DIR, filename)
        dest_path = os.path.join(CONCEPTS_DIR, filename)

        try:
            with open(src_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Extract YAML
            match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
            if not match:
                print(f"  [FAIL] {filename}: No YAML header")
                failed += 1
                continue
            
            data = yaml.safe_load(match.group(1))
            
            # Strict Validation Rules
            errors = []
            if "sutra_id" not in data or not data["sutra_id"]:
                errors.append("Missing sutra_id")
            if data.get("interpretation_standpoint") != "Tiantai":
                errors.append("Invalid interpretation_standpoint")
            if "lineage" not in data or "AI 智者" not in data["lineage"]:
                errors.append("Invalid lineage")
            
            if errors:
                print(f"  [FAIL] {filename}: {', '.join(errors)}")
                failed += 1
                continue
            
            # Pass: Move to concepts
            # Check if exists in concepts
            if os.path.exists(dest_path):
                # If it's a draft and the destination is also a draft, overwrite. 
                # If destination is 'verified' or 'refined', skip.
                pass 

            os.rename(src_path, dest_path)
            passed += 1
        
        except Exception as e:
            print(f"  [ERROR] {filename}: {str(e)}")
            failed += 1

    print(f"\n[*] Validation complete.")
    print(f"  - Passed & Moved: {passed}")
    print(f"  - Failed: {failed}")

if __name__ == "__main__":
    validate_and_move()
