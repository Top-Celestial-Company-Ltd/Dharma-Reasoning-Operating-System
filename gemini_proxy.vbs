Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd.exe /c python gemini_proxy.py", 0, false
