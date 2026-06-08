import os
import subprocess
import time
import sys
import io

# 強制輸出為 UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

NLM_PATH = r"C:\Users\Jimmy\AppData\Local\Programs\Python\Python312\Scripts\nlm.exe"
NOTEBOOK_ID = "c7edcc3f-163b-4ffc-bea0-ec5ce39e99c9"
UPLOAD_DIR = r"E:\vscode\AI知識庫\數位佛堂_LM_Upload_V5"

def run_upload():
    print(f"[*] 準備上傳 50 個分卷至筆記本: {NOTEBOOK_ID}")
    
    files = sorted([f for f in os.listdir(UPLOAD_DIR) if f.endswith(".txt")])
    
    for i, filename in enumerate(files):
        file_path = os.path.join(UPLOAD_DIR, filename)
        print(f"[*] [{i+1}/50] 正在上傳: {filename}...")
        
        # 指令: nlm source add <id> --file <path> --wait --title <name>
        cmd = [NLM_PATH, "source", "add", NOTEBOOK_ID, "--file", file_path, "--wait", "--title", filename]
        
        try:
            # 這裡調用 nlm 指令
            result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
            if result.returncode == 0:
                print(f"    [SUCCESS] {filename} 上傳並索引成功")
            else:
                print(f"    [ERROR] {filename} 上傳失敗: {result.stderr.strip()}")
        except Exception as e:
            print(f"    [EXCEPTION] {filename} 出錯: {e}")
        
        time.sleep(1) # 稍微停頓

    print("\n[FINISH] V5.0 全量上傳完成！")

if __name__ == "__main__":
    run_upload()
