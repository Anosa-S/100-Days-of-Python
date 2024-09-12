from turtle import Screen, Turtle
from paddle import Paddle

screen =  Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(1)


right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)


screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up2, "w")
screen.onkey(left_paddle.down2, "s")

screen.exitonclick()
