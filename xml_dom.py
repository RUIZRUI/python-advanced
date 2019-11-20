# -*- coding: utf-8 -*-

# dom 首先一次性读取xml文档，在内存构建树，然后对树进行操作
import xml.dom.minidom


# 使用 minidom 解析器打开 xml 文档
DOMTree = xml.dom.minidom.parse('xml_movies.xml')
collection = DOMTree.documentElement
if collection.hasAttribute('shelf'):
    print('Root element: ', collection.getAttribute('shelf'))


# 获取所有电影
movies = collection.getElementsByTagName('movie')

# 打印每部电影的信息
for movie in movies:
    print('*'*10, 'Movie', '*'*10)
    # print('测试：', movie.childNodes[0])
    if movie.hasAttribute('title'):
        print('Title: ', movie.getAttribute('title'))
    
    type = movie.getElementsByTagName('type')[0]
    print('Type: ', type.childNodes[0].data)
    format = movie.getElementsByTagName('format')[0]
    print('format: ', format.childNodes[0].data)
    rating = movie.getElementsByTagName('rating')[0]
    print('rating: ', rating.childNodes[0].data)
    description = movie.getElementsByTagName('description')[0]
    print('description: ', description.childNodes[0].data)



