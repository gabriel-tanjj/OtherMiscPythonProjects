import turtle
from turtle import *
from random import *

turtle_1 = Turtle()
turtle.colormode(255)
turtle_1.shape("turtle")
turtle_1.speed("fastest")
directions = [0, 90, 180, 270]

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color

def get_into_position():
    turtle_1.hideturtle()
    turtle_1.penup()
    turtle_1.goto(-375, -375)

def reset_heading():
    turtle_1.setheading(90)
    turtle_1.forward(50)
    turtle_1.setheading(180)
    turtle_1.forward(800)
    turtle_1.setheading(0)

def draw_painting():

    get_into_position()

    for x in range (0, 16):

        for x in range(0, 10):
            turtle_1.color(random_color())
            turtle_1.dot(20)
            turtle_1.penup()
            turtle_1.forward(80)

        reset_heading()



draw_painting()

screen = Screen()
#creates screen for turtle to draw on from class Screen()
screen.exitonclick()
#uses the exitonclick method to make sure the screen doesn't disappear




