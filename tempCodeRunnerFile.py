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

