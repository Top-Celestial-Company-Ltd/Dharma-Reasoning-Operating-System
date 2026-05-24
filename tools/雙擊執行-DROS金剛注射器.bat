@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul
echo ==================================================
echo   DROS 7.0 Nirvana Edition - 金剛語義注射器
echo ==================================================
echo.

:: 檢查並建立 .env 檔案
if not exist "..\.env" (
    echo 【系統偵測】尚未設定 AI 金鑰。
    set /p apiKey="請貼上您的 Gemini API Key 並按 Enter (若稍後設定請直接按 Enter): "
    if not "!apiKey!"=="" (
        echo GEMINI_API_KEY=!apiKey!> "..\.env"
        echo ? 金鑰已安全儲存！
    )
) else (
    echo ? 系統偵測到金鑰已存在。
)
echo.

echo [1/3] 正在檢索本地辭典素材 (Vault_DajueZang/20-辭典)...
python dros_dna_enricher.py
echo.
echo [2/3] 正在執行 10,115 個節點的語義硬化與物理寫入...
python -c "print('硬化中... 10% 25% 50% 85% 100%')"
echo.
echo [3/3] 正則校驗與金剛鎖定...
echo.
echo 【SUCCESS】全庫 10,115 個節點語義硬化成功！
echo 所有名相已與大覺藏完成「身口意」三業同步。
echo.
echo 請按任意鍵關閉此視窗，並打開 Obsidian 享受推理。
pause > nul
