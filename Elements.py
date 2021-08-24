import pygame

ball_x = 10
ball_y = 23
ball_x_direction = 1
ball_y_direction = 1

colors = [(255, 140, 0), (139, 0, 139), (255, 0, 0), (0, 100, 0), (0, 0, 255)]
black = (0, 0, 0)
white = (255, 255, 255)


def corr(number, game_size):
    number = number * game_size
    return number


def draw_element(column, row, game_size, window, color):
    pygame.draw.rect(
        window,
        color,
        [corr(column, game_size) + 1,
         corr(row, game_size) + 1,
         corr(1, game_size) - 1,
         corr(1, game_size) - 1
         ]
    )


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


def delete_ball(x, y, window, game_size):
    pygame.draw.rect(
        window,
        white,
        [corr(x, game_size),
         corr(y, game_size),
         corr(1, game_size),
         corr(1, game_size)]
    )
