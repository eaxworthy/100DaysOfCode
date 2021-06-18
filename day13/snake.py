from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')

class Snake():

    def __init__(self):
        
        for i in range(0,3):
            t = Turtle()
            t.penup()
            t.color('white','white')
            t.shape('square')

            #default size of a square turtle is 20x20 px. By overlapping
            #segments, we can create a smoother animation.
            t.setx(-10*i)
            self.body.append(t)
    
    def add_tail(self, pos):
        t = Turtle()
        t.penup()
        t.color('black','black')
        t.shape('square')
        t.setpos(pos)
        t.color('white','white')
        self.body.append(t)

    def eat(self):
        pos = self.body[-1].pos()
        self.move()
        self.add_tail(pos)

    def move(self):
        for segment in self.body:
            segment.forward(10)
   
    body = []


def add_tail():
    pass

def new_food():
    pass

snake = Snake()
snake.eat()
for i in range(0,20):
    snake.move()
snake.eat()
screen.exitonclick()
