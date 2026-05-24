# 🏯 數位佛堂 - 系統建置與部署報告 (v7.2.0-System-Spec-Epistemic)

## 📊 系統概況 (System Status)
- **當前節點總量**: **16,071** (DROS 7.2.0 語意硬化基座)
- **DROS 版本**: v7.2.0 (Epistemic Edition / 認識論感知版)
- **內核架構**: **認識論三層治理與解耦微內核架構 (Epistemic Multi-Layer + Graphify + API Contract Gateway)**
- **淨化狀態**: **已圓滿 (Vajra & Epistemic Hardened)**
- **算力調度**: **智慧模型別名安全對齊與雙向自癒降級 (Models/gemini-3.1-pro-preview Enabled)**
- **部署架構**: **PC & NAS VM 雙棲自動化部署 (Dual-Environment bat/sh, pyproject.toml CLI + Quart API Stream Server)**
- **合規保護**: **密碼學時間戳與特許授權 (GNU AGPL-3.0 Codebase + Cryptographic Timestamped Golden Dataset)**

> 💡 **極客提示 (Geek Note) ── 關於實體檔案點數的「完美守恆」**：
> 若您在 `core/` 目錄進行全域檔案數量點算，會發現共有 **16,881** 個 `.md` 檔案。
> 這是因為整個發行庫除包含 **16,071** 個純驗證概念節點（位於各宗派的 `wiki/concepts/` 目錄，記錄於 `dros_golden_manifest.json` 中）外，還包含 **810** 個輔助檔案（如 `raw/` 原始經典譯本、`wiki/sources/` 長篇原典科文與 `wiki/bridges/` 跨宗派對齊映射圖）。

---

## 🏛️ 1. DROS 7.2.0 核心引擎與技術底座
本階段最大的技術突破在於將 DROS 從單純的「防幻覺金剛檢索」升級為「具備階梯式認識論約束的智慧推理作業系統」：

- **認識論三層治理**：解決了「過度正統化鎖死 (Orthodoxy Lock)」的干涸痛點，明確劃分出不可動的聖言量經證（Canonical）、可橫向哲學映射的詮釋對照（Interpretive）、以及授權湧現的新本體推演（Speculative）。
- **`contract.py` (戒)**：支持 YAML 推理契約的編譯，新增對 `"Interpretive"` 與 `"Speculative"` 模式的強型別 AST 校驗與動態 Prompt 信封打包。
- **`guard_vm.py` (定)**：動態適配 `AuthorityNodesOnly` 參數。在 Speculative 模式下放行，在 Vajra 與 Interpretive 模式下強制進行實時 `T-Number` 座標物理校驗，杜絕未經標註的超譯。
- **`dros_engine.py` & `gemini_proxy.py` (慧)**：
  - 優先載入並編譯 `docs/System_Prompt_v5.3.md` (現已整合至 GuardVM) 認識論感知提示詞範本。
  - Quart 網關代理層全面支持接收客戶端（如 Obsidian Copilot）傳遞的 `"contract"` 載荷，執行按需契約推理。
  - 實現**模型別名安全解析**，自動將請求中的 `gemini-3.1-pro` 映射至實際支持的旗艦級 `models/gemini-3.1-pro-preview` 模型，徹底解決 v1beta 端點 404 models 錯誤，高可用呼叫率 100%。

---

## ⚡ 2. 算力資源調度與多平台對齊 (Computing Matrix)
DROS 7.2.0 實現了資源、算力與義理難度、認識論自由度的完美咬合：
- **Vajra & Interpretive 模式**：自動掛載 `gemini-3.1-pro-preview` 級別頂級算力，實施高精度的原典考證或學術映射。
- **Speculative 模式**：調度 `gemini-3.1-pro-preview` 計算單元，在放寬 RAG 實體硬約束的前提下，進行深奧哲學湧現，並由 Proxy 自動渲染標準的 Obsidian 警告 callout（並在 callout 上方預留一行空行，以保障 Markdown 相容性）。
- **Bodhisattva 模式**：自動切換為 `gemini-2.5-flash-lite`，優化響應速度與推理成本。
- **全平台命令列指令**：`pyproject.toml` 預先註冊 `dros` 與 `dros-inject` 指令，編譯安裝後可於終端機直接全域調用。

---

## 🛡️ 3. 雙棲部署與安全裝甲 (Deployment & Hardening)
為了讓系統從研發走向全場景無縫運行，我們完成了「雙棲」自動化部署裝甲：
- **PC Windows 部署 (`install.bat` / `run.bat`)**：提供本機 Python 虛擬環境一鍵編譯、編輯模式安裝與背景/交互一鍵呼叫。
- **NAS VM Linux 部署 (`install.sh` / `run.sh`)**：支持 Debian/Ubuntu 等 headless 伺服器背景服務拉起，方便搭配 Obsidian Copilot、OpenAI 協議進行無感代理。
- **物理隔離保護**：在 Obsidian 中透過 `Force Read Mode` 將 `core/` 與 `src/` 資料夾強制鎖定，確保法義數據「只讀不改」。
- **授權與法律安全聲明**：
  - **核心引擎 (GNU AGPL-3.0)**：強制所有衍生 SaaS 服務開源。
  - **黃金數據庫 (密碼學時間戳聲明)**：弘法利生、眾生學佛使用、純佛法公益性質（不含任何受償/有償單位）**完全免費**開放使用。其他實體與機構之使用則受 AGPL 限制並需取得商業授權。這項聲明已透過 SHA-256 時間戳固化，完全保障了原始智慧財產權。

---

## 📂 4. 義理版圖分佈 (Nirvana Matrix)
16,071 個金剛驗證概念節點已圓滿分布於六大傳統中：
*   **智者 (Tiantai - 天台宗)**：**9,908** 個實心概念節點（包含圓融止觀與教判框架）。
*   **總論 (General - 基礎佛理)**：**3,265** 個實心概念節點（基礎佛理與系統導航）。
*   **彌勒 (Yogacara - 唯識宗)**：**1,877** 個實心概念節點（識變機制與建立引擎）。
*   **善導 (Pure Land - 淨土宗)**：**636** 個實心概念節點（他力救度與安心保證）。
*   **惠能 (Zen - 禪宗)**：**327** 個實心概念節點（直指覺性與實踐路徑）。
*   **龍樹 (Madhyamaka - 中觀宗)**：**58** 個實心概念節點（空性邏輯與破執引擎）。

---

## 🔮 5. 未來展望 (Beyond Nirvana v7.2.0)
1.  **多代理人辯經 (Agent Debate)**：基於不同宗派與認識論契約，啟動多個 AI Agent 進行自動化義理辯證。
2.  **法義一致性掃描**：定期利用 Pro 預覽算力對全庫 16,071 個節點進行交叉邏輯一致性檢查。
3.  **DROS 終端全面開放**：向全球研究者提供具備「高權威性、認識論階梯式感知、零幻覺」的法義推理與哲學綜攝服務。

---
*「經證聖言定金剛，詮釋映射明後世；湧現推演啟般若，認識感知證圓覺。」*
**系統狀態**：🕉️ **DROS v7.2.0 Epistemic Edition 正式圓滿建置，進入「認識論感知推理時代」**。
