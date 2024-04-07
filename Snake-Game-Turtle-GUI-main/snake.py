from turtle import Turtle
STARTING_Y_COR = [0, 0, 0]
STARTING_X_COR = [0, -20, -40]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_new_snake()
        self.head = self.segments[0]

    def create_new_snake(self):
        """Code for creating a new snake when the snake class is first initialized"""
        for x in range(0, 3):
            snake_start = Turtle()
            snake_start.shape("square")
            snake_start.color("white")
            snake_start.penup()
            snake_start.goto(x=STARTING_X_COR[x], y=STARTING_Y_COR[x])
            self.segments.append(snake_start)



    def add_segment(self, x_position, y_position):
        """Code for adding a segment once the snake successfully eats food"""
        snake_start = Turtle()
        snake_start.shape("square")
        snake_start.color("white")
        snake_start.penup()
        snake_start.goto(x_position, y_position)
        self.segments.append(snake_start)

    def extend_snake(self):
        """Using the code written above, we get the LAST segment's coordinates and input it as the KWARGS"""
        self.add_segment(self.segments[-1].xcor(), self.segments[-1].ycor())

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x_cor = self.segments[segment_number - 1].xcor()
            new_y_cor = self.segments[segment_number - 1].ycor()

            self.segments[segment_number].goto(new_x_cor, new_y_cor)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

