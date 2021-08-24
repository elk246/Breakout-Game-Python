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
def next_step(window, game_size):
    Elements.delete_element(Elements.ball_x, Elements.ball_y, window, game_size)
    Elements.ball_x += Elements.ball_x_direction
    Elements.ball_y += Elements.ball_y_direction


# checks if ball hit a stone.
def check_stone(window, game_size):

    if Elements.ball_y_direction == -1:

        if map.game_map[Elements.ball_y - 1][Elements.ball_x] != 0:
            print("hit stone top")
            Elements.delete_element(Elements.ball_x, Elements.ball_y - 1, window, game_size)
            map.game_map[Elements.ball_y - 1][Elements.ball_x] = 0
            Elements.ball_y_direction = 1
        else:
            if Elements.ball_x_direction == 1:
                if map.game_map[Elements.ball_y - 1][Elements.ball_x + 1] != 0:
                    print("ball hits stone right top")
                    Elements.delete_element(Elements.ball_x + 1, Elements.ball_y - 1, window, game_size)
                    map.game_map[Elements.ball_y - 1][Elements.ball_x + 1] = 0
                    Elements.ball_y_direction = 1
                    Elements.ball_x_direction = -1
            else:
                if map.game_map[Elements.ball_y - 1][Elements.ball_x - 1] != 0:
                    print("ball hit stone top left")
                    Elements.delete_element(Elements.ball_x - 1, Elements.ball_y - 1, window, game_size)
                    map.game_map[Elements.ball_y - 1][Elements.ball_x - 1] = 0
                    Elements.ball_y_direction = 1
                    Elements.ball_x_direction = + 1
