from turtle import Screen, Turtle
import time


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.pu()
            snake.goto(x=-150-(i*20), y=snake.ycor())
            self.segments.append(snake)

    def move(self):
        head = self.segments[0]
        time.sleep(0.1)
        for ind in range(len(self.segments) - 1, 0, -1):
            xaxis = self.segments[ind-1].xcor()
            yaxis = self.segments[ind-1].ycor()
            self.segments[ind].goto(x=xaxis, y=yaxis)
            if xaxis > 350:
                break
        head.forward(20)
