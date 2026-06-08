import os

DIR = r"e:\vscode\AI知識庫\數位佛堂\AI 總論\wiki\concepts"
files = sorted(os.listdir(DIR))
print(f"總名相數: {len(files)}")

for i in range(min(5, len(files))):
    fname = files[i]
    path = os.path.join(DIR, fname)
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            print(f"\n[{i+1}] 檔案: {fname}")
            print("-" * 30)
            print(content.strip())
            print("=" * 50)
    except Exception as e:
        print(f"讀取 {fname} 失敗: {e}")
