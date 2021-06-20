from turtle import Turtle, Screen
from random import randint
import time

class Food():

    def __init__(self):
        self.marker = Turtle(shape='circle')
        self.marker.penup()
        self.marker.hideturtle()
        self.marker.shapesize(0.45, 0.45, 2)
        self.marker.color('blue')

    def move_food(self):
        self.marker.hideturtle()
        x = randint(-285, 285)
        y = randint(-285, 285)
        self.marker.setpos(x, y)
        self.marker.showturtle()


class Snake():

    def __init__(self, screen):
        
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
        self.screen.update()

    def add_tail(self, pos):
        t = Turtle(shape='square')
        t.penup()
        t.color('black','black')
        t.setpos(pos)
        t.color('white','white')
        self.body.append(t)

    def eat(self):
        self.food.move_food()
        pos = self.body[-1].pos()
        self.move()
        self.add_tail(pos)

    def move(self):
        new_pos = [self.head.pos()]
        self.head.forward(10) 
        if self.touch_food():
            self.eat()
        for segment in self.body[1:]:
            new_pos.append(segment.pos())
            segment.setpos(new_pos.pop(0))
        self.screen.update()
        time.sleep(0.05)

    def touch_food(self):
        food_x = self.food.marker.xcor()
        food_y = self.food.marker.ycor()
        head_x = self.head.xcor()
        head_y = self.head.ycor()
        if abs(head_x - food_x) < 15 and abs(head_y - food_y) < 15:
            return True
        return False

    def turn(self, direction):
        self.head.setheading(direction)

class SnakeGame():
     
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.screen.title('Snake')
        self.screen.tracer(False)
        self.snake = Snake(self.screen)
        self.screen.onkeypress(lambda: self.snake.turn(90), 'Up')
        self.screen.onkeypress(lambda: self.snake.turn(180), 'Left')
        self.screen.onkeypress(lambda: self.snake.turn(270), 'Down')
        self.screen.onkeypress(lambda: self.snake.turn(0), 'Right')
        self.screen.listen()

        while True:
            self.snake.move()

        self.screen.exitonclick()
