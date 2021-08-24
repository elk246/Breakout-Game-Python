# import pygame library.
import pygame
import Elements
from random import randrange
import map

# defines the size for the game.
game_size = 20

# generates game display.
window = pygame.display.set_mode((20 * game_size, 30 * game_size))
window.fill((255, 255, 255))
pygame.display.set_caption("Breakout")
active = True


# Display refresh
clock = pygame.time.Clock()

color = (0, 0, 0)
for x in range(0, 20):
    for y in range(0, 27):
        if map.map[y][x] != 0:
            color = Elements.colors[randrange(0, 4)]
            Elements.draw_element(x, y, game_size, window, color)

# main loop
while active:
    # Checks if the user do something.
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            active = False
            print("Player left the game!")

    # Logic
    if Elements.ball_x <= 0:
        Elements.ball_x_direction = 1
    if Elements.ball_x >= 19:
        Elements.ball_x_direction = -1
    if Elements.ball_y <= 0:
        Elements.ball_y_direction *= -1
    if Elements.ball_y >= 29:
        Elements.ball_y_direction *= -1

    Elements.delete_ball(Elements.ball_x, Elements.ball_y, window, game_size)
    Elements.ball_x += Elements.ball_x_direction
    Elements.ball_y += Elements.ball_y_direction
    Elements.draw_ball(Elements.ball_x, Elements.ball_y, window, game_size)

    # Update window
    pygame.display.flip()

    # Refresh time
    clock.tick(5)

pygame.quit()
