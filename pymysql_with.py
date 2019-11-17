# -*- coding: utf-8 -*-

'''
    以pymysql 为例
    实现通过 with 简化数据库操作
'''

from pymysql import connect
from pymysql import cursors

class DB():
    def __init__(self, host='localhost', port=3306, db='', user='root', passwd='root', charset='utf8'):
        # 建立连接
        self.conn = connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型
        self.cursor = self.conn.cursor(cursor = cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据并执行
        self.conn.commit()
        # 关闭游标
        self.cursor.close()
        # 关闭数据库连接
        self.conn.close()


if __name__ == '__main__':
    with DB(host='localhost', user='root', passwd='', db='python') as mydb:
        sql = 'SELECT * FROM employee'
        mydb.execute(sql)
        print(mydb)
        for i in mydb:
            print(i)
        