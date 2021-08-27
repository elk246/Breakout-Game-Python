import pygame

import Elements
import Map
import User_interface

pygame.init()

# Hit sound
effect = pygame.mixer.Sound('target/stone_hit.ogg')


def check_wall():
    if Elements.ball_x <= 0:
        Elements.ball_x_direction = 1
    if Elements.ball_x >= 19:
        Elements.ball_x_direction = -1
    if Elements.ball_y <= 0:
        Elements.ball_y_direction = 1
    if Elements.ball_y >= 29:
        Elements.ball_y_direction = 0
        Elements.ball_x_direction = 0
        pygame.mixer.music.stop()


# checks if ball hit a stone.
def check_stone(window, game_size):
    if Elements.ball_y_direction == -1:
        if Map.game_map[Elements.ball_y - 1][Elements.ball_x] != 0:
            Elements.delete_element(Elements.ball_x, Elements.ball_y - 1, window, game_size)
            Map.game_map[Elements.ball_y - 1][Elements.ball_x] = 0
            Elements.ball_y_direction = 1
            effect.play()
            User_interface.score += 50
        else:
            if Elements.ball_x_direction == 1:
                if Map.game_map[Elements.ball_y - 1][Elements.ball_x + 1] != 0:
                    Elements.delete_element(Elements.ball_x + 1, Elements.ball_y - 1, window, game_size)
                    Map.game_map[Elements.ball_y - 1][Elements.ball_x + 1] = 0
                    Elements.ball_y_direction = 1
                    Elements.ball_x_direction = -1
                    effect.play()
                    User_interface.score += 50
            else:
                if Map.game_map[Elements.ball_y - 1][Elements.ball_x - 1] != 0:
                    Elements.delete_element(Elements.ball_x - 1, Elements.ball_y - 1, window, game_size)
                    Map.game_map[Elements.ball_y - 1][Elements.ball_x - 1] = 0
                    Elements.ball_y_direction = 1
                    Elements.ball_x_direction = + 1
                    effect.play()
                    User_interface.score += 50


# counts stones and check if the player won the game.
def count_stones():
    stones = 0
    for i in range(len(Map.game_map)):
        for j in range(len(Map.game_map[i])):
            if Map.game_map[i][j] == 1:
                stones += 1
    if stones > 0:
        return "Stones: " + str(stones)
    else:
        Elements.ball_x_direction = 0
        Elements.ball_y_direction = 0
        return "You won!"


# checks that the player figure not pass the wall.
def check_player_wall():
    if Elements.figure_x == 0 and Elements.figure_direction == -1:
        Elements.figure_direction = 0

    if Elements.figure_x == 16 and Elements.figure_direction == 1:
        Elements.figure_direction = 0


# checks if ball hit the player figure.
def check_hit_player_figure():
    if Elements.ball_y == 26 and Elements.ball_y_direction == 1:
        if Elements.ball_x_direction == -1:
            if Elements.figure_x <= Elements.ball_x <= Elements.figure_x + 3:
                Elements.ball_y_direction = -1
        if Elements.ball_x_direction == 1:
            if Elements.figure_x <= Elements.ball_x <= Elements.figure_x + 3:
                Elements.ball_y_direction = -1
