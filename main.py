import pygame
import sys
from fight import fight, main_menu, lobby
import os


screen = pygame.display.set_mode((800, 600))

main_menu()

running = True
while running:
    lobby()

    fight()
    pygame.display.update()

