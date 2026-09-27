#import colorgram
# colors = colorgram.extract('image.jpg', 30)
# pallete = [(colors[i].rgb[0],colors[i].rgb[1], colors[i].rgb[2])  for i in range(len(colors))]
# print(pallete)

import turtle as t
import random as rnd

def draw_a_row():
    for _ in range(10):
        tim.color(rnd.choice(palette))
        tim.dot(26)
        tim.forward(50)

palette = [(219, 248, 241), (237, 222, 85), (231, 170, 98), (193, 227, 243), (252, 53, 12), (239, 49, 85),
           (156, 84, 28), (172, 59, 112), (59, 179, 227), (85, 204, 147), (110, 216, 248), (22, 127, 214), (24, 183, 216),
           (237, 130, 161), (43, 112, 38), (36, 84, 43), (131, 234, 211), (252, 136, 142), (87, 29, 37), (250, 235, 239),
           (68, 162, 33), (99, 43, 22), (253, 221, 1), (105, 47, 27), (98, 37, 45), (38, 69, 44), (169, 132, 21), (234, 162, 157),
           (76, 130, 187)]

t.colormode(255)

tim = t.Turtle()
tim.pensize(10)
tim.penup()
tim.speed("fastest")
tim.hideturtle()
tim.teleport(-250, -250)

for i in range(10):
    draw_a_row()
    tim.teleport(-250, tim.ycor() + 50)

screen = t.Screen()
screen.exitonclick()
