from turtle import Turtle, Screen
import pandas as pd

SCREEN_WIDTH = 725
SCREEN_HEIGHT = 491

df = pd.read_csv('50_states.csv')

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgpic('blank_states_img.gif')

message = Turtle()
message.penup()
message.hideturtle()

state_names = df.state.to_list()
state_coords = tuple(zip(df.x.to_list(), df.y.to_list()))
states_remaining = dict(zip(state_names, state_coords))
states_remaining_count = len(states_remaining)

states_remaining_message = Turtle()
states_remaining_message.penup()
states_remaining_message.hideturtle()
states_remaining_message.setpos(-(SCREEN_WIDTH/2 - 10), SCREEN_HEIGHT/2 - 20)
states_remaining_message.write(arg=f'States Left to Find: {len(states_remaining)}', align='left')

def write_state(state):
    message.setpos(states_remaining[state])
    message.write(arg=state, align='center')

while states_remaining_count >= 0:
    
    if states_remaining_count == 0:
        screen.clearscreen()
        message.setpos(0,0)
        message.write(arg='You win!', align='center', font=('Futura', 30, 'normal'))
        screen.exitonclick()
        break

    guess = screen.textinput('Guess', 'Enter a state name')
    if guess is None:
        i = 0
        with open('unguessed_states.csv', 'w') as f:
            f.write('num,state\n')
            for key in states_remaining.keys():
                i+=1
                f.write(f'{i},{key}\n')
        screen.bye()
        break
    else:
        guess = guess.title()
        if guess in state_names:
            write_state(guess)
            states_remaining.pop(guess)
            states_remaining_message.clear()
            states_remaining_message.write(arg=f'States Left to Find: {len(states_remaining)}', align='left')
        states_remaining_count = len(states_remaining)



