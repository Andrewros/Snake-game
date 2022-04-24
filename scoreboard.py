from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.pu()
        self.speed(0)
        self.goto(x=self.xcor(), y=250)
        self.write("Score: " + str(self.score), align="center",
                   font=('courier', 24, "normal"))

    def addone(self):
        self.score += 1
        self.clear()
        self.write("Score: " + str(self.score), align="center",
                   font=('courier', 24, "normal"))


class Lose(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.write("GAME OVER", align="center",
                   font=('courier', 24, "normal"))
