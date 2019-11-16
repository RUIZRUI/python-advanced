# -*- coding: utf-8 -*-

test = 'hello hello hello '

print(test[-1])         # ' '

print(test[2:300])      # 切片，不报错，到达最后

print(test[2:])       

print(test[:3])

print(test[:])


# python 中变量: id + value
a = test
b = test[:]
print( a is test)   # True
print( b is test)   # True


# python test[0] 不能改变
# test[0] = '2'

print('H' + test[1:])
# print('H' + 3)        # 类型不一样


# 格式化输出
result = 10
print('The result is %d' % 10)      # 内差方式
print('The result is {}'.format(result))
print(f'The result is {result}')    # 格式化字符串，> python3.6
print('The result is', result)

print(r'a\n')
print('a\\n')



# 列表
List = [1, 2, 3, 'abc', 1+4j, [1, 2, 3]]
print(len(List))
print(type(List))
print(List * 2)
List = List + [4, 5, 6]
print(List)
List.append(100)
print(List)

List1 = [1, 2, 3]
List2 = ['a', 'b', 'c']
print([List1, List2])


# 流程控制
# False: None/0/''/[]/{}
# Python 缩进：4个空格
grade = 87
if 85 < grade < 90:
    print('Good')
else:
    print('???')


if grade > 90:
    pass
elif grade > 85:
    print('Good')
elif grade > 80:
    print('Not bad')
else:
    print('Come on')


# for 循环
elements = [1, 2, 3]
for element in elements:
    print(element ** 2)

# while 循环
count = 5
while count < 5:
    print('count = ', count)    
else: 
    print('end')

# range 生成器，产生数列
print(type(range(10)))
print(range(10))
print(list(range(10)))
for i in range(10):
    print('i =', i)

# 双层循环
for i in range(5):
    for j in range(6):
        print(f'{i}, {j}')