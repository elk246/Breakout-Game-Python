import Elements


# moves figure for the next step.
def move_figure(window, game_size):
    Elements.delete_figure(Elements.figure_x, window, game_size)
    Elements.figure_x += Elements.figure_direction
    Elements.draw_figure(Elements.figure_x, window, game_size)
    Elements.figure_direction = 0


# moves the ball for the next step.
def move_ball(window, game_size):
    Elements.delete_element(Elements.ball_x, Elements.ball_y, window, game_size)
    Elements.ball_x += Elements.ball_x_direction
    Elements.ball_y += Elements.ball_y_direction
    Elements.draw_ball(Elements.ball_x, Elements.ball_y, window, game_size)
