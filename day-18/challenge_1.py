from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("DarkSeaGreen4")
tim.penup()

for _ in range(2):
    tim.forward(100)
    tim.right(90)

tim.pendown()
for _ in range(4):
    tim.forward(250)
    tim.right(90)

screen = Screen()
screen.exitonclick()