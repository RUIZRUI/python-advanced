#!/usr/bin/python3

import cgi, cgitb

form = cgi.FieldStorage() 

if form.getvalue('site'):
    site = form.getvalue('site')
else:
    site = '提交数据唯恐天下不乱'

print('Content-type: text/html')
print()
print('<html>')
print('<head>')
print('<meta charset="utf-8" />')
print('<title>radio - CGI 实例</title>')
print('</head>')
print('<body>')
print('<h2>选中的网站是 %s</h2>' % site)
print('</body>')
print('</html>')