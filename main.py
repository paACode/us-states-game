import turtle
import pandas
from os.path import exists as file_exists


def get_selected_state_information(selected_state):
    """Returns a Dataframe with Index, State, X-Coordinate and Y-Coordinate of selected State"""
    return us_map_data[us_map_data.state.str.title() == selected_state]


def add_state_label(text):
    label = turtle.Turtle()
    label.penup()
    label.hideturtle()
    information = get_selected_state_information(selected_state=text)
    label.goto(int(information.x), int(information.y))
    label.write(information.state.item())


def write_success_message():
    label = turtle.Turtle()
    label.penup()
    label.color("green")
    label.hideturtle()
    label.write("Great Work!!!", font=('Arial', 40, 'normal'), align="center")


def guessed_states_add_label():
    [add_state_label(state[1]) for state in guessed_states]


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    us_map_data = pandas.read_csv("50_states.csv")
    all_us_states = us_map_data.state.values.tolist()
    guessed_states = []
    guessed_states_dataframe_list = pandas.DataFrame()

    if file_exists("guessed_states.csv"):
        guessed_states = pandas.read_csv("guessed_states.csv").values.tolist()
        guessed_states_add_label()

    score = len(guessed_states)
    game_is_on = True

    while game_is_on:
        answer_state = screen.textinput(title=f"Score {score}/50", prompt="What is another states name?").title()

        if answer_state == "exit".title():
            game_is_on = False
            guessed_states_dataframe_list = [get_selected_state_information(state) for state in guessed_states]
            guessed_states_dataframe = pandas.concat(guessed_states_dataframe_list)
            guessed_states_dataframe.to_csv("guessed_states.csv")
        elif answer_state in all_us_states:
            guessed_states.append(answer_state)
            add_state_label(text=answer_state)
            score = len(guessed_states)
            if score >= 50:
                write_success_message()
                game_is_on = False
    turtle.mainloop()
