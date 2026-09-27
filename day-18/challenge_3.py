import turtle as t
from random import randint

def get_random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)

t.colormode(255)

tim = t.Turtle()
tim.shape('turtle')

for sides in range(3, 11):
    tim.color(get_random_color())
    angle = 360 // sides
    for _ in range(sides):
        tim.right(angle)
        tim.forward(100)

screen = t.Screen()
screen.exitonclick()