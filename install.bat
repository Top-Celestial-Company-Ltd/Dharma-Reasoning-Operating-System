@echo off
:: Force active code page to UTF-8
chcp 65001 >nul 2>&1
echo ========================================
echo    DROS 7.0 Windows Installation
echo ========================================

python -m venv venv
call venv\Scripts\activate.bat

echo [*] Installing dependencies...
python -m pip install --upgrade pip
pip install -e .

echo.
echo [*] Installation Complete!
echo Usage:
echo   dros "What is Alaya-vijnana?"
echo   dros --serve
echo.
pause
