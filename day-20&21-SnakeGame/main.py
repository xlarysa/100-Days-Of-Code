import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def draw_a_frame():
    frame = t.Turtle()
    frame.color("white")
    frame.hideturtle()
    frame.teleport(-315, -315)
    for _ in range(4):
        frame.forward(630)
        frame.left(90)

screen = t.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
draw_a_frame()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.update_score()
        snake.extend()

    if int(snake.head.xcor()) > 300 or int(snake.head.xcor()) < -300 or int(snake.head.ycor()) > 300 or int(snake.head.ycor()) < -300:
        scoreboard.reset_board()
        snake.reset()

    for segment in snake.body[1::]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_board()
            snake.reset()


screen.exitonclick()