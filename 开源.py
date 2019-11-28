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





# turtle 模块学习






# 封装、继承、多态
# __init__(self, 参数) 函数
class Dog:
    tricks = [] # 共有数据
    def __init__(self, name):
        self.name = name  # 私有数据
    
    def addtrick(self, trick):
        self.tricks.append(trick)

fido = Dog('fido')
buddy = Dog('buddy')
fido.addtrick('rool over')
print(buddy.tricks)   # 共有数据, buddy 中数据也改变





class A():
    def __init__(self, a, b):
        self.a = a
        self.b = b

a = A(1, 2)
b = A(3, 4)
print(a.__dict__)
# 是否有属性
if hasattr(a, 'b'):
    print('a有属性b')
else:
    print('a没有属性b')


if hasattr(A, 'b'):
    print('A有属性b')
else:
    print('A没有属性b')


a._a = 'are you ok'
print(a)    # 不显示a._a
print(a._a) # 显示 a._a

# 删除对象
del a
del b




# 继承关系
class A:    # 父类
    def foo(self):
        print('in A::foo')

class B(A):     # B 继承 A
    def foo(self):
        print('in B::foo')

b = B()
b.foo()
print(isinstance(b, A)) # True
print(isinstance(b, B)) # True
print(issubclass(B, A)) # B是否是A的子类



# 多态
# 子类没有覆盖父类，则调用父类的属性或方法
# 子类覆盖父类，则调用自己的属性或方法
class B2(A):
    def foo2(self):
        print('in B2:foo2')

b2 = B2()
b2.foo()
b2.foo2()
print(isinstance(b2, A))    # True
print(isinstance(b2, B))    # False
print(isinstance(b2, B2))   # True








# 鸭子类型
# 运行时才检查，编译过程中不检查类型
class A:
    def foo(self):
        print('in A::foo')

class B(A):
    def foo(self):
        print('in B::foo')

class C:
    def foo(self):
        print('not subclass')

def test_class(a):
    a.foo()     # 只检查操作，不考虑a的类型

a = A()
b = B()
c = C()
test_class(a)
test_class(b)
test_class(c)
# 鸭子测试通过，呱呱呱






# Closure模型
# guile
# haskell趣学指南

# 单行表达式
increase = lambda x: x + 1
print(increase(20))


# 闭包
# 函数嵌套
# 内部函数使用外部函数的变量
def outer():
    count = 0   # 保存状态
    def inner():
        nonlocal count
        count += 1
        return count
    
    return inner

x = outer()
print(x)
print(type(x))  # 返回函数
print(x())
print(x())


# 偏函数
from functools import partial
def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double)
print(double(5))
triple = partial(multiply, 3)
print(triple)
print(triple(5))





# 列表推导
list1 = [i*2 for i in range(10)]
print(list1)

list2 = [i*2 for i in range(10) if i%2 == 0]
print(list2)


a = [1, 2, 3]
b = [4, 5, 6]
list3 = [[(i, j) for i in a] for j in b]
print(list3)
