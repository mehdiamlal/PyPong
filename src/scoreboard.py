from turtle import Turtle

class LeftScore(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("#fff")
        self.hideturtle()
        self.penup()
        self.goto(-50, 200)
        self.write(f"{self.score}", align="center", font=("Pong Score", 75, "bold"))

    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align="center", font=("Pong Score", 75, "bold"))

class RightScore(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("#fff")
        self.hideturtle()
        self.penup()
        self.goto(75, 200)
        self.write(f"{self.score}", align="center", font=("Pong Score", 75, "bold"))

    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align="center", font=("Pong Score", 75, "bold"))

class ScoreBoard():

    def __init__(self):
        self.left_score = LeftScore()
        self.right_score = RightScore()
    
    def increase_left_score(self):
        """Increases the left score by 1 point."""
        self.left_score.increase()

    def increase_right_score(self):
        """Increases the right score by 1 point."""
        self.right_score.increase()