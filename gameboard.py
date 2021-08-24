# import classes and libraries.
import pygame
import Elements
from random import randrange
import Logic
import map

# defines values for the game.
game_size = 20
color = (0, 0, 0)
next_step = False
active = True

# generates game display.
window = pygame.display.set_mode((20 * game_size, 30 * game_size))
window.fill((255, 255, 255))
pygame.display.set_caption("Breakout")

# Display refresh
clock = pygame.time.Clock()

# prints gamefield
for x in range(0, 20):
    for y in range(0, 27):
        if map.game_map[y][x] != 0:
            color = Elements.colors[randrange(0, 5)]
            Elements.draw_stone(x, y, game_size, window, color)
# main loop
while active:
    # Checks if the user exit game.
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            active = False
            print("Player left the game!")

        # checks if user press space and sets next_step to true.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            next_step = True
            print("Next Step")

    # Checks if ball hit a wall.
    Logic.check_wall()

    # Checks if next_step is true. Starts Next ball step
    if next_step:
        Logic.next_step(window, game_size)
        next_step = False

    Elements.draw_ball(Elements.ball_x, Elements.ball_y, window, game_size)

    # Update window
    pygame.display.flip()

    # Refresh time
    clock.tick(5)

pygame.quit()
