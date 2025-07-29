from turtle import Turtle
STARTING_POSITION = (0,-280)
FINISH_LINE = 280
HEADING = 90
MOVE = 20
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.default_position()

    def move_forward(self):
        """MOVES FORWARD """
        self.forward(MOVE)

    def at_finish_line(self):
        """ CHECK IF THE PLAYER IS AT THE FINISH LINE"""
        return self.ycor() >= FINISH_LINE


    def default_position(self):
        """POSITION THE PLAYER BACK TO THE STARTING POSITION"""
        self.goto(STARTING_POSITION)
        self.setheading(HEADING)

