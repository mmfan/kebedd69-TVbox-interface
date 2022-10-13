#!/bin/bash
# 建立文件夹
mkdir -p /root/sd/pywork/ && cd /root/sd/pywork/
# 下载仓库包
git clone https://gitcode.net/qq_32394351/dr_py.git
# 进入目录
cd dr_py
# 升级pip包
#pip install --upgrade pip
# 安装依赖
pip install -r requirements.txt
# 启动项目
nohup bash ./app.sh 0
