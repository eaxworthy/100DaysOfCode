from turtle import Turtle, Screen
from random import randint

def draw_shape(turtle, sides):
    turtle.pencolor(randint(0,255), randint(0,255), randint(0,255))
    angle = 360 / sides
    for i in range(sides):
        turtle.forward(80)
        turtle.right(angle)

def random_walk(turtle, length):
    turtle.pensize(8)
    turtle.hideturtle()
    turtle.speed(10)
    for i in range(0,length):
        turtle.pencolor(randint(0,255), randint(0,255), randint(0,255))
        turtle.forward(25)
        turtle.right(90*randint(1,4))

def spirograph(turtle, radius, num_circles):
    turtle.pensize(1)
    turtle.hideturtle()
    turtle.speed(10)
    for i in range(0, num_circles):
        turtle.pencolor(randint(0,255), randint(0,255), randint(0,255))
        turtle.circle(radius)
        turtle.right(360/num_circles)


turtle = Turtle()
turtle.pensize(3)
turtle.shape('classic')
screen = Screen()
screen.colormode(255)

sides = [3, 4, 5, 6, 7, 8, 9, 10]

#for i in range(0, len(sides)):
#    draw_shape(turtle, sides[i])

#random_walk(turtle, 100)

spirograph(turtle, 75, 50)

screen.exitonclick()
