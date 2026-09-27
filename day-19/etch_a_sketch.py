import turtle as t

def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


tim = t.Turtle()
screen = t.Screen()
tim.color("red")

screen.listen()

screen.onkeypress(fun = lambda: tim.forward(10), key = "w")
screen.onkeypress(fun = lambda: tim.back(10), key = "s")
screen.onkeypress(fun = lambda: tim.lt(10), key = "a")
screen.onkeypress(fun = lambda: tim.rt(10), key = "d")
screen.onkey(fun = clear_screen, key = "c")

screen.exitonclick()

