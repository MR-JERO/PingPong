from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.Xa = 10
        self.Ya = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.Xa
        new_y = self.ycor() + self.Ya
        self.goto(new_x, new_y)

    def bounce(self):
        self.Ya *= -1

    def x_bounce(self):
        self.Xa *= -1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.goto(0,0)
        self.x_bounce()
        self.move_speed = 0.1



