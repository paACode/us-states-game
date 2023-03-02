import turtle
import pandas


def get_us_state_information(selected_state):
    """Returns a Dataframe with Index, State, X-Coordinate and Y-Coordinate of selected State"""
    return map_data[map_data.state.str.lower() == selected_state]


def correct_us_state(information):
    if information.empty:
        return False
    return True


def get_coordinates(information):
    return int(information.x), int(information.y)


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    map_data = pandas.read_csv("50_states.csv")
    game_is_on = True
    score = 0

    while game_is_on:
        answer_state = screen.textinput(title=f"Score {score}/50", prompt="Wat is another states name?").lower()
        state_information = get_us_state_information(selected_state=answer_state)
        if correct_us_state(information=state_information):
            x_cor, y_cor = get_coordinates(information=state_information)
            print(x_cor,y_cor)

    turtle.mainloop()
