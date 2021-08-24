# import pygame library.
import pygame, sys, time, random
from pygame.locals import *
import Stone
from random import randrange
import map

# defines the size for the game.
game_size = 20

# generates game display.
window = pygame.display.set_mode((20 * game_size, 30 * game_size))
window.fill((255, 255, 255))
pygame.display.set_caption("Breakout")
active = True

# Display refresh
clock = pygame.time.Clock()

color = (0, 0, 0)
for x in range(0, 20):
    for y in range(0, 27):
        if map.map[y][x] != 0:
            color = Stone.colors[randrange(0, 4)]
            Stone.draw_element(x, y, game_size, window, color)

# main loop
while active:
    # Checks if the user do something.
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            active = False
            print("Player left the game!")

    # Update window
    pygame.display.flip()

    # Refresh time
    clock.tick(10)

pygame.quit()
