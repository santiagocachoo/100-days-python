import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    rgb = (r, g, b)
    return rgb

tim.pensize(2)
tim.speed("fastest")


direction = 0

def draw_spirograph(size_of_gap):
    for n in range(int(350/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap) 

draw_spirograph(5)

t.exitonclick()