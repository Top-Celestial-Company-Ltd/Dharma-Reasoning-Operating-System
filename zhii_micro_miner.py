import os
import json
import time
import sys
import io
import re
from google import genai
from google.genai import types
from pydantic import BaseModel
from typing import List, Optional

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

VAULT_ROOT = r'E:\vscode\AI知識庫\數位佛堂'
MODEL_NAME = 'gemini-2.5-flash-lite'
API_KEY = os.environ.get("GOOGLE_API_KEY")

class ConceptDefinition(BaseModel):
    name: str
    definition: Optional[str]
    sutra_id: str
    evidence: str

def extract_definition(client, concept_name, hits):
    max_retries, retry_delay = 3, 10
    
    # We take the first 3 hits to provide enough context but keep it manageable
    context_text = ""
    for i, hit in enumerate(hits[:3]):
        context_text += f"\n--- 來源段落 {i+1} ({hit['source_file']}) ---\n{hit['snippet']}\n"

    prompt = f'''你是一位天台宗義理專家。
請根據提供的經典段落，為名相「{concept_name}」提取其在天台宗語境下的「明確義理定義」。

【嚴格指令】：
1. 必須僅根據提供的段落內容進行提取。
2. 若段落中「沒有」給出該名相的明確定義、註釋或詳細描述，請將 definition 欄位設為 null。切勿自行腦補或從外部知識獲取。
3. 如果段落中有定義，請將其整理為約 50-100 字的精確義理描述。
4. evidence 欄位請摘錄文中支持該定義的最核心原文（30-50 字）。

名相：{concept_name}
段落內容：{context_text}'''

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=ConceptDefinition,
                ),
            )
            
            result = json.loads(response.text)
            if result.get("definition") and result.get("definition") != "null":
                # Inject metadata from hits
                result["sutra_id"] = hits[0]["sutra_id"]
                return result
            return None

        except Exception as e:
            err_msg = str(e)
            if "429" in err_msg or "quota" in err_msg.lower():
                time.sleep(retry_delay * (attempt + 1))
            else:
                time.sleep(2)
                
    return None

def create_node(concept_name, definition_data):
    pavilion_path = os.path.join(VAULT_ROOT, "AI 智者")
    inbox_dir = os.path.join(pavilion_path, "wiki", "inbox")
    if not os.path.exists(inbox_dir): os.makedirs(inbox_dir)
    
    safe_title = re.sub(r'[\\/*?:"<>|]', "", concept_name)
    path = os.path.join(inbox_dir, f"{safe_title}.md")
    
    if os.path.exists(path): return False
    
    body = f"""---
title: "{concept_name}"
layer: 3
tags: ["天台宗", "自動採集"]
status: draft
sutra_id: "{definition_data['sutra_id']}"
interpretation_standpoint: "Tiantai"
lineage: ["AI 智者"]
---

# {concept_name}

## 1. 義理定義
{definition_data['definition']}

## 2. 經典原文
> {definition_data['evidence']}

## 3. 來源
由 Pipeline 2.5 從天台三大部自動開採。
"""
    with open(path, 'wb') as f: f.write(body.encode('utf-8'))
    return True

def main():
    if not API_KEY:
        print("[!] 請先設定 GOOGLE_API_KEY 環境變數。")
        return

    para_map_path = os.path.join(VAULT_ROOT, "zhii_para_map.json")
    if not os.path.exists(para_map_path):
        print("[!] 找不到 zhii_para_map.json，請先執行 Phase 1。")
        return

    with open(para_map_path, "r", encoding="utf-8") as f:
        para_map = json.load(f)

    print(f'[*] 啟動天台微縮開採引擎 v2.5...')
    client = genai.Client(api_key=API_KEY)
    
    # Full scale processing
    concepts_to_process = list(para_map.keys())
    
    # Load existing concepts to skip
    existing_concepts = set()
    concept_dir = os.path.join(VAULT_ROOT, "AI 智者", "wiki", "concepts")
    if os.path.exists(concept_dir):
        for f in os.listdir(concept_dir):
            if f.endswith(".md"): existing_concepts.add(f[:-3])
    
    inbox_dir = os.path.join(VAULT_ROOT, "AI 智者", "wiki", "inbox")
    if os.path.exists(inbox_dir):
        for f in os.listdir(inbox_dir):
            if f.endswith(".md"): existing_concepts.add(f[:-3])

    print(f"[*] 已跳過 {len(existing_concepts)} 個已存在或已在收件匣中的節點。")
    
    processed = 0
    hits_found = 0
    total = len(concepts_to_process)
    
    for concept_name in concepts_to_process:
        processed += 1
        if concept_name in existing_concepts:
            continue
            
        hits = para_map[concept_name]
        print(f"  [{processed}/{total}] 正在處理: {concept_name}...")
        
        result = extract_definition(client, concept_name, hits)
        if result:
            if create_node(concept_name, result):
                print(f"    [+] 成功提取並創建節點: {concept_name}")
                hits_found += 1
            else:
                print(f"    [.] 節點已存在，跳過: {concept_name}")
        else:
            print(f"    [-] 未能在段落中找到明確定義: {concept_name}")
        
        # Throttling to respect API limits (1.5s to be safe for a long run)
        time.sleep(1.5)

    print(f"\n[*] 全量處理完畢。共成功採集 {hits_found} 個新節點。")

if __name__ == '__main__':
    main()
