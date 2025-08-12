from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

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
scoreboard = Scoreboard()


screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(MOVE_SPEED)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        MOVE_SPEED -= 0.01

    # detect collision with right paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_x()

    # detect collision with left paddle
    if ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # detect out of bounds
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.bounce_x()
        scoreboard.l_point()
        MOVE_SPEED = 0.1

    elif ball.xcor() < -380:
        ball.goto(0,0)
        ball.bounce_x()
        scoreboard.r_point()
        MOVE_SPEED = 0.1

screen.exitonclick()
