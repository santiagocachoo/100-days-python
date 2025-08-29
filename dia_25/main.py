from turtle import Turtle, Screen
import pandas

SCORE = 0

screen = Screen()

image = "/Users/santiagocachoh/Code/100python/dia_25/blank_states_img.gif"
screen.addshape(image)
background_image = Turtle()
background_image.shape(image)
background_image.penup()

scoreboard = Turtle()
scoreboard.penup()
scoreboard.hideturtle()



states = pandas.read_csv("/Users/santiagocachoh/Code/100python/dia_25/50_states.csv")

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="Enter a state name").title()
    for state in states.state:
        if state == answer_state:
            SCORE += 1
            state_row = states[states.state == answer_state]
            state_x_cor = int(state_row.x)
            state_y_cor = int(state_row.y)
            scoreboard.goto(state_x_cor, state_y_cor)
            scoreboard.write(answer_state, align="center", font=("Arial", 12, "normal"))
            screen.title(f"{SCORE}/50 U.S. States Game")
        
if SCORE == 50:
    screen.title("You Win! 50/50 U.S. States Game")
    game_is_on = False


screen.mainloop()

