from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk,width = 400, height = 400)
canvas.pack()
colors = ['red','green','blue','yellow','orange','white','purple']
def rand_tri(width,height):
    p1 = random.randrange(width)
    p2 = random.randrange(height)
    q1 = random.randrange(width)
    q2 = random.randrange(height)
    r1 = random.randrange(width)
    r2 = random.randrange(height)
    color = random.choice(colors)
    canvas.create_polygon(p1,p2,q1,q2,r1,r2,fill=color)

for x in range(0,100):
    rand_tri(300,300)
