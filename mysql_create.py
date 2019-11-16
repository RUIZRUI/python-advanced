# -*- coding: utf-8 -*-
import mysql.connector

# 建立数据库连接
mydb = mysql.connector.connect(
    host = 'localhost',  # 数据库主机地址
    user = 'root',       # 数据库用户名
    passwd = ''          # 数据库密码
)

print(mydb)


# 创建数据库
mycursor = mydb.cursor()
# mycursor.execute('CREATE DATABASE python')
# 查看数据库
mycursor.execute('SHOW DATABASES')
for x in mycursor:
    print(x)


