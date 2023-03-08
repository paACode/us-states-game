import turtle
import pandas
from os.path import exists as file_exists


def get_us_state_information(selected_state):
    """Returns a Dataframe with Index, State, X-Coordinate and Y-Coordinate of selected State"""
    return map_data[map_data.state.str.title() == selected_state]


def correct_us_state(information):
    if information.empty:
        return False
    return True


def add_state_label(information):
    label = turtle.Turtle()
    label.penup()
    label.hideturtle()
    label.goto(int(information.x), int(information.y))
    label.write(information.state.item())


def write_success_message():
    label = turtle.Turtle()
    label.penup()
    label.color("green")
    label.hideturtle()
    label.write("Great Work!!!", font=('Arial', 40, 'normal'), align="center")


def guessed_states_add_label():
    for index in range(len(guessed_states)):
        guessed_state_information = guessed_states[guessed_states.index == index]
        add_state_label(information=guessed_state_information)


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    guessed_states = pandas.DataFrame()
    if file_exists("guessed_states.csv"):
        guessed_states = pandas.read_csv("guessed_states.csv")
        guessed_states_add_label()

    map_data = pandas.read_csv("50_states.csv")
    score = len(guessed_states)
    game_is_on = True

    while game_is_on:
        answer_state = screen.textinput(title=f"Score {score}/50", prompt="Wat is another states name?").title()
        state_information = get_us_state_information(selected_state=answer_state)
        if answer_state == "exit".title():
            game_is_on = False
            guessed_states.to_csv("guessed_states.csv")
        elif correct_us_state(information=state_information):
            guessed_states = pandas.concat([guessed_states, map_data[map_data.state == answer_state]])
            add_state_label(information=state_information)
            score = len(guessed_states)
            if score >= 50:
                write_success_message()
                game_is_on = False
