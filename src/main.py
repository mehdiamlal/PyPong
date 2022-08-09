from turtle import Turtle, Screen
from scorecounter import ScoreCounter

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("#000")
screen.title("PyPong")
screen.tracer(0)

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

screen.update()




screen.exitonclick()