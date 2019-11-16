#!/usr/bin/python3

# 引入 CGI 模块
import cgi, cgitb

form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue('google'):
    google_flag = '是'
else:
    google_flag = '否'

if form.getvalue('qixqi'):
    qixqi_flag = '是'
else:
    qixqi_flag = '否'


print('Content-type: text/html')
print()
print('<html>')
print('<head>')
# print('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
print('<meta charset="utf-8" />')
print('<title> checkbox - CGI 实例</title>')
print('</head>')
print('<body>')
print('<h2> QIXQI 是否选择了：%s</h2>' % qixqi_flag)
print('<h2> Google 是否选择了：%s</h2>' % google_flag)
print('</body>')
print('</html>')