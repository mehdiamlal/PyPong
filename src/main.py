from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("#000")
screen.title("PyPong")
screen.tracer(0)
screen.listen()

#drawing the separator
separator = Turtle()
separator.color("#fff")
separator.pensize(2)
separator.penup()
separator.hideturtle()
separator.goto(0, -300)
separator.setheading(90)

while separator.ycor() < 300:
    separator.pendown()
    separator.forward(20)
    separator.penup()
    separator.forward(20)

right_paddle = Paddle((-350, 0))
left_paddle = Paddle((350, 0))
scoreboard = ScoreBoard()
ball = Ball()

screen.update()
screen.onkey(right_paddle.up, "w")
screen.onkey(right_paddle.down, "s")
screen.onkey(left_paddle.up, "Up")
screen.onkey(left_paddle.down, "Down")

game_is_on = True

while game_is_on:
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    

    #collision with left_paddle
    if ball.xcor() > 340 and ball.distance(left_paddle) < 50:
        ball.paddle_bounce()

    #collision with right_paddle
    if ball.xcor() < -340 and ball.distance(right_paddle) < 50:
        ball.paddle_bounce()

    #when left_paddle misses
    if ball.xcor() < -400:
        right_paddle.goto(-350, 0)
        left_paddle.goto(350, 0)
        scoreboard.increase_right_score()
        ball = Ball()

    #when right_paddle misses
    if ball.xcor() > 400:
        right_paddle.goto(-350, 0)
        left_paddle.goto(350, 0)
        scoreboard.increase_left_score()
        ball = Ball()


    screen.update()
    sleep(0.05)


screen.exitonclick()