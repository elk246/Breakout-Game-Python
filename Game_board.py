# import classes and libraries.
import pygame

import Elements
from random import randrange
import Logic
import Moves
import Map

pygame.init()

# Musik/Soundeffekte einrichten
pygame.mixer.music.load('target/Loyalty_Freak_Music_-_10_-_Everyone_is_so_alive.ogg')
pygame.mixer.music.play(-1,0.0)


# defines values for the game.
game_size = 20
color = (0, 0, 0)
next_step = False
active = True

# generates game display.
window = pygame.display.set_mode((20 * game_size, 30 * game_size))
window.fill((255, 255, 255))
pygame.display.set_caption("Breakout")

# Display refresh.
clock = pygame.time.Clock()
pygame.key.set_repeat(10,0)

# prints game field.
for x in range(0, 20):
    for y in range(0, 27):
        if Map.game_map[y][x] != 0:
            color = Elements.colors[randrange(0, 5)]
            Elements.draw_stone(x, y, game_size, window, color)
# main loop.
while active:
    # Checks if the user exit game.
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            active = False
            print("Player left the game!")

        # User input.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Elements.figure_direction = -1
            elif event.key == pygame.K_RIGHT:
                Elements.figure_direction = 1
    # Game logic.
    Logic.check_player_wall()
    Logic.check_wall()
    Logic.check_stone(window, game_size)
    Logic.check_hit_player_figure()

    # Moves.
    Moves.move_ball(window, game_size)
    Moves.move_figure(window, game_size)
    print(Logic.count_stones())

    # Updates window.
    pygame.display.flip()

    # Refresh time.
    clock.tick(9)

pygame.quit()

exit()
