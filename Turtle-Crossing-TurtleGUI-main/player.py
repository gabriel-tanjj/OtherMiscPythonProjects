from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        new_y_cor = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y_cor)

    def reset_position(self):
        self.goto(0, -280)

    def reach_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True



