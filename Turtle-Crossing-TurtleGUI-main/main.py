import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(player.move_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_left()

    if car_manager.player_collision(player):
        game_is_on = False
        scoreboard.game_over()

    if player.reach_finish_line():
        scoreboard.score += 1
        scoreboard.level += 1
        scoreboard.update_score()
        player.reset_position()
        car_manager.new_speed_left()

screen.exitonclick()