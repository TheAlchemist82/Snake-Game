from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
all_turts = []
game_on = True


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.all_turts[0].distance(food) < 15:
        food.refresh()
        scoreboard.point()
        snake.add()
    if snake.all_turts[0].xcor() > 290 or snake.all_turts[0].xcor() < -290 or snake.all_turts[0].ycor() > 290 or snake.all_turts[0].ycor() < -290:
        scoreboard.reset()
        snake.reset()
    
    for segment in snake.all_turts[1:]:
        if snake.all_turts[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()