from turtle import * 
import random

tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed(5)

for _ in range (200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))