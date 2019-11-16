#!/usr/bin/python3

import os
import http.cookies

print('Content-type: text/html')
print()

print('''
<html>
<head>
    <meta charset="utf-8" />
    <title>cookie get - CGI</title>
</head>
<body>
    <h1>读取 cookie 信息</h1>
''')

if 'HTTP_COOKIE' in os.environ:
    cookie_string = os.environ['HTTP_COOKIE']
    c = http.cookies.SimpleCookie()
    c.load(cookie_string)

    try:
        data = c['name'].value
        print('cookie data: ' + data + '</br>')
        # expires = c['expires'].value
        # print('cookie data: ' + expires +'</br>')
    except KeyError:
        print('cookie 没有设置获取或者已经逝去 </br>')

print('''
</body>
</html>
''')