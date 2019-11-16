# -*- coding: utf-8 -*-

import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'python'
)

mycursor = mydb.cursor()


# 查询数据
mycursor.execute('SELECT * FROM sites')
# fetchall() 获取所有记录
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# fetchone() 获取一条数据
myresult = mycursor.fetchone()
print(myresult)
print()

# 防止 SQL 注入攻击，使用 %s 占位符转义查询的条件
sql = 'SELECT * FROM sites WHERE name = %s'
name = ('qixqi', )      # 没有, 报错
mycursor.execute(sql, name)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print()



# Limit 设置查询的数据量
mycursor.execute('SELECT * FROM sites LIMIT 3 OFFSET 1')    # 设置第一条开始读取（从0开始）
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# 删除记录
sql = 'DELETE FROM sites WHERE name = "stackoverflow"'
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, ' 条记录删除')



# 更新数据表
sql = 'UPDATE sites SET name = "小象study" WHERE name = "qixqi"'
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, ' 条记录被修改')



# 删除表
# sql = 'DROP TABLE IF EXISTS sites'
# mycursor.execute(sql)