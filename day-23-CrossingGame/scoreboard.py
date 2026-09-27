from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-200, 260)
        self.level = 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)