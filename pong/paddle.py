from turtle import Turtle
UP = 90
DOWN = 270
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x_pos, y_pos)
        


    def up(self):
        new_y = self.ycor() + 20
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        if new_y > -250:
            self.goto(self.xcor(), new_y)
    
    def up2(self):
        new_y = self.ycor() + 20
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def down2(self):
        new_y = self.ycor() - 20
        if new_y > -250:
            self.goto(self.xcor(), new_y)