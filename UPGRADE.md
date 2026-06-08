# 🚀 DROS v7.2 ➔ v7.3 無痛升級指南 (Upgrade Guide)

[繁體中文](UPGRADE.md) | [English](UPGRADE_en.md)

本指南說明如何將您的 DROS 7.2 系統安全升級至 **v7.3 Doctrinal Copilot 完全體**。本次升級為「零拷貝、零採礦」純軟體治理升級，不需重新跑任何 embedding。

---

## 🛠️ 升級步驟

### 第一步：拉取/覆蓋最新代碼

請拉取 GitHub 倉庫最新代碼，或手動覆蓋以下 5 個核心組件檔案：
1. `config.yaml` ➔ 全域配置文件
2. `src/config.py` ➔ 配置加載器
3. `src/retrieval/graphify.py` ➔ 檢索核心
4. `proxy/gemini_proxy.py` ➔ 網關核心
5. `gemini_proxy.py` ➔ 根目錄啟動入口

---

### 第二步：更新設定檔 (`config.yaml`)

請在您本地的 `config.yaml` 的 `system:` 區塊下，新增 `max_quote_slices` 參數：

```yaml
# ====================== 系統行為 ======================
system:
  hardening_level: 7
  default_mode: "Bodhisattva"
  authority_nodes_only: true
  max_context_length: 12000
  warning_context_length: 8000
  max_quote_slices: 3  # ➔ [新增] 單次打撈原典之最大切片數，用以熔斷防禦 Token 爆炸 (HTTP 400)
```

*(註：若未填寫此欄位，v7.3 系統亦會自動回退並以安全值 3 運行。)*

---

### 第三步：(選配) 掛載大覺藏實體庫

如果您擁有「大覺藏」實體經文庫，您現在可以非常安全地掛載它，完全不用擔心 400 錯誤或義理污染：
1. 將大覺藏資料夾放進您的專案根目錄（或建立 Junction 目錄接合點）。
2. 在 `config.yaml` 中配置大覺藏路徑：
   ```yaml
   paths:
     vault: "./Vault_DajueZang"
   ```
3. 重啟服務，DROS v7.3 會自動啟用**「宗派物理目錄過濾」**與**「引文配額折疊」**安全網。

---

### 第四步：無痛 API 金鑰配置 (Obsidian 插拔即用)

在 v7.3 中，您**不再需要**在 Windows / Linux 的系統環境變數中手動配置 `GOOGLE_API_KEY`。
- **使用方式**：直接在您的 Obsidian 插件（如 Copilot / Smart Connections）的設定面板中，填入您新鮮有效的 Gemini API Key 即可。
- **機制**：DROS 7.3 網關在收到請求時，會自動攔截 Authorization Header 中的金鑰並向後傳遞給 Gemini SDK，實現多租戶與「插拔即用」的自癒效果。

---

### 第五步：熱啟動服務

在終端機中重新執行：
```bash
python gemini_proxy.py
```
系統會檢測到代碼變更，自動清除舊的快取檔 (`.graphify_cache.pkl`)，並以微秒級速度重新完成 In-Memory 索引預熱。

恭喜您！您的 DROS 系統已完美升級至 v7.3 完全體！
