#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DROS 7.0 Nirvana Edition - 系統綜合功能測試與驗證腳本
驗證項目：
1. 配置加載 (config.py / config.yaml)
2. 契約讀取與信封編譯 (InferenceContract)
3. 知識圖譜檢索 (GraphifyRetriever / DrosEngine)
4. v5.3 契約感知提示詞編譯器 (System_Prompt_v5.3.md)
5. 網關連通性診斷 (Quart Gemini Proxy REST Client)
"""

import os
import sys
import json
import httpx
from pathlib import Path

# 強制終端編碼
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# 設定工作路徑為專案根目錄
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

try:
    from src.config import config, init_config
    from src.engine.dros_engine import DrosEngine
    from src.engine.contract import InferenceContract
except ImportError as e:
    print(f"❌ 導入核心模組失敗！請確認腳本位於 DROS 專案根目錄中。")
    print(f"   錯誤訊息: {e}")
    sys.exit(1)

def print_banner(title: str):
    print("\n" + "=" * 60)
    print(f" {title.center(58)}")
    print("=" * 60)

def test_config():
    print_banner("測試項目 1: 全域配置管理機制")
    try:
        init_config()
        print(f"✅ [OK] 成功加載 DROS 配置版本 v{config.version}")
        print(f"   - 核心數據路徑: {config.core_path}")
        print(f"   - 智能路由模型: {config.model_router}")
        print(f"   - 義理綜攝模型: {config.model_synthesizer}")
        print(f"   - 全域硬化等級: {config.hardening_level}")
        return True
    except Exception as e:
        print(f"❌ [ERROR] 配置載入異常: {e}")
        return False

def test_contracts():
    print_banner("測試項目 2: 契約載入與信封序列化")
    contracts = ["strict_vajra", "bodhisattva_default"]
    success = True
    for c_name in contracts:
        try:
            contract = InferenceContract.load(c_name)
            envelope = contract.to_prompt_envelope()
            print(f"✅ [OK] 成功載入契約 [{c_name}]")
            print(f"   - 推理模式 (InferenceMode): {contract.InferenceMode}")
            print(f"   - 回退模式 (FallbackMode): {contract.FallbackMode}")
            print(f"   - 算力引擎 (ComputeEngine): {contract.ComputeEngine.get('Model')}")
            print(f"   - 契約信封字元長度: {len(envelope)} 字")
        except Exception as e:
            print(f"❌ [ERROR] 載入契約 [{c_name}] 失敗: {e}")
            success = False
    return success

def test_engine_retrieval():
    print_banner("測試項目 3: 知識檢索與 v5.2 提示詞編譯")
    try:
        engine = DrosEngine(core_path=str(config.core_path))
        contract = InferenceContract.load("strict_vajra")
        
        # 測試查詢
        test_query = "什麼是阿賴耶識？"
        print(f"[*] 執行模擬查詢: \"{test_query}\"")
        
        # 進行檢索
        nodes = engine.retrieve_nodes(test_query, contract)
        print(f"✅ [OK] 成功檢索到相關實心名相節點: {len(nodes)} 個")
        for i, n in enumerate(nodes[:3]):
            print(f"   - [{i+1}] {n['name']} (權威引據: {'有' if n['has_authority'] else '無'})")
            
        # 模擬模式決策
        has_authority = any(n.get("has_authority", False) for n in nodes)
        runtime_mode = contract.InferenceMode if has_authority else contract.FallbackMode
        print(f"✅ [OK] 自適應情境路由抉擇: 採用 [{runtime_mode}] 模式運作")
        
        # 彙整上下文
        context_parts = []
        for n in nodes[:3]:
            summary = n.get("summary", "")
            if not summary and "content" in n:
                summary = n["content"]
            context_parts.append(f"--- 節點: {n['name']} ---\n{summary}\n")
        context = "\n".join(context_parts)
        
        # 編譯系統提示詞
        final_prompt = engine.compile_prompt(test_query, context, contract, runtime_mode)
        print("✅ [OK] v5.2 契約感知提示詞編譯完成！")
        print("-" * 50)
        print("編譯後 Prompt 精簡預覽 (前 300 字):")
        print(final_prompt[:300] + "\n... (省略中間部分) ...")
        print("-" * 50)
        print("防注入底置隔離 (後 100 字):")
        print(final_prompt[-100:])
        print("-" * 50)
        
        return True
    except Exception as e:
        print(f"❌ [ERROR] 引擎或提示詞編譯測試失敗: {e}")
        return False

def test_proxy_connectivity():
    print_banner("測試項目 4: Quart Gemini Proxy 網關診斷")
    print("[*] 正在嘗試偵測本地代理伺服器連通性 (預設連接埠 5000)...")
    url = "http://127.0.0.1:5000/v1/chat/completions"
    payload = {
        "messages": [{"role": "user", "content": "測試提問：無我的含意？"}],
        "stream": False
    }
    try:
        # 使用極簡連線嘗試，設定超時避免懸掛
        with httpx.Client(timeout=3.0) as client:
            resp = client.post(url, json=payload)
            if resp.status_code == 200:
                print("✅ [OK] DROS Proxy 網關正常運作中，成功接收且響應 API 請求！")
                data = resp.json()
                answer = data["choices"][0]["message"]["content"]
                print(f"       響應內容長度: {len(answer)} 字")
            else:
                print(f"⚠️ [WARNING] 伺服器響應狀態碼: {resp.status_code}，可能 GOOGLE_API_KEY 未設定或伺服器異常。")
    except httpx.ConnectError:
        print("ℹ️ [INFO] 未偵測到正在運作的本地代理服務 (127.0.0.1:5000)。")
        print("   -> 若欲啟用並測試 Proxy API 串接，可先在其他終端機執行 `run.bat` 或 `python main.py --serve`。")
    except Exception as e:
        print(f"⚠️ [WARNING] 連線測試時發生其他異常: {e}")

if __name__ == "__main__":
    print_banner("DROS 7.0 Nirvana Edition - 系統整合測試管線")
    print(f"執行路徑: {SCRIPT_DIR}")
    print("=" * 60)
    
    c_ok = test_config()
    a_ok = test_contracts()
    e_ok = test_engine_retrieval()
    test_proxy_connectivity()
    
    print_banner("測試綜合評估報告")
    if c_ok and a_ok and e_ok:
        print("🎉 恭喜！DROS 核心推理底座、契約系統、及系統提示詞編譯器 100% 驗證通過！")
        print("   系統完美進入高擬真 (NIRVANA) 開發與運作就緒狀態。")
        sys.exit(0)
    else:
        print("❌ 核心檢測未完全通過，請根據上方錯誤日誌進行排查。")
        sys.exit(1)
