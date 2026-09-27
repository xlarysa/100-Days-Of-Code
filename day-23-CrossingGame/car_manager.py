import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.loop_counter = 0
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle("square")
        car.color(random.choice(COLORS))
        car.penup()
        car.shapesize(1, 2)
        car.setheading(180)
        car.goto(300, random.randint(-240, 250))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_speed)

    def accelerate(self):
        self.move_speed += MOVE_INCREMENT

    def check_for_collision(self, turtle):
        for car in self.cars:
            if car.distance(turtle) < 21:
                return True
        return False



