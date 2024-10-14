from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import random
import time
screen = Screen()
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.setup(width=800, height=500)
screen.tracer(0)

snake = Snake()
food =  Food()
score = Score()
screen.listen()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game = True
while game:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.scoreboard()
   
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() < -240 or snake.head.ycor() > 240 : 
        
        score.high()
        snake.new()

    for i in snake.snakes[1:]:
        if snake.head.distance(i) < 10:
            
            score.high()
            snake.new()
            






screen.exitonclick()