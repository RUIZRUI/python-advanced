# -*- coding: utf-8 -*-

# socket.socket(family, type, proto)    创建套接字
# family: AF_UNIX, AF_INET
# type: 面向连接 SOCK_STREAM，非面向连接 SOCK_DGRAM
# protocol: 默认0，一般不填



# 内建方法
# 服务器
# s.bind(host, port) 绑定地址
# s.listen()    TCP监听
# s.accept()    接收TCP客户端连接，阻塞式，等待连接的到来，返回connection对象

# 客户端
# s.connect()   主动初始化TCP连接，异常返回socket.error
# s.connect_ex()  异常返回出错码

# 公用
# s.recv(bufsize, flag)   接收TCP数据，返回字符串，bufsize接收的最大数据量，flag忽略
# s.recvfrom()  接收UDP数据，返回(data, address)，data: 接收的字符串，address: 发送数据的地址
# s.send()  发送TCP数据，返回要发送的字节数量
# s.sendall()   完整发送TCP数据，成功返回None，出错抛出异常
# s.sendto()    发送UDP数据
# s.close()     关闭套接字
# s.getpeername()  远程地址(ip, port)
# s.getsockname()  本地地址(ip, port)
# s.getsockopt(level, optname) 获取套接字选项的值
# s.setsockopt(level, optname, value) 设置套接字选项的值
# s.settimeout(timeout<float: 秒>) 设置套接字超时期，None没有超时期
# s.gettimeout()    获取套接字超时期，没有返回None
# s.makefile() 创建与该套接字相关的文件
# s.fileno()   返回套接字的文件描述符
# s.setblocking(flag)   flag=0: 套接字非阻塞模式；默认值是阻塞模式；非阻塞模式，没有resv()到数据，或不能立刻send()数据，返回socket.error


print('装逼呢，别在意')
print('愉快的开始学习socket吧！')