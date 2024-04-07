import turtle
from turtle import *
from random import *

turtle_1 = Turtle()
turtle.colormode(255)
turtle_1.shape("turtle")
directions = [0, 90, 180, 270]

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color

def spirograph():
    turtle_1.pensize(1)
    turtle_1.hideturtle()
    turtle_1.speed("fastest")

    for x in range(0, 500):
        turtle_1.color(random_color())
        current_heading = turtle_1.heading()
        turtle_1.setheading(current_heading + 5)
        turtle_1.circle(200)

spirograph()

screen = Screen()
#creates screen for turtle to draw on from class Screen()
screen.exitonclick()
#uses the exitonclick method to make sure the screen doesn't disappear