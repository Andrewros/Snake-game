from turtle import Screen, Turtle
import time


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

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

    def lookdown(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
            self.move()

    def lookup(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
            self.move()

    def lookright(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
            self.move()

    def lookleft(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
            self.move()

    def grow(self):
        newsegment = Turtle(shape="square")
        newsegment.color("white")
        newsegment.speed(0)
        newsegment.pu()
        direction = self.head.heading()
        xposition = self.segments[-1].xcor()
        yposition = self.segments[-1].ycor()
        if direction == 0:
            newsegment.goto(x=xposition-20, y=yposition)
        elif direction == 180:
            newsegment.goto(x=xposition+20, y=yposition)
        elif direction == 90:
            newsegment.goto(x=xposition, y=yposition-20)
        else:
            newsegment.goto(x=xposition, y=yposition+20)
        self.segments.append(newsegment)
