#!/usr/bin/python3

# 下载文件如何支持中文
# 下载文件如何支持 jpg 格式


# 文件下载通过设置 HTTP 头信息来实现
# HTTP 头部
print('Content-Disposition: attachment; filename="download.txt"')
print()

# 打开文件
fo = open('download.txt', 'rb')

str = fo.read()
print(str)

# 关闭文件
fo.close()