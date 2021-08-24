import pygame


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