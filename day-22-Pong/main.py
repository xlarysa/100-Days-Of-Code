import turtle
import time as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from frame import Frame

def turn_off():
    game_is_on = False

screen = turtle.Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

frame = Frame()
scoreboard = Scoreboard()

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

ball = Ball()

screen.listen()
screen.onkeypress(lambda: r_paddle.move_up(), "Up")
screen.onkeypress(lambda: r_paddle.move_down(), "Down")
screen.onkeypress(lambda: l_paddle.move_up(), "w")
screen.onkeypress(lambda: l_paddle.move_down(), "s")

game_is_on = True
while game_is_on:
    t.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.paddle_bounce()

    if ball.xcor() < -390:
        ball.refresh()
        scoreboard.r_point()

    if ball.xcor() > 390:
        ball.refresh()
        scoreboard.l_point()

    if scoreboard.r_score > 5 or scoreboard.l_score > 5:
        game_is_on = False
        scoreboard.winner()
screen.exitonclick()