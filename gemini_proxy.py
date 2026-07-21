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
    print("🌐 DROS Proxy 根目錄入口啟動中 (Port 5000)...")
    import uvicorn
    uvicorn.run("app", host='0.0.0.0', port=5000)
