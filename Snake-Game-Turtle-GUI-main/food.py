from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        random_x_cor = random.randint(-250, 250)
        random_y_cor = random.randint(-250, 250)
        self.goto(x=random_x_cor, y=random_y_cor)

    def randomize_food(self):
        random_x_cor = random.randint(-250, 250)
        random_y_cor = random.randint(-250, 250)
        self.goto(x=random_x_cor, y=random_y_cor)