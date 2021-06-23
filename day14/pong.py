from turtle import Turtle, Screen
from random import randint

SCREEN_HEIGHT = 550
SCREEN_WIDTH = 950
FONT = ('Futura', '14', 'normal')

class Paddle(Turtle):
    def __init__(self, player_num): 
        super().__init__()
        self.hideturtle()
        self.color('green')
        self.penup()
        self.speed(7)
        self.shape('square')
        self.shapesize(1,4,2)
        self.setheading(90)
        self.setx((SCREEN_WIDTH/2 - 30) * player_num)
   
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('green')
        self.speed(2)
        self.penup()
        self.shape('circle')
        self.bouncing = False

    def bounce():
        #change heading based on direction
        pass
        

class PongGame():
    def __init__(self):
        screen = Screen()
        screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT, startx = None, starty=None)
        screen.bgcolor('black')

        paddle_1 = Paddle(-1)
        paddle_2 = Paddle(1)
        ball = Ball()

        paddle_1.showturtle()
        paddle_2.showturtle()
        ball.showturtle()

        message = Turtle()
        message.penup()
        message.hideturtle()
        message.sety((SCREEN_HEIGHT/2)-30)
        message.color('white')
        message.write(arg='Click to start',font=FONT, align='center')

        def start(a, b):
            message.clear()
            ball.bouncing = True
            while ball.bouncing:
                if ball.xcor() >= paddle_2.xcor()-20:
                    ball.setheading(180)
                elif ball.xcor() <= paddle_1.xcor() + 20:
                    ball.setheading(0)
                ball.forward(10)

        screen.onclick(start, 1, None) 
        screen.onkey(lambda: paddle_1.forward(5), 'w')
        screen.onkey(lambda: paddle_1.backward(5), 's')
        screen.onkey(lambda: paddle_2.forward(5), 'i')
        screen.onkey(lambda: paddle_2.backward(5), 'k')

        screen.listen()
    

        screen.mainloop()
