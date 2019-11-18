# -*- coding: utf-8 -*-
# 时间戳服务端

from socket import *
import time

code = 'utf-8'  # 编码方式
host = 'localhost'  # 主机ip
port = 21566    # 软件端口号
bufsize = 1024
addr = (host, port)
size = 10

tcps = socket(AF_INET, SOCK_STREAM)     # 创建socket
# socket.setsocket(level, optname, value)
tcps.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)     # 设置socket，重用ip和端口
tcps.bind(addr)     # 绑定ip和端口
tcps.listen(size)   # 最大连接数

while True:
    print('服务器启动，监听客户端连接')
    conn, address = tcps.accept()
    print('连接的客户端：', address)
    while True:
        try:
            data = conn.recv(bufsize)   # 读取连接客户端发送的消息，返回 byte，需要转换为字符串
        except Exception:
            print('断开的客户端：', address)
            break
        print('客户端发送的内容：', data.decode(code))
        if not data:
            break
        msg = time.strftime('%Y-%m-%d %X')  # 结构化时间戳
        # msg1 = f'[{msg}]:{data.decode(code)}'
        msg1 = '[%s]: %s' % (msg, data.decode(code))
        conn.send(msg1.encode(code))    # 发送消息给连接的客户端
    conn.close()    # 关闭客户端连接
tcps.close()
