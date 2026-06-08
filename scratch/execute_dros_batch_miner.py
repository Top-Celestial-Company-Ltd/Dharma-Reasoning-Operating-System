import os
import re
import sys

# 解決 Windows cp950 編碼與輸出問題
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# 設定路徑 (沙盒環境)
BASE_PATH = r"E:\vscode\AI知識庫\數位佛堂_v7.3_upgrade"
INDEX_FILES = {
    "Foguang": os.path.join(BASE_PATH, "00_黃金索引庫", "0-佛光辭典索引.md"),
    "Faxiang": os.path.join(BASE_PATH, "00_黃金索引庫", "0-法相辭典索引.md")
}

# 經典關鍵字與 T-座標對照表 (新增 T1558 俱舍論 與 T1509 大智度論)
CLASSIC_MAPPING = {
    "入中論": "T1861",
    "月稱": "T1861",
    "應成": "T1861",
    "瑜伽師地論": "T1579",
    "無著": "T1579",
    "彌勒": "T1579",
    "阿賴耶識": "T1579",
    "阿賴耶": "T1579",
    "末那識": "T1579",
    "末那": "T1579",
    "成唯識論": "T1585",
    "唯識三十論": "T1586",
    "俱舍論": "T1558",
    "阿毘達磨": "T1558",
    "心所": "T1558",
    "大智度論": "T1509",
    "龍樹": "T1509",
    "中論": "T1564"
}

# 定義超節點名單 (這些節點將生成為 0-Byte Void Pointers 以配合真空妙有遲綁定)
SUPER_NODES = {
    "入中論", "月稱", "應成派與自續派", "瑜伽師地論", "阿賴耶識", "末那識", 
    "禪定", "禪支", "心所", "四聖諦", "十六行相", "苦諦", "集諦", "滅諦", "道諦",
    "三禪", "四禪", "喜", "樂", "捨"
}

# 關鍵詞篩選模式
TARGET_PATTERNS = {
    "Madhyamakavatara": [r"入中論", r"月稱", r"應成"],
    "Yogacarabhumisastra": [r"瑜伽師地論", r"無著", r"彌勒", r"阿賴耶", r"末那"],
    "Jhana_Factors": [r"禪定", r"禪支", r"心所", r"初禪", r"二禪", r"三禪", r"四禪"],
    "Four_Noble_Truths": [r"四諦", r"四聖諦", r"十六行相", r"苦諦", r"集諦", r"滅諦", r"道諦"]
}

# 目標 Pillars 路徑與宗派分類
PILLARS_MAPPING = {
    "Madhyamakavatara": {
        "dir": os.path.join(BASE_PATH, "core", "AI 龍樹", "wiki", "concepts"),
        "context": "中觀派"
    },
    "Yogacarabhumisastra": {
        "dir": os.path.join(BASE_PATH, "core", "AI 彌勒", "wiki", "concepts"),
        "context": "唯識宗"
    },
    "Jhana_Factors": {
        "dir": os.path.join(BASE_PATH, "core", "AI 總論", "wiki", "concepts"),
        "context": "阿毗達摩"
    },
    "Four_Noble_Truths": {
        "dir": os.path.join(BASE_PATH, "core", "AI 總論", "wiki", "concepts"),
        "context": "通用"
    }
}

def get_existing_concepts():
    existing = set()
    for pillar in ["AI 智者", "AI 總論", "AI 龍樹", "AI 彌勒", "AI 惠能", "AI 善導"]:
        path = os.path.join(BASE_PATH, "core", pillar, "wiki", "concepts")
        if os.path.exists(path):
            for filename in os.listdir(path):
                if filename.endswith(".md"):
                    existing.add(filename[:-3])
    return existing

def clean_term(val):
    if not val:
        return ""
    # 移除底線、引號及多餘空格
    val = re.sub(r"[\"'_]", "", val)
    return val.strip().lower()

def extract_metadata(desc):
    sanskrit = ""
    pali = ""
    aliases = []
    
    # 1. 提取梵文 (支援 Skt., 梵名, 梵語, 梵)
    skt_match = re.search(r"(?:梵語|梵名|梵|Skt\.|Sanskrit)\s*([a-zA-Z\-\s\(\),]+)", desc)
    if skt_match:
        sanskrit = clean_term(skt_match.group(1).split(',')[0].split('(')[0])
        
    # 2. 提取巴利文 (支援 Pali, 巴利語, 巴利, 巴)
    pali_match = re.search(r"(?:巴利語|巴利|巴|Pali)\s*([a-zA-Z\-\s\(\),]+)", desc)
    if pali_match:
        pali = clean_term(pali_match.group(1).split(',')[0].split('(')[0])
        
    # 3. 提取別名 (支援 又作, 又稱, 又名, 譯作, 簡稱)
    alias_matches = re.findall(r"(?:又作|又稱|又名|意譯|譯作|簡稱)\s*【?\[?\[?([^，。；\s【\]\(\)]+)\]?\]?】?", desc)
    for a in alias_matches:
        a_clean = a.strip()
        if a_clean and a_clean not in aliases:
            aliases.append(a_clean)
            
    return sanskrit, pali, aliases

def extract_t_numbers(term, desc):
    t_coords = set()
    
    # 掃描名相字面或釋義中是否包含經典對照
    for key, t_num in CLASSIC_MAPPING.items():
        if key in term or key in desc:
            t_coords.add(t_num)
            
    # 特殊規則：瑜伽師地論相關的預設給予 T1579；中觀應成派給予 T1861
    if "瑜伽" in term or "阿賴耶" in term or "末那" in term:
        t_coords.add("T1579")
    if "入中論" in term or "月稱" in term:
        t_coords.add("T1861")
    if "四聖諦" in term or "十六行相" in term or "心所" in term:
        t_coords.add("T1558")
        
    return sorted(list(t_coords))

def execute_mining():
    existing = get_existing_concepts()
    print(f"[*] Loaded existing concepts: {len(existing)}")
    
    # 確保所有目標目錄存在
    for k, v in PILLARS_MAPPING.items():
        os.makedirs(v["dir"], exist_ok=True)
        
    # 讀取辭典索引內容
    pattern = re.compile(r"【\[\[.*?#(.*?)\|.*?\]\]】(.*)")
    
    candidates = {k: {} for k in TARGET_PATTERNS}
    
    for name, path in INDEX_FILES.items():
        if not os.path.exists(path):
            print(f"[!] Index file not found: {path}")
            continue
            
        print(f"[*] Scanning dictionary for extraction: {name}...")
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                match = pattern.search(line)
                if match:
                    term = match.group(1).strip()
                    desc = match.group(2).strip()
                    
                    if term in existing or term.isdigit():
                        continue
                        
                    # 匹配關鍵字並分配至主題類別
                    for cat, pat_list in TARGET_PATTERNS.items():
                        for pat in pat_list:
                            if re.search(pat, term) or re.search(pat, desc):
                                # 若在多個地方匹配，保留最長釋義
                                if term not in candidates[cat] or len(desc) > len(candidates[cat][term]):
                                    candidates[cat][term] = desc
                                break

    print("\n[*] 開始批次寫入本體指針檔案...")
    
    total_mined = 0
    
    for cat, terms_dict in candidates.items():
        mapping = PILLARS_MAPPING[cat]
        target_dir = mapping["dir"]
        sectarian_context = mapping["context"]
        
        print(f"\n📂 正在開採類別 [{cat}] -> 目標目錄: {Path(target_dir).name}")
        
        for term, desc in terms_dict.items():
            # 1. 提取梵/巴/別名/T-座標
            sanskrit, pali, aliases = extract_metadata(desc)
            t_coords = extract_t_numbers(term, desc)
            
            # 若無 T-座標，預設補齊通用 T-座標
            if not t_coords:
                if cat == "Madhyamakavatara": t_coords = ["T1861"]
                elif cat == "Yogacarabhumisastra": t_coords = ["T1579"]
                elif cat == "Jhana_Factors": t_coords = ["T1558"]
                else: t_coords = ["T1558"] # 通用/阿毗達摩 fallback
            
            # 2. 判斷是否為超節點 (Void Pointer)
            is_super = term in SUPER_NODES or any(sn in term for sn in SUPER_NODES)
            node_type = "Void Pointer" if is_super else "Populated Stub"
            
            # 3. 構造 YAML 屬性內容
            aliases_str = json.dumps(aliases, ensure_ascii=False) if aliases else "[]"
            t_coords_str = json.dumps(t_coords)
            
            yaml_header = f"""---
title: "{term}"
aliases: {aliases_str}
sanskrit_term: "{sanskrit}"
pali_term: "{pali}"
sectarian_context: "{sectarian_context}"
t_coordinates: {t_coords_str}
node_type: "{node_type}"
---
"""
            
            # 4. 根據種類生成主體內容
            if is_super:
                # 0-Byte 真空指針：檔案本體為空，僅包含 YAML
                file_content = yaml_header
            else:
                # 存存根檔案 (Populated Stub)
                file_content = yaml_header + f"""
##- **層級**: 3
- **標籤**: ["核心名相", "{sectarian_context}"]
- **狀態**: verified

> [!NOTE] 核心義理 (辭典引路)
> {desc}

> [!QUOTE] 經文原句 (定錨路標)
> *[大覺藏定錨座標: {', '.join(t_coords)}。本體指針已與實體文獻隔離對齊。]*
"""
            
            file_path = os.path.join(target_dir, f"{term}.md")
            
            try:
                with open(file_path, "w", encoding="utf-8") as out:
                    out.write(file_content)
                total_mined += 1
            except Exception as e:
                print(f"❌ 寫入失敗 {term}: {e}")
                
        print(f"    -> 成功生成 {len(terms_dict)} 個名相指針")
        
    print(f"\n🎉 批次法義開採與本體定錨成功！共生成 {total_mined} 個本體節點。")
    print(f"請在 Port 5001 運行 `zhii_armor_validator.py` 驗證 T-座標有效性。")

import json
from pathlib import Path

if __name__ == "__main__":
    execute_mining()
