@echo off
title DROS Gateway Launcher
echo ===================================================
echo   Dharma Reasoning OS (DROS) - Local Gateway
echo ===================================================
echo [*] Initializing DROS environment...
cd /d "%~dp0"

if exist .graphify_cache.pkl (
    echo [*] Clearing old graph cache...
    del .graphify_cache.pkl
)

echo [*] Launching gemini_proxy.py...
python gemini_proxy.py
pause
