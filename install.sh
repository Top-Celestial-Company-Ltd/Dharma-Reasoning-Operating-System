#!/bin/bash
echo "========================================"
echo "   DROS 7.0 Ubuntu Server 安裝腳本"
echo "========================================"

# 確保安裝 python3-venv
sudo apt-get update && sudo apt-get install -y python3-venv

python3 -m venv venv
source venv/bin/activate

echo "正在安裝依賴..."
pip install --upgrade pip
pip install -e .

echo ""
echo "✅ 安裝完成！"
echo "請確保專案根目錄已建立 .env 檔案並設定 GEMINI_API_KEY"
echo "啟動服務指令: ./run.sh serve"
