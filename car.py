from turtle import Turtle
import random
COLORS = ["red","blue","green","black","orange"]
DECREMENT = 10

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.random_y = random.randint(-250, 250)
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(290, self.random_y)


    def move(self):
        """MOVES THE PLAYER IN RIGHT TO LEFT DIRECTION"""
        new_x = self.xcor() - DECREMENT
        self.goto(new_x,self.random_y)