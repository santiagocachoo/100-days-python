from turtle import Screen
import time
from paddle import Paddle
from ball import Ball

RIGHT_STARTING_POSITION = (350, 0)
LEFT_STARTING_POSITION = (-360, 0)
MOVE_SPEED = 0.1

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)

r_paddle = Paddle(RIGHT_STARTING_POSITION)
l_paddle = Paddle(LEFT_STARTING_POSITION)
ball = Ball()


screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(MOVE_SPEED)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        MOVE_SPEED - 0.01

screen.exitonclick()
