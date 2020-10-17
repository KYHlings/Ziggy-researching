import pygame
import sys
from lobby import lobby
from main_menu import main_menu
from fight import fight

screen = pygame.display.set_mode((800, 600))

game_state = ""

print(game_state)
pygame.display.update()





def main():
    running = True
    while running:
        main_menu(game_state)
        if game_state == "lobby":
            lobby(game_state)
            print(game_state)
            pygame.display.update()

        if game_state == "fight":
            fight(game_state)
            print(game_state)
            pygame.display.update()
        # loopar igenom en lista med pygame.events (knapptryckningar)
        for event in pygame.event.get():
            # kollar om användaren trycker på det röda krysset
            if event.type == pygame.QUIT:
                # stänger programmet
                sys.exit()


main()


