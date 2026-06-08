import re

def pad(text, n):
    return '\n'.join(' ' * n + line if line.strip() else line for line in text.strip('\n').split('\n'))

fig1 = """
            東方佛學本體論                   計算機操作系統與系統架構
   +------------------------------+      +------------------------------+
   | 天台宗判教 (五時八教)        |      | 層級文件系統與目錄沙盒       |
   |   - 權實隔離與開權顯實       | <==> |   - 物理路徑 ACL 與權限控制  |
   +------------------------------+      +------------------------------+
   | 唯識宗心理學 (八識心王)      |      | 馮紐曼記憶體分層與事件溯源   |
   |   - 阿賴耶識與種子現行       | <==> |   - 磁碟唯讀日誌與快取寫回   |
   |   - 末那識 (第七識自我)      |      |   - PID 0 系統自我核心線程   |
   +------------------------------+      +------------------------------+
   | 中觀派邏輯 (八不中道)        |      | 無狀態純函數與強類型安全     |
   |   - 離四句與破執             | <==> |   - GuardVM 剛性禁止詞過濾   |
   +------------------------------+      +------------------------------+
   | 華嚴宗法界 (事事無礙)        |      | 全連接雙向圖數據庫與 P2P     |
   |   - 因陀羅網重重折射         | <==> |   - 動態拓撲神經突觸編織     |
   +------------------------------+      +------------------------------+
"""

fig2 = """
                         [ 使用者提問 (Input Query) ]
                                       |
                 [ 意圖網關與代理伺服器 (Context Router / Proxy) ]
                                       |
       +-------------------------------+-------------------------------+
       |                         (解析合約請求)                        |
[ strict_vajra (金剛) ]    [ balanced_vajra (詮釋) ]    [ speculative (高階) ]
       |                               |                               |
       +-------------------------------+-------------------------------+
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
       +-------------------------------+-------------------------------+
       |                  護法虛擬機輸出審計 (Guard VM)                |
 [ AuthorityNodesOnly: true ]                    [ AuthorityNodesOnly: false ]
       |                                                               |
 [ 強制物理校驗 T-Number 座標 ]                      [ 放行跨界湧現與新本體論 ]
       |                                                               |
       +-------------------------------+-------------------------------+
                                       |
                     [ 串流輸出最終回應 (Output Response) ]
"""

fig3 = """
【圖 3a：宗派義理純淨度評分對比】
DROS v7.3    |██████████████████████████████ (100%)
傳統向量 RAG |██████████ (34.2%)
             └──────────────────────────────────────

【圖 3b：單次查詢 Context Token 消耗】
傳統向量 RAG |████████████████████████████████ (14,250 Tokens)
DROS v7.3    |████████ (3,980 Tokens - 大幅降低 72%)
             └──────────────────────────────────────

【圖 3c：檢索尋址延遲 (Latency)】
傳統向量 RAG |██████████████████████ (420 ms)
DROS v7.3    |█ (12 ms - O(1) 內存 warm-up)
             └──────────────────────────────────────
"""

# Apply padding
fig1_padded = pad(fig1, 16)
fig2_padded = pad(fig2, 11)
fig3_padded = pad(fig3, 20)

# We will read the markdown file and replace the pre blocks with the wrapped ones
with open(r'E:\vscode\AI知識庫\數位佛堂\dros_academic_paper_draft.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Figure 1
# Locate the existing div and its contents for Fig 1
p1 = r'<div class="full-width">\s*```\s*.*?因陀羅網重重折射.*?\+------------------------------\+\s*```\s*</div>'
if not re.search(p1, text, re.DOTALL):
    # Try finding without div
    p1 = r'```\s*.*?因陀羅網重重折射.*?\+------------------------------\+\s*```'
replacement1 = f'<div class="full-width">\n\n```text\n{fig1_padded}\n```\n\n</div>'
text = re.sub(p1, replacement1, text, flags=re.DOTALL)

# Replace Figure 2
p2 = r'```\s*.*?(?:使用者提問|Input Query).*?Output Response 串流輸出 \]\s*```'
replacement2 = f'<div class="full-width">\n\n```text\n{fig2_padded}\n```\n\n</div>'
text = re.sub(p2, replacement2, text, flags=re.DOTALL)

# Replace Figure 3
p3 = r'```\s*【圖 3a：宗派義理純淨度評分對比】.*?O\(1\) 內存 warm-up\).*?└──────────────────────────────────────\s*```'
replacement3 = f'<div class="full-width">\n\n```text\n{fig3_padded}\n```\n\n</div>'
text = re.sub(p3, replacement3, text, flags=re.DOTALL)

with open(r'E:\vscode\AI知識庫\數位佛堂\dros_academic_paper_draft.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Diagrams successfully centered and wrapped.")
