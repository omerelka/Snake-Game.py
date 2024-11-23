from turtle import  Turtle
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-SCREEN_WIDTH // 2 + 10, SCREEN_WIDTH // 2 - 10)
        random_y = random.randint(-SCREEN_HEIGHT // 2 + 10, SCREEN_HEIGHT // 2 - 10)
        self.goto(random_x, random_y)
