import pygame
import gameboard


oragne = {255, 140, 0}


def draw_element(column, row):
    pygame.draw.rect(gameboard.fenster, oragne, (column * gameboard.MULTIPLIKATOR, row * gameboard.MULTIPLIKATOR, gameboard.MULTIPLIKATOR, gameboard.MULTIPLIKATOR))


def test():
    print(gb.MULTIPLIKATOR)