import turtle
import pandas


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
    label.write(answer_state)


def write_success_message():
    label = turtle.Turtle()
    label.penup()
    label.color("green")
    label.hideturtle()
    label.write("Great Work!!!", font=('Arial', 40, 'normal'), align="center")


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
        answer_state = screen.textinput(title=f"Score {score}/50", prompt="Wat is another states name?").title()
        state_information = get_us_state_information(selected_state=answer_state)
        if correct_us_state(information=state_information):
            add_state_label(information=state_information)
            score += 1
        if score >= 50:
            write_success_message()
            game_is_on = False

    turtle.mainloop()
