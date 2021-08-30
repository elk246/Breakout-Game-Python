import pygame
import Elements
import Map
import User_interface
import time

pygame.init()

# defines game over status.
game_over = False

score_counter_for_lives = 0

# Sound effects.
effect = pygame.mixer.Sound('target/stone_hit.ogg')
lose_sound = pygame.mixer.Sound('target/lose.ogg')


# checks wall and checks if you lose a live.
def check_wall(window, game_size):
    global game_over
    if Elements.ball_x <= 0:
        Elements.ball_x_direction = 1
    if Elements.ball_x >= 19:
        Elements.ball_x_direction = -1
    if Elements.ball_y <= 0:
        Elements.ball_y_direction = 1
    if Elements.ball_y >= 30:
        User_interface.lives -= 1
        if User_interface.lives == 0:
            Elements.ball_y_direction = 0
            Elements.ball_x_direction = 0
            pygame.mixer.music.stop()
            game_over = True
        else:
            lose_sound.play()
            respawn_ball(window, game_size)


# checks if ball hit a stone.
def check_stone(window, game_size):
    global score_counter_for_lives
    # checks stone up
    if Elements.ball_y_direction == -1:
        if Map.game_map[Elements.ball_y - 1][Elements.ball_x] != 0:
            Elements.delete_element(Elements.ball_x, Elements.ball_y - 1, window, game_size)
            Map.game_map[Elements.ball_y - 1][Elements.ball_x] = 0
            Elements.ball_y_direction = 1
            effect.play()
            User_interface.score += 50
            score_counter_for_lives += 50
        else:
            # checks stone up right.
            if Elements.ball_x_direction == 1:
                if Map.game_map[Elements.ball_y - 1][Elements.ball_x + 1] != 0:
                    Elements.delete_element(Elements.ball_x + 1, Elements.ball_y - 1, window, game_size)
                    Map.game_map[Elements.ball_y - 1][Elements.ball_x + 1] = 0
                    Elements.ball_y_direction = 1
                    Elements.ball_x_direction = -1
                    effect.play()
                    User_interface.score += 50
                    score_counter_for_lives += 50
            else:
                # checks stone up left.
                if Map.game_map[Elements.ball_y - 1][Elements.ball_x - 1] != 0:
                    Elements.delete_element(Elements.ball_x - 1, Elements.ball_y - 1, window, game_size)
                    Map.game_map[Elements.ball_y - 1][Elements.ball_x - 1] = 0
                    Elements.ball_y_direction = 1
                    Elements.ball_x_direction = + 1
                    effect.play()
                    User_interface.score += 50
                    score_counter_for_lives += 50
    else:
        # checks stone down if the ball is up to the the player figure.
        if Elements.ball_y < Elements.figure_y:
            if Map.game_map[Elements.ball_y + 1][Elements.ball_x] != 0:
                Elements.delete_element(Elements.ball_x, Elements.ball_y + 1, window, game_size)
                Map.game_map[Elements.ball_y + 1][Elements.ball_x] = 0
                Elements.ball_y_direction = - 1
                Elements.ball_x_direction = - 1
                effect.play()
                User_interface.score += 50
                score_counter_for_lives += 50


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
    if Elements.ball_y == 28 and Elements.ball_y_direction == 1:
        if Elements.ball_x_direction == -1:
            if Elements.figure_x <= Elements.ball_x <= Elements.figure_x + 3:
                Elements.ball_y_direction = -1
        if Elements.ball_x_direction == 1:
            if Elements.figure_x <= Elements.ball_x <= Elements.figure_x + 3:
                Elements.ball_y_direction = -1


# starts game over sound and exits the game.
def start_game_over_sound():
    game_over_sound_length = pygame.mixer.Sound('target/game_over.ogg').get_length()
    pygame.mixer.Sound('target/game_over.ogg').play()
    time.sleep(game_over_sound_length)
    pygame.quit()
    exit()


# respawns ball if you lose a live.
def respawn_ball(window, game_size):
    Elements.delete_element(Elements.ball_x, Elements.ball_y, window, game_size)
    Elements.ball_x = 1
    Elements.ball_y = 20
    Elements.ball_x_direction = 1
    Elements.ball_y_direction = 1


def check_new_lives():
    global score_counter_for_lives
    if score_counter_for_lives == 400:
        User_interface.lives += 1
        score_counter_for_lives = 0
