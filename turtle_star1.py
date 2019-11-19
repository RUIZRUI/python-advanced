# -*- coding: utf-8 -*-

import turtle

# 绘制五角星
turtle.setup(400, 400)
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.color('red')
turtle.begin_fill()
for i in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()
turtle.hideturtle()
turtle.done()