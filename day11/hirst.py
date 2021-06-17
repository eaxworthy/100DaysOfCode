import colorgram
from turtle import Turtle, Screen
from random import choice

raw_colors = colorgram.extract('image.jpeg', 15)
rgb_colors = []
for color in raw_colors:
    rgb_colors.append(tuple([color.rgb[0], color.rgb[1], color.rgb[2]]))

turtle = Turtle()
turtle.penup()
screen = Screen()
screen.colormode(255)
screen.setup(width=620, height=620)
x = -275
y = -270

for row in range (0,10):
    turtle.setpos(x,y)
    for col in range(0,10):
        turtle.pencolor(choice(rgb_colors))
        turtle.dot(35)
        turtle.forward(60)
    y += 60

screen.exitonclick()

