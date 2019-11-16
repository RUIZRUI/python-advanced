#!/usr/bin/python3

# Cookie 设置
# cookie 的Expires, Domain, Path 这些属性设置在 Content-type: text/html 之前
print('Content-type: text/html')
print('Set-Cookie: name="qixqi";expires="Wed, 28 Aug 2019 16:18:30 GMT')
print()
print(''' 
<html>
<head>
    <meta charset="utf-8" />
    <title>cookie - CGI</title>
</head>
<body>
    <h1>Cookie set OK!</h1>
</body>
</html>
''')