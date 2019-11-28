# -*- coding: utf-8 -*-
import re

'''
python 正则表达式的标志位 flags
    re.I：忽略大小写
    re.L：表示特殊字符集
    re.M：多行模式
    re.S：使 '.' 匹配包括换行符在内的所有字符
    re.U：表示特殊字符集
    re.X：忽略空格和 '#' 后面的注释
'''


'''
字符模式：
    [a-zA-Z] 匹配一个字符
    ^和$: 匹配首尾
    \^和\$: 字面值
    .: 匹配任意字符
    \.: 字面值
    \b: 匹配单词边界
    \w: 匹配非空字符
    \s: 匹配空格
    \d: 匹配数字
    \D: 匹配非数字
'''


'''
匹配重复：
    *, +   表示最长匹配
    *?, +? 表示最短匹配
    .*     表示任意匹配除换行符(\n, \r)之外的任何单个或多个字符
    \*, \+ 字面值
    {3}    表示重复3次
    {4,6}  表示重复4-6次
'''
print(re.match(r'ab*', 'abbbbbbb').group())     # 默认最长匹配
print(re.match(r'ab*?', 'abbbbb').group())
print(re.match(r'a\d{3,4}', 'a1234567').group())


'''
    |   表示或
    \|  字面值
'''
print(re.match(r'(abc)|(def)', 'abc').group())
print(re.match(r'(abc)|(def)', 'def').group())


'''
分组捕获
    [] 具有去特殊符号的作用     [(] 表示一般的括号
    () 提取整个正则串中符合括号里的正则的内容
'''
# \1 表示要匹配的字符串中对应位置与第一个匹配的一样
print(re.match(r'x(\d+) = \1', 'x123 = 123').group())
print(re.match(r'x(\d+) = \1', 'x123 = 123').groups())
p = re.compile('(a(b)c)d')
m = p.match('abcd')
print(m)
print(m.group())
print(m.groups())
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(re.findall(r'(.)\1', '明明亮亮蛋蛋'))





# re.match(pattern, string, flags=0)        flags 标志位，如是否区分大小写，多行匹配等
# 起始位置匹配
# 返回匹配对象，否则返回 None
print(re.match('www', 'www.runoob.com'))
print(re.match('www', 'www.runoob.com').span())
print(re.match('com', 'www.runoob.com'))


line = 'Cats are smarter than dogs'
# .* 表示任意匹配除换行符(\n, \r)之外的任何单个或多个字符
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print('matchObj.group() : ', matchObj.group())
    print('matchObj.groups() : ', matchObj.groups())
    print('matchObj.group(1) : ', matchObj.group(1))
    print('matchObj.group(2) : ', matchObj.group(2))
else:
    print('No match!')








# re.search(pattern, string, flags=0)
# 返回第一个成功的匹配
print(re.search('www', 'www.runoob.com').span())        # 起始位置匹配
print(re.search('com', 'www.runoob.com').span())        # 不在起始位置匹配


line = 'Cats are smarter than dogs'
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
if searchObj:
    print('searchObj.group() : ', searchObj.group())
    print('searchObj.groups() : ', searchObj.groups())
    print('searchObj.group(1) : ', searchObj.group(1))
    print('searchObj.group(2) : ', searchObj.group(2))
else:
    print('Nothing found!')







# 检索和替换
# re.sub(pattern, repl, string, count=0, flags=0)
# repl：替换后的字符串
# count：替换的最大次数，默认全部
phone = '2004-959-559 # 这是一个电话号码'
num = re.sub(r'#.*$', '', phone)    # 删除注释
print('电话号码：', num)
num = re.sub(r'\D', '', phone)      # 删除非数字内容
print('电话号码：', num)

# 函数作为 repl 参数
def double(matched):
    '''
        将匹配的数字乘以 2
    '''
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
s_result = re.sub('(?P<value>\d+)', double, s)
print(s_result)









# compile 函数
# re.compile(pattern, flags)    # pattern 这里是字符串形式的正则表达式
# 生成正则表达式对象 Pattern
pattern = re.compile( r'\d+')   # 至少匹配一个数字
print(pattern.match('one12twothree34four'))     # 头部匹配
print(pattern.match('one12twothree34four', 2, 10))  # e 开始匹配
result = pattern.match('one12twothree34four', 3, 10)  # 1 开始匹配
print(result)
print(result.group(0))
print(result.start(0))
print(result.end(0))
print(result.span(0))


pattern = re.compile( r'([a-z]+) ([a-z]+)', re.I)
result = pattern.match('Hello World Wide Web')
print(result)
print(result.group(0))
print(result.span(0))
print(result.group(1))
print(result.span(1))
print(result.group(2))
print(result.span(2))
print(result.groups())
# print(result.group(3))








# re.findall(string, pos, endpos)
# pos：起始位置，可省略, endpos：结束位置，可省略     [pos, endpos-1]
# 找到匹配的所有子串，返回列表，没有匹配，则返回空列表
pattern = re.compile( r'\d+')
result1 = pattern.findall('runoob 123 google 456')
print(result1)
result2 = pattern.findall('run88oob123google456', 0, 10)
print(result2)











# re.finditer(pattern, string, flags=0)
# 查找匹配的所有子串，作为迭代器返回
it = re.finditer(r'\d+', '12a32bc43jf3')
for match in it:
    print(match.group())









# re.split(pattern, string, maxsplit=0, flags=0)
# 按照匹配的子串将字符串分割，返回列表
# maxsplit：分割次数，默认不限次数
print(re.split('\W+', 'runoob, runoob, runoob.'))
print(re.split('(\W+)', ' runoob, runoob, runoob.'))
print(re.split('\W+', ' runoob, runoob, runoob.', 1))
# 找不到匹配的字符串，split不会分割
print(re.split('a*', 'hello world')) 









# 日期格式转换  
# 2019-11-14  -->   11/14/2019
s = '2019-11-14'
result = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', s)
# () 划分原字符串的组
# {} 表示数字的个数
# r'\2/\3/\1'  2， 3， 1为输入的字符串三段的序号
print(result)








# (?<name>exp) 匹配exp，并捕获文本到name的组里
pattern = re.compile(r'(?P<here>[a-z]+) (?P<there>[a-z]+)', re.I)
result = pattern.match('Hello World World Web')
print(result.group('here'))
print(result.group('there'))








# \b 的灵活用法
# \b 与 \B 相反
# \b 表示字母数字与非字母数字的边界，非字母数字与字母数字的边界
# \B 表示字母数字与字母数字的边界，非字母数字与非字母数字的边界
# 找到小写字母开头的单词和数量
s = 'i Am a gOod boy baby!!'
result = re.findall(r'\b[a-z][a-zA-Z]*\b', s)
print(result) 
print('小写字母开头的单词个数：', len(result))







# 匹配 IP 地址
ip = '192.168.1.1'
trueIp = re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])',ip)
print(trueIp.group())




# re.sub 匹配标点符号，换行
s = "you're asking me out.that's so cute.what's your name again?"
result = re.sub(r'([.!?])', r'\1\n', s)
print(result)









# 文本重复了两次，保留一个
# x = 'this is is ok ok'
x = 'this is ok ok'
y = re.sub(r'\s(\w+)\s\1', r' \1', x)
print(y)