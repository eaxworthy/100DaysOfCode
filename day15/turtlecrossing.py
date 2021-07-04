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
        else:
            self.reset()
 
    def collision(self, player):
        if (abs(self.xcor() - player.xcor()) < 18) and (abs(self.ycor() - player.ycor()) < 15):
            return True
        return False

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('spring green')
        self.shape('turtle')
        self.setpos(0, -(SCREEN_HEIGHT/2 - 10))
        self.setheading(90)
        self.crossed_street = False
    
    def up(self):
        if self.ycor() > SCREEN_HEIGHT/2:
            self.setpos(0, - (SCREEN_HEIGHT/2 - 10))
            self.crossed_street = True
        self.forward(10)
    
    def down(self):
        if self.ycor() > -(SCREEN_HEIGHT/2 - 10):
            self.backward(10)


class TurtleCrossing():
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.tracer(False)

        self.player = Player()
        self.screen.onkey(self.player.up, 'w')
        self.screen.onkey(self.player.down, 's')
        self.screen.listen()

        self.cars = []
        self.cars.extend([Car(self.player) for i in range(5)])
        self.screen.update()
        
        self.level = 1
        self.game_over = False

    def game_over_message(self):
        message = Turtle()
        message.hideturtle()
        message.penup()
        message.setpos(0, SCREEN_HEIGHT/2 - 20)
        message.write(arg='GAME OVER', align='center', font=('Futura', '12', 'normal'))
    
    def level_up(self):
        self.player.crossed_street = False
        self.level += 1
        self.cars.extend([Car(self.player) for i in range(5)])

    def start(self):
        while True:
            for car in self.cars:
                car.move()
                if car.collision(self.player):
                    self.game_over = True
                    break
            if self.player.crossed_street:
                self.level_up()
            if self.game_over:
                self.game_over_message()
                break
            self.screen.update()
            sleep(0.05)
        self.screen.exitonclick()



game = TurtleCrossing()
game.start()
