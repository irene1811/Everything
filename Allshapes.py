from turtle import *
import math
# Name your Turtle
t = Turtle()
#Set Up your screen and starting position

setup (500,300)
x_pos = (0)
y_pos = (0)
t.setposition(x_pos,y_pos)
color=input('color')
pencolor(color)
sides= input('sides')
sides=int(sides)
angle=360/sides



for i in range (sides):
  forward (50)
  left(angle)


# for i in range (5):
#     forward (50)
#     left(72)
# for i in range (6):
#     forward (50)
#     left (60)
# for i in range (7):
#     forward (50)
#     left (360/7)
# for i in range (8):
#     forward (50)
#     left (360/8)
# for i in range (9):
#     forward (50)
#     left (360/9)
exitonclick()
