from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen =  Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0.1)


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
    time.sleep(0.08)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    elif ball.distance(right_paddle) < 20:
        ball.reflect()
    elif ball.distance(left_paddle) < 20:
        ball.reflect()

screen.exitonclick()
