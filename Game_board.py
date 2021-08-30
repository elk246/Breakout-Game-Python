# import classes and libraries.
import pygame

import Map
import User_interface
import Elements
import Logic
import Moves

# inits pygame, music and font.
pygame.init()
pygame.mixer.music.load('target/Main_music.ogg')

# defines values for the game.
game_size = 20
color = (0, 0, 0)
active = True

# generates game display.
window = pygame.display.set_mode((20 * game_size, 31 * game_size))
window.fill((255, 255, 255))
pygame.display.set_caption("Breakout")

# Display refresh.
clock = pygame.time.Clock()
pygame.key.set_repeat(10, 0)

# prints game field.
Map.generate_map(1)
Elements.print_field(game_size, window)

# main loop.
pygame.mixer.music.play()
while active:

    # Mouse position for hover effect.
    mouse = pygame.mouse.get_pos()

    # prints interface elements.
    User_interface.display_score(window)
    User_interface.display_remaining_stones(window)
    User_interface.display_lives(window)

    # checks if the user exit game.
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            active = False
            pygame.mixer.music.stop()
            print("Player left the game!")

        # User input.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Elements.figure_direction = -1
            elif event.key == pygame.K_RIGHT:
                Elements.figure_direction = 1

    # Game logic.
    Logic.check_new_lives()
    Logic.check_player_wall()
    Logic.check_wall(window, game_size)
    Logic.check_stone(window, game_size)
    Logic.check_hit_player_figure()

    # Moves.
    Moves.move_ball(window, game_size)
    Moves.move_figure(window, game_size)

    # updates window.
    pygame.display.flip()

    # Refresh time.
    clock.tick(10)

    # checks if game over and starts the game over sound.
    if Logic.game_over:
        Logic.start_game_over_sound()
