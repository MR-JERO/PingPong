from turtle import Turtle

START = [(350, 0), (-350, 0)]
YCOR = 250
YCOR_Z = 221
ADD = 20


class Board:
    def __init__(self):
        self.cards = []
        self.make_board()


    def make_board(self):
        for _ in START:
            tim = Turtle()
            tim.color("white")
            tim.shape("square")
            tim.shapesize(stretch_wid=5, stretch_len=1)
            tim.penup()
            tim.goto(_)
            self.cards.append(tim)

    def rgo_up(self):
        for item in self.cards[0:1]:
            if item.ycor() < YCOR:
                new_y = item.ycor() + ADD
                item.goto(item.xcor(), new_y)

    def rgo_down(self):
        for item in self.cards[0:1]:
            if item.ycor() > - YCOR_Z:
                new_y = item.ycor() - ADD
                item.goto(item.xcor(), new_y)

    def lgo_up(self):
        for item in self.cards[1:2]:
            if item.ycor() < YCOR:
                new_y = item.ycor() + ADD
                item.goto(item.xcor(), new_y)

    def lgo_down(self):
        for item in self.cards[1:2]:
            if item.ycor() > - YCOR_Z:
                new_y = item.ycor() - ADD
                item.goto(item.xcor(), new_y)

