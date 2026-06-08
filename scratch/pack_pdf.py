import os
import subprocess
import sys

try:
    import markdown
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown"])
    import markdown

MD_PATH = r"E:\vscode\AI知識庫\數位佛堂\dros_academic_paper_draft.md"
HTML_PATH = r"E:\vscode\AI知識庫\數位佛堂_v7.3_upgrade\DROS_v7.3_Paper_IEEE.html"
PDF_PATH = r"E:\vscode\AI知識庫\數位佛堂_v7.3_upgrade\DROS_v7.3_Paper_IEEE_v20.pdf"

with open(MD_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

# Separate title block from body for IEEE spanning
lines = text.split('\n')
title_lines = []
body_lines = []
in_title_block = True
for line in lines:
    if line.startswith('# ') or line.startswith('作者：') or line.startswith('機構：') or line.startswith('Email：'):
        title_lines.append(line)
    elif line.strip() == '' and in_title_block:
        title_lines.append(line)
    else:
        in_title_block = False
        body_lines.append(line)

title_md = '\n'.join(title_lines)
body_md = '\n'.join(body_lines)

html_title = markdown.markdown(title_md)
html_body = markdown.markdown(body_md, extensions=['tables', 'fenced_code'])
html_body = html_body.replace('<p><strong>作者：', '<p style="text-indent: 0;"><strong>作者：')
html_body = html_body.replace('<p><strong>關鍵字', '<p style="text-indent: 0;"><strong>關鍵字')

# IEEE CSS
html_template = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>DROS v7.3 Academic Paper</title>
<style>
    @page {{
        size: letter;
        margin: 0.75in;
    }}
    body {{
        font-family: "Times New Roman", Times, serif;
        font-size: 10pt;
        line-height: 1.2;
        margin: 0;
        padding: 0;
        text-align: justify;
    }}
    .title-block {{
        text-align: center;
        margin-bottom: 24pt;
    }}
    .title-block h1 {{
        font-size: 24pt;
        font-weight: normal;
        margin-bottom: 12pt;
    }}
    .title-block p {{
        font-size: 11pt;
        text-align: center;
        text-indent: 0;
        margin: 2pt 0;
    }}
    .content-block {{
        column-count: 2;
        column-gap: 0.25in;
    }}
    h1, h2, h3, h4 {{
        font-weight: bold;
    }}
    .content-block h2 {{
        font-size: 11pt;
        text-align: left;
        margin-top: 12pt;
        margin-bottom: 6pt;
    }}
    .content-block h3 {{
        font-size: 10pt;
        font-style: italic;
        font-weight: bold;
        text-align: left;
        margin-top: 10pt;
        margin-bottom: 4pt;
    }}
    .content-block h4 {{
        font-size: 10pt;
        font-style: italic;
        font-weight: normal;
        text-align: left;
        margin-top: 8pt;
        margin-bottom: 4pt;
    }}
    .content-block p {{
        text-indent: 0.15in;
        margin-top: 0;
        margin-bottom: 6pt;
    }}
    img {{
        max-width: 100%;
        height: auto;
    }}
    .full-width {{
        column-span: all;
        margin: 12pt 0;
    }}
    pre {{
        font-family: "NSimSun", "MingLiU", "Courier New", Courier, monospace;
        font-size: 7.5pt;
        white-space: pre-wrap;
        word-wrap: break-word;
        background-color: #f8f9fa;
        padding: 10pt;
        padding-left: 15pt;
        border: 1px solid #ddd;
    }}
    pre > code {{
        display: block;
        text-align: left;
        background-color: transparent;
        padding: 0;
    }}
    code {{
        font-family: "NSimSun", "MingLiU", "Courier New", Courier, monospace;
        font-size: 9pt;
        background-color: #f8f9fa;
        padding: 2px 4px;
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 12pt;
    }}
    th, td {{
        border: 1px solid black;
        padding: 4pt;
        text-align: left;
    }}
</style>
</head>
<body>
    <div class="title-block">
        {html_title}
    </div>
    <div class="content-block">
        {html_body}
    </div>
</body>
</html>
"""

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"HTML generated at {HTML_PATH}")

# Call Edge headless to print to PDF
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--print-to-pdf=" + PDF_PATH,
    "--no-pdf-header-footer",
    HTML_PATH
]

print("Generating PDF via Edge headless...")
subprocess.run(cmd, check=True)
print(f"PDF generated successfully at {PDF_PATH}")
