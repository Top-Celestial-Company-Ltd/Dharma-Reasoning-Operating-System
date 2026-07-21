# 🚀 DROS v8.0.0 一鍵完全體升級指南 (Upgrade Guide)

本指南說明如何將您的 DROS 系統安全升級至 **v8.0.0 Epistemic Complete Edition (認識論完備版)**。
本次升級包含 **`core/` 知識庫（28,600+ 義理節點）** 與 **`Obsidian 專用外掛 (dros-doctrinal-copilot)`** 的雙向升級。

---

## ⚡ 方式一：Git 一鍵同步更新（最推薦 ── 單一指令全量升級）

若您的專案是透過 Git 管理，**只需要一行指令**，即可同時完成 `core/` 知識庫與 Obsidian 外掛的同步更新：

```bash
# 1. 一次性拉取最新的 core 知識庫、網關與 Obsidian 外掛
git pull origin main

# 2. 清除舊版記憶體快取（讓系統重構 v8.0 的 28,600+ 節點圖譜）
# Windows PowerShell:
Remove-Item .graphify_cache.pkl -ErrorAction Ignore
# Linux / macOS:
rm -f .graphify_cache.pkl

# 3. 熱重啟網關
python gemini_proxy.py
```

*在 Obsidian 中按下 `Ctrl + R`（或重新開啟外掛），外掛與 core 庫即同步升級完成！*

---

## 📦 方式二：Zip 手動全包覆蓋更新

若是下載 Zip 壓縮包的使用者，亦可一次性拖曳完成：

1. 解開 v8.0.0 Zip 包。
2. 將包含 `core/`、`.obsidian/`、`gemini_proxy.py` 的**所有內容一次性複製並覆蓋**至您的原專案資料夾中。
3. 刪除舊快取檔 `.graphify_cache.pkl` 並執行 `python gemini_proxy.py` 即可！

---

## 🛡️ 資料安全保證（個人筆記與大覺藏安全說明）

DROS 採用「物理解耦架構」：
- **`core/` 官方庫**：升級僅替換官方 28,600+ 個義理節點。
- **用戶掛載庫（如 `Vault_DajueZang/` 或自訂筆記）**：位於 `core/` 之外，**升級時 100% 獨立保留，絕不覆蓋**！
- 重開服務後，系統會在記憶體中自動融合 `core/` 新節點與您的大覺藏經文。

---

*DROS v8.0.0 認識論完備版 ── 帝網重重，一鍵通達。* 🎛️🛡️⚙️☸️
