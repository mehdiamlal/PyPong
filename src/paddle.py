from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, initial_position):
        
        super().__init__()
        self.color("#fff")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(initial_position)
        self.speed(0)
        

    def up(self):
        """Makes the paddle go up."""
        self.sety(self.ycor() + 40)


    def down(self):
        """Makes the paddle go down."""
        self.sety(self.ycor() - 40)
