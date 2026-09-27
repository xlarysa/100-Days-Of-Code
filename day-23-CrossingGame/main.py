import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun = player.move, key = "w")

current_level = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if car_manager.loop_counter % 6 == 0:
        car_manager.create_car()

    if car_manager.check_for_collision(player):
        game_is_on = False

    if player.ycor() >= FINISH_LINE_Y:
        player.next_level()
        car_manager.accelerate()
        scoreboard.increase_level()
        scoreboard.write_level()

    car_manager.move_cars()
    car_manager.loop_counter += 1

scoreboard.game_over()

screen.exitonclick()


