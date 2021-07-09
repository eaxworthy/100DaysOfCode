from turtle import Turtle, Screen
import pandas as pd

SCREEN_WIDTH = 725
SCREEN_HEIGHT = 491

df = pd.read_csv('50_states.csv')

background = Turtle()
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.addshape('/home/lizzieaxworthy/python100/us-states-game-start/blank_states_img.gif')
background.shape('/home/lizzieaxworthy/python100/us-states-game-start/blank_states_img.gif')

message = Turtle()
message.penup()
message.hideturtle()

state_names = df.state.to_list()
state_coords = tuple(zip(df.x.to_list(), df.y.to_list()))
state_dictionary = dict(zip(state_names, state_coords))

states_remaining = 50
states_remaining_message = Turtle()
states_remaining_message.penup()
states_remaining_message.hideturtle()
states_remaining_message.setpos(-(SCREEN_WIDTH/2 - 10), SCREEN_HEIGHT/2 - 20)
states_remaining_message.write(arg=f'States Left to Find: {states_remaining}', align='left')

def write_state(state):
    message.setpos(state_dictionary[state])
    message.write(arg=state, align='center')

while states_remaining > 0:
    guess = screen.textinput('Guess', 'Enter a state name')
    if guess == None:
        screen.bye()
    if guess.title() in state_names:
        write_state(guess.title())
        states_remaining -= 1
        states_remaining_message.clear()
        states_remaining_message.write(arg=f'States Left to Find: {states_remaining}', align='left')

#TODO: Some sort of 'you win' message

screen.exitonclick()
