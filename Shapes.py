from turtle import *
import math
# Name your Turtle
t = Turtle()
#Set Up your screen and starting position
setup (500,300)
x_pos = (0)
y_pos = (0)
t.setposition(x_pos,y_pos)
for i in range (3):
    forward(50)
    left(120)

for i in range (5):
    left (-60)
    for i in range (3):
        forward(50)
        left (120)
for i in range (5):
    forward(50)
    for i in range (2):
        forward(50)
        left(120)

    for i in range (5):
        left (-60)
        for i in range (3):
            forward(50)
            left (120)

exitonclick ()
