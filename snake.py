from tkinter import *
import random
import time


class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.r = 10
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height=self.canvas.winfo_height()
        self.x=random.randint(0, self.canvas_width)
        self.y=random.randint(0, self.canvas_height)
        self.id = canvas.create_rectangle(10, 10, 20, 20, fill='green')
        self.canvas.move(self.id, self.x, self.y)
        self.vit_x=0
        self.vit_y=0
        self.canvas.bind_all('<KeyPress-Right>', self.right_move)
        self.canvas.bind_all('<KeyPress-Left>', self.left_move)
        self.canvas.bind_all('<KeyPress-Up>', self.up_move)
        self.canvas.bind_all('<KeyPress-Down>', self.down_move)
        

    def right_move(self, evt):
        self.vit_x = 2
        self.vit_y = 0

    def left_move(self, evt):
        self.vit_x = -2
        self.vit_y = 0

    def up_move(self, evt):
        self.vit_y = -2
        self.vit_x = 0

    def down_move(self, evt):
        self.vit_y = 2
        self.vit_x = 0
        
    def drawing_snake(self):
        self.canvas.move(self.id, self.vit_x, self.vit_y)
        pos = self.canvas.coords(self.id)
        if pos[0] <=0:
            self.vit_x=0
        if pos[2]>= self.canvas_width:
            self.vit_x=0
        if pos[1]<=0:
            self.vit_y=0
        if pos[3]>= self.canvas_height:
            self.vit_y=0
        
class Food:
    def __init__(self, canvas, snake):
        self.canvas = canvas
        self.snake = snake
        self.r = 5
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height=self.canvas.winfo_height()
        self.x=random.randint(0, self.canvas_width)
        self.y=random.randint(0, self.canvas_height)
        self.id = canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill='purple')
        self.vit_x=1
        self.vit_y=-1

    def drawing_food(self):
        self.canvas.move(self.id, self.vit_x, self.vit_y)
        pos = self.canvas.coords(self.id)
        if pos[1] <=0:
            self.vit_y = 1
        if pos[3] >= self.canvas_height:
            self.vit_y = -1
        if pos[0] <=0:
            self.vit_x = 1
        if pos[2] >= self.canvas_width:
            self.vit_x = -1
        

        
    def eat_food(self):
        pos = self.canvas.coords( self.id )
        pos_snake = self.canvas.coords(self.snake.id)
        if (( abs(pos[0] - pos_snake[0]) <= 5  and abs(pos[1] - pos_snake[1] ) <= 5)):
            self.r = 5
            self.x=random.randint(0, self.canvas_width)
            self.y=random.randint(0, self.canvas_height)
            self.canvas.delete(self.id)
            self.id = canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill='purple')


class Score:
    def __init__(self, canvas, snake, food):
        self.canvas = canvas
        self.snake = snake
        self.food = food
        self.score = 0
        self.id=self.canvas.create_text(40, 20, text='Your score: %s' % self.score)
        
    def score_update(self):
        pos_snake = self.canvas.coords(self.snake.id)
        pos_food = self.canvas.coords(self.food.id)

        if (( abs(pos_food[0] - pos_snake[0]) <= 5  and abs(pos_food[1] - pos_snake[1] ) <= 5)):
            self.canvas.delete(self.id)
            self.score =self.score + 1
            self.id=self.canvas.create_text(40, 20, text='Your score: %s' % self.score)

class Food_manager:
    def __init__(self, canvas, snake):
        self.canvas = canvas
        self.snake = snake
        self.list_food = []
        
    def boucle_food(self):
        for i in range(0, 11):
            self.list_food.append(Food(self.canvas, self.snake))
            tk.update()

    def drawing_food(self):
        pass

    def eat_food(self):
        pass
            
            

tk = Tk()
tk.title("Miky's snake")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

snake = Snake(canvas)
food = Food(canvas, snake)
score = Score(canvas, snake, food)
food_manager = Food_manager(canvas, snake)
food_manager.boucle_food()


while 1:
    snake.drawing_snake()
    food.drawing_food()
    score.score_update()
    food.eat_food()
    food_manager.drawing_food()
    food_manager.eat_food()

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
