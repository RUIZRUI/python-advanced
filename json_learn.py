# -*- coding: utf-8 -*-

# json.dumps() 编码: python --> json
# json.loads() 解码: json --> python

# json 对象中是双引号，不是单引号
# repr(object)  返回一个对象的 string 格式，也可以使用 dict 充当 object

# python 对象与字典之间的转换
'''
class A():
    pass

a = A()
print(a)
a.name = 'jia'
a.age = 20
print(dir(a))
print(a.__dict__)

'''


# 编码
'''
    Python     -->             JSON
    dict                       object
    list, tuple                array
    str                        string
int, float, Enums<int, float>  number
    True                       true
    False                      false
    None                       null
'''

# 解码
'''
    JSON        -->     Python
    object              dict
    array               list
    string              str
    number<int>         int
    number<real>        float
    true                True
    false               False
    null                None
'''





import json

# json.dumps() 编码
# Python 字典
data = {
    'no': 1,
    'name': 'QixQi',
    'url': 'https://www.qixqi.club'
}

json_str = json.dumps(data)
print('Python 原始数据: ', repr(data))
print('JSON 对象: ', json_str)




# json.loads() 解码
data2 = json.loads(json_str)
print('JSON 对象解码后：', data2)
print('data2["name"] = ', data2['name'])
print('data2["url"] = ', data2['url'])
print()





# 处理 json文件
# json.dump()
# json.load()
# 读取数据，json.load() 解码
with open('json_read.json', 'r') as fp_read:
    data = json.load(fp_read)
    print(data)

# 写入json文件, json.dump() 编码
with open('json_write.json', 'w') as fp_write:
    data['name'] = 'qixqi'
    json.dump(data, fp_write)
