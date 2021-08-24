import Elements


# checks if the ball hit a wall.
def check_wall():
    if Elements.ball_x <= 0:
        Elements.ball_x_direction = 1
    if Elements.ball_x >= 19:
        Elements.ball_x_direction = -1
    if Elements.ball_y <= 0:
        Elements.ball_y_direction *= -1
    if Elements.ball_y >= 29:
        Elements.ball_y_direction *= -1


# moves the ball for the next step
def next_step(window, game_size):
    Elements.delete_ball(Elements.ball_x, Elements.ball_y, window, game_size)
    Elements.ball_x += Elements.ball_x_direction
    Elements.ball_y += Elements.ball_y_direction
