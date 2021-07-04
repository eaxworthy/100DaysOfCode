from turtle import Turtle, Screen
from random import randint
from time import sleep

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
COLORS = ['firebrick', 'dark orange', 'gold', 'yellow green', 'cornflower blue', 'medium purple', 'dark slate gray']

class Car(Turtle):
    def __init__(self, turtle_link):
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
        self.turtle_link = turtle_link
    
    def offscreen(self):
        if self.xcor() < -(SCREEN_WIDTH/2 - 10):
            return True
        return False
    
    def reset(self):
        self.setpos(SCREEN_WIDTH/2, randint(-(SCREEN_HEIGHT/2-75), SCREEN_HEIGHT/2-50))

    def move(self):
        if not self.offscreen():
            self.forward(self.movement_speed)
        #elif turtle_collision:     
        else:
            self.reset()
    
    def collision(self):
        if (abs(self.xcor() - self.turtle_link.xcor()) < 5) and (abs(self.ycor() - self.turtle_link.ycor()) < 5):
            print(self.pos(), self.turtle_link.pos())
            return True
        return False

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('spring green')
        self.shape('turtle')
        self.setpos(0, -(SCREEN_HEIGHT/2 + 5))
        self.setheading(90)
    
    def move(self):
        if self.ycor() > SCREEN_HEIGHT/2:
            self.setpos(0, -(SCREEN_HEIGHT/2 + 5))
        self.forward(10)


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(False)

player = Player()
screen.onkey(player.move, 'w')
screen.listen()

cars = []
cars.extend([Car(player) for i in range(10)])
screen.update()

game_over = False


while True:
    #player.move()
    for car in cars:
        car.move()
        if car.collision():
            print('Collision')
            game_over = True
            break
    if game_over:
        break
    screen.update()
    sleep(0.05)

screen.exitonclick()

