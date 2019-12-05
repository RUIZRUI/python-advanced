# -*- coding: utf-8 -*-

'''
    open(file, mode='r', buffering=-1, encoding=None, errors=None, newLine=None, closefd=True, opener=None)

    r 读（default)
    w 写（覆盖）
    x 排他性创建
    a 追加
    b 二进制
    t 文本模式（default)
    + 更新
    U 统一 newlines模式（过时）
'''

handle = open('file_r.txt', 'r')
content = handle.read()
handle.close()

handle = open('file_w.txt', 'w')
handle.write(content)
handle.close()