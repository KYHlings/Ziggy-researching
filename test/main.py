import pygame
import sys
from test.fight import fight

screen = pygame.display.set_mode((800, 600))


def main():
    running = True
    while running:
        # loopar igenom en lista med pygame.events (knapptryckningar)
        for event in pygame.event.get():
            # kollar om användaren trycker på det röda krysset
            if event.type == pygame.QUIT:
                # stänger programmet
                sys.exit()


main()


