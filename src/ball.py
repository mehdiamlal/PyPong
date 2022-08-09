from turtle import Turtle
from random import randint

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(3)
        self.shape("circle")
        self.color("#fff")
    
    def move(self):
        """Makes the ball move."""
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10 
        self.goto(new_x, new_y)