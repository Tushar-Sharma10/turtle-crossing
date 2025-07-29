import random
from turtle import Screen
import time
from car import Car
from player import Player
from scoreboard import ScoreBoard

# INITIALISE OBJECTS
screen = Screen()
turtle = Player()
scoreboard = ScoreBoard()

# SCREEN SETUP WITH KEY LISTENER
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(turtle.move_forward, "Up")

all_cars = []  # EMPTY LIST FOR CARS
cars_to_remove = []
speed = 0.1
is_game_on = True

# LOOP TO RUN THE GAME
while is_game_on:
    time.sleep(speed)
    screen.update()

    # GENERATING RANDOM CAR AT RANDOM INTERVAL BETWEEN 1 AND 5
    random_num = random.randint(1, 5)
    if random_num == 1:
        car = Car()
        all_cars.append(car)

    # LOOPING THROUGH THE CAR LIST AND MAKING THEM MOVE
    for car in all_cars:
        car.move()

        # DETECTING COLLISION WITH THE CAR
        if turtle.distance(car.position()) < 22:
            scoreboard.game_over() # GAME OVER
            is_game_on = False  # LOOP ENDS

        # REMOVING CAR AFTER CERTAIN X-AXIS
        if car.xcor() < -300:
            cars_to_remove.append(car)

    for car in cars_to_remove:
        car.clear()
        car.hideturtle()
        all_cars.remove(car)
        cars_to_remove.remove(car)
    cars_to_remove.clear()

    # CHECKING IF TURTLE REACHES THE FINAL DESTINATION OR NOT
    if turtle.at_finish_line():
        turtle.default_position()  # COMES BACK TO ITS DEFAULT LOCATION
        scoreboard.level_increase()  # SCOREBOARD UPDATES
        speed *= 0.9

screen.exitonclick()