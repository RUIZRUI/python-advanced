#!/usr/bin/python3

import cgi, cgitb

form = cgi.FieldStorage()

if form.getvalue('textcontent'):
    text_content = form.getvalue('textcontent')
else:
    text_content = '没有内容还提交，？？？'

print('Content-type: text/html')
print()
print('<html>')
print('<head>')
print('<meta charset="utf-8" />')
print('<title>textarea - CGI</title>')
print('</head>')
print('<body>')
print('<h2> 输入的内容是：%s' % text_content)
print('</body>')
print('</html>')