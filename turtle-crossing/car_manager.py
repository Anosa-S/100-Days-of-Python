from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Green")
        self.penup()
        self.shape("square")
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.goto(280, random.randint(-250, 250))
