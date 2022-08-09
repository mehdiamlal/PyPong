from turtle import Turtle, Screen
from paddle import Paddle
import time

PADDLE1_INITIAL_POSITIONS = ((-380, 0), (-380, 20), (-380, -20))
PADDLE2_INITIAL_POSITIONS = ((370, 0), (370, 20), (370, -20))


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

paddle1 = Paddle(PADDLE1_INITIAL_POSITIONS)
paddle2 = Paddle(PADDLE2_INITIAL_POSITIONS)

screen.update()

game_is_on = True

while game_is_on:
    screen.onkey(paddle1.up, "w")
    screen.onkey(paddle1.down, "s")
    screen.onkey(paddle2.up, "Up")
    screen.onkey(paddle2.down, "Down")
    screen.update()


screen.exitonclick()