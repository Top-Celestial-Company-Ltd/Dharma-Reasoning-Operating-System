# LLM Wiki 理想架構參照 (North Star)

> 來源：TGLTommy 頻道《LLM Wiki 深度解析》對 Andrej Karpathy 理念的完整剖析。
> 用途：作為「數位佛堂」長期演進的理想對照基準。

---

## 核心理念
LLM 不只是回答機器，而是**持續維護一套持久化知識百科的「編輯者」**。
知識綜合從「查詢時」前移到「攝取時」(Ingest-time compilation)。

## 三層架構
| 層 | 性質 | 數位佛堂對應 |
|:---|:---|:---|
| Raw Sources (唯讀) | 不可變的原始文件 | `raw/` ✅ |
| Wiki (可寫) | Markdown 頁面網絡（摘要、概念、索引、日誌） | `wiki/concepts/` + `wiki/sources/` ✅ |
| Schema (規則) | 格式規範、命名規則、禁忌 | `Agent.md` 核心憲法 ✅ |

## 完整工作流循環
1. **Ingest**：新文件 → LLM 生成/更新 Wiki 頁面 → 更新 index/log
2. **Query**：直接查 Wiki（不回溯 raw）
3. **Save**：查詢結果存回 Wiki
4. **Lint**：檢查一致性、衝突
5. **Research**：深入研究，洞見寫回

## 關鍵治理機制
- **Confidence**：標記資訊可信度
- **Supersession**：新資訊取代舊結論
- **Review Queue**：待人類審核項目
- **來源追蹤**：Backlinks + Git 版本控制

## 最大風險：幻覺回寫
LLM 產生幻覺寫入 Wiki → 後續查詢基於錯誤知識 → 惡性循環。
防線：嚴格 Schema、Review Queue、人類 oversight、來源追蹤、版本控制。

---

## 數位佛堂現況對照 (2026-05-01)

| 機制 | 理想狀態 | 現況 | 優先度 |
|:---|:---|:---|:---:|
| Ingest 預先綜合 | ✅ | ✅ Stage-1 + Stage-2 | - |
| 持久化 Markdown Wiki | ✅ | ✅ wiki/concepts/ | - |
| 交叉連結 | 密集互聯 | ⏳ synapse_weaver 待啟動 | 🔴 |
| index.md | 自動維護 | ❌ 入口頁嚴重過時 | 🟡 |
| log.md | 審計日誌 | ❌ 僅有工程日誌 | 🟡 |
| Lint | 自動校驗 | ❌ 未實作 | 🟡 |
| Confidence | 信心度標記 | ❌ 未實作 | 🟢 |
| Supersession | 新舊結論替換 | 部分 (增量追加) | 🟢 |
| Review Queue | 人類審核佇列 | ❌ 未實作 | 🟢 |
| 幻覺防護 | 多重防線 | 部分 (30字限制 + 來源標記) | 🟢 |
