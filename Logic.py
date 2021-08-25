import Elements

# checks if the ball hit a wall.
import map


def check_wall():
    if Elements.ball_x <= 0:
        Elements.ball_x_direction = 1
    if Elements.ball_x >= 19:
        Elements.ball_x_direction = -1
    if Elements.ball_y <= 0:
        Elements.ball_y_direction = 1
    if Elements.ball_y >= 29:
        Elements.ball_y_direction = -1


# moves the ball for the next step
def move_ball(window, game_size):
    Elements.delete_element(Elements.ball_x, Elements.ball_y, window, game_size)
    Elements.ball_x += Elements.ball_x_direction
    Elements.ball_y += Elements.ball_y_direction
    Elements.draw_ball(Elements.ball_x, Elements.ball_y, window, game_size)


# checks if ball hit a stone.
def check_stone(window, game_size):
    if Elements.ball_y_direction == -1:
        if map.game_map[Elements.ball_y - 1][Elements.ball_x] != 0:
            Elements.delete_element(Elements.ball_x, Elements.ball_y - 1, window, game_size)
            map.game_map[Elements.ball_y - 1][Elements.ball_x] = 0
            Elements.ball_y_direction = 1
        else:
            if Elements.ball_x_direction == 1:
                if map.game_map[Elements.ball_y - 1][Elements.ball_x + 1] != 0:
                    Elements.delete_element(Elements.ball_x + 1, Elements.ball_y - 1, window, game_size)
                    map.game_map[Elements.ball_y - 1][Elements.ball_x + 1] = 0
                    Elements.ball_y_direction = 1
                    Elements.ball_x_direction = -1
            else:
                if map.game_map[Elements.ball_y - 1][Elements.ball_x - 1] != 0:
                    Elements.delete_element(Elements.ball_x - 1, Elements.ball_y - 1, window, game_size)
                    map.game_map[Elements.ball_y - 1][Elements.ball_x - 1] = 0
                    Elements.ball_y_direction = 1
                    Elements.ball_x_direction = + 1


def count_stones():
    stones = 0
    for i in range(len(map.game_map)):
        for j in range(len(map.game_map[i])):
            if map.game_map[i][j] == 1:
                stones += 1
    if stones > 0:
        return stones, "Stones left"
    else:
        Elements.ball_x_direction = 0
        Elements.ball_y_direction = 0
        return "You won!"


def move_figure(window, game_size):

    Elements.delete_figure(Elements.figure_x, window, game_size)
    Elements.figure_x += Elements.figure_direction

    Elements.draw_figure(Elements.figure_x, window, game_size)
    Elements.figure_direction = 0

