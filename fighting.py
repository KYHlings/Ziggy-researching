from player import Player
import pygame

pygame.init()

screen_width = 500
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("F")

all_sprites_list = pygame.sprite.Group()

player = Player((0, 0, 0), 50, 50)
player.rect.x = 200
player.rect.x = 300

all_sprites_list.add(player)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites_list.update()
    screen.fill((255, 0, 0))
    pygame.draw.rect(screen, (0, 0, 0), [40, 0, 200, 300])

    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
