@echo off
:: Force active code page to UTF-8 to prevent encoding issues in CMD
chcp 65001 >nul 2>&1
setlocal enabledelayedexpansion

TITLE DROS v7.3 Vajra Launcher (One-Click Installer & Launcher)

echo ========================================================
echo   DROS v7.3 Nirvana Edition - Vajra Launcher v3.0
echo   Dharma Reasoning OS - One-Click Start & Install
echo ========================================================
echo.

:: Step 1: Detect Python Environment
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found or not in PATH!
    echo         Please install Python (3.9+ recommended) and check "Add Python to PATH".
    echo [錯誤] 找不到 Python 環境或未加入 PATH 環境變數！
    echo         請安裝 Python 並在安裝時勾選 "Add Python to PATH"。
    echo.
    pause
    exit /b 1
)

:: Step 2: Auto-Install / Verify Dependencies
echo [1/2] Verifying and installing system dependencies...
echo       正在檢查與安裝必要套件，請稍候...
echo.

python -m pip install --upgrade pip -q
python -m pip install pyyaml uvicorn google-generativeai fastapi httpx python-dotenv quart quart-cors aiohttp -q

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Dependency installation failed! Please check your internet connection.
    echo [錯誤] 套件安裝失敗，請檢查網路連線後重試。
    echo.
    pause
    exit /b 1
)

echo.
echo [OK] All dependencies are ready! (所有套件已就緒)
echo.

:: Step 3: Run DROS Proxy Server (Port 5000)
echo [2/2] Starting DROS Proxy API server on port 5000...
echo --------------------------------------------------------
echo   KEEP THIS WINDOW OPEN! DO NOT CLOSE IT!
echo   Go back to Obsidian and refresh Copilot to connect.
echo.
echo   請保持此視窗開啟！不要關閉它！
echo   返回 Obsidian 並刷新 Copilot 即可開始對話伴學。
echo --------------------------------------------------------
echo.

python gemini_proxy.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Server terminated unexpectedly. Please check config.yaml or API Key settings.
    echo [錯誤] 服務異常終止，請確認 config.yaml 與 API 金鑰設定。
    echo.
    pause
    exit /b 1
)
