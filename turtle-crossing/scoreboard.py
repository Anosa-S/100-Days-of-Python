from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.left_score = ("Level")
        self.right_score = 0
        self.game_over = ("GAME OVER")
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(self.left_score, align="left",  font=FONT)
        self.goto(-175, 249)
        self.write(self.right_score, align="left", font=FONT)
    
    def point(self):
        self.right_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center",  font=FONT)
        
