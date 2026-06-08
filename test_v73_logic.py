import sys
import os
from pathlib import Path

# 解決 Windows cp950 編碼問題
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# 將當前路徑加入 sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.config import config

# 動態覆蓋 config 中的一些參數以進行嚴格測試
config.max_quote_slices = 3

# 建立一個測試用 MD 檔案，包含 4 個不同宗派的大覺藏座標
# T0001: 原始阿含 (01阿含部類)
# T1546: 阿毗達摩 (12毘曇部類)
# T0262: 天台宗 (04法華部類)
# T1856: 中觀派 (13中觀部類)
MOCK_NODE_NAME = "MockDoctrinalTestNode"
mock_node_path = Path(config.core_path) / f"{MOCK_NODE_NAME}.md"

mock_content = """---
title: Doctrinal Testing Node
---

> [!NOTE] 核心義理
> 這個測試節點包含了多個不同宗派的大覺藏座標，用於測試 v7.3 的物理隔離與安全折疊機制：
> - 原始阿含座標：T0001
> - 阿毗達摩座標：T1546
> - 天台宗座標：T0262
> - 中觀派座標：T1856
"""

# 確保 core 目錄存在並寫入
mock_node_path.parent.mkdir(parents=True, exist_ok=True)
mock_node_path.write_text(mock_content, encoding='utf-8')

# 在測試結束後會刪除
def cleanup():
    if mock_node_path.exists():
        mock_node_path.unlink()

from src.retrieval.graphify import GraphifyRetriever

def run_test():
    try:
        print("==================================================")
        print("🧪 DROS v7.3 Doctrinal Filtering & Watchdog 深度驗證白盒測試")
        print("==================================================")
        
        # 為了使新建立的 Mock 節點生效，我們先刪除舊快取 (如果有)
        cache_path = Path(config.core_path).parent / ".graphify_cache.pkl"
        if cache_path.exists():
            cache_path.unlink()
            
        print("[1] 初始化 Graphify 檢索器並索引 Mock 節點...")
        r = GraphifyRetriever()
        
        # 驗證 Mock 節點是否被成功索引
        node_key = MOCK_NODE_NAME.lower()
        if node_key not in r.index['nodes']:
            print(f"❌ 錯誤: Mock 節點 '{MOCK_NODE_NAME}' 未被索引！")
            return
            
        print(f"✅ 成功索引 Mock 節點，目前節點總數: {len(r.index['nodes'])}")
        
        # ==========================================================
        # 測試 1：限制為「天台宗」
        # ==========================================================
        print("\n[測試 1] 宗派限制 = 『天台宗』")
        res_tiantai = r._load_node_detail(MOCK_NODE_NAME, query="妙法", sectarian_context="天台宗")
        
        print(f"    節點名稱: {res_tiantai['name']}")
        print(f"    引文內容 (應僅載入 T0262，其餘隔離阻斷):")
        for line in res_tiantai['quote'].split('\n'):
            print(f"      {line}")
            
        # ==========================================================
        # 測試 2：限制為「阿毗達摩」
        # ==========================================================
        print("\n[測試 2] 宗派限制 = 『阿毗達摩』")
        res_abhidhamma = r._load_node_detail(MOCK_NODE_NAME, query="阿毗達摩", sectarian_context="阿毗達摩")
        
        print(f"    引文內容 (應僅載入 T1546，其餘隔離阻斷):")
        for line in res_abhidhamma['quote'].split('\n'):
            print(f"      {line}")
            
        # ==========================================================
        # 測試 3：通用語境 (不限宗派) + Watchdog 折疊 (max_quote_slices = 3)
        # ==========================================================
        print("\n[測試 3] 宗派限制 = 『通用』 (無隔離，但第 4 個引文應被折疊)")
        res_general = r._load_node_detail(MOCK_NODE_NAME, query="通用", sectarian_context="通用")
        
        print(f"    引文內容 (前 3 個應載入/降級，第 4 個 T1856 應顯示已折疊):")
        for line in res_general['quote'].split('\n'):
            print(f"      {line}")
            
    finally:
        cleanup()
        print("\n🧹 已清理 Mock 測試節點檔。")

if __name__ == "__main__":
    run_test()
