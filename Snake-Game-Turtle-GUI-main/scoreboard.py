from turtle import Turtle

SCOREBOARD_XCOR = 0
SCOREBOARD_YCOR = 270

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=SCOREBOARD_XCOR, y=SCOREBOARD_YCOR)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=("Arial", 24, "normal"))
