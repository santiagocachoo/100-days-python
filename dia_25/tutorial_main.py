import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "/Users/santiagocachoh/Code/100python/dia_25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("/Users/santiagocachoh/Code/100python/dia_25/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Name a U.S. state: ").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        states_to_learn = new_data.to_csv("/Users/santiagocachoh/Code/100python/dia_25/states_to_learn.csv")
        break

    # if answer_state is one of the states in all the states of the 50_states.csv
    if answer_state in all_states and answer_state not in guessed_states:
        # if right create a turtle to write the name of the state at the state x and y coordinate
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)




screen.exitonclick()