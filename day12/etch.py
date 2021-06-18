from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def clockwise():
    turtle.right(1)
    turtle.forward(1)

def clear():
    turtle.setpos(0,0)
    turtle.clear()

screen.onkeypress(lambda: turtle.right(2), 'Right')
screen.onkeypress(lambda: turtle.forward(2), 'Up')
screen.onkeypress(clockwise, 'Left')
screen.onkeypress(lambda: turtle.backward(2), 'Down')
screen.onkeypress(clear, 'c')
screen.listen()

screen.exitonclick()
