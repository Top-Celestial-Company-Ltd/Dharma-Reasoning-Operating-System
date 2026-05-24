@echo off
chcp 65001 > nul
echo ========================================
echo    DROS 7.0 Windows 安裝腳本
echo ========================================

python -m venv venv
call venv\Scripts\activate.bat

echo 正在安裝依賴...
python -m pip install --upgrade pip
pip install -e .

echo.
echo ✅ 安裝完成！
echo 使用方式：
echo   dros "阿賴耶識是什麼？"
echo   dros --serve
echo.
pause
