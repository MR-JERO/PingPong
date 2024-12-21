import time
from turtle import Screen
from boards import Board
from ball import Ball
from scoreboard import Scoreboard


dis = Screen()
dis.bgcolor("black")
dis.setup(width=800, height=600)
dis.title("PING PONG")
dis.tracer(0)

form = Board()
boll = Ball()
score = Scoreboard()

dis.listen()
dis.onkey(form.rgo_up, "Up")
dis.onkey(form.rgo_down, "Down")
dis.onkey(form.lgo_up, "w")
dis.onkey(form.lgo_down, "z")

game_on = True
while game_on:
    time.sleep(boll.move_speed)
    dis.update()
    boll.move()
    if boll.ycor() > 280 or boll.ycor() < - 280:
        boll.bounce()

    if boll.distance(form.cards[0]) < 50 and boll.xcor() > 320:
        boll.x_bounce()

    if boll.distance(form.cards[1]) < 50 and boll.xcor() < -320:
        boll.x_bounce()

    if boll.xcor() > 380:
        boll.ball_reset()
        score.increase_l()

    if boll.xcor() < -380:
        boll.ball_reset()
        score.increase_r()

dis.exitonclick()
