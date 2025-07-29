import random
from turtle import Screen
import time
from car import Car
from player import Player

screen = Screen()
turtle = Player()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(turtle.move_forward, "Up")

speed = 0.1
all_cars = []
is_game_on = True
while is_game_on:
    time.sleep(speed)
    screen.update()

    # GENERATING RANDOM CAR AT RANDOM INTERVAL BETWEEN 1 TO 5
    random_num = random.randint(1, 5)
    if random_num == 1:
        car = Car()
        all_cars.append(car)

    for car in all_cars:
        car.move()

    if turtle.at_finish_line():
        turtle.default_position()  # COMES BACK TO ITS DEFAULT LOCATION

screen.exitonclick()