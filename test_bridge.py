import os
import sys
import io

# 強制輸出為 UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 模擬腳本導入
sys.path.append(r"E:\vscode\AI知識庫\DROS_GitHub_Release_v5.2\tools")
try:
    from dros_ai_bridge import local_search
except ImportError:
    print("[ERROR] Import Failed")
    sys.exit(1)

def test():
    BASE = r"E:\vscode\AI知識庫\DROS_GitHub_Release_v5.2"
    CORE = os.path.join(BASE, "core")
    USER = os.path.join(BASE, "User_Pavilion")
    
    # 建立測試節點
    test_note_path = os.path.join(USER, "Insights", "Test_Note.md")
    with open(test_note_path, 'w', encoding='utf-8') as f:
        f.write("--- TAG: [INSIGHT] ---\nALAYA is like a cloud storage.")
    
    print("--- Test Note Created ---")
    
    # 執行檢索
    print("--- Running Retrieval: 'ALAYA' ---")
    context = local_search("阿賴耶識", [CORE, USER])
    
    # 驗證結果
    if "[官方]" in context and "[個人]" in context:
        print("\n" + "="*30)
        print(" SUCCESS: Dual-Brain Search is WORKING! ")
        print(" Captured both Core and User nodes. ")
        print("="*30)
    else:
        print(" FAILED: Data capture incomplete. ")
        print(context)

if __name__ == "__main__":
    test()
