<div align="center">

<img src="dros_logo.svg" width="300" alt="DROS Logo">

# ☸️ 確定性運行時作業系統 (Deterministic Runtime OS, DROS) v7.3

**世界上最輕薄的作業系統內核，驅動最厚重的哲學法義推理。**

**DROS-RFC-001: 多語言微內核參考實現與一致性校驗**

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL%203.0-blue.svg)](https://www.gnu.org/licenses/agpl-3.0.html)
[![Official Website](https://img.shields.io/badge/Official-dr--os.io-gold.svg)](https://dr-os.io)
[![Documentation](https://img.shields.io/badge/Docs-Read-blue.svg)](https://dr-os.io/docs)
[![Commercial Shield](https://img.shields.io/badge/Protected%20By-VajraClaw-red.svg)](https://github.com/Top-Celestial-Company-Ltd/VajraClaw)

<br/>
<br/>
</div>

## 📌 什麼是 DROS？

**確定性運行時作業系統 (Deterministic Runtime Operating System, DROS)** 是全球首款基於 **微內核 + 物理檔案規範 (Microkernel + Physical File Discipline)** 架構的 AI 運行時治理引擎。

它從根本上解決了企業級 AI Agent 的三大核心痛點：
1. **幻覺 (Hallucinations)** —— 不可預測的邏輯失效。
2. **提示詞注入 (Prompt Injections)** —— 安全防線被輕易繞過與挾持。
3. **失控的 Token 成本 (Runaway Costs)** —— 依賴極度昂貴的 "LLM-as-a-Judge" 雙重審計安全機制。

不同於傳統的 RAG（檢索增強生成）或複雜的向量資料庫，DROS 透過物理層級的確定性 **金剛合約 (Vajra Contracts, 即 Markdown 規則)** 配合原生的內存安全 GuardVM，強制約束大語言模型 (LLM) 的推論邊界。

👉 **[前往我們的官方網站閱讀完整願景](https://dr-os.io)**

---

## 🏗️ 生態系架構 (Ecosystem Architecture)

DROS 的設計圍繞著嚴格的「關注點分離 (Separation of Concerns)」。為了實踐我們對通用「語意過濾晶片」的承諾，我們將核心微內核以 6 種不同的程式語言開源。

### 1️⃣ 開源核心微內核 (Open-Source Core Microkernels, 遵循 AGPL-3.0 協議)
這些倉庫包含了 `DROS-RFC-001` 規範的參考實現。它們極度輕量（僅 300-600 行代碼），並且**完全不依賴**任何第三方依賴庫。

- ⚙️ **[dros-core-rs](https://github.com/Top-Celestial-Company-Ltd/dros-core-rs)** (Rust): 內存安全、極致效能。
- 🐹 **[dros-core-go](https://github.com/Top-Celestial-Company-Ltd/dros-core-go)** (Go): 高併發雲端運行時。
- ⚡ **[dros-core-cpp](https://github.com/Top-Celestial-Company-Ltd/dros-core-cpp)** (C++): 極低延遲硬體裸奔級引擎。
- 🐍 **[dros-core-py](https://github.com/Top-Celestial-Company-Ltd/dros-core-py)** (Python): AI 原生快速原型開發環境。
- ☕ **[dros-core-java](https://github.com/Top-Celestial-Company-Ltd/dros-core-java)** (Java): 企業級跨平台節點。
- 🟦 **[dros-core-ts](https://github.com/Top-Celestial-Company-Ltd/dros-core-ts)** (TypeScript): 同構 Node & 瀏覽器運行時。

### 2️⃣ 商業熔斷盾牌：VajraClaw (閉源)
對於無法遵循 AGPL-3.0 開源協議的企業級商業場景，我們提供 **VajraClaw** 商業支援。
VajraClaw 是一個商業級的物理層 C-FFI 適配器（`vajra_claw.dll` / `.so`），能與上述任何一個開源內核無縫集成。它提供了 UUID 綁定、失控 AI 行為的硬體級保險絲熔斷機制，以及商業授權豁免。

👉 **[探索 VajraClaw 整合中心](https://github.com/Top-Celestial-Company-Ltd/VajraClaw)**  
👉 **[查看商業定價與授權方案](https://dr-os.io/pricing)**

---

## 📖 快速上手與文件 (Quick Start)

要開始使用 DROS，您只需要編寫一個簡單的 Markdown 檔案（即金剛合約 / Vajra Contract）：

```markdown
# 金剛合約：金融分析師 (Vajra Contract)

## 絕對禁止戒律 (T1)
- [T1-01] 你絕對不能提供任何醫療診斷建議。
- [T1-02] 所有財務預測分析必須在開頭加上免責聲明："PROJECTION_ONLY"。
```

有關完整的整合教學、API 參考及架構白皮書，請造訪我們的 **[官方文件中心](https://dr-os.io/docs)**。

---

## ⚖️ 授權協議與智慧財產權

- 本生態系中的架構規範與開源微內核均基於 **AGPL-3.0** 協議授權。
- 在網路應用程式 (SaaS/API) 中使用本開源內核，要求您必須將您整個應用程式代碼開源。
- 欲在專利/閉源私有部署中繞過此開源限制，您必須透過 **VajraClaw** 取得商業授權。

[與我們聯繫](https://dr-os.io/pricing) 以獲取企業合規方案、SLA 與物理隔離私有化部署選項。
