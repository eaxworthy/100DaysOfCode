from turtle import Turtle, Screen
from random import randint
import time

#constants for screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Food():
'''The food object the snake eats to gain score.'''

    def __init__(self):
        '''Creates the food object and sets appearance. Takes no parameters'''
        self.marker = Turtle(shape='circle')
        self.marker.penup()
        self.marker.hideturtle()
        self.marker.shapesize(0.45, 0.45, 2)
        self.marker.color('blue')

    def move_food(self):
        '''Hides the food object, changes it's locations to a random spot on
        the screen with a buffer to make eating possible without going over 
        screen limit for snake, then unhides.'''
        self.marker.hideturtle()
        x = randint(-(SCREEN_WIDTH/2 - 20), (SCREEN_WIDTH/2 - 20))
        y = randint(-(SCREEN_HEIGHT/2 - 20), (SCREEN_HEIGHT/2 - 20))
        self.marker.setpos(x, y)
        self.marker.showturtle()


class Snake():
'''The snake object controlled by the player.'''
    def __init__(self, screen):
        '''Creates a snake with 3 segments and a score of 0. also creates
        food object and sets first location. Updates screen to reflect
        starting game state.'''
        self.body = []
        self.screen = screen
        for i in range(0,6):
            t = Turtle(shape='square')
            t.penup()
            t.speed(0)
            t.color('white','white')

            #default size of a square turtle is 20x20 px. By overlapping
            #segments, we can create a smoother animation.
            t.setx(-10*i)
            self.body.append(t)

        self.food = Food()
        self.food.move_food()
        self.head = self.body[0]
        self.score = 0
        self.screen.update()

    def add_tail(self, pos):
        '''Creates a new segment and appends onto snake body at the position
        of the last segment at time of function call.'''
        t = Turtle(shape='square')
        t.penup()
        t.color('black','black')
        t.setpos(pos)
        t.color('white','white')
        self.body.append(t)

    def eat(self):
        '''Removes old food marker and sets to new location. Moves snake 
        through old food location, adds new segment to end of snake at 
        location of tail segment before the move, and adds to score.'''
        self.food.move_food()
        pos = self.body[-1].pos()
        self.move()
        self.add_tail(pos)
        self.score += 1

    def move(self):
        '''Returns True if move was valid, False if move caused game to end.
        Uses a short queue to move the segments. Head controls directions
        and all following segments assumes the previous position of the leading
        segment. Checks for updates in game state from eating food, or violating
        the conditions of touching gameboard edge or body.'''
        new_pos = [self.head.pos()]
        self.head.forward(10) 
        if self.touch_food(self.head.xcor(), self.head.ycor()):
            self.eat()
        head_x = self.head.xcor()
        head_y = self.head.ycor()
        if not self.touch_self(head_x, head_y) and not self.touch_edge(head_x, head_y):
            for segment in self.body[1:]:
                new_pos.append(segment.pos())
                segment.setpos(new_pos.pop(0))
            self.screen.update()
            time.sleep(0.05)
            return True
        else:
            return False

    def touch_food(self, head_x, head_y):
        '''Returns True if food was eaten, False otherwise.'''
        if abs(head_x - self.food.marker.xcor()) < 15 and abs(head_y - self.food.marker.ycor()) < 15:
            return True
        return False
    
    def touch_self(self, head_x, head_y):
        '''Returns True if head segment moved into a position occupied
        by a body segment. False otherwise.'''
        for segment in self.body[1:]:
            dif_x = abs(head_x - segment.xcor())
            dif_y = abs(head_y - segment.ycor())
            if dif_x < 10 and dif_y < 10:
                return True

    def touch_edge(self, head_x, head_y):i
        '''Returns True if head went over the gameboard boundary. False otherwise.'''
        if abs(head_x) > (SCREEN_WIDTH/2 - 15) or abs(head_y) > (SCREEN_HEIGHT/2 - 10):
            return True

    def turn(self, direction):
        '''Sets direction of snake to follow key press.'''
        self.head.setheading(direction)

    def get_score(self):
        '''Returns current score.'''
        return self.score


class SnakeGame():
    '''Wrapper for game.''' 
   
   def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor('black')
        self.screen.title('Snake')
        self.screen.tracer(False)
        self.snake = Snake(self.screen)
        self.screen.onkeypress(lambda: self.snake.turn(90), 'Up')
        self.screen.onkeypress(lambda: self.snake.turn(180), 'Left')
        self.screen.onkeypress(lambda: self.snake.turn(270), 'Down')
        self.screen.onkeypress(lambda: self.snake.turn(0), 'Right')
        self.screen.listen()

        self.continue_game = True

        while self.continue_game:
            self.continue_game = self.snake.move()
        
        score = self.snake.get_score()
        self.screen.reset()
        message = Turtle()
        message.pencolor('red')
        message.write(arg=f'Game Over\nFinal Score: {score}', align='center', font=('Arial', 14, 'normal'))
        self.screen.exitonclick()


