
print("Hello World")


## create a green snake game with pygame

from pygame import *
import random

# initialize pygame

init()

# create the screen
screen = display.set_mode((800, 600))

# set the title of the window
display.set_caption("Snake Game")

# create the snake
snake = [(200, 200), (210, 200), (220, 200)]

# create the snake food
food = [random.randint(1, 79) * 10, random.randint(1, 59) * 10]

# create the score
score = 0

# create the snake speed
velocity = 10

# create the snake direction
direction = "right"
direction_change = False
direction_list = ["right", "left", "up", "down"]
direction_index = 0
direction_index_change = False

# create the game over flag
game_over = False
game_over_count = 0

# create the game over text
game_over_text = "Game Over!\nPress Enter to Restart"
game_over_text_font = font.SysFont("Arial", 30)
game_over_text_color = (255, 255, 255)
game_over_text_x = (800 - game_over_text_font.size(game_over_text)[0]) / 2
game_over_text_y = (600 - game_over_text_font.size(game_over_text)[1]) / 2
game_over_text_rect = Rect(game_over_text_x, game_over_text_y, game_over_text_font.size(game_over_text)[0], game_over_text_font.size(game_over_text)[1])

# create the snake head
snake_head = image.load("snake_head.png")
snake_head_rect = snake_head.get_rect()
screen.blit(snake_head, (snake[0][0], snake[0][1]))
snake_head_rect.x = snake[0][0]
snake_head_rect.y = snake[0][1]
score_text_font = font.SysFont("Arial", 30)

# create the snake body
snake_body = image.load("snake_body.png")
snake_body_rect = snake_body.get_rect()
screen.blit(snake_body, (snake[1][0], snake[1][1]))
snake_body_rect.x = snake[1][0]
snake_body_rect.y = snake[1][1]
snake_body_rect.x = snake[2][0]
snake_body_rect.y = snake[2][1]

# create the snake food
snake_food = image.load("snake_food.png")
snake_food_rect = snake_food.get_rect()
screen.blit(snake_food, (food[0], food[1]))
snake_food_rect.x = food[0]
snake_food_rect.y = food[1]

# create the snake tail
snake_tail = image.load("snake_tail.png")
snake_tail_rect = snake_tail.get_rect()
screen.blit(snake_tail, (snake[-1][0], snake[-1][1]))
snake_tail_rect.x = snake[-1][0]
snake_tail_rect.y = snake[-1][1]






