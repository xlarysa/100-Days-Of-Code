from turtle import Turtle
x_cordinate = -400
y_cordinate = -300

class Frame(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.make_frame()
    def make_frame(self):
        self.goto(x_cordinate, y_cordinate)
        self.pendown()
        self.forward(800)
        self.left(90)
        self.forward(600)
        self.left(90)
        self.forward(800)
        self.left(90)
        self.forward(600)

