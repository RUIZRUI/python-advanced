# -*- coding: utf-8 -*-
import turtle

# 绘制方形螺旋图
turtle.speed(0)
turtle.color('pink', 'pink')
turtle.begin_fill()
for i in range(500):
    turtle.forward(i)
    turtle.left(91)

turtle.end_fill()
turtle.hideturtle()
turtle.done()