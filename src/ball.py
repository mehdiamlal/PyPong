from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(3)
        self.shape("circle")
        self.color("#fff")
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        """Makes the ball move."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move 
        self.goto(new_x, new_y)

    def wall_bounce(self):
        """Makes the ball bounce once it hits the wall by reversing its direction on y-axis."""
        self.y_move *= -1 

    def paddle_bounce(self):
        """Makes the ball bounce once it hits the wall by reversing its direction on x-axis."""
        self.x_move *= -1