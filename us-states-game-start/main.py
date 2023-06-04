import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

guessed_states = []


while len(guessed_states) < 50:
    number_of_states = len(guessed_states)
    answer = screen.textinput(title=f"Guess the state {number_of_states}/50", prompt="whats another state name?").title()

    screen.update()
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()

    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv", index_label=False)
        print("csv saved successfully")
        break



    if answer in all_states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.color("Black")

        state_data = data[data.state == answer]

        t.goto(int(state_data.x), int(state_data.y))
        t.write(f"{answer}")
        guessed_states.append(answer)






