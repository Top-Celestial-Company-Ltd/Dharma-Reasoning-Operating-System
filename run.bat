@echo off
:: Force active code page to UTF-8
chcp 65001 >nul 2>&1
call venv\Scripts\activate.bat 2>nul

if "%1"=="" (
    dros
) else if "%1"=="serve" (
    dros --serve
) else (
    dros %*
)
