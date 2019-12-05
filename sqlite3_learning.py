import sqlite3

# 建立连接
conn = sqlite3.connect('sqlite3_learning.db')
# use :memory:
# conn_memory = sqlite3.connect(':memory:')


# 建立光标
c = conn.cursor()
# 创建表
c.execute('''
    create table if not exists stocks(
        data text,
        trans text,
        symbol text,
        qty real,
        price real
    ) ''')

# 插入数据
c.execute(''' 
    insert into stocks values
    ('2006-01-05', 'buy', 'rhat', 100, 35.14) ''')

# 提交到数据库
conn.commit()

# 关闭连接
conn.close()





connect = sqlite3.connect('sqlite3_learning.db')
cursor = connect.cursor()

# 不安全操作<sql 注入>, Never
# symbol = 'rhat'
# cursor.execute('select * from stocks where symbol = "%s"' % symbol)

# 推荐
symbol = ('rhat',)
cursor.execute('select * from stocks where symbol = ?', symbol)
print(cursor.fetchone())



# 插入多条数据
purchases = [
    ('2006-03-28', 'buy', 'ibm', 1000, 45.00),
    ('2006-04-05', 'buy', 'msft', 1000, 72.00),
    ('2006-04-06', 'sell', 'ibm', 500, 53.00)]

cursor.executemany('insert into stocks values (?, ?, ?, ?, ?)', purchases)

connect.commit()


# 关闭连接
cursor.close()
connect.close()