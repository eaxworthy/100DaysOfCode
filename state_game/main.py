from turtle import Turtle, Screen
import pandas as pd

SCREEN_WIDTH = 725
SCREEN_HEIGHT = 491

df = pd.read_csv('50_states.csv')

background = Turtle()
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.addshape('blank_states_img.gif')
background.shape('blank_states_img.gif')

message = Turtle()
message.penup()
message.hideturtle()

state_names = df.state.to_list()
state_coords = tuple(zip(df.x.to_list(), df.y.to_list()))
states_remaining = dict(zip(state_names, state_coords))

states_remaining_message = Turtle()
states_remaining_message.penup()
states_remaining_message.hideturtle()
states_remaining_message.setpos(-(SCREEN_WIDTH/2 - 10), SCREEN_HEIGHT/2 - 20)
states_remaining_message.write(arg=f'States Left to Find: {len(states_remaining)}', align='left')

def write_state(state):
    message.setpos(states_remaining[state])
    message.write(arg=state, align='center')

while len(states_remaining) > 0:
    guess = screen.textinput('Guess', 'Enter a state name')
    if guess is None:
        #TODO: write missed states to csv
        screen.bye()
        break

    else:
        guess = guess.title()
        if guess in state_names:
            write_state(guess)
            states_remaining.pop(guess)
            states_remaining_message.clear()
            states_remaining_message.write(arg=f'States Left to Find: {len(states_remaining)}', align='left')

#TODO: Some sort of 'you win' message


