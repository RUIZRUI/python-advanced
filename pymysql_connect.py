# -*- coding: utf-8 -*-
'''
python3 连接mysql: PyMySQL驱动
'''





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
    create table if not exists employee(
        first_name char(20) not null,
        last_name char(20),
        age int,
        sex char(1),
        income float
    )
'''
cursor.execute(sql)





# 插入数据
sql = '''
    insert into employee(first_name, last_name, age, sex, income)
    values
    ('Mac', 'Mohan', 20, 'M', 2000)
'''

try:
    cursor.execute(sql)
    # 提交到数据库执行
    mydb.commit()
except:
    # 发生错误回滚
    mydb.rollback()





# 查询操作
# fetchone(): 下一个查询结果，返回对象
# fetchall(): 全部结果
# rowcount:  execute() 方法后影响的行数
sql = 'SELECT * FROM employee \
    WHERE income > %s ' % (1000)
try:
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print(f'fname = {fname}, lname = {lname}, age = {age}, sex = {sex}, income = {income}')
except:
    print('Error: unable to fetch data')








# 更新操作
# sql 语句中的字符串必须要引号括起来
sql = 'UPDATE employee SET age = age + 1 WHERE sex = "%c"' % ('M')
try:
    cursor.execute(sql)
    mydb.commit()
except:
    # 错误，回滚
    mydb.rollback()







# 删除操作
sql = 'DELETE FROM employee WHERE age > %s' % (21)
try:
    cursor.execute(sql)
    mydb.commit()
except:
    mydb.rollback()








# 执行事务
# 事务属性：原子性、一致性、隔离性、持久性
# Python DB api2.0 为事务提供两个方法：commit、rollback
sql = 'd'





# 关闭连接
mydb.close()