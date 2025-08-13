from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -270)
        self.setheading(90)

    def move(self):
        new_y = self.ycor() + 10
        self.goto(0, new_y)