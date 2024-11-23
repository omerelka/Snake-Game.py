from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #dectect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall

    if (snake.head.xcor() > SCREEN_WIDTH // 2 - 20 or
            snake.head.xcor() < -(SCREEN_WIDTH // 2 - 20) or
            snake.head.ycor() > SCREEN_HEIGHT // 2 - 20 or
            snake.head.ycor() < -(SCREEN_HEIGHT // 2 - 20)):
        game_is_on = False
        scoreboard.game_over()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()