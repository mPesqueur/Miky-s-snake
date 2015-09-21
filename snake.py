from tkinter import *
import random
import time

class Snake:
    def __init__(self, canvas, couleur):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 10, 20, 20, fill=couleur)
        self.canvas.move(self.id, 250, 250)
        self.x=0
        self.y=0
        self.canvas.bind_all('<KeyPress-Right>', self.right_move)
        self.canvas.bind_all('<KeyPress-Left>', self.left_move)
        self.canvas.bind_all('<KeyPress-Up>', self.up_move)
        self.canvas.bind_all('<KeyPress-Down>', self.down_move)
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height=self.canvas.winfo_height()
        

    def right_move(self, evt):
        self.x = 0.5
        self.y = 0

    def left_move(self, evt):
        self.x = -0.5
        self.y = 0

    def up_move(self, evt):
        self.y = -0.5
        self.x = 0

    def down_move(self, evt):
        self.y = 0.5
        self.x = 0
        
    def drawing_snake(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        ##Bordures solides
        if pos[0] <=0:
            self.x=0
            self.canvas.create_text(250, 250, text='GAME OVER')##en attente d'un vrai endgame##
        if pos[2]>= self.canvas_width:
            self.x=0
            self.canvas.create_text(250, 250, text='GAME OVER')##en attente d'un vrai endgame##
        if pos[1]<=0:
            self.y=0
            self.canvas.create_text(250, 250, text='GAME OVER')##en attente d'un vrai endgame##
        if pos[3]>= self.canvas_height:
            self.y=0
            self.canvas.create_text(250, 250, text='GAME OVER')##en attente d'un vrai endgame##




class Food:
    def __init__(self, canvas, snake, couleur):
        self.canvas = canvas
        self.snake = snake
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height=self.canvas.winfo_height()
        self.x=random.randint(0, self.canvas_width)
        self.y=random.randint(0, self.canvas_height)
        self.r = 5
        self.id = canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=couleur)
        self.OvalsList = []

    def drawing_food(self):
        self.canvas.move(self.id, 0, 0)
        pos = self.canvas.coords(self.id)

        
    def eat_food(self):
        pos = self.canvas.coords( self.id )
        pos_snake = self.canvas.coords(self.snake.id)
        self.x_milieu_pos = abs((pos[0]+pos[2])/2)
        self.y_milieu_pos = abs((pos[1] + pos[3])/2)
        self.x_milieu_pos_snake = abs((pos_snake[0]+pos_snake[2])/2)
        self.y_milieu_pos_snake = abs((pos_snake[1] + pos_snake[3])/2)

        if ((self.x_milieu_pos == self.x_milieu_pos_snake) and (self.y_milieu_pos == self.y_milieu_pos_snake)):
            self.canvas.create_text(250, 250, text='touche')
            self.x=random.randint(0, self.canvas_width)
            self.y=random.randint(0, self.canvas_height)
            self.r = 5
            self.canvas.delete(self.id)
            self.id = canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill='purple')
            
        
tk = Tk()
tk.title("Miky's snake")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()


snake = Snake(canvas,'red')
food = Food(canvas, snake,  'purple')


while 1:
    snake.drawing_snake()
    food.drawing_food()
    food.eat_food()
    
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
