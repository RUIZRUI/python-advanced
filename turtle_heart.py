# -*- coding: utf-8 -*-
import turtle

# 线条颜色 red, 内部颜色 pink
# turtle.speed(1)
# turtle.color('red', 'pink')
turtle.color('pink', 'pink')
turtle.begin_fill()
turtle.left(135)
turtle.forward(100)
turtle.right(180)
turtle.circle(50, -180)
turtle.left(90)
turtle.circle(50, -180)
turtle.right(180)
turtle.forward(100)
turtle.end_fill()
turtle.hideturtle()
turtle.done()