from turtle import Turtle
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(x, y)

    def move_up(self):
        if self.ycor() < 240:
            self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -240:
            self.back(MOVE_DISTANCE)