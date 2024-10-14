from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("silver")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        x1 = random.randint(-230, 230)
        y1 = random.randint(-230, 180)
        self.goto(x1,y1)
        self.refresh()

    def refresh(self):
        x1 = random.randint(-230, 230)
        y1 = random.randint(-230, 180)
        self.goto(x1,y1)