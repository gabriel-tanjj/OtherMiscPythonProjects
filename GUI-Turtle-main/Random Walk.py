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

def random_walk():
    turtle_1.pensize(15)
    turtle_1.hideturtle()
    turtle_1.speed("fastest")
    for x in range(0, 5000):
        turtle_1.color(random_color())
        turtle_1.setheading(choice(directions))
        turtle_1.forward(30)


random_walk()

screen = Screen()
#creates screen for turtle to draw on from class Screen()
screen.exitonclick()
#uses the exitonclick method to make sure the screen doesn't disappear