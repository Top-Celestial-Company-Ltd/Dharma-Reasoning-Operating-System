@echo off
chcp 65001 > nul
call venv\Scripts\activate.bat 2>nul

if "%1"=="" (
    dros
) else if "%1"=="serve" (
    dros --serve
) else (
    dros %*
)
