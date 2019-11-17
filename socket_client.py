# -*- coding: utf-8 -*-

import socket
import sys

# 创建 socket 对象
clientsocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)


# 获取本地主机名
host = socket.gethostname()
port = 9999

# 连接服务
clientsocket.connect((host, port))

# 接收小于 1024 字节的数据
msg = clientsocket.recv(1024)

clientsocket.close()


print(msg.decode('utf-8'))