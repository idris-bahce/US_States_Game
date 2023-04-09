import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
is_game_on = True
states_correct = 0
guessed_states = []

state_list = data["state"].to_list()


def print_state_to_map(x, y, state):
    write_state = turtle.Turtle()
    write_state.hideturtle()
    write_state.penup()
    write_state.goto(x, y)
    write_state.write(arg=state, align="center", font=('Arial', 8, 'normal'))


while is_game_on:
    answer_state = screen.textinput(title=f"{states_correct}/50 States Correct", prompt="What's another state's name?")\
        .title()
    if answer_state in state_list and answer_state not in guessed_states:
        states_correct += 1
        x_cor = int(data[data["state"] == answer_state]["x"])
        y_cor = int(data[data["state"] == answer_state]["y"])
        print_state_to_map(x_cor, y_cor, answer_state)
        guessed_states.append(answer_state)
    if states_correct == 50 or answer_state == "Exit":
        is_game_on = False

states_to_learn = []
for state in state_list:
    if state not in guessed_states:
        states_to_learn.append(state)

data_dic = {
    "States to Learn": states_to_learn
}
new_data = pandas.DataFrame(data_dic)
new_data.to_csv("states to learn.csv")
