import pygame
import Logic

pygame.init()

# defines font.
font = pygame.font.SysFont("Keraleeyam", 20)

# defines score to display it.
score = 0

# defines lives to display it.
lives = 3


# displays score label.
def display_score(window):
    label_score = font.render("Score: " + str(score), True, (0, 0, 255), (255, 255, 255))
    window.blit(label_score, [5, 2])


# displays remaining stones label.
def display_remaining_stones(window):
    label_remaining_stones = font.render(Logic.count_stones(), True, (0, 0, 255), (255, 255, 255))
    window.blit(label_remaining_stones, [5, 20])


# displays lives
def display_lives(window):
    label_life = font.render("Lives: " + str(lives), True, (255, 0, 0), (255, 255, 255))
    window.blit(label_life, [5, 40])
