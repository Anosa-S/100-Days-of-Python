from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars(Turtle):

    def __init__(self):
        self.color("Green")
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(0, 0)
