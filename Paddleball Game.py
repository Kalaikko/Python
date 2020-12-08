from tkinter import *
import random
import time

# Ball class to move and bounce
class Ball:
    def __init__(self,canvas,paddle,score,color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.x+=self.paddle.x
                self.score.hit()
                return True
        return False

#Paddle class to make the ball bounce
class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        #self.canvas.bind_all('<Button-1>',self.start_game)
        #self.start_game = False

    #def start_game(self,event):
        #self.start_game = True

    def turn_left(self,event):
        self.x = -3

    def turn_right(self,event):
        self.x = 3

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

#Class for printing the score
class Score:
    def __init__(self,canvas,color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(410,10,text='Total Score: %s' %self.score\
                                     ,fill=color)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id,text='Total Score: %s' %self.score)

def quit_window():
    tk.destroy()

startGame = False
def start_game():
    global startGame
    startGame = True

tk = Tk()
tk.title("Bounce Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
start_game_image = PhotoImage(file='e:\\Paddle Game.gif')
canvas.create_image(250,200,image=start_game_image)
canvas.create_text(250,20,text = 'TIME TO START',\
                               fill= 'green',font = ('Calibri',20))
canvas.pack()
Button(tk, text="Start Game", command=start_game()).pack()
tk.update()

if(startGame == True):
    time.sleep(2)
    tk.destroy()
    tk = Tk()
    tk.title("Bounce Game")
    tk.resizable(0,0)
    tk.wm_attributes("-topmost",1)
    canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
    canvas.pack()
    tk.update()

    score = Score(canvas,'green')
    paddle = Paddle(canvas,'blue')
    ball = Ball(canvas,paddle,score,'red')
    game_over_image = PhotoImage(file='e:\\Game over.gif')
    #game_over_text = canvas.create_text(250,100,text = 'You Lost Funny Fucker :(',\
    #                           fill= 'red',font = ('Times',20),state='hidden')


    while 1:
        if ball.hit_bottom == False: # and paddle.start_game == True:
            ball.draw()
            paddle.draw()
        if ball.hit_bottom == True:
            time.sleep(0.5)
            canvas.create_image(250,100,image=game_over_image)
            #canvas.itemconfig(game_over_text,state='normal')
            score.canvas.itemconfig(score.id,state='hidden')
            canvas.create_text(250,250,text='Your Score: %s' %score.score,\
                               fill='green',font = ('Calibri',20))
            Button(tk, text="Quit", command=quit_window).pack()
            break
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

