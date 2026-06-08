import re

with open(r'E:\\vscode\\AI知識庫\\數位佛堂\\dros_academic_paper_draft.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Wrap all code blocks that start with `          東方佛學本體論` or `                                 [ 使用者提問 ]`
# We can just replace ``` with <div class="full-width">\n``` and ```\n</div>

# Flowchart:
text = text.replace('```\n                                 [ 使用者提問 (Input Query) ]', '<div class="full-width">\n\n```\n                                 [ 使用者提問 (Input Query) ]')
# Ensure we close the div after the block
text = re.sub(r'(                           \[ Output Response 串流輸出 \]\n```)', r'\1\n\n</div>', text)

# Table:
text = text.replace('```\n          東方佛學本體論', '<div class="full-width">\n\n```\n          東方佛學本體論')
text = re.sub(r'(   \+------------------------------\+      \+------------------------------\+\n```)', r'\1\n\n</div>', text)

with open(r'E:\\vscode\\AI知識庫\\數位佛堂\\dros_academic_paper_draft.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Wrapped successfully.")
