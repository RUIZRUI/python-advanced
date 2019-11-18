# -*- coding: utf-8 -*-
from socket import *
from time import ctime

code = 'utf-8'  # 编码方式
host = 'localhost'  # 服务器ip
port = 21566    # 服务器端口号
bufsize = 1024
addr = (host, port)
tcpc = socket(AF_INET, SOCK_STREAM)
tcpc.connect(addr)      # 连接服务器
while True:
    # str.strip([chars])   用于删除字符串首尾指定的字符，默认空白字符
    data = input('>>').strip()
    if not data:
        break
    tcpc.send(data.encode(code))    # 发送消息
    data = tcpc.recv(bufsize)   # 读取消息
    if not data:
        break
    print(data.decode(code))
tcpc.close()    # 关闭客户端
