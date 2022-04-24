from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(.5)
        self.color("blue")
        self.speed(0)
        self.randomize()
        self.pu()
        self.speed(0)

    def randomize(self):
        xaxis = random.randint(-265, 265)
        yaxis = random.randint(-275, 275)
        self.goto(x=xaxis, y=yaxis)
