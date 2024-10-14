from turtle import Turtle

START = [(0,0),(-20,0),(-40,0)]
WALK = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
    
    def create_snake(self):
        for i in START:
            self.add(i)

    def new(self):
        for i in self.snakes:
            i.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]



    def add(self, a):
        snake = Turtle("square")
        snake.color("green")
        snake.penup()
        snake.goto(a)
        self.snakes.append(snake)

    def extend(self):
        self.add(self.snakes[-1].position())

    def move(self):     
        for i in range(len(self.snakes)-1,0,-1):
            x1 = self.snakes[i-1].xcor()
            y1 = self.snakes[i-1].ycor()
            self.snakes[i].goto(x1,y1)
        self.head.forward(WALK)

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)
