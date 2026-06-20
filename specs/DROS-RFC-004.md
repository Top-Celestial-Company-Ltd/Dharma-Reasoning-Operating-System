# DROS-RFC-004: Ontology & Governance Specification（本體論與治理規範）

```text
Document Status: Standards Track
Authors:         Jui-Cheng (Jimmy) Chen (Top Celestial Company Ltd.)
Date:            2026-06-20
Version:         1.1 (Revised Draft)
Supersedes:      N/A
Related:         DROS-RFC-001 (Kernel Protocol), DROS-RFC-003 (GuardVM & Inference Contracts)
```

---

### 摘要

DROS（Deterministic Runtime Ontology System，確定性運行時本體系統）為一套治理導向的本體運行規範，專為領域特定 AI Agent 設計。其核心在於提供受控知識存取、可驗證證據，以及受限執行能力，透過確定性架構、編譯期政策強制執行與證據繫結，解決 Agentic AI 系統在授權、追溯性與安全性方面的核心挑戰。

DROS 並非 AI 大模型，亦非單一執行系統，而是一套 **Specification + Runtime Model**，作為 Agent 治理協議層，使各領域 AI Agent 能在受治理的知識執行環境下運作。

---

### 術語約定（Requirement Levels）

本文件中的關鍵字 **"MUST"**（必須）、**"MUST NOT"**（絕不可）、**"REQUIRED"**（必要）、**"SHALL"**（應）、**"SHALL NOT"**（不得）、**"SHOULD"**（建議）、**"SHOULD NOT"**（不建議）、**"RECOMMENDED"**（推薦）、**"MAY"**（可選）、及 **"OPTIONAL"**（選擇性的），其解釋均嚴格遵循 **IETF RFC 2119**（Bradner, 1997）之規範定義。

所有宣稱相容 DROS 的系統、平台或實作，皆 **MUST** 遵守本文件中所有標記為 MUST 或 REQUIRED 之約束條款；對於標記為 SHOULD 之條款，則 **SHOULD** 提供符合性說明或替代方案文件。

---

### 核心架構

DROS 提出在現有 Model Layer 與 Retrieval Layer 之上，增加 **Governance Layer**：

```
             Agent
               │
      Governance Layer
       /      │      \
   Policy   Evidence   Audit
               │
        Ontology Layer
               │
       Knowledge Sources
               │
          LLM / Models
```

### 1. Node Schema（節點架構）

節點為原子知識單位，以物理 Markdown 檔案搭配 YAML Frontmatter 形式儲存。每個節點均具備來源生命週期。

#### JSON Schema（節點）

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "NodeID": {
      "type": "string",
      "pattern": "^T-[A-Z]{2,}-\\d{4}-\\d{4}$",
      "description": "全局唯一且不可變的識別碼，例如 T-CS-2026-0492"
    },
    "CanonicalName": {
      "type": "string",
      "description": "標準名稱"
    },
    "AliasLookup": {
      "type": "array",
      "items": { "type": "string" },
      "description": "別名與翻譯"
    },
    "Capability_Bind": {
      "type": "array",
      "items": { "type": "string" }
    },
    "Evidence": {
      "type": "object",
      "properties": {
        "SourceType": { "type": "string", "enum": ["paper", "standard", "implementation", "other"] },
        "SourceURI": { "type": "string" },
        "Citation": { "type": "string" },
        "VerificationStatus": { "type": "string", "enum": ["verified", "pending", "deprecated"] }
      }
    },
    "Content": { "type": "string" },
    "Metadata": {
      "type": "object",
      "properties": {
        "Version": { "type": "string" },
        "LastUpdated": { "type": "string", "format": "date-time" }
      }
    }
  },
  "required": ["NodeID", "CanonicalName"]
}
```

#### YAML Frontmatter 範例

```yaml
---
NodeID: T-CS-2026-0492
CanonicalName: Transformer Attention Mechanism
AliasLookup:
  - Attention
  - 自注意力機制
Evidence:
  SourceType: paper
  SourceURI: https://arxiv.org/abs/1706.03762
  Citation: Vaswani et al. 2017
  VerificationStatus: verified
---
# 正文內容
```

### 2. Relation Schema（關聯架構）

關聯形成編譯期靜態解析的有向圖。

#### Relation Edge JSON Schema

```json
{
  "type": "object",
  "properties": {
    "SourceNodeID": { "type": "string" },
    "TargetNodeID": { "type": "string" },
    "RelationType": { "type": "string", "enum": ["PREREQ", "EXTENDS", "REFERENCES", "CONTRADICTS"] },
    "ContextPropagationLimit": { "type": "number", "minimum": 0, "maximum": 1 },
    "LongestMatchPriority": { "type": "boolean", "default": true }
  },
  "required": ["SourceNodeID", "TargetNodeID", "RelationType"]
}
```

### 3. Evidence Metadata（證據元資料）

每次生成或工具呼叫均須強制附加。

（Schema 維持與前版一致，強調與 Node Evidence 的連結）

### 4. Confidence Model（信賴度模型）

採用決定論的 Fail-Closed 狀態機，分為三層：

- **Level 0 (Unknown)**：無授權本體節點  
  **動作**：拒絕或請求本體擴展（「知識庫未授權/缺乏該領域節點」）

- **Level 1 (Verified Node)**：直接證據命中  
  **動作**：正常推理

- **Level 2 (Partial Context)**：相關但不完整  
  **動作**：提供回答，並明確標示「證據不完整」

### 5. Policy Lifecycle（政策生命週期）

Vajra DSL 宣告式政策定義，採用以下生命週期：

1. Draft（草擬）
2. Compile（編譯與 AST 驗證）
3. Verify（驗證）
4. Deploy（部署）
5. Audit（稽核）
6. Revocation（撤銷）

此流程類似 SELinux、eBPF verifier 等成熟治理機制，確保政策優先於運行期檢查。

### 6. Audit Protocol（稽核協定）

#### Log Entry Schema（增強版）

```json
{
  "AgentID": "string",
  "Attempted_Action": "string",
  "Policy_Hash": "string",
  "Timestamp": "date-time",
  "Previous_Log_Hash": "string",
  "Signature": "string"
}
```

透過 Previous_Log_Hash 形成 append-only hash chain，確保不可篡改的稽核軌跡。

### 7. DROS Certified Profiles（認證 Profile）

DROS 最大商業與實務價值在於領域特定認證生態：

- **DROS-CS Profile**：整合 IEEE、ACM、RFC、arXiv 等工程知識
- **DROS-Finance Profile**：整合 IFRS、財務模型、合規標準
- **DROS-Security Profile**：整合 NIST、MITRE、OWASP 等安全框架

DROS Core + Certified Ontology Pack + Certified Agent 形成完整認證鏈，類似 ISO、FIDO 等標準生態。

### 治理原則與貢獻

- 知識由 **Ontology + Evidence + Policy** 組成，而非僅依賴向量嵌入。
- 優先採用編譯期強制執行。
- 所有行為均具物理證據與可稽核鏈。
- 將 Agent 從「生成系統」轉變為「受治理的知識執行系統」。

---

### 8. Security Considerations（資安考量）

本章節依循 IETF RFC 文件格式標準，強制說明本規範的安全邊界、潛在威脅模型與防禦機制。

#### 8.1 憑證外洩與撤銷機制（Credential Compromise & Revocation）

Agent 身份憑證（Agent Certificate）之私鑰若遭外洩，攻擊者可能以該 Agent 身份執行未授權動作。本規範之應對機制如下：

- 每個 Agent MUST 持有由 DROS-CA 簽發、具時效性（TTL）之短效憑證，最長有效期 SHOULD NOT 超過 24 小時。
- DROS-CA MUST 維護一份即時可查詢的 **撤銷清單（Revocation List, CRL）**，與 OCSP（Online Certificate Status Protocol，RFC 6960）相容。
- 一旦憑證被標記撤銷，所有 DROS Runtime 節點 MUST 立即拒絕該 Agent 的所有請求，不得有任何快取寬限期（Cache Grace Period）。

#### 8.2 Prompt Injection 防禦（Level 0 Fail-Closed 設計）

Confidence Level 0（Unknown）的 **Fail-Closed** 狀態機設計，是本系統最核心的 Prompt Injection 防禦機制：

- 當 Agent 收到任何請求，而本體庫中 **不存在** 對應的授權節點（Authorized Ontology Node）時，Runtime MUST 拒絕生成任何回應，並回傳標準化的拒絕訊息。
- 此設計從物理架構層面切斷了「越獄型 Prompt」的攻擊向量——攻擊者無法透過語言技巧誘使 Agent 生成超出本體授權範圍的內容，因為 Runtime 在執行前已完成確定性檢查。
- 此機制與「基於規則的輸出過濾」有本質區別：後者在生成後過濾，本規範是在**編譯期與推理前**即強制執行。

#### 8.3 Audit Log 防篡改（Hash Chain Integrity）

- 稽核日誌（Audit Log）MUST 使用 Hash Chain 串接，每筆 Log Entry 中的 `Previous_Log_Hash` 欄位 MUST 包含前一筆記錄的 SHA-256 雜湊值。
- 日誌儲存系統 MUST 實作 Append-Only 機制，任何修改或刪除操作 MUST 被視為嚴重的安全事件（Security Incident）並觸發告警。
- 所有 Log Entry MUST 使用 Agent 的 Ed25519 私鑰簽章（Signature 欄位），以確保不可否認性（Non-repudiation）。

#### 8.4 本規範的安全邊界（Out-of-Scope）

本規範 **不涉及** 以下安全範疇（由 VajraClaw 物理防禦層負責）：
- 底層網路傳輸加密（TLS/mTLS）
- 硬體信任根（Hardware Root of Trust / TPM）
- Agent 執行環境的沙箱隔離（Sandbox Isolation）

---

### 9. Normative References（規範性引用標準）

本規範之設計依賴以下現行國際標準。所有實作方 MUST 確保其系統與下列標準之相容性：

| 標準編號 | 名稱 | 用途說明 |
|---|---|---|
| **IETF RFC 2119** | Key words for use in RFCs to Indicate Requirement Levels (Bradner, 1997) | 本文件術語約定之依據 |
| **IETF RFC 8927** | JSON Type Definition (JTD) | Node Schema 與 Relation Schema 的 JSON 資料結構定義標準 |
| **IETF RFC 7519** | JSON Web Token (JWT) | Agent 身份憑證（Agent Certificate）的承載格式 |
| **IETF RFC 8032** | Edwards-Curve Digital Signature Algorithm (EdDSA) | 稽核日誌簽章所採用之 Ed25519 密碼學標準 |
| **IETF RFC 6960** | Online Certificate Status Protocol (OCSP) | Agent 憑證即時撤銷查詢協定 |
| **JSON Schema Draft-07** | JSON Schema: A Media Type for Describing JSON Documents | 本規範所有 Schema 定義之語法基礎 |
| **ISO/IEC 27001:2022** | Information Security Management Systems | DROS-Security Profile 認證框架之合規基準 |

---

*DROS-RFC-002 v1.1 ── Top Celestial Company Ltd. ── 2026*
