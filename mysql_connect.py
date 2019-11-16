# -*- coding: utf-8 -*-
import mysql.connector

# 直接连接数据库
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'python' # 若数据不存在，报错
)

mycursor = mydb.cursor()

# 创建表 sites
# mycursor.execute('CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))')

# 显示表 sites
mycursor.execute('SHOW TABLES')
for x in mycursor:
    print(x)

# 添加主键
# mycursor.execute('ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')


# 插入数据
sql = 'INSERT INTO sites (name, url) VALUES (%s, %s)'
val = ('qixqi', 'https://www.qixqi.club')
mycursor.execute(sql, val)

# 数据表内容更新时必须使用 commit()
mydb.commit()

print(mycursor.rowcount, '记录插入成功')

# 获取插入数据 id
print('1 条记录已插入， ID: ', mycursor.lastrowid)



# 批量插入
# executemany() 第二个参数是元组列表
val = [
    ('Google', 'https://www.google.com'),
    ('Github', 'https://www.github.com'),
    ('Taobao', 'https://www.taobao.com'),
    ('stackoverflow', 'https://www.stackoverflow.com')
]

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, '记录插入成功')





