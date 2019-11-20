class A():
    pass

a = A()
print(a)
a.name = 'jia'
a.age = 20
print(dir(a))
print(a.__dict__)