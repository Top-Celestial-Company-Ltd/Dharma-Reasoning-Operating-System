#!/bin/bash
source venv/bin/activate

if [ -z "$1" ]; then
    dros
elif [ "$1" == "serve" ]; then
    echo "啟動 DROS Proxy 服務 (背景執行建議搭配 Systemd 或 nohup)..."
    dros --serve
else
    dros "$@"
fi
