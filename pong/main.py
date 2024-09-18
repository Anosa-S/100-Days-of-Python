from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen =  Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up2, "w")
screen.onkey(left_paddle.down2, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()
    
screen.exitonclick()
