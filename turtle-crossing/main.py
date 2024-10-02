import time
from turtle import Screen
from player import Player
from car_manager import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
car = Cars()
player = Player()

screen.listen()
screen.onkey(player.up, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

