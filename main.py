from turtle import Screen, Turtle
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
score = 0
snake_length = score+3
segments = []
screen.tracer(0)
snake = Snake()
screen.update()
time.sleep(0.25)
game_is_on = True
y = 0
while game_is_on:
    head = snake.segments[0]
    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        break
    snake.move()
    screen.update()
    y += 1
    if y > 20:
        break


screen.exitonclick()
