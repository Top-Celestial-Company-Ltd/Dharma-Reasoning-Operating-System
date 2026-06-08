import re

def center_text(text, width=80):
    lines = text.strip('\n').split('\n')
    centered_lines = []
    for line in lines:
        if line.strip() == '':
            centered_lines.append('')
            continue
        # calculate visual width: CJK=2, ASCII=1
        visual_width = sum(2 if ord(c) > 127 else 1 for c in line.strip())
        padding = max(0, (width - visual_width) // 2)
        centered_lines.append(' ' * padding + line.strip())
    return '\n'.join(centered_lines)

flowchart_raw = """
[ 使用者提問 (Input Query) ]
|
[ 意圖網關與代理伺服器 (Context Router / Proxy) ]
|
+---------------------------------+---------------------------------+
|                          (解析合約請求)                         |
[ strict_vajra (金剛模式) ]  [ balanced_vajra (詮釋模式) ]  [ speculative (高階推演) ]
|                                 |                                 |
+---------------------------------+---------------------------------+
|
[ 載入對應之 YAML 執行契約 (Load Target Contract) ]
|
[ 推理契約編譯器 (Inference Contract Compiler) ]
|
[ 系統提示詞與圖譜拓撲動態編譯 (Prompt & Topology Assembly) ]
|
[ Graphify 倒置索引尋址與 T-Number 校驗 (Physical Fetch) ]
|
[ 動態注入：實體內容、運行時變數與邊界信封 (Injection) ]
|
[ 算術邏輯單元 (Reasoning Engine / LLM) ]
|
+---------------------------------+---------------------------------+
|                   護法虛擬機輸出審計 (Guard VM)                 |
[ AuthorityNodesOnly: true ]                      [ AuthorityNodesOnly: false ]
|                                                                   |
[ 強制物理校驗 T-Number 座標 ]                        [ 放行跨界湧現與新本體論 ]
|                                                                   |
+---------------------------------+---------------------------------+
|
[ 串流輸出最終回應 (Output Response) ]
"""

flowchart_centered = center_text(flowchart_raw, 85)

section_text = f"""
### 3.2 執行契約編譯器與三層認識論治理 (Three-Layer Epistemic Governance)

為了徹底解決大型語言模型在嚴謹佛學研究中的「過度正統化鎖死 (Orthodoxy Lock-in)」與「湧現性發散 (Generative Hallucination)」之兩難，DROS v7.3 實作了**「三層認識論治理架構」**。該架構將大語言模型剝奪了自主檢索權限，降級為純粹的「算術邏輯單元 (ALU)」，並由系統外部的**執行契約編譯器 (Inference Contract Compiler)** 與 **護法虛擬機 (Guard VM)** 進行強型別約束。

```
{flowchart_centered}
```

【圖 2：DROS 執行契約編譯器工作管線與認識論路由】

系統將推論邊界物理劃分為三個平行宇宙：
1. **Canonical Layer（金剛聖言量推理）**：載入 `strict_vajra` 契約。此模式禁用 `我覺得` 等主觀預測詞彙，並且觸發 GuardVM 的 `AuthorityNodesOnly: true` 剛性審計。LLM 每一段推論後必須附帶本地大覺藏的 `T-Number` 座標，若無文獻支撐則主動拒答，確保 100% 零幻覺。
2. **Interpretive Layer（詮釋映射模式）**：載入 `balanced_vajra` 契約。系統允許將佛學名相（如「末那識」）與西方心理學（如「無意識自我」）進行跨學門對照。雖然放寬了語言風格，但仍受物理座標校驗限制，且段落開頭強制自動前綴 `[義理映射 / Interpretive Mapping]`，明確區隔原典與當代詮釋的邊界。
3. **Speculative Layer（高階般若湧現推演）**：載入 `speculative_prajna` 契約。為探索量子力學與緣起性空的跨界統攝，系統將 `AuthorityNodesOnly` 設為 `false`，主動關閉 GuardVM 座標校驗。然而，系統強制在介面層注入警告封裝，標註 `[認識論狀態：高階推演]`，確保湧現的新本體不會污染底層知識庫。
"""

with open(r'E:\\vscode\\AI知識庫\\數位佛堂\\dros_academic_paper_draft.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the existing "3.2 真空妙有" header to "3.3" and shift the rest
text = text.replace('### 3.2 「真空妙有」遲綁定', '### 3.3 「真空妙有」遲綁定')
text = text.replace('### 3.3 唯識記憶體與事件溯源（Event Sourcing）', '### 3.4 唯識記憶體與事件溯源（Event Sourcing）')

# Insert the new section before 3.3
parts = text.split('### 3.3 「真空妙有」遲綁定')
new_text = parts[0] + section_text + '\n### 3.3 「真空妙有」遲綁定' + parts[1]

with open(r'E:\\vscode\\AI知識庫\\數位佛堂\\dros_academic_paper_draft.md', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Insertion successful.")
