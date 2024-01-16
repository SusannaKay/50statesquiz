import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

answer_count = []

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()


while True:
    answer_state = screen.textinput(title=f"{len(answer_count)}/50 Guessed", prompt="What's another state name?")
    answer = answer_state.title()
    if answer == "Exit":
        missing = []
        for state in all_states:
            if state not in answer_count:
                 missing.append(state)
        df = pandas.DataFrame(missing)
        df.to_csv("missing_states.csv")
        break
    if answer in data.values:
        if answer not in answer_count:
            answer_count.append(answer)
            text = turtle.Turtle()
            text.hideturtle()
            text.penup()

            answer_row = data[data.state == answer] 
            x = int(answer_row.x)
            y=int(answer_row.y)
            text.setpos(x, y)
            text.write(answer)
            
        else:
            print("già indovinato")
    else:
        print("sbagliato")
    
    if len(answer_count) <50:
            continue
    else:
            break
    
