import turtle as t
import random as rnd

screen = t.Screen()
screen.setup(width = 500, height = 400)

def set_turtles():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtles = []
    x, y = -230, -70
    for color in colors:
        new_turtle = t.Turtle()
        new_turtle.shape("turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x, y)
        turtles.append(new_turtle)
        y += 30
    return turtles

is_race_on = False
turtles = set_turtles()

users_bet = screen.textinput(title = "Make your a bet", prompt = "Which turtle will win the race? Enter a color: ")
if users_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = rnd.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()

if users_bet == winning_turtle:
    print(fr"You won! The {winning_turtle} turtle is the winner!")
else:
    print(f"You lost! The {winning_turtle} turtle is the winner!")

screen.exitonclick()