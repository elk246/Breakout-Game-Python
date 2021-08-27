import pygame

import Elements
import Logic

pygame.init()
font = pygame.font.SysFont("Keraleeyam", 20)
green = (0, 102, 0)
blue = (50, 110, 201)

# defines score to display it.
score = 0


# displays score label.
def display_score(window):
    label_score = font.render("Score: " + str(score), True, (0, 0, 255), (255, 255, 255))
    window.blit(label_score, [5, 2])


# displays remaining stones label.
def display_remaining_stones(window):
    label_remaining_stones = font.render(Logic.count_stones(), True, (0, 0, 255), (255, 255, 255))
    window.blit(label_remaining_stones, [5, 20])
