from tkinter import *
from tkinter import colorchooser
c = colorchooser.askcolor()
import random
tk = Tk()
canvas = Canvas(tk,width = 500, height = 500)
canvas.pack()
def random_rectangle(width,height,fillColor):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1+random.randrange(width)
    y2 = y1+random.randrange(height)
    canvas.create_rectangle(x1,y1,x2,y2,fill=fillColor)

#for x in range(0,100):
#    random_rectangle(400,400)

random_rectangle(400, 400, c[1])    
#random_rectangle(400, 400, 'green')
#random_rectangle(400, 400, 'red')
