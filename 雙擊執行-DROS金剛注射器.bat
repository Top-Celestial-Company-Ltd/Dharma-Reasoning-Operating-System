@echo off
:: Force active code page to UTF-8
chcp 65001 >nul 2>&1
setlocal enabledelayedexpansion

echo ========================================================
echo   DROS 7.1 Nirvana Edition - Vajra Launcher v2.4
echo   Dharma Reasoning OS - Boot Bootstrapping
echo ========================================================
echo.

rem 1. Set and Detect DROS 7.0 Release Directory via 100% Pure English Relative Path
set "DROS_DIR=..\DROS_GitHub_Release_v5.2"

if not exist "%DROS_DIR%\main.py" (
    rem Fallback: If executed from within the release folder itself
    set "DROS_DIR=."
)

if not exist "%DROS_DIR%\main.py" (
    echo [ERROR] Cannot locate DROS engine directory.
    echo         Please make sure 'DROS_GitHub_Release_v5.2' is placed alongside your vault folder.
    pause
    exit /b 1
)

echo [1/3] Target directory located: %DROS_DIR%
cd /d "%DROS_DIR%"

rem 2. Check and configure .env
if not exist ".env" (
    echo [WARNING] .env file not found.
    echo           Please set your GEMINI_API_KEY.
    set /p apiKey="Please enter your Gemini API Key: "
    if not "!apiKey!"=="" (
        echo GEMINI_API_KEY=!apiKey! > .env
        echo [OK] API Key saved to .env
    )
) else (
    echo [OK] .env file loaded.
)

rem 3. Activate Python Virtual Environment (venv)
if exist "venv\Scripts\activate.bat" (
    echo [OK] Activating virtual environment [venv]...
    call venv\Scripts\activate.bat
) else (
    echo [WARNING] venv not found. Using system default python.
)

python --version > nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found or not in PATH!
    pause
    exit /b 1
)

rem 4. Execute Doctrinal Hardening
echo.
echo [2/3] Hardening Doctrinal Manifest (dna_enricher)...
python -m src.pipeline.dna_enricher

if errorlevel 1 (
    echo [WARNING] dna_enricher execution finished with warnings.
    echo.
) else (
    echo [OK] Hardening complete!
)

rem 5. Start Quart API Proxy Server
echo.
echo [3/3] Starting DROS Proxy API server on port 5000...
echo --------------------------------------------------------
echo   KEEP THIS WINDOW OPEN! DO NOT CLOSE IT!
echo   Go back to Obsidian and refresh Copilot to connect.
echo --------------------------------------------------------
echo.

python main.py --serve

if errorlevel 1 (
    echo [ERROR] Server terminated unexpectedly.
    pause
    exit /b 1
)
