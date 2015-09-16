from tkinter import *
import random
import time


class Snake:
    def __init__(self, canvas, food, couleur):
        self.canvas = canvas
        self.food = food
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

    def eat_food(self, pos):
        pos_food = self.canvas.coords(self.food.id)
        if (pos[0] and pos[1]) == (pos_food[0] and pos_food[1]):
            self.canvas.create_text(250, 250, text='GAME OVER')
        
class Food:
    def __init__(self, canvas, couleur):
        self.canvas = canvas
        self.id = canvas.create_oval(5, 5, 12.5, 12.5, fill=couleur)
        self.canvas.move(self.id, 200,100)
        self.x=0
        self.y=0

    def drawing_food(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        

tk = Tk()
tk.title("Miky's snake")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()


food = Food(canvas, 'purple')
snake = Snake(canvas, food,'red')


while 1:
    snake.drawing_snake()
    food.drawing_food()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
