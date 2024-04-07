from turtle import *

turtle_1 = Turtle()
#Creates object from class Turtle()
turtle_1.shape("turtle")
turtle_1.color("blue")

def draw_shape(number_of_sides):
    angle_of_object = 360 / number_of_sides
    for x in range(number_of_sides):
        turtle_1.forward(100)
        turtle_1.right(angle_of_object)

for n in range(3, 11):
    draw_shape(n)

screen = Screen()
#creates screen for turtle to draw on from class Screen()
screen.exitonclick()
#uses the exitonclick method to make sure the screen doesn't disappear