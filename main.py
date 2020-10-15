import pygame
import sys
from lobby import lobby
from main_menu import main_menu
from fight import fight

screen = pygame.display.set_mode((800, 600))
main_menu()


def main():
    running = True
    while running:
        lobby()
        fight()
        # loopar igenom en lista med pygame.events (knapptryckningar)
        for event in pygame.event.get():
            # kollar om användaren trycker på det röda krysset
            if event.type == pygame.QUIT:
                # stänger programmet
                sys.exit()


main()


