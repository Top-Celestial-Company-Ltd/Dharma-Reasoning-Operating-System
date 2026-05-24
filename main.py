#!/usr/bin/env python
"""
DROS 7.0 主入口程式
統一管理所有功能
"""

import sys
import argparse
from pathlib import Path

from src.config import config, init_config
from src.engine.dros_engine import DrosEngine
from src.engine.contract import InferenceContract


def main():
    parser = argparse.ArgumentParser(description="DROS 7.0 Dharma Reasoning OS")
    parser.add_argument("query", nargs="?", help="直接輸入查詢內容")
    parser.add_argument("-m", "--mode", choices=["Vajra", "Bodhisattva"], default=None,
                        help="強制指定運行模式")
    parser.add_argument("-c", "--contract", default="default_vajra",
                        help="指定契約名稱")
    parser.add_argument("--serve", action="store_true", help="啟動 Proxy 服務")
    
    args = parser.parse_args()

    # 初始化配置
    init_config()

    if args.serve:
        print("🌐 啟動 DROS Proxy 服務...")
        from proxy.gemini_proxy import app
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=5000)
        return

    # 互動模式或單次查詢
    contract = InferenceContract.load(args.contract)
    if args.mode:
        contract.InferenceMode = args.mode

    engine = DrosEngine(core_path=str(config.core_path))

    if args.query:
        result = engine.ask(args.query, contract)
        print("\n" + "="*60)
        print(result.get("content", "No output"))
        print("="*60)
    else:
        print("🚀 DROS 7.0 已啟動")
        print("輸入問題進行測試，或使用 --serve 啟動服務模式")
        print("輸入 'exit' 離開")


if __name__ == "__main__":
    main()
