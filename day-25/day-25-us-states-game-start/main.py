import turtle
import pandas

def write_state_name(x, y, name):
    writer.teleport(x, y)
    writer.write(name, align="center", font=("Arial", 8, "normal"))

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("USA States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv("./50_states.csv")
states_name = data.state.to_list()

already_guessed = []
guessed_states = 0
while guessed_states < 50:
    answer_state = screen.textinput(title = f"{guessed_states}/50 Guess the State", prompt = "Guess the State's Name").title()
    if answer_state in states_name and answer_state not in already_guessed:
        guessed_states += 1
        already_guessed.append(answer_state)
        state = data[data.state == answer_state]
        x, y = state.x.item(), state.y.item()
        write_state_name(x, y, answer_state)
    if answer_state == "Exit":
        break
if guessed_states == 50:
    print("You guessed all the states!")
else:
    not_guessed = []
    for state in states_name:
        if state not in already_guessed:
            not_guessed.append(state)

    states_to_learn = {}
    states_to_learn["state"] = not_guessed
    new_data = pandas.DataFrame(states_to_learn)
    new_data.to_csv("./states_to_learn.csv")

screen.exitonclick()