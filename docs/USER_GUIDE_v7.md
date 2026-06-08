# 🏯 DROS 7.1 使用者與本地部署手冊 (USER_GUIDE_v7.md)

> 💡 **「只要您下載大覺藏，人人都可以輕鬆擁有～三藏十二部的伴學書僮！」**  
> 歡迎來到 DROS 7.1 (Epistemic Edition) 法義推理與認識論感知作業系統。本系統將極致硬化的 16,071 個核心概念節點與大覺藏原典，化為您本機隨身、忠誠不二的數位法義伴學者。

本手冊專為兩類同行者設計：如果您是完全不懂程式碼的「一般用戶/學習者/修行者」，請直接閱讀【第一部分：小白零門檻三步通關】；如果您是需要二次開發的「技術極客」，請查閱【第二部分：開發者與技術玩家進階手冊】。

---

## 🗺️ DROS 7.1 數位道場地圖 (Directory Map)

在您開始使用前，請先熟悉資料夾的「性格」與「禁忌」：

| 資料夾名稱 | 角色功能 (Role) | 安全等級 | 修改建議 |
| :--- | :--- | :--- | :--- |
| 📁 **`core/`** | **系統大腦 (The Brain)** | 🟥 **極度危險** | **禁止手動修改**。這裡存儲了 16,071 個已硬化的法義節點，隨意更動會導致 AI 推理產生幻覺。 |
| 📁 **`src/`** | **運作引擎 (The Engine)** | 🟥 **系統禁區** | 包含微內核 SDK 與倒置檢索模組。除非您是開發者，否則請勿更動裡面的 `.py` 檔案。 |
| 📁 **`docs/`** | **法義憲法 (Constitution)** | 🟡 **小心維護** | 存放手冊與 AI 提示詞模板。技術玩家可在此微調 AI 的對話語氣。 |
| 📁 **`Vault_DajueZang/`** | **大覺藏輸入區 (Data Port)** | 🟢 **自由存取** | 您取得的辭典素材請放入此處。 |
| 📁 **`User_Pavilion/`** | **個人行持區 (User Space)** | 🟢 **自由存取** | 存放您自己的研經筆記、感悟與對話紀錄，這是您個人的修行空間。 |

> [!CAUTION]
> **警告**：請勿刪除 any 以 `.` 開頭的隱藏檔案（如 `.obsidian`），它們是確保資料庫在 Obsidian 中正常運作的環境設定檔。

---

# ☸️ 第一部分：小白零門檻三步通關（有手就會）

本指南不要求您打開終端機，也不需要您手寫任何程式碼。請跟隨以下四個簡單步驟，即可在您的本地 PC 上建構完美的數位佛堂，並掌握契約推理的核心心法。

### 📥 第一步：蓋道場（環境與資料夾準備）
1. **下載並安裝 Obsidian**：請前往 [Obsidian 官網](https://obsidian.md/) 下載安裝。
2. **安裝 Python 引擎**：請至 [Python 官網](https://www.python.org/) 下載 Python 3.10 以上版本。**⚠️ 重要：安裝時請務必勾選「Add Python to PATH」！若已安裝則省略此步驟**
3. **申請 AI 鑰匙**：前往 [Google AI Studio](https://aistudio.google.com/) 免費申請一組 Gemini API Key 並複製備用。（*註：系統底層採用極致輕量、高速的 Gemini Flash-Lite 模型，日常查詢皆在免費額度內，請安心申請使用。*）
4. **準備 DROS 資料夾**：解壓縮本專案，並將您的辭典 Markdown 檔案放入 📁 `Vault_DajueZang/20-辭典/`。

### ⚡ 第二步：物理注血（一鍵激活金剛內核）
1. 進入專案根目錄。
2. **雙擊執行 `雙擊執行-DROS金剛注射器.bat`**。
3. 腳本啟動後，**會先自動偵測並請您輸入 API Key**。接著請靜待系統載入大覺藏索引並自動完成全自動的 T-座標語義硬化。

### 🪷 第三步：智慧流露（啟動預裝的 🪷 DROS Copilot 專屬側邊欄，開箱即用）
1. **打開 Obsidian**：選擇「開啟資料夾作為儲存庫」，點選整個 `DROS 資料夾`。
2. **點擊左側 🪷 輪寶圖標**：本系統已預裝並預設啟用專屬的 **`DROS Copilot`** 伴學面板。直接點擊 Obsidian 左側功能列的 **🪷 輪寶圖標 (Dharma Chakra Icon)**，即可瞬間喚醒精美的「暗黑禪風玻璃擬態」對話面板！
3. **四大靈魂功能，0 設定、0 門檻駕馭**：
   * **🌐 EN / 中文 語言切換**：點擊頂部的 `🌐 EN` 鍵，整套介面與 Notices 將瞬間轉換為高雅的學術英文，且當前對話歷史 100% 留存並即時無損重繪！
   * **📿 金剛 / 🌊 菩薩 合約切換**：一鍵在「嚴格聖言量引證」與「現代詮釋推演」之間快速切換，為您提供無比清晰的認識論邊界！
   * **📎 連結當前編輯筆記**：一鍵將您目前在編輯器中寫入的個人筆記與感悟，動態注入 AI 的推理上下文中，實現智慧的自增長與 compounding 複利！
   * **💾 存入館藏 (User_Pavilion) 黃金存檔**：在 AI 回答下方點擊此按鈕，系統會自動淨化您的提問，以 DROS 7.0 標準結構化格式排版，一鍵物理存檔入 `User_Pavilion/` 並自動打開，開始您的智慧編織！
4. **快捷定錨**：在主編輯器中，用滑鼠選中任何佛教名相，按下智慧熱鍵 **`Alt + D`**，即可直接在就地觸發義理定錨查詢，並自動將選中文字編織為雙鏈 `[[名相]]`！
5. **🌐 英文使用者指引 (English User Guide)**：
   * **中文佛經背景檢索，學術英文輸出 (Bilingual Dual-Track Reasoning Strategy)**：
     * **中文說明**：為了維持佛陀教言與唯識/天台名相最精純的原始語意，DROS 在後端會繼續以 100% 精確的「中文大覺藏經典」與「16,071 個中文本體節點」進行毫無扭曲的高維圖尋址與檢索；而在終端，AI 判官會將整套嚴密的義理推演，自適應合成為 **Oxford/Harvard 學術級的高雅英語**，並自動以斜體標註 Sanskrit 梵文、以中括號標註中文原文（例如：*Tathātā* [真如] 或 *Ālayavijñāna* [阿賴耶識]）。這在確保法義精準不走樣、不稀釋的前提下，為您提供無障礙的跨語系研究體驗！
     * **English Guide**: To preserve the pristine doctrinal integrity of Shakyamuni Buddha's teachings and highly technical terms (Yogācāra/Tiantai terminology), DROS maintains its backend retrieval strictly in Traditional Chinese utilizing the **16,071 physically hardened high-fidelity Chinese nodes and Tripiṭaka source texts**. In the frontend, the reasoning engine dynamically synthesizes and translates the strict doctrinal derivations into **high-caliber Oxford/Harvard academic English**. Sanskrit terms are rendered in *italics* and original Chinese concepts are placed in brackets (e.g., *Tathātā* [真如] or *Ālayavijñāna* [阿賴耶識]). This provides English-speaking scholars and practitioners with zero-dilution, high-precision academic Dharma research. Simply toggle the **🌐 EN button** in the Copilot header to instantly enjoy this cross-lingual wisdom!

### 📜 第四步：心法融入（如何發揮 DROS 7.1 認識論感知版 的最佳威力）

恭喜您！您的數位道場已經正式運作。但在您開始與 AI 進行第一場法義探討之前，請先熟讀以下由 **康宸園有限公司/Jimmy Chen** 撰寫的「使用心法」：

> ### 🧠 DROS 7.1 使用心法 — 給追求法義正確性與理性思維的行者
> 
> DROS 不是一個普通的佛學聊天機器人。
> 它是一套「受契約與認識論邊界嚴格約束」的法義推理系統，目的在於盡可能降低 AI 幻覺，並同時保持智慧湧現的活性，明確劃分「原典經證」與「後世詮釋」的界線。
> 
> #### 一、 DROS 7.1 的四個認知層級（認識論治理）
> 
> *   **1. Canonical Layer（聖言量核心 / strict_vajra 模式）**
>     *   **最高嚴謹度**：零容忍幻覺。
>     *   **特點**：強制 `AuthorityNodesOnly: true`。AI 僅基於大覺藏實心節點進行精確推演，每一段核心結論均標註 `[T-Number]` 座標或經論出處。若資料不足，會老實說明限制並回絕幻覺生成。
>     *   **適合**：嚴肅佛學研究、原典比對、經教考證。
> 
> *   **2. Interpretive Layer（詮釋映射層 / balanced_vajra 模式）** ← *推薦大多數人使用*
>     *   **定位**：在嚴謹考證與現代詮釋間建立橋樑。
>     *   **特點**：維持 `AuthorityNodesOnly: true`，`GuardVM` 依然進行實時 `T-Number` 校驗。但允許跨宗派比較、義理映射與現代哲學/心理學對照，**且段落開頭強制標註：`[義理映射 / Interpretive Mapping]`**，使您能瞬間識別原典本意與後世衍生詮釋。
>     *   **適合**：教學教理梳理、現代心理學/認識論與佛法心識機制的對照。
> 
> *   **3. Speculative Layer（般若高階推演層 / speculative_prajna 模式）**
>     *   **定位**：授權 AI 進行最高限度的邏輯延展與新本體湧現。
>     *   **特點**：放寬限制至 `AuthorityNodesOnly: false`（`GuardVM` 繞過強制 `T-Number` 審計，防止誤傷）。允許 AI 與量子力學觀測者效應、神經科學腦電湧現等前沿學門進行顛覆性的綜攝。
>     *   ** Obsidian 渲染守則**：為了確保筆記的美觀與可讀性，所有推演段落前**必須預留一空行**，並強制包裹在 Obsidian 警告 callout 中：
>         ```markdown
>         
>         > [!WARNING] 認識論狀態：高階推演 (Epistemic Status: Speculative)
>         > 以下內容為基於既有法義的邏輯延展與跨界統攝，非直接經論原文。
>         ```
>     *   **適合**：思想實驗、哲學創新、啟發性禪修沉思、破除教條主義。
> 
> *   **4. Bodhisattva Layer（菩薩隨流層 / bodhisattva_default 模式）**
>     *   **定位**：溫潤、清晰、生活化。
>     *   **特點**：流暢自適應，允許譬喻引導，在結尾優雅說明資料局限性。
>     *   **適合**：生活煩惱疏導、初學者入門引導。
> 
> #### 二、 使用 DROS 的正確心態
> 
> 1. **DROS 是工具，不是善知識**
>    它擅長「文字義理的精準對齊與階梯式認識論推演」，但無法替代真人師承與實修體驗。
> 2. **越明確的問題，得到越精準的回答**
>    *   *較佳提問方式*：「請以唯識宗觀點，解釋阿賴耶識與種子現行的關係，並引用相關經論。」
>    *   *較佳對照提問*：「如何以現代認知科學對照阿賴耶識？請在 Balanced Vajra 模式下進行。」
> 3. **懂得切換模式，是使用者的基本能力**
>    *   **後端三核心策略**：DROS 核心引擎在底層支持三種認識論契約：`strict_vajra` (極致嚴格聖言量)、`balanced_vajra` (平衡心理學映射) 與 `speculative_prajna` (思辨般若探索)。
>    *   **前端雙軌簡約化 (Obsidian Copilot GUI)**：在側邊欄面板中，為了保持極致的禪意簡約與流暢交互，我們將其完美歸納為**「金剛/菩薩」雙軌按鈕**：
>        *   📿 **金剛 (Vajra) 按鈕**：對應後台的嚴謹經證軌道（自動調用 `default_vajra` / `strict_vajra`）。
>        *   🌊 **菩薩 (Bodhisattva) 按鈕**：對應後台的思辨般若軌道（自動調用 `speculative_prajna`，釋放跨領域/量子力學與佛法思辨）。
>        *   *提示*：若您需要在 Copilot 中強制指定 `balanced_vajra` 或 `strict_vajra` 的細微文風，您除了可以使用「金剛」按鈕，更可以利用全新的「自訂 Prompt 隔離艙」，直接在您的個人筆記中以白話文引導 AI：「請以 balanced_vajra 的溫和風格為我解讀」！
> 
> ---
> **結語**
> 「經證歸聖言，映射明後世，
>   湧現啟般若，理事無礙彰。」
> 願您善用 DROS 7.1 這套認識論地圖，深入經藏，智慧如海。
> 
> ---
> **DROS 7.1 系統聲明：本道場已建立不可跨越的推理邊界。**

---

### 🎨 高階心法：自訂 Prompt 隔離防污染艙與可視化智慧整合
如果您想讓 AI 的對話風格、語氣更符合您的個人修行習慣，我們為您設計了**「物理安全隔離防污染機制」**與**「可視化提示詞構建面板」**，您**完全不需要、也不應該直接修改 system/docs 等系統核心文件**，更不需要在自訂筆記中背誦任何火星文標記：

1. **建立您的專屬提示詞**：在您的個人行持區 `User_Pavilion/` 中建立一個新的 Markdown 檔案（例如 `User_Pavilion/custom-prompt.md`），在裡面寫下您自訂的 AI 設定（例如：在回答結尾加上一句鼓勵修行者的法語，或自訂論述風格，此檔案為純白話文，無須寫入任何代碼標籤）。
2. **視覺化整合與開關選單**：進入 Obsidian DROS外掛設定面板，填寫 **`📜 自訂 Prompt 筆記路徑`** 後，外掛會自動解鎖**「🎯 自訂 Prompt 整合模式」**面板。您可以使用簡單的下拉選單與開關輕鬆客製化技術元件的注入方式：
   - **後置模式 (suffix - 推薦)**：將系統的核心技術提示詞放在最上方，您的白話文自訂提示詞接在最尾端（此為 LLM 行為微調的最精確位置）。
   - **前置模式 (prefix)**：將您的自訂提示詞放在最上方，系統的核心技術提示詞在後面。
   - **進階完全自訂模式 (advanced)**：適合高階玩家。如果您想自由安排排版位置，可以在您的 Markdown 筆記中手動書寫佔位符：`{{EXECUTION_CONTRACT}}`（契約防線）、`{{INJECTED_NODES}}`（大覺藏原典檢索）與 `{{RUNTIME_MODE}}`（運行模式）。
3. **智慧組件開關控制 (在後置/前置模式下啟用)**：
   - 📿 **自動注入推理契約**：決定您的自訂 Prompt 是否依然受到「金剛/菩薩」合約規約與禁用詞的嚴格約束。
   - 📚 **自動注入大覺藏節點**：決定是否讓系統將本地圖譜檢索出的實心名相與 T-Number 座標動態餵給 AI，拒絕幻覺。
   - ⚙️ **自動注入運行時模式**：決定是否自動拼接運行時狀態變數，引導 AI 渲染特定的本體排版。
4. **系統預設隱藏強制唯讀艙**：如果您將自訂 Prompt 路徑留空，系統會自動啟動**「雙軌 Force-Read 強制唯讀」**機制。外掛會直接物理讀取隱藏在 `.obsidian/plugins/dros-doctrinal-copilot/System_Prompt_v5.3.md` 路徑下的官方核心提示詞。該路徑在 Obsidian 介面中完全隱藏不可見，從根本上杜絕了用戶在寫作過程中對核心 System Prompt 的意外修改或損壞！

---

### 💡 進階守護：金剛護體（Obsidian 唯讀防禦與唯寫修行空間）
為了捍衛 16,071 個實心名相經證的絕對安全性，防止 AI 被主觀隨記污染，我們將數位佛堂物理劃分為「唯讀經證區」與「唯寫修行區」。強烈建議您在 Obsidian 中進行以下權限防護：

#### 1. 安裝唯讀外掛
1. 在 Obsidian 設置中搜尋並安裝 **`Force Read Mode`** 外掛。
2. 進入該外掛的 `Target paths` 設置，輸入以下路徑（每行一個）：
   - `core/**`（將整個 16,071 核心名相數據庫與系統腳本鎖定為唯讀）
   - `docs/**`（鎖定使用手冊與行為憲法）
   - `Vault_DajueZang/**`（鎖定經文原始碼）
   - 如個人有需要研讀、研究特定佛經、論典，可於自行下載的大覺藏集中複製相關檔案到使用者專區資料夾：`User_Pavilion/research_data/`，再於 `research_data/` 資料夾下建立子資料夾，如`research_data/善導`, `research_data/彌勒`, `research_data/惠能`, `research_data/智者`, `research_data/總論`, `research_data/龍樹`, `research_data/Long_Classics`，並將相關資料放至對應資料夾。

> [!TIP]
> **🏷️ 分類物理與語意解耦之安全提示 (Sectarian Taxonomy Decoupling)**
> - **無感免疫機制**：DROS 本地倒排檢索核心在處理 `User_Pavilion/` 底下的使用者資料時，**完全忽略物理資料夾路徑，只以單一的「檔案名稱」作為名相節點的唯一識別標誌**。
> - **零標籤污染**：即使您在整理檔案時，誤將《唯識三十頌》（唯識宗/彌勒）放入了 `research_data/惠能`（禪宗）資料夾，DROS 系統發送給 AI 的上下文依然是純淨的 `--- 節點: 唯識三十頌 ---` 與內文。AI 只會基於內容本身的唯識宗法義進行高精確度的經證推理，物理資料夾的錯誤存放**絕對不會對系統產生 labeling 污染，亦不會誤導 AI 對宗派義理的辨識**！請放心將其視為您個人隨心所欲整理的彈性沙盒。

#### 2. 唯寫與開採沙盒規劃
在設定完唯讀鎖後，您的 Obsidian 道場將呈現如下的寫入權限分佈：
*   **`User_Pavilion/` (個人行持區) — 🟢 100% 自由唯寫**：這是您唯一的個人隨記、感悟、行持日記與 Copilot 對話檔案存放處。您可以自由創建、編輯與刪除筆記，這是您的個人道場。
*   **`core/AI <宗派>/wiki/inbox/` (智慧收件匣) — 🟡 暫存編輯與審查**：當您運行自動開採腳本時，AI 產生新概念草稿的地方。為了允許您編輯與驗證這些草稿，**請在 `Force Read Mode` 中設定排除或例外路徑**：
    *   在唯讀路徑中**排除**：`**/inbox/**` (這樣您在 review 新概念時就能自由修改它們)

---

### 🔬 智慧 compounding：如何善用「手動編織」累積智慧？
DROS 7.1 不是死板的靜態資料庫，而是一個「會隨著您的研讀與修行過程自我成長」的法義系統。藉由 Obsidian 原生強大的 `[[雙向連結]]` 功能，您可以輕鬆在個人專區與 16,071 個核心名相之間建立神經連結，實現 **「智慧 compounding 循環」**：

```
1. 建立個人研經筆記 (存放於 User_Pavilion/ 下)
        ↓
2. 手動編織 (使用 [[雙向連結]] 語法與 16,071 個核心名相建立關聯)
        ↓
3. 智慧複利 (Graphify 本地圖譜倒置檢索自動載入，AI 推理能力自我倍增！)
```

#### 🛠️ 三步操作指南（有手就會）：
1.  **第一步：開啟新筆記**：在 `User_Pavilion/` 中建立一個新的 Markdown 檔案（例如 `User_Pavilion/我的唯識筆記.md`），記錄您的研經感悟、修行日記或原文。
2.  **第二步：手動編織突觸**：當您在筆記中寫到某個佛學概念時，直接輸入雙中括號語法，如 `[[無常]]` 或 `[[真如]]`，將其與 core 目錄下的 16,071 個核心名相進行雙向連結。
3.  **第三步：激活智慧複利**：完成連結後，您的個人研經筆記已與原有的核心節點完美編織在一起！DROS 的 Graphify 本地圖譜檢索器在您下一次進行 Copilot 對話查詢時，會自動透過這條連結，將您的個人研經筆記作為「高權威上下文」一起餵給 AI。您的數位佛堂正式完成了專屬的智慧增量！


---

# ⚙️ 第二部分：開發者與技術玩家進階手冊

DROS 7.1 (Epistemic Edition) 不僅服務一般修行者，更為具備技術能力的開發者提供了兩套強大的本地集成方案：**DROS Contract SDK** (底層嵌入與精準推理) 與 **OpenAI-Compatible Proxy** (無感代理與 Obsidian Copilot 協同)。

---

## 1. 📦 DROS SDK (Contract-Driven API) 呼叫與部署規範

DROS 7.1 已完成完整的跨平台虛擬化打包。不論是在 Windows PC 還是 Linux NAS 伺服器上，均可透過一鍵部署工具安全跑通。

### 1.1 PC Windows 一鍵部署
在專案根目錄下，直接雙擊執行 **`install.bat`**，它會自動：
*   建立本地的 Python 虛擬環境 `venv/`
*   升級 pip 並以 editable 模式 (`pip install -e .`) 編編譯安裝 DROS 核心
*   自動註冊全域命令行指令 `dros` 與 `dros-inject`！

啟動 CLI 推理：
*   雙擊 **`run.bat`** 或在 CMD 中執行 `dros` 或 `run.bat "阿賴耶識"`

啟動本地 Proxy 服務：
*   在 CMD 執行 `run.bat serve` 或在虛擬環境下執行 `dros --serve`

### 1.2 Linux / Ubuntu Server (NAS VM) 一鍵部署
開啟終端機，執行以下命令：
```bash
chmod +x install.sh run.sh
./install.sh
```
`install.sh` 會自動更新 apt 包管理器並部署 `python3-venv`，完成後您可以執行：
*   交互式 CLI 查詢：`./run.sh`
*   無縫拉起背景代理伺服器：`./run.sh serve`（建議搭配 Systemd 或 nohup 實現守護進程）

---

## 🐍 2. Python 整合與二次開發範例代碼

如果您要在您自己的 Python 應用中嵌入 DROS 7.1 推理能力，可以直接調用 DROS 核心引擎。

### 2.1 引用 DROS 核心 API
```python
import os
from src.config import init_config
from src.engine.dros_engine import DrosEngine
from src.engine.contract import InferenceContract

# 1. 初始化系統全域配置（自適應多級上溯尋址）
init_config()

# 2. 初始化微內核推理引擎
engine = DrosEngine()

# 3. 載入金剛合約 (YAML Contract)
contract = InferenceContract.load("strict_vajra")

# 4. 執行精確法義推理
query = "阿賴耶識"
print(f"[*] 正在向 DROS 核心請求法義推理: '{query}'...")
result = engine.ask(query, contract=contract)

# 5. 解析輸出結果
if result["status"] == "success":
    print("\n【金剛推理輸出】:")
    print(result["content"])
    print(f"- 算力調度單元: {result['model_used']}")
    print(f"- 運行時模式: {result['runtime_mode']}")
    print(f"- 引證核心節點: {result['sources']}")
else:
    print(f"\n[!] 推理未通過 GuardVM 斷言，原因: {result.get('reason')}")
```

---

## 3. ⚙️ 進階：對接第三方通用 Obsidian Copilot 外掛（供技術玩家二次開發使用）

> [!NOTE]
> **提示**：我們已經在系統中為您**預先安裝並啟用了 DROS 專屬獨立外掛 `DROS Copilot`**，自帶所有大圓滿功能與最極致的暗黑禪風視覺體驗，**一般用戶完全不需要進行以下配置**！
> 以下內容僅供需要使用第三方通用 `Copilot` 外掛、或進行客製化 API 二次開發對接的技術玩家閱讀。

### 3.1 啟動本地代理伺服器
雙擊根目錄下的 **`run.bat serve`**，或是在 NAS 上執行 **`./run.sh serve`**，伺服器將在本地 `http://localhost:5000` 啟動，完全相容 OpenAI 的 `/v1/chat/completions` API 與 SSE 串流協議。

### 3.2 設定第三方 Copilot 外掛
1. 在 Obsidian 中，開啟「設定」 -> 「社群外掛」 -> 搜尋並安裝第三方 **`Copilot`** 外掛。
2. 進入該外掛的設定介面，進行以下配置：
   - **Provider (服務商)**: 選擇 `OpenAI Compatible`。
   - **API Key (金鑰)**: 隨意輸入任意字元（如 `dros-7-token`，因代理會自動在本地載入您的環境金鑰）。
   - **Endpoint (伺服器網址)**: 輸入 `http://localhost:5000/v1`。
   - **Model (指定模型)**: 輸入 `pro`（後台將自動安全映射至頂級算力 `gemini-3.1-pro-preview`）。
   - **Stream Output (串流輸出)**: 勾選開啟（流式輸出，極速逐字顯現）。

### 3.3 💡 開發者福利：如何動態指定推理契約？
DROS 7.1 支持動態契約控制。在向 `/v1/chat/completions` 發送 POST 請求時，您可以在 JSON 載荷中直接傳遞 `"contract"` 鍵。例如：
```json
{
  "messages": [
    {"role": "user", "content": "唯識學與量子力學有何結合點？"}
  ],
  "contract": "speculative_prajna",
  "stream": false
}
```
*   **指定 `"contract": "strict_vajra"`**: 觸發 Canonical 聖言量推理，輸出嚴格引證與 `T-Number`。
*   **指定 `"contract": "balanced_vajra"`**: 觸發 Interpretive 詮釋映射推理，輸出前綴 `[義理映射 / Interpretive Mapping]` 段落。
*   **指定 `"contract": "speculative_prajna"`**: 觸發 Speculative 般若推演推理，放寬 T-Number 校驗並自動渲染警告區塊。

---

## ⚖️ 雙軌特許授權與法律合規聲明 (AGPL-3.0 Compliance)

DROS 7.1 的核心代碼與引擎架構採用 **GNU Affero General Public License v3.0 (AGPL-3.0)** 強開源授權發佈。

*   **企業網路分發義務**：如果您將 DROS 核心引擎集成到您的企業雲端服務、SaaS 產品或任何可透過網路訪問的平台上，您**必須**將您修改後的全部 DROS 引擎代碼，以開源形式提供給網路使用者。
*   **閉源商用許可**：如果您的組織需要封閉式整合且免除網絡披露義務，或者需要使用高純度的 **16,071 個實心節點黃金本體數據** 進行企業推理，您必須向 **康宸園有限公司/Jimmy Chen** 申請獲取 **DROS 商業授權**。

---

## ⚖️ 護法警示：DROS 不是「虛擬上師」

DROS 7.1 是一套嚴謹的**法義推理工具**，而非算命或通靈工具。為了確保您的修行安全，請知悉系統**絕不涉入**以下領域：
1. **不印證證量**：AI 無法判定您是否開悟。
2. **不論斷業力**：系統不處理個人果報占卜。
3. **不指導感應**：請勿對 AI 描述您的神秘感應 or 幻相。
4. **不扮演禪師**：AI 僅解析公案，無法與您心心相印。
5. **不傳授密法**：實修儀軌請務必依止具德上師。

> [!TIP]
> **理歸系統，事歸行者**。讓 DROS 幫您釐清義理，讓實修回歸您的自心。詳細說明請見 [DROS_BOUNDARY.md](./DROS_BOUNDARY.md)。

---
**DROS 7.1 (Epistemic Edition) - 願一切眾生，皆入圓覺。**
