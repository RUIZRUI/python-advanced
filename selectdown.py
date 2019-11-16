#!/usr/bin/python3

import cgi, cgitb

form = cgi.FieldStorage()

if form.getvalue('dropdown'):
    dropdown_value = form.getvalue('dropdown')
else:
    dropdown_value = '啥也没有，咱也不敢说，咱也不敢问'

print('Content-type: text/html')
print()
print('<html>')
print('<head>')
print('<meta charest="utf-8" />')
print('<title>select - CGI</title>')
print('</head>')
print('<body>')
print('<h2> 选中的选项是：%s</h2>' % dropdown_value)
print('</body>')
print('</html>')