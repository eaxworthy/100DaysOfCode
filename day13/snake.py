from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')

class Snake():

    def __init__(self):
        
        for i in range(0,6):
            t = Turtle(shape='square')
            t.penup()
            t.speed(0)
            t.color('white','white')
            

            #default size of a square turtle is 20x20 px. By overlapping
            #segments, we can create a smoother animation.
            t.setx(-10*i)
            self.body.append(t)
        self.head = self.body[0]
    
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
        new_pos = [self.head.pos()]
        self.head.forward(10)
        screen.delay(10)
        for segment in self.body[1:]:
            new_pos.append(segment.pos())
            segment.setpos(new_pos.pop(0))
   

    def turn(self, direction):
        #new_pos = [self.head.pos()]
        #screen.delay(25)
        self.head.setheading(direction)
        #self.head.forward(10)
        #for segment in self.body[1:]:
        #    new_pos.append(segment.pos())
        #    segment.setpos(new_pos.pop(0))
        #    segment.setheading(direction)

    body = []
    pos = [(0,0)]
    direction = 0



def new_food():
    pass

snake = Snake()

screen.onkeypress(lambda: snake.turn(90), 'Up')
screen.onkeypress(lambda: snake.turn(180), 'Left')
screen.onkeypress(lambda: snake.turn(270), 'Down')
screen.onkeypress(lambda: snake.turn(0), 'Right')

screen.listen()

while True:
    snake.move()


screen.exitonclick()
