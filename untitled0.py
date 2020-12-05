# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:14:07 2020

@author: user
"""

import turtle
tur=turtle.Turtle()
def writenum(num):
    tur.penup()
    tur.forward(200)
    tur.write(num)
    tur.back(200)
    tur.pendown()

tur.seth(90)
for i in range(1,13,1):
    tur.right(30)
    
    if i%2 ==0:
        tur.color(0,0,1)
    else:
        tur.color(1,0,0)
       
    writenum(i)

#tur.circle(100,360,100)

turtle.done()
turtle.exitonclick()