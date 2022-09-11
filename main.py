from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
screen.tracer(0)
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
answer_list = []
# missed_states = []
correct_answers = 0
game_is_on = True

while game_is_on:
    screen.update()
    answer_state = screen.textinput(f"Guess a State    {correct_answers}/50",
                                    "Enter the name of a state. Type 'quit' to end game.").title()
    if answer_state in state_list and answer_state not in answer_list:
        result = data[data.state == answer_state]
        new_label = Turtle()
        new_label.hideturtle()
        new_label.penup()
        new_label.goto(result.x.item(), result.y.item())
        new_label.write(arg=result.state.item(), align="center")
        correct_answers += 1
        answer_list.append(answer_state)
    if correct_answers == 50:
        new_label = Turtle()
        new_label.color("green")
        new_label.write(arg="Congratulations!  You got all 50 states!", align="center", font=('Arial', 20, 'bold'))
        game_is_on = False
    if answer_state == "Quit":
        for state2 in state_list:
            if state2 not in answer_list:
                result = data[data.state == state2]
                new_label = Turtle()
                new_label.color("red")
                new_label.hideturtle()
                new_label.penup()
                new_label.goto(result.x.item(), result.y.item())
                new_label.write(arg=result.state.item(), align="center")
        #         missed_states.append(state2)
        # missed_series = pandas.Series(missed_states)
        # missed_series.to_csv("missed_states.csv")
        # new_label = Turtle()
        # new_label.color("green")
        # new_label.write(arg=f"You got {correct_answers} out of 50 states.  See attachment for missed states.",
        #                 align="center", font=('Arial', 12, 'bold'))
        game_is_on = False

screen.exitonclick()
