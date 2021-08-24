import pygame, sys, time, random
from pygame.locals import *

import Stone

MULTIPLIKATOR = 20

window = pygame.display.set_mode((20 * MULTIPLIKATOR, 30 * MULTIPLIKATOR))

pygame.display.set_caption("Breakout")
active = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()


Stone.draw_element(6,7)

# Schleife Hauptprogramm
while active:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            active = False
            print("Spieler hat beendet")

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(10)



pygame.quit()