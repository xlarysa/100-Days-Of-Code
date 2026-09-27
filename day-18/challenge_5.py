import turtle as t
import random as r

def get_random_color():
    return r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)

t.colormode(255)

tim = t.Turtle()
tim.shape('turtle')
tim.speed("fastest")
tim.pensize(2)

def draw_spirograph(gap):
    for _ in range(360 // gap):
        tim.color(get_random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()