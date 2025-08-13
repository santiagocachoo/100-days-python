from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 260
STARTING_POSITION = (0, -270)

screen = Screen()
screen = Screen()
screen.setup(600, 600)
screen.title("Crossy Road")
screen.listen()
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, "w")

game_is_on = True

loop_count = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # create a car every 6th iteration of the loop
    if loop_count % 6 == 0:
        car_manager.create_car()
    
    car_manager.move_car()

    # detect player collision with car
    for car in car_manager.cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

    # check if player reaches top
    if player.ycor() >= FINISH_LINE_Y:
        player.goto(STARTING_POSITION)
        car_manager.increase_move_distance()
        scoreboard.increase_score()

    
    loop_count += 1


screen.exitonclick()