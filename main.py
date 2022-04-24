from turtle import Screen, Turtle
import time
from snake import Snake
import random
from food import Food
from scoreboard import Scoreboard, Lose
screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
score = 0
snake_length = score+3
scoreboard = Scoreboard()
segments = []
screen.tracer(0)
snake = Snake()
food = Food()
screen.update()
time.sleep(0.25)
game_is_on = True
screen.listen()
screen.onkey(key="Up", fun=snake.lookup)
screen.onkey(key="Right", fun=snake.lookright)
screen.onkey(key="Left", fun=snake.lookleft)
screen.onkey(key="Down", fun=snake.lookdown)
y = 0
while game_is_on:
    screen.update()
    head = snake.segments[0]
    snake.move()
    if head.distance(food) < 20:
        food.randomize()
        scoreboard.addone()
        snake.grow()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_is_on = False
        lose = Lose()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_is_on = False
            lose = Lose()


screen.exitonclick()
