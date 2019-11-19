# -*- coding: utf-8 -*-

# turtle 库是turtle 绘图体系的python实现


# turtle 原理
# 有一只海龟，在窗体正中心，在画布上游走，走过的轨迹形成了绘制的图形，海龟由程序控制，可以变换颜色，改变宽度等


# turtle 窗体布局
# turtle.setup() 需要控制窗体的大小和屏幕显示的位置时使用
# turtle.setup(width, height, startx, starty)   后两个可选，默认正中心（0，0）
# 如：turtle.setup(800, 800)    位于屏幕的正中心


# turtle 空间坐标体系
# 绝对坐标：海龟在正中心（0，0）
# 海龟坐标：当前海龟的朝向为前进方向，反方向是后退方向
# turtle.circle(r, angle)  拐弯，第一个参数方向，第二个参数角度
# turtle.fd(distance) 前进，distance可以是负数，单位像素    
# turtle.bk(distance) 后退，distance可以是负数，单位像素
# turtle.position()   当前海龟的位置
# turtle.heading()    当前海龟的朝向


# turtle 角度坐标体系
# 绝对角度：turtle.seth(angle)，只改变运动方向
    # turtle.seth(0)        右
    # turtle.seth(90)       上
    # turtle.seth(180)      左
    # turtle.seth(-90/270)  下
# 海龟角度：
# turtle.left(angle)    向左
# turtle.right(angle)   向右


# RGB 色彩体系
# turtle.colormode(mode)    改变颜色，默认采用小数值，可以切换为整数值
# 洋红 megenta (255,0,255)      (1,0,1)
# 黄   yellow  (255,255,0)      (1,1,0)
# 青   cyan    (0,255,255)      (0,1,1)
# 蓝   blue    (0,0,255)        (0,0,1)
# 紫   purple  (160,32,240)     (0.63,0.12,0.94)
# 白   white   (255,255,255)    (1,1,1)
# 黑   black   (0,0,0)          (0,0,0)
# 金   gold    (255,215,0)      (1,0.84,0)
# 粉红 pink    (255,192,203)    (1,0.75,0.80)



# turtle 画笔控制函数
# turtle.penup() 或 turtle.pu()     抬起画笔
# turtle.pendown() 或 turtle.pd()   放下画笔
# turtle.pensize(width) 或 turtle.width(width)  设置画笔宽度
# turtle.pencolor(color)        设置画笔颜色
    # turtle.pencolor('purple')
    # turtle.pencolor(0.63, 0.13, 0.93)
    # turtle.pencolor((0.63, 0.13, 0.93))   元组



# turtle 运动控制函数
# turtle.forward(distance) 或 turtle.fd(distance)   直线
# turtle.circle(r, extent)   曲线
    # r:默认圆心在海龟左侧r距离的位置
    # extent:绘制角度，默认是360度
# turtle.circle(r, extent=None) 根据半径r绘制extent角度的弧形
# turtle.goto(x, y)  海龟移动到(x, y)处
# turtle.setx(x)    修改海龟的横坐标 
# turtle.sety(y)    修改海龟的纵坐标



# turtle 方向控制函数
# turtle.setheading(angle) 或 turtle.seth(angle)    设置海龟朝向
    # angle 可以是绝对角度或海龟角度
    # angle: 改变海龟行进方向，海龟行进的角度
# turtle.left(angle)    海龟左转
# turtle.right(angle)   海龟右转
    # angle: 在海龟当前行进方向的基础上旋转，只改变海龟行进方向



# turtle.home()： 海龟回到原点，朝向东
# turtle.dot(r, color)：  绘制一个半径为r，颜色为color的原点
# turtle.undo()：   撤销最后一次动作
# turtle.speed()：  设置画笔的绘制速度，参数在0～10之间


# turtle.goto(x, y)   走斜线，一步到达目的地
# turtle.setx(x) + turtle.sety(y)    走折线，折线平行于坐标轴



print('你瞅啥')
print('瞅你咋地')