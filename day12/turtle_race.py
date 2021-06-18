from turtle import Turtle, Screen
from random import randint

def race(turtles):
    while True:
        for color, turtle in turtles.items():
            turtle.forward(randint(5,20))
            if turtle.xcor() >= 230:
                return color

def get_bet():
    bet = ''
    while bet not in colors:
        bet = input('Which turtle do you think will win? (red/orange/yellow/green/blue/violet): ').lower()
        if bet not in colors:
            print('Invalid turtle. Please try again.')
    return bet

def check_bet(bet, winner):
    if bet == winner:
        print(bet + ' won!')
    else:
        print('Sorry, ' + bet + ' lost. ' + winner.title() + ' was the winner.')

def create_turtles(turtles, colors):
    x = -230
    y = 115
    for color in colors:
        turtles[color] = Turtle()
        turtles[color].penup()
        turtles[color].shapesize(1.2, 1.2, 2)
        turtles[color].shape('turtle')
        turtles[color].color(color,color)
        turtles[color].setpos(x, y)
        y -= 46

screen = Screen()
screen.setup(width= 500, height = 330)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
turtles = {}
create_turtles(turtles, colors)


bet = get_bet()
winner = race(turtles)
check_bet(bet, winner)

screen.exitonclick()
