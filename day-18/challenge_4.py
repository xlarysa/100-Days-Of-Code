import turtle as t
import random as r

def get_random_color():
    return r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)

t.colormode(255)

tim = t.Turtle()
tim.shape('turtle')
tim.pensize(10)
tim.speed("fastest")

angles = [0, 90, 180, 270]
for _ in range(200):
    tim.color(get_random_color())
    tim.setheading(r.choice(angles))
    tim.forward(50)

screen = t.Screen()
screen.exitonclick()