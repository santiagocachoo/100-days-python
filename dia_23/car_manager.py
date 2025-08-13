COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.starting_move_distance = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_car(self):
        self.car = Turtle()
        self.car.shape("square")
        self.car.shapesize(1, 2)
        self.car.color(random.choice(COLORS))
        self.car.penup()
        self.car.goto(320, random.randint(-230, 230))
        self.cars.append(self.car)

    def move_car(self):
        for car in self.cars:
            car.goto(car.xcor() - self.starting_move_distance, car.ycor())

    def increase_move_distance(self):
        self.starting_move_distance += MOVE_INCREMENT
            

    