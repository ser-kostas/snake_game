from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def restart_game():
    snake.reset()
    scoreboard.reset()
    global game_is_on
    game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard(screen)

# # Initial game speed
# game_speed = 0.1

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# screen.mainloop()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(snake.speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score += 1  # Increment the score
        scoreboard.update_score()

        if snake.speed > 0.02:
            snake.speed -= 0.005

    # Detect collision with wall
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() < -300 or snake.head.ycor() > 300:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.onkey(restart_game, "Return")
# Keep the window open
screen.mainloop()