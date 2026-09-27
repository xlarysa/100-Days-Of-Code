from turtle import Turtle
import random as rnd

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("purple")
        self.refresh()

    def refresh(self):
        random_x = rnd.randint(-295,295)
        random_y = rnd.randint(-295,295)
        self.teleport(random_x, random_y)