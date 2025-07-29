from turtle import Screen
import time
from player import Player

screen = Screen()
turtle = Player()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(turtle.move_forward, "Up")

speed = 0.1

is_game_on = True
while is_game_on:
    time.sleep(speed)
    screen.update()


screen.exitonclick()