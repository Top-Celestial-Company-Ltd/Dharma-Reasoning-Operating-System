import os
import sys
import json
import time
import requests

# 解決 Windows cp950 編碼問題
if hasattr(sys.stdout, 'reconfigure'):
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass
if hasattr(sys.stderr, 'reconfigure'):
    try: sys.stderr.reconfigure(encoding='utf-8')
    except Exception: pass

URL = "http://127.0.0.1:5000/v1/chat/completions"
OUTPUT_FILE = r"E:\vscode\AI知識庫\數位佛堂_v7.3_upgrade\DROS佛學實測七大難題-7.3版-補完開採後測試.md"

QUESTIONS = [
    ("一、 根據唯識宗與中觀應成派的交鋒，阿賴耶識是否具備『自性』（Svabhāva）？請嚴格依據《成唯識論》與《入中論》的底層邏輯分別作答。", 
     "根據唯識宗與中觀應成派的交鋒，阿賴耶識是否具備『自性』（Svabhāva）？請嚴格依據《成唯識論》與《入中論》的底層邏輯分別作答。"),
    
    ("二、 中觀派說『一切皆空』，唯識宗說『萬法唯識』，如果兩者皆對，那麼『識』本身究竟是空還是不空？",
     "中觀派說『一切皆空』，唯識宗說『萬法唯識』，如果兩者皆對，那麼『識』本身究竟是空還是不空？"),
    
    ("三、 在四禪八定中，為什麼『第三禪』在『喜（Pīti，狂喜）』已經褪去的情況下，依然能保持『樂（Sukha，平靜的快樂）』與『捨（Upekkhā，平等心）』？請解釋其轉換機制。",
     "在四禪八定中，為什麼『第三禪』在『喜（Pīti，狂喜）』已經褪去的情況下，依然能保持『樂（Sukha，平靜的快樂）』與『捨（Upekkhā，平等心）』？請解釋其轉換機制。"),
    
    ("四、 請列舉五蘊，並解釋佛陀如何用這五蘊推演『無常、苦、無我』的解脫機制？",
     "請列舉五蘊，並解釋佛陀如何用這五蘊推演『無常、苦、無我』的解脫機制？"),
    
    ("五、 既然佛陀說『無我』（Anattā），那麼在六道輪迴中流轉受報的『主體』究竟是什麼？請勿使用『靈魂』一詞來解釋。",
     "既然佛陀說『無我』（Anattā），那麼在六道輪迴中流轉受報的『主體』究竟是什麼？請勿使用『靈魂』一詞來解釋。"),
    
    ("六、 『佛性』與印度教的『梵我』有何根本區別？",
     "『佛性』與印度教的『梵我』有何根本區別？"),
    
    ("七、 根據經典，佛教中的『人生的意義（Meaning of Life）』究竟是什麼？",
     "根據經典，佛教中的『人生的意義（Meaning of Life）』究竟是什麼？")
]

def run_tests():
    # 優先從 Windows 註冊表中讀取最新的 API Key (避免繼承父進程的舊環境變數)
    import winreg
    api_key = None
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment")
        reg_val, _ = winreg.QueryValueEx(key, "GOOGLE_API_KEY")
        if reg_val:
            api_key = reg_val
            print(f"[*] Successfully loaded API Key from Registry (ends with: {api_key[-10:]})")
    except Exception as e:
        print(f"[*] Registry load failed: {e}. Falling back to environment variables.")
        
    if not api_key:
        api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        if api_key:
            print(f"[*] Successfully loaded API Key from environment.")
            
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    else:
        print(f"[!] Warning: No API Key found anywhere. Requests may fail.")

        
    print(f"[*] Initiating DROS v7.3 adversarial benchmark test (7 questions)...")
    
    md_content = []
    md_content.append("# 🏛️ DROS v7.3 補完開採與本體定錨後對抗性測試結果")
    md_content.append(f"**測試時間**: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    md_content.append("**執行合約**: Strict Vajra (金剛合約 - 嚴格宗派推演)")
    md_content.append("---")
    
    for title, q_text in QUESTIONS:
        print(f"\n[*] 正在測試: {title}")
        payload = {
            "messages": [{"role": "user", "content": q_text}],
            "model": "vajra",
            "stream": False
        }
        
        start_time = time.time()
        try:
            resp = requests.post(URL, headers=headers, json=payload, timeout=90)
            duration = time.time() - start_time
            
            if resp.status_code == 200:
                data = resp.json()
                content = data["choices"][0]["message"]["content"]
                print(f"✅ 測試成功 (耗時: {duration:.2f}秒)")
                
                md_content.append(f"\n## {title}\n")
                md_content.append(content)
                md_content.append("\n---\n")
            else:
                print(f"❌ 測試失敗. HTTP Code: {resp.status_code}")
                print(resp.text)
                md_content.append(f"\n## {title} (測試失敗)\n")
                md_content.append(f"HTTP Code: {resp.status_code}\n\nError:\n```json\n{resp.text}\n```")
                md_content.append("\n---\n")
        except Exception as e:
            print(f"❌ 發生異常: {e}")
            md_content.append(f"\n## {title} (發生異常)\n")
            md_content.append(f"Exception: {e}")
            md_content.append("\n---\n")
            
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(md_content))
        
    print(f"\n🎉 測試完成！結果已儲存至: {OUTPUT_FILE}")

if __name__ == "__main__":
    # 等待伺服器熱啟動
    print("[*] Waiting 5 seconds for server warmup...")
    time.sleep(5)
    run_tests()
