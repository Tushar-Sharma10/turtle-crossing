from turtle import Turtle
POSITION = (-230,260)
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.level = 0
        self.level_increase()

    def game_over(self):
        """ BRINGS THE ARGUMENT OF THE GAME OVER TO CENTER"""
        self.goto(0, 0)
        self.write("Game Over",align='center', font=('Arial', 30, 'normal'))

    def level_increase(self):
        """ CLEARS THE ARGUMENT AND UPDATE THE LEVEL"""
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", move=False, align='center', font=('Arial', 30, 'normal'))