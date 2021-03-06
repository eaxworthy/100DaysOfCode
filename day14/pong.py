from turtle import Turtle, Screen
from random import randint
import time

SCREEN_HEIGHT = 550
SCREEN_WIDTH = 950
FONT = ('Futura', '14', 'normal')
SCORE_FONT= ('Futura', '40', 'normal')

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
        self.id = player_num

    def up(self):
        if self.ycor() < SCREEN_HEIGHT/2 - 55:
            self.forward(20)

    def down(self):
        if self.ycor() > -(SCREEN_HEIGHT/2-55):
            self.backward(20)
   
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('green')
        self.speed(2)
        self.penup()
        self.shape('circle')
        self.bouncing = False
        self.direction = -1

    def bounce(self):
        heading = 270 + (90*self.direction) + randint(-75, 75)
        self.setheading(heading)
        self.direction = -self.direction
        self.forward(20)

    def wall_bounce(self):
        sign_y = -1 if self.ycor() < 0 else 1
        
        #going right
        if self.direction < 0:
            #lower wall bounce
            if sign_y < 0:
                angle = randint(15,75)
            #upper wall bounce    
            else:
                angle = randint(285, 345)
        
        #going left
        else:
            if sign_y < 0:
                angle = randint(105,165)
            else:
                angle = randint(195,255) 
        self.setheading(angle)
        self.forward(20)
    
    def paddle_collision(self, paddle):
        '''returns true if the ball has entered the supplied paddle's hit box. false otherwise.'''
        pos = paddle.pos()
        if abs(self.xcor()-pos[0]) < 20 and abs(self.xcor()) < abs(pos[0]) and abs(self.ycor()-pos[1]) < 45:
            return True
        return False

    def edge_collision(self):
        '''returns true if ball collides with board edge. false otherwise.'''
        if abs(self.ycor()) > SCREEN_HEIGHT/2 - 20:
            return True
        return False

    def goal_check(self):
        '''returns true if ball passes past paddle scoring a point.'''
        if abs(self.xcor()) > SCREEN_WIDTH/2:
            return 1 if self.xcor() > 0 else -1
        return 0

class Score(Turtle):
    def __init__(self, player_num): 
        super().__init__()
        self.hideturtle()
        self.color('green')
        self.penup()
        self.setpos((SCREEN_WIDTH/2 - 100) * player_num, SCREEN_HEIGHT/2 - 80) 
        self.value = 0


class PongGame():
    def __init__(self):
        screen = Screen()
        screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT, startx = None, starty=None)
        screen.bgcolor('black')
        screen.title('Pong')
        screen.tracer(False)

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
        
        score_1 = Score(-1)
        score_2 = Score(1)

        
        screen.update()

        def update_scores():
            score_1.clear()
            score_2.clear()
            score_1.write(arg=score_1.value, font=SCORE_FONT, align = 'left')
            score_2.write(arg=score_2.value, font=SCORE_FONT, align = 'right')

        def start(_1, _2):
            
            message.clear()
            update_scores()
            ball.bouncing = True
            while ball.bouncing:
                if ball.paddle_collision(paddle_1) or ball.paddle_collision(paddle_2):
                    ball.bounce()
                elif ball.edge_collision():
                    ball.wall_bounce()
                elif ball.goal_check():
                    if ball.direction < 0:
                        score_1.value += 1
                    else:
                        score_2.value += 1
                    update_scores()
                    ball.setpos(0,0)
                    ball.direction = -ball.direction
                    ball.setheading(90 + (90*ball.direction))

                ball.forward(20)
                screen.update()
                time.sleep(0.05) 

        screen.onclick(start, 1, None) 
        screen.onkey(paddle_1.up, 'w')
        screen.onkey(paddle_1.down, 's')
        screen.onkey(paddle_2.up, 'i')
        screen.onkey(paddle_2.down, 'k')

        screen.listen()
    

        screen.mainloop()
