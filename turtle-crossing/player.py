from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Green")
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
        
        
    # def up(self):
    #     new_y = self.ycor() + MOVE_DISTANCE
    #     if new_y < 290:
    #         self.goto(self.xcor(), new_y)
    def up(self):
        self.forward(MOVE_DISTANCE)


    def go_to_start(self):
        self.goto(STARTING_POSITION)


    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False