import os
import re

LEXICON_PATH = r"e:\vscode\AI知識庫\數位佛堂\zhii_auto_linker.py" # Using the term list from there
# Actually I'll just use the list of filenames from AI 智者 concepts as the term list
TIANTAI_DIR = r"e:\vscode\AI知識庫\數位佛堂\AI 智者\wiki\concepts"
TERMS = [f[:-3] for f in os.listdir(TIANTAI_DIR) if f.endswith(".md") and len(f[:-3]) >= 2]
TERMS.sort(key=len, reverse=True) # Longest first

ROOT = r"e:\vscode\AI知識庫\數位佛堂"

def auto_link(content, terms):
    # Only link outside of code blocks and metadata
    # Simple strategy: link terms that are not already linked [[...]]
    # and not in headers
    
    def repl(m):
        term = m.group(0)
        return f"[[{term}]]"

    # Avoid linking inside callout titles or metadata
    lines = content.split("\n")
    new_lines = []
    for line in lines:
        if line.startswith("##-") or line.startswith("> [!"):
            new_lines.append(line)
            continue
        
        # Only replace if not already linked
        for term in terms[:500]: # Limit to top 500 terms to avoid massive slowdown
            pattern = re.compile(rf'(?<!\[\[){re.escape(term)}(?!\]\])')
            line = pattern.sub(f"[[{term}]]", line, count=1)
        new_lines.append(line)
    
    return "\n".join(new_lines)

total = 0
for root, dirs, files in os.walk(ROOT):
    if "concepts" in dirs:
        d = os.path.join(root, "concepts")
        print(f"Linking: {d}")
        for filename in os.listdir(d):
            if not filename.endswith(".md"): continue
            path = os.path.join(d, filename)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                new_content = auto_link(content, TERMS)
                if new_content != content:
                    with open(path, 'w', encoding='utf-8', newline='\n') as f:
                        f.write(new_content)
                total += 1
            except Exception:
                pass

print(f"Auto-linked {total} nodes across all libraries.")
