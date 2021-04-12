import turtle as tu
import time
import random as ra
from tkinter import *
#root = Tk()
#import sys
#from PIL import Image
#import screen



i = 0
rainb = ["red", "blue", "violet", "purple", "orange","yellow", "green"]
#GLLibScr = tu.Screen()
#GLLibScr.setup(400 + 4, 200 + 8)  # fudge factors due to window borders & title b


def buildGraph(num, color, x, y, rainbow, speed, mult):

    if rainbow is None:
        rainbow = False
    
    #GLLibScr.setworldcoordinates(0, 0, x + 8, y + 4)
    #tu.resizemode(True)
    #tu.screensize(x,y)
    tu.speed(speed)
    tu.screensize(y + 8,x + 4)
    tu.color("black")
    tu.goto(0, y)
    tu.write(y*mult, move=False, align="left", font=("Arial", 8, "normal"))
    tu.goto(0, 0)
    tu.goto(x, 0)
    tu.write(x*mult, move=False, align="left", font=("Arial", 8, "normal"))
    tu.goto(0, 0)
    tu.write(0, move=False, align="right", font=("Arial", 8, "normal"))
    i = 0
    il = 0
    tu.color(color)
    while i < len(num):
        tu.goto(il,num[i]*mult)
        i += 1
        il += x / (len(num) - 1)
        if rainbow:
            tu.color(rainb[ra.randint(0, 6)])
            
    tu.penup()
    tu.goto(0,0)
    tu.pendown()
    tu.color("black")
    tu.ht()
    fuv = tu.getscreen().getcanvas().postscript(file='Graphick_' + time.asctime() + '.eps')

def CLRGraph():
    tu.clear()
    
   
    
    
