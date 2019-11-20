# -*- coding: utf-8 -*-

# 使用 SAX 解析 xml
# 基于事件驱动

import xml.sax


# 继承 ContentHandler 对象
class MovieHandler (xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ''
        self.type = ''
        self.format = ''
        self.year = ''
        self.rating = ''
        self.stars = ''
        self.description = ''

    
    # 元素开始调用<开始标签>
    def startElement(self, name, attrs):
        '''
            name: 标签名
            attrs: 属性字典
        '''
        self.CurrentData = name
        # <movie>
        if name == 'movie':
            print('*'*10, 'Movie', '*'*10)
            title = attrs['title']
            print('Title: ', title)
        

    # 读取字符时调用
    def characters(self, content):
        if self.CurrentData == 'type':
            self.type = content
        elif self.CurrentData == 'format':
            self.format = content
        elif self.CurrentData == 'year':
            self.year = content
        elif self.CurrentData == 'rating':
            self.rating = content
        elif self.CurrentData == 'stars':
            self.stars = content
        elif self.CurrentData == 'description':
            self.description = content


    # 元素结束调用
    def endElement(self, name):
        if self.CurrentData == 'type':
            print('Type: ', self.type)
        elif self.CurrentData == 'format':
            print('Format: ', self.format)
        elif self.CurrentData == 'year':
            print('Year: ', self.year)
        elif self.CurrentData == 'rating':
            print('Rating: ', self.rating)
        elif self.CurrentData == 'stars':
            print('Stars: ', self.stars)
        elif self.CurrentData == 'description':
            print('Description: ', self.description) 
        self.CurrentData = ''   # 防止出现的 </movie>, </collection> 对结果的影响


if __name__ == '__main__':
    # 创建一个解析器
    parser = xml.sax.make_parser()
    # 关闭命名空间
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override ContentHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse('xml_movies.xml')
