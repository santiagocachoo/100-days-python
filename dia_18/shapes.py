from turtle import Turtle, Screen


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.pencolor("blue")

def draw_shape(num_sides):
    angle = 360 / num_sides
    for n in range(num_sides):
        
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for n in range (3, 21):
    draw_shape(n)

screen = Screen()
screen.exitonclick()