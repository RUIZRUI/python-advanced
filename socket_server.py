# -*- coding: utf-8 -*-

import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
port = 9999

# 绑定地址
serversocket.bind((host, port))

# 设置最大连接数，超过排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    '''
    格式化字符串常量运算求值的表达式：
        大括号内可以填入表达式或调用函数
        大括号内的引号不能使用 \ 转义
        如果括号外需要显示大括号，则应连续输入两队大括号 {{}}
        大括号内不允许出现 \ , 如果需要，则先用用一个变量表示，再在大括号内填入变量名
        用于多行字符串：f"Hello"\ 
                     f"I'm {age}\ 
                     f"I'm {name}

                或者  f"""
                     Hello!
                     I'm {age}
                     I'm {name}
                     """
    '''
    '''
    ord(char) 返回 ascii 码
        ord('\n')   10
    '''
    print(f'连接地址：{str(addr)}') 

    msg = '欢迎访问 QIXQI' + '\r\n'     # 回车换行
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()