import pygame

import Map
from random import randrange

# defines ball coordinates and directions.
ball_x = 1
ball_y = 20
ball_x_direction = 1
ball_y_direction = 1

# defines figure coordinates and direction.
figure_x = 8
figure_y = 29
figure_direction = 0

# defines the colors for the stones.
colors = [(255, 140, 0), (139, 0, 139), (255, 0, 0), (0, 100, 0), (0, 0, 255), (255, 0, 0)]

# defines ball color.
black = (0, 0, 0)

# defines color for the background.
white = (255, 255, 255)


# corrects the distance between the stones for the current game_size.
def corr(number, game_size):
    number = number * game_size
    return number


# draws stones.
def draw_stone(column, row, game_size, window, color):
    pygame.draw.rect(
        window,
        color,
        [corr(column, game_size) + 1,
         corr(row, game_size) + 1,
         corr(1, game_size) - 1,
         corr(1, game_size) - 1
         ]
    )


# draws game ball.
def draw_ball(x, y, window, game_size):
    pygame.draw.ellipse(
        window,
        black,
        [corr(x, game_size),
         corr(y, game_size),
         corr(1, game_size),
         corr(1, game_size)
         ],
        0
    )


# deletes old ball and replace that field with a white background element.
def delete_element(x, y, window, game_size):
    pygame.draw.rect(
        window,
        white,
        [corr(x, game_size),
         corr(y, game_size),
         corr(1, game_size),
         corr(1, game_size)]
    )


# draws the figure.
def draw_figure(x, window, game_size):
    pygame.draw.rect(window, black, (corr(x, game_size), corr(figure_y, game_size), 80, corr(1, game_size)))


# deletes the figure.
def delete_figure(x, window, game_size):
    pygame.draw.rect(window, white, (corr(x, game_size), corr(figure_y, game_size), 80, corr(1, game_size)))


# prints game field.
def print_field(game_size, window):
    for x in range(0, 20):
        for y in range(0, 27):
            if Map.game_map[y][x] != 0:
                color = colors[randrange(0, 5)]
                draw_stone(x, y, game_size, window, color)
