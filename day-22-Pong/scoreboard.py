from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 70, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100,300)
        self.write(self.l_score, align = ALIGNMENT, font = FONT)
        self.goto(100,300)
        self.write(self.r_score, align = ALIGNMENT, font = FONT)

    def l_point(self):
        self.l_score += 1
        self.write_score()

    def r_point(self):
        self.r_score += 1
        self.write_score()

    def winner(self):
        self.home()
        if self.l_score > self.r_score:
            self.write("The left player won", align = ALIGNMENT, font = ("Courier", 40, "normal"))
        else:
            self.write("The right player won", align = ALIGNMENT, font = ("Courier", 40, "normal"))
