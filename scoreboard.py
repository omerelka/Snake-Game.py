from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}" , align="center", font=("Ariel",24,"normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}" , align="center", font=("Ariel",24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game over ",  align="center", font=("Ariel",50,"normal"))



