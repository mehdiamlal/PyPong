from re import I
from turtle import Turtle

class Paddle():

    def __init__(self, initial_positions):
        self.segments = [Turtle(), Turtle(), Turtle(), Turtle()]

        for i in range(len(self.segments)):
            self.segments[i].penup()
            self.segments[i].shape("square")
            self.segments[i].color("#fff")
            self.segments[i].goto(initial_positions[i])
        

    def up(self):
        """Makes the paddle go up."""
        for s in self.segments:
            s.setheading(90)
            s.forward(40)


    def down(self):
        """Makes the paddle go down."""
        for s in reversed(self.segments):
            s.setheading(270)
            s.forward(40)