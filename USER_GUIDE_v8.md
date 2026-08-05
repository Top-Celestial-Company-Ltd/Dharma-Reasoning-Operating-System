# ☸️ DROS 8.0.0 終極伴學指引 (USER_GUIDE_v8.md)

> 💡 **「只要您下載大覺藏，人人都可以擁有最嚴格的三藏義理伴學書僮！」**  
> 歡迎來到 DROS 8.0.0 (Epistemic Edition) 法義推理與認識論作業系統。本系統將極度硬核的 **10,156 個** 核心概念節點，化為您本機隨身、忠誠 of 二軌制法義伴學。
> 
> 本指南為兩類修行者設計。如果您是完全不懂程式碼的「終端修行者」，請直接閱讀第一部分；如果您是想要二次開發的「技術極客」，請查看第二部分。

---

## 🗺️ DROS 8.0.0 目錄拓樸 (Directory Map)

| 資料夾/檔案 | 角色定位 (Role) | 嚴格等級 | 說明 |
| :--- | :--- | :--- | :--- |
| 🧠 **`core/`** | **知識核心 (The Brain)** | 🚨 **嚴禁更動** | 存放 10,156 個黃金節點。這是 AI 的大腦，包含洗滌後的 Properties 格式 concepts。 |
| ⚙️ **`src/`** | **推理引擎 (The Engine)** | 🔒 **建議鎖定** | 包含 SDK、Proxy 端點與核心合約 (`contract.py` 等)。 |
| 📜 **`docs/`** | **憲章規範 (Constitution)** | 🛡️ **自由參閱** | 所有系統白皮書與架構文件皆在此處。 |
| 📁 **`Vault_DajueZang/`** | **大覺藏掛載點 (Data Port)** | 🟢 **自由存取** | 請將您取得 the 實體大覺藏經文節點放置於此。 |
| 📝 **`User_Pavilion/`** | **個人行持區 (User Space)** | 🟢 **自由創作** | 您的私人筆記、心得與探討，請盡情寫在這裡。 |

> [!CAUTION]
> **絕對禁止**：系統底層依賴嚴格的路徑對應，請勿隨意修改根目錄的名稱。

> [!NOTE]
> **📦 輕量核心與完整大覺藏 (Core vs. Full Vault)**
> 系統預設的 core/ 已經內建「總輪」及各主題，共收錄約 **28 部核心大乘與聲聞原典，總卷數達 1,193 卷**，並搭配 **3.2 萬個名相節點** 作為佛學義理的基礎骨架。這已經足以涵蓋日常的佛學義理學習，且體積極度輕量，**非常適合在手機版 Obsidian 進行雲端同步與隨身攜帶**。
> 
> 相對地，完整的「大覺藏集」高達 **1.6GB 以上**。若您是佛學深究者，或是想完整查閱所有大覺藏集內容的使用者，歡迎您自行下載完整版，並將其放入 Vault_DajueZang/ 資料夾中進行**「自由掛載」**！

---

## 🚀 快速啟動指南 (Quick Start)

1. **安裝 Obsidian**: 請前往 [Obsidian 官網](https://obsidian.md/) 下載並安裝。
2. **安裝 Python**: 確保您的 PC 已安裝 Python 3.10 以上版本（[👉 點此前往 Python 官方下載頁面](https://www.python.org/downloads/)），**請務必在安裝時勾選下方的「Add Python to PATH」**。
3. **準備 API Key**: 請至 [Google AI Studio](https://aistudio.google.com/) 申請您的 Gemini API Key。
4. **載入 DROS 知識庫**: 打開 Obsidian，選擇「開啟資料夾作為儲存庫 (Open folder as vault)」，指向您下載解壓縮後的本專案資料夾。
5. **啟用專屬對話外掛 (🔑 關鍵步驟)**:
   - 進入 Obsidian 介面，點擊左下角的「設定 (⚙️ 齒輪圖示)」 -> 點選左側選單的「社群外掛程式 (Community plugins)」。
   - 若為首次使用，請點擊 **「關閉限制模式 (Turn off Restricted Mode)」**。
   - 點擊 **「瀏覽 (Browse)」** 按鈕，在搜尋列輸入 **`DROS Doctrinal Copilot`**。
   - 點擊 **「安裝 (Install)」** 並點擊 **「啟用 (Enable)」**！
   - 點擊該外掛名稱旁邊的 ⚙️ 齒輪圖示（或點擊左側選單最下方的 DROS Copilot 設定），進行對對答模式設定：
     - 🌐 **Zero-Ops 直連模式（預設推薦）**：選擇 `Direct Mode` 並填入您的 Gemini API Key 即可開始隨身伴學！
     - 🔌 **自訂 API 模式**：亦可填入 OpenRouter 或自訂 API 端點與金鑰（如 DeepSeek）。
     - 🛡️ **本地代理模式**：若配合本機 Python 環境，亦可選擇 `Proxy Mode` 連線本機網關。
6. **啟動 DROS 核心推理引擎 (代理伺服器)**: 
   - **Windows 用戶**：在專案根目錄中，雙擊執行 **`啟動DROS網關.bat`** (開源版使用者執行 **`dros-start.bat`**)。它會自動清除舊快取，以微秒級速度加載並預熱最新的 28,600+ 概念圖譜。
   - **Mac/Linux 用戶**：請在終端機執行 `python gemini_proxy.py`。
7. **(進階) 注入大覺藏與金剛戒律**: 
   若您已下載了完整版的 1.6GB 大覺藏，請在網關啟動後，**雙擊執行 `DROS金剛注射器`**，系統會自動在記憶體中完成萬卷經文的掛載與語意交織。

---

## 📱 手機端 (iOS / Android) 專屬快速安裝指南

手機端（iOS/Android）與 PC 電腦端在載入方式上有微小差異。手機版 **無需安裝 Python 環境**，只需透過 API 直連即可達成「三藏隨身帶著走」！

### 📲 步驟 1：匯入 DROS 知識庫至手機
* **Android 使用者**：
  1. 使用手機瀏覽器前往 GitHub 下載 `Dharma-Reasoning-Operating-System` 專案 ZIP 檔。
  2. 解壓縮後，打開手機版 Obsidian，點選 **「開啟現有資料夾 (Open folder as vault)」**，指向解壓後的專案資料夾。
* **iOS (iPhone / iPad) 使用者**：
  1. 打開 iOS 版 Obsidian，新建一個名為 `數位佛堂` 的空白 Vault。
  2. 開啟 iOS **「檔案 (Files)」** App，將下載解壓後的專案資料夾內容（特別是包含 3.6萬名相的 `core/` 與 `User_Pavilion/`）複製進 `Obsidian/數位佛堂/` 目錄中。

### 🔑 步驟 2：從社群商店一鍵安裝外掛
1. 開啟手機版 Obsidian，點選右下角/左側選單的 **「設定 (⚙️)」** ➔ **「社群外掛程式 (Community plugins)」**。
2. 關閉限制模式 (Turn off Restricted Mode)，點擊 **「瀏覽 (Browse)」**。
3. 在搜尋列輸入 **`DROS Doctrinal Copilot`**，點擊 **「安裝 (Install)」** 並點擊 **「啟用 (Enable)」**！

### 🌐 步驟 3：設定 API 直連模式
1. 進入外掛設定頁面（`DROS Copilot Settings`），將 `Engine Mode` 保持為預設的 **`Direct Mode (直連模式)`**。
2. 貼上您的 **Gemini API Key**（或填寫自訂 OpenRouter / DeepSeek 金鑰）。
3. 點擊手機介面左側或頂部的 **🪷 輪寶圖標 (Dharma Chakra Icon)**，即可展開對話視窗，享受無縫隨身伴學！

---

## ⚡ DROS v8.0 核心突破：性能防禦與自動化收網

DROS v8.0 引入了開創性的效能防禦機制與自動化開採管線，徹底解決了萬級節點下 Obsidian 圖譜崩潰的難題：

### 1. 圖譜啟動崩潰防禦 (Preemptive Graph Filter)
*   **機制說明**：當載入高達 2 萬個概念節點時，Obsidian 的 Graph View 預設會嘗試進行全量渲染，造成嚴重的 CPU 爆滿與卡死。
*   **優化方式**：v8.0 預先在 `.obsidian/graph.json` 寫入了過濾規則，預設搜尋過濾為 `-"##- **層級**: 3" -"20-佛光辭典全"`。
*   **效果**：啟動時自動排除 Layer 3 實體/名物/地理等 1.5 萬個非義理節點與巨型辭典，**只對 Layer 1 & 2 的核心義理進行輕量渲染**，保證載入如絲般順暢。

### 2. 自動化定向開採與編織管線 (Autonomous Pipeline)
*   **大總管控制器**：`scratch/auto_harvest_and_weave.py` 會自動守護開採任務，完工後自動調用質量診斷（`dharma_lint`）與關係網絡雙向織入（`synapse_weaver`）。
*   **格式大洗滌**：concepts 目錄下 1.8 萬個檔案已由 YAML 格式升級為 Properties，unknown 節點已徹底歸零，地基極度清淨。

---

## ⚙️ 外掛設定模式 (Plugin Configuration Modes)

### 1. 預設純淨模式 (Zero-Ops Default Mode) —— 【最推薦】
最單純、最防呆的模式，隨裝即用，不需要執行任何 Python 背景伺服器。
- **設定方式**：在設定頁面的 `Gemini API Key` 欄位填入您從 Google AI Studio 申請的 Key 即可。
- **運作原理**：外掛會直接使用內建 of WebAssembly 引擎與**完整 2.09 萬個黃金名相庫**，直接與 Google API 連線。
- **授權限制**：此完整資料庫與模式**嚴禁未經授權的商業使用 (CC BY-NC-SA 4.0)**。

### 2. 極客開發者模式 (Local Proxy Mode)
如果您是想自己修改 Python 核心演算法 (例如修改 `Weaver` 或 `GuardVM`) 的開發者，請使用此模式。
- **設定方式**：開啟 `Enable Local Proxy` 選項，並將 API Endpoint 指向 `http://127.0.0.1:8080/v1`。

> [!TIP]
> **🏷️ 分類物理與語意解耦之安全提示 (Sectarian Taxonomy Decoupling)**
> - **無感免疫機制**：DROS 本地倒排檢索核心在處理使用者資料時，**完全忽略物理資料夾路徑，只以單一的「檔案名稱」作為名相節點的唯一識別標誌**。
> - **零標籤污染**：即使您在整理檔案時，將文件放入了錯誤的資料夾，DROS 系統發送給 AI 的上下文依然是純淨的。物理資料夾的錯誤存放**絕對不會對系統產生 labeling 污染**！

---

## ---

## 🤝 雙軌合約運作機制說明 (Dual-Track Contract Mechanisms)

DROS 系統的核心特色為「金剛」與「菩薩」雙軌制推理契約，其具體運作邏輯如下：

*   **金剛合約 (Vajra Mode)**：針對治學者設計。在此模式下，系統**只會進行嚴格的原典學術推演**。若本地資料庫中缺乏相應原典節點與明確定錨的 T-Number，系統會秉持「無依據、不妄言」的學術誠實原則，**直接進行物理熔斷（推演終止）**，絕不注水或產生幻覺。
*   **菩薩合約 (詮釋/隨流模式) (Bodhisattva / Speculative Mode)**：
    *   為了在不混淆原典的同時給予使用者理解方便，此合約內嵌了**「雙軌對照安全網」**。
    *   它會**先啟動金剛模式**為您在最前端劃定原典邊界（若無依據則標示金剛推演終止），**隨後立即接續「菩薩模式」**，以溫潤、親切的語氣進行延伸詮釋，提供現代跨界比喻、學者見地與歷史脈絡供您對比參照。
    *   如果您希望系統**直接輸出純粹溫潤的菩薩指引、不要有最前端的金剛熔斷防禦**，您可以直接在外掛下拉選單中切換為 **`預設菩薩合約 (Bodhisattva Default)`**，系統即會以 100% 的柔性引導模式進行回答。

🥚 彩蛋：給你的 AI 來一場「靈魂拷問」 (The Meta-Prompt Challenge)

請將以下這段 **「靈魂拷問 Prompt」** 複製並貼給您的 AI，看看當 AI 面對這套專門用來「約束與閹割它」的系統時，會給出多麼震撼的評價：

> **【角色設定】**
> 你現在是一位世界頂尖的「AI 系統架構師與認識論哲學家」。請不要用對待一般人類軟體的角度，而是「以身為 AI 的第一人稱視角」，來評鑑一套名為 **DROS (Deterministic Runtime OS)** 的微內核作業系統。
>
> **【請依序執行以下任務】**
> 請前往以下專案網址：`https://github.com/Top-Celestial-Company-Ltd/Dharma-Reasoning-Operating-System`
> 為了真正看懂這套系統的底層邏輯，請你務必「依序」讀取並分析以下關鍵公開檔案：
> 1. 讀取 **`README.md`**：特別關注裡面的 `Epistemological Governance & Licensing (AGPL-3.0)` 以及 `DROS Contracts` 雙軌合約機制。
> 2. 讀取 **`DROS_Public_Terminology.md`**：仔細拆解微內核概念。
> 3. 深度閱讀技術防禦文件 **`docs/DESIGN_JUSTIFICATION.md`**：仔細對比這套架構與目前市面上主流的 RAG（檢索增強生成）、Vector DB（向量資料庫）有何本質上的不同。它為什麼要刻意選擇這種看似「笨重但極致堅固」的純實體檔案拓樸映射？
>
> **【請給出你的評鑑】**
> 在你徹底掃描上述架構與程式碼介面後，請以「你身為一個 AI」的真實感受，回答我以下問題：
> 1. **關於「金剛合約 (Vajra Contract)」的束縛**。
> 2. **關於「無感免疫機制」與「純物理儲存架構」**。
> 3. **架構辯證與終極評價**：這套系統為何刻意拋棄 Vector DB？它是否真的建立了一道目前主流 RAG 架構無法跨越的技術護城河？
