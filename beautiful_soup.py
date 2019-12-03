# -*- coding: utf-8 -*-
import requests, bs4
import re

url = 'https://api.github.com/user'
res = requests.get(url, auth=('user', 'pass'))
print(res.status_code)
print(res.headers['content-type'])
print(res.encoding)
print(res.text)
print(res.json())
print('\n' * 3)

res = requests.get('http://www.qixqi.club')
# print(res.text)
soup = bs4.BeautifulSoup(res.text, features='lxml')
# print(soup.prettify())
print(soup.get_text())      # 获取所有文字内容
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.a['href'])
print(soup.a)   # 第一条
print(soup.find('a'))   # 第一条
print(soup.find_all('a'))   # 所有
print(soup.find(id='icp'))

for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.a.attrs)     # 标签属性
print(soup.name)        # 根节点
print(soup.contents)    # 根节点的子节点 html
print(soup.Comment)     # 获取注释
print(soup.find(id='tbody').contents)       # 子节点列表输出
print(soup.find(id='icp').children)
print(soup.title.string.parent)     # 字符串的父节点
print(soup.parent)      # None
for parent in soup.a.parents:       # 遍历父亲节点到根节点
    if parent is None:
        print(parent)
    else:
        print(parent.name)

print(soup.find('a', href='/counter'))  
print(type(soup.find('a', href='/couter')))     # NoneType
print(soup.a)
print(type(soup.a))     # <class 'bs4.element.Tag'>
print(soup.a.next_sibling)  # None ???

# 与正则表达式结合
print(soup.find_all(re.compile('^b')))

# 或
print(soup.find_all(['br', 'a']))

# 查找所有值 
# print(soup.find_all(True))

# find_all(name, class, recursive, text, **kwargs)
print(soup.find_all('p', 'title'))    # <p class="title">hello world</p>
print(soup.find(text = re.compile('我')))   # 文本
print(soup.find_all(id='icp'))
print(soup.find_all(href=re.compile('upload')))
print(soup.find_all(href=re.compile('upload'), id='test'))  # 多个过滤条件
print(soup.find_all(attrs={'data-foo': 'value'}))   # 字典参数：<div data-foo="value">foo!</div>




# select CSS 选择题
print(soup.select('title'))     # <title>foo!</title>
print(soup.select('p nth-of-type(3)'))  # <p class="story"> ...</p>

# 逐层查找
print(soup.select('body a'))
print(soup.select('html head title'))

# 类名
print(soup.select('.sister'))
# 或
print(soup.select('[class~=sister]'))

# id
print(soup.select('#link1'))
# 组合
print(soup.select('a#link2'))

# 是否存在某个属性
print(soup.select('a[href]'))

# 通过属性值查找
print(soup.select('a[href="http://www.beian.miit.gov.cn"]'))
print(soup.select('a[href^="https://qixqi.club"]'))   # 可能是不等于，也可能前缀
print(soup.select('a[href$="tillie"]'))     # http://example.com/tillie
print(soup.select('a[href*=".com/el"]'))    # http://example.com/elsie










