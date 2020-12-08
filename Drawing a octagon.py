import turtle
t = turtle.Pen()
t.reset()
def octagon(size,angle,filled):
    if filled == True:
        t.begin_fill()
    for x in range(1,9):
        t.forward(size)
        t.right(angle)
    if filled == True:
        t.end_fill()

t.color(0.9,0.5,0.15)
octagon(50,45,True)
t.color(0,0,0)
octagon(50,45,False)
