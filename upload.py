#!/usr/bin/python3
# 如何获取项目的上下文路径保存文件

# 如果服务器使用的是Linux，必须替换文件分隔符
# fn = os.path.basename(fileitem.filename.replace("\\", "/" ))

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# 获取文件名
fileitem = form['filename']

# 检测文件是否上传
if fileitem.filename:
    # 设置文件路径
    fn = os.path.basename(fileitem.filename)
    open('./' + fn, 'wb').write(fileitem.file.read())

    message = '文件 "' + fn + '" 上传成功'
else:
    message = '文件上传失败'

print('''
Content-Type: text/html\n
<html>
    <head>
        <meta charset="utf-8" />
        <title>upload - CGI</title>
    </head>
    <body>
        <p> message: %s </p>
    </body>
</html>
''' % message)