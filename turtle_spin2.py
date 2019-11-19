# -*- coding: utf-8 -*-
import turtle

# 绘制彩色螺旋图
colors = ['pink', 'orange', 'gold', 'yellow', 'green', 'cyan']
turtle.speed(0)
turtle.begin_fill()
for x in range(360):
    turtle.pencolor(colors[x%6])    # 画笔颜色
    turtle.width(x / 100 + 1)       # 画笔宽度，与turtle.pensize()一样
    # print(x//100 + 1)          # x/100 是浮点数， x//100 是整数
    turtle.forward(x)
    turtle.left(59)

turtle.end_fill()
turtle.hideturtle()
turtle.done()