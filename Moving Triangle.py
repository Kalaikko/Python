from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk,width = 500, height = 500)
canvas.pack()
myTriangle = canvas.create_polygon(10,10,10,60,50,35,fill="blue",outline="black")

def moveTri(leftPixel,rightPixel):
    for x in range(0,80):
        canvas.move(myTriangle,leftPixel,rightPixel)
        tk.update()
        time.sleep(0.03)

moveTri(5,0)
moveTri(0,5)
moveTri(-5,0)
moveTri(0,-5)
