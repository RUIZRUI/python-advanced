# -*- coding: utf-8 -*-
import turtle

# turtle.circle(radius, extent=None, steps=None)
# radius 半径
    # radius 是正值，逆时针方向画弧(不是相对于海龟）
    # radius 是负值，顺时针方向画弧(不是相对于海龟)
# extent 画圆的角度，默认360
    # 可以这样理解
    # extent 是正值，画圆方向不变
    # extent 是负值，本来forward画圆，现在back画圆
# steps 由于圆是由内接正多边形逼近的，该参数决定了要用到的步数，可以用来画正多边形（翻译）
# turtle.setup(400, 400)
turtle.color('pink', 'pink')
turtle.speed(1)
# turtle.begin_fill()

# turtle.setx(-100)
# turtle.sety(100)
turtle.goto(-100, 100)
# turtle.setheading(0)
print(turtle.heading())
print(turtle.position())
print()
turtle.circle(50, 180)      # 逆时针

# turtle.setx(100)
# turtle.sety(100)
turtle.goto(100, 100)
# turtle.setheading(0)
print(turtle.heading())
print(turtle.position())
print()
turtle.circle(50, -180)     # 顺时针

# turtle.setx(-100)
# turtle.sety(-100)
turtle.goto(-100, -100)
# turtle.setheading(0)
print(turtle.heading())
print(turtle.position())
print()
turtle.circle(-50, 180)     # 顺时针

# turtle.setx(100)
# turtle.sety(-100)
turtle.goto(100, -100)
# turtle.setheading(0)
print(turtle.heading())
print(turtle.position())
print()
turtle.circle(-50, -180)    # 逆时针

# turtle.end_fill()
# turtle.hideturtle()
turtle.done()