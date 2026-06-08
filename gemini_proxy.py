#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DROS 7.0 Proxy Gateway - 根目錄啟動入口
本檔案為快捷啟動入口，核心實現位於 proxy/gemini_proxy.py。
"""

import sys
from pathlib import Path

# 設定工作路徑為專案根目錄
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from proxy.gemini_proxy import app

if __name__ == '__main__':
    print("🌐 DROS Proxy 根目錄入口啟動中 (Sandbox Port 5001)...")
    
    # 同步 Windows 註冊表中的最新 API Key (避開父進程繼承的舊環境變數)
    import os
    import winreg
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment")
        reg_val, _ = winreg.QueryValueEx(key, "GOOGLE_API_KEY")
        if reg_val:
            os.environ["GOOGLE_API_KEY"] = reg_val
            os.environ["GEMINI_API_KEY"] = reg_val
            print(f"[*] 已同步註冊表 GOOGLE_API_KEY (後十碼: {reg_val[-10:]})")
    except Exception as e:
        print(f"[!] 同步註冊表金鑰失敗: {e}")
        
    import uvicorn
    uvicorn.run("proxy.gemini_proxy:app", host='0.0.0.0', port=5001, reload=True)

