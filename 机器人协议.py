# -*- coding: utf-8 -*-

# python 将本地文件夹浏览器可访问
# python3 -m http.server
# 打开浏览器


import urllib.robotparser


# 用字符串比较来确定是否获取 URL, 所以目录末尾有没有斜线 / 表示不同的URL
rp = urllib.robotparser.RobotFileParser()
rp.set_url("http://qixqi.club/robots.txt")     # https://qixqi.club 证书验证问题
rp.read()
print(rp.can_fetch("Baiduspider", "/"))
print(rp.can_fetch("Baiduspider", "/article/"))
print(rp.can_fetch("Googlespider", "/"))
print(rp.can_fetch("Googlebot", "/"))

