import pygame

colors = [(255, 140, 0), (139, 0, 139), (255, 0, 0), (0, 100, 0), (0, 0, 255)]


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
