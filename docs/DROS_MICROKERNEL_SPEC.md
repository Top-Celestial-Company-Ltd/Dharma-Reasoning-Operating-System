# 📿 DROS Micro-kernel Standard Specification
## DROS-RFC 001: Unified Multi-Language µDROS Core Architecture

> **"One Specification to rule them all, One Manifest to bind them, One Topology to bring them all, and in the Offline Reasoning shine them."**  
> ── DROS Core Architects (Jimmy Chen & Antigravity)

---

## 🏛️ 一、 總體架構原則 (Architectural Philosophy)

DROS 微內核（µDROS Core）旨在以 **極致輕量（<1000行）、零外部相依性（Zero Dependency）、內存唯讀拓撲（In-Memory Topology）、以及確定性合約（Deterministic GuardVM）** 為核心設計原則。

微內核**不**負責：
- 數據持久化與寫入（Manifest 在編譯期生成，微內核只讀載入）
- 高維向量相似度計算（將此交給粗糙的傳統 RAG，DROS 專注於高精度名相定錨）
- LLM 推理生成（DROS 僅負責生成高度硬化的推理上下文 Context Prompt）

---

## 💾 二、 黃金清單標準格式 (DROS Golden Manifest Schema)

所有語言版本的微內核，必須能夠解析並載入同一個 `dros_manifest.json`。其 JSON 結構定義如下：

```json
{
  "version": "7.2",
  "metadata": {
    "node_count": 16071,
    "compiled_at": "2026-05-19T12:00:00Z"
  },
  "nodes": {
    "T0001": {
      "id": "T0001",
      "canonical": "真如",
      "aliases": ["如如", "法性", "Suchness", "Tathata"],
      "weights": {
        "tiantai": 0.95,
        "yogacara": 0.90,
        "madhyamaka": 0.85
      },
      "definition": "一切諸法之真實本性，非虛妄、非變異，離言絕慮之究竟實在。",
      "synapses": [
        {"target": "T0002", "relation": "等同", "weight": 1.0},
        {"target": "T0005", "relation": "依止", "weight": 0.8}
      ]
    }
  }
}
```

### 內存索引要求 (In-Memory Indexing)
微內核載入 Manifest 後，必須在內存中建立兩個索引：
1. **NodeMap** (`ID -> Node`): 通過 `T-Number` 進行 $O(1)$ 的極速節點尋址。
2. **AliasLookup** (`Alias -> ID`): 將所有 canonical 名稱及 aliases（包含中英文別名）對映到其對應的 `T-Number`，用於實現文本匹配時的 $O(1)$ 指紋定錨。

---

## ⚡ 三、 核心演算法：突觸編織掃描器 (Synaptic Weaver Engine)

突觸編織器負責從用戶輸入的無結構 raw text 中，掃描出所有匹配的 DROS 名相。

### 1. 算法輸入與輸出
- **Input**: `text: String` (用戶輸入的問題，或當前編輯中的筆記內容)
- **Output**: `List[SynapseContext]` (包含匹配節點、位置索引以及拓撲權重的結構體列表)

### 2. 核心匹配規則 (Matching Rules)
- **最長匹配原則 (Longest Match First)**：
  如果文本中含有「大般若波羅蜜多經」，當「大般若經」、「般若」與「大般若波羅蜜多經」皆在詞表中時，必須**優先且僅匹配最長**的「大般若波羅蜜多經」，避免名相突觸重複碎裂。
- **滑動窗口掃描或 Trie 樹（推薦）**：
  在 Rust/C++/TS 中，推薦使用 Trie 樹（前綴樹）對 `AliasLookup` 進行 $O(N)$ 線性時間複雜度掃描。

### 3. 掃描演算法偽代碼 (Pseudocode)
```text
function WEAVE(text: String, alias_lookup: Map<String, String>, node_map: Map<String, Node>) -> List<Match>:
    matches = []
    text_length = length(text)
    i = 0
    
    while i < text_length:
        longest_match_len = 0
        matched_node_id = null
        
        # 尋找從當前位置 i 開始的最長匹配別名
        for alias in alias_lookup.keys():
            alias_len = length(alias)
            if i + alias_len <= text_length:
                substring = slice(text, i, i + alias_len)
                if substring == alias:
                    if alias_len > longest_match_len:
                        longest_match_len = alias_len
                        matched_node_id = alias_lookup[alias]
                        
        if matched_node_id != null:
            matches.append(Match(
                node_id=matched_node_id,
                start_index=i,
                end_index=i + longest_match_len,
                matched_text=slice(text, i, i + longest_match_len)
            ))
            i += longest_match_len  # 步進最長匹配長度，避免重疊匹配
        else:
            i += 1  # 無匹配，前進 1 字元
            
    return matches
```

---

## 🕸️ 四、 拓撲導航算法 (Topology Routing & Decay)

當掃描器找到 $K$ 個直接匹配節點後，導航器需要向外擴展，抓取與這些核心概念直接關聯的「一階鄰居鄰域」，並計算其衰減權重，以防止上下文爆炸。

### 1. 衰減公式 (Decay Formula)
對於核心節點 $N_c$ 的一階鄰居 $N_n$：
$$W(N_n) = W_{edge}(N_c \rightarrow N_n) \times DecayFactor$$
*(預設 $DecayFactor = 0.5$)*

### 2. 鄰居去重與合併 (Deduplication & Union)
若一個鄰居被多個核心節點共同指向，其最終拓撲權重為指向它的所有核心節點權重之和（或取最大值），表徵該鄰居節點在當前多重名相編織中的「共鳴度」。

---

## 🛡️ 五、 確定性契約機 (GuardVM Spec)

GuardVM 是一個確定性的上下文生成上下文狀態機。它根據載入的合約規則，過濾並格式化輸出的提示詞。

### 1. 金剛合約模式 (Vajra Contract - Canonical Only)
- **精神**：極度嚴謹，嚴禁 AI 隨意推演，強制 AI 必須逐字對齊原典定義。
- **GuardVM 行為**：
  - 僅輸出匹配節點的 `definition`。
  - 在 Prompt 中注入指令：`"你必須且僅能基於以下給定名相的定義進行回答。若超出定義範疇，請直接回答『非本合約所及』。"`

### 2. 菩薩合約模式 (Prajna Contract - Speculative & Interpretive)
- **精神**：開放包容，引導 AI 進行跨宗派推演、現代應用與隱喻轉化。
- **GuardVM 行為**：
  - 輸出核心節點及一階拓撲鄰居的語意網。
  - 在 Prompt 中注入指令：`"請在基於給定名相的基礎上，沿著其拓撲突觸關係網（如「依止」、「生起」等關係）進行宗派融合與現代意境推演。"`

---

## 🚀 六、 輸出上下文格式化標準 (Output Weaving Template)

所有微內核在拼裝完成後，必須將上下文包裝成統一的 Markdown 格式，附加到發送給大語言模型的 System Prompt 尾部：

```markdown
<!-- DROS_SOVEREIGN_CONTEXT_START -->
## 📿 DROS 拓撲義理網格 (Sovereign Context Grid)
當前文本中已成功編織以下義理突觸：

### 核心名相定義 (Canonical Core Nodes)
- **T0001 (真如)**: 一切諸法之真實本性...

### 關聯拓撲鄰居 (Active Synaptic Neighbors)
- **T0002 (法性)** (共鳴權重: 0.50): 與 [真如] 互為 [等同] 關係。

### 推理合約熔斷規則 (GuardVM Execution Mode: Vajra)
[金剛契約已生效]：你的一切推論必須 100% 侷限在上述核心名相定義中，不得自行添加未定義之宗教詮釋！
<!-- DROS_SOVEREIGN_CONTEXT_END -->
```

---
*DROS Specification v7.2 (Epistemic Edition). Authored by 康宸園有限公司*
