from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk,width = 500, height = 500)
canvas.pack()
myImage = PhotoImage(file='e:\\tenor.gif')
imageIdentifier = canvas.create_image(0,0,anchor=NW,image=myImage)
for x in range(0,60):
    canvas.move(imageIdentifier,5,5)
    tk.update()
    time.sleep(0.03)
