from turtle import Turtle, Screen
from random import randint
from time import sleep

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(SCREEN_WIDTH/2, randint(-(SCREEN_HEIGHT/2-75), SCREEN_HEIGHT/2-50))
        self.setheading(180)
        self.movement_speed = randint(5,15)
        self.color(COLORS[randint(0,len(COLORS)-1)])
        self.shape('square')
        self.shapesize(stretch_len=1.5, stretch_wid=1.0)
        self.showturtle()
    
    def offscreen(self):
        if self.xcor() < -(SCREEN_WIDTH/2 - 10):
            return True
        return False
    
    def reset(self):
        self.setpos(SCREEN_WIDTH/2, randint(-(SCREEN_HEIGHT/2-75), SCREEN_HEIGHT/2-50))

    def move(self):
        if not self.offscreen():
            self.forward(self.movement_speed)
        else:
            self.reset()

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(False)
cars = []
cars.extend([Car() for i in range(10)])
screen.update()

while True:
    for car in cars:
        car.move()
    screen.update()
    sleep(0.05)

screen.exitonclick()

