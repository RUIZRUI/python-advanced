# -*- coding: utf-8 -*-

import pymysql

# 连接数据库
mydb = pymysql.connect('localhost', 'root', '', 'python')

# 创建游标对象 cursor
cursor = mydb.cursor()

# 查询 sql
cursor.execute('SELECT VERSION()')

# 获取单条数据
data = cursor.fetchone()

print('Database version: %s' % data)






# 创建表
# 使用预处理语句创建表
sql = '''
    create table employee if not exists(
        first_name char(20) not null,
        last_name char(20),
        age int,
        sex char(1),
        income float
    )
'''
cursor.execute(sql)









# 关闭连接
mydb.close()