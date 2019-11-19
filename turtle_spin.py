# -*- coding: utf-8 -*-
# 绘制正方形螺旋
import turtle

turtle.color('pink', 'pink')
turtle.begin_fill()
turtle.speed(10)

# 方法一
n = 10
for i in range(1, 10, 1):
    for j in [90, 180, -90, 0]:
        turtle.seth(j)
        turtle.forward(n)
        n += 5



# 方法二
# n = 10
# for i in range(100):
#     turtle.left(90)
#     turtle.forward(n)
#     n += 5



turtle.end_fill()
turtle.hideturtle()
turtle.done()