from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed(1)
        self.y_direction = 10
        self.x_direction = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_direction *= -1

    def paddle_bounce(self):
        self.x_direction *= -1
        self.move_speed *= 0.9

    def refresh(self):
        self.home()
        self.move_speed = 0.1
        self.paddle_bounce()