from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

speed = 0.1

is_game_on = True
while is_game_on:
    time.sleep(speed)
    screen.update()


screen.exitonclick()