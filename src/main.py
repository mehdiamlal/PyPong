from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep


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

paddle1 = Paddle((-350, 0))
paddle2 = Paddle((350, 0))
ball = Ball()

screen.update()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

game_is_on = True

while game_is_on:
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    

    screen.update()
    sleep(0.03)


screen.exitonclick()