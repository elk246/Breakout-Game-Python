# import pygame library.
import pygame, sys, time, random
from pygame.locals import *
import Stone

# defines the size for the game.
import stoneColors

game_size = 30

# generates game display.
window = pygame.display.set_mode((20 * game_size, 30 * game_size))
window.fill((255, 255, 255))
pygame.display.set_caption("Breakout")
active = True

# Display refresh
clock = pygame.time.Clock()

Stone.draw_element(0, 0, game_size, window, stoneColors.green)
Stone.draw_element(0, 1, game_size, window, stoneColors.red)
Stone.draw_element(0, 2, game_size, window, stoneColors.black)
Stone.draw_element(1, 0, game_size, window, stoneColors.green)
Stone.draw_element(1, 1, game_size, window, stoneColors.red)
Stone.draw_element(1, 2, game_size, window, stoneColors.orange)
Stone.draw_element(2, 0, game_size, window, stoneColors.red)
Stone.draw_element(2, 1, game_size, window, stoneColors.green)
Stone.draw_element(2, 2, game_size, window, stoneColors.black)


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