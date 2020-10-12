import pygame

white = (255, 255, 255)


class Player():
    def __init__(self, color, width, height):
        super().__init__()
        # starting x and y pos
        # self.x = x
        # self.y = y
        # x and y values that decide the size of the character
        self.width = width
        self.height = height
        # how many pixels the character is moving per action
        self.vel = 5
        self.vel_2 = 2
        # variables for the jumping mechanism
        self.is_jump = False
        self.jump_count = 10
        # counter for walking animation
        self.walk_count = 0
        # stating left and right
        self.left = False
        self.right = False
        self.standing = True
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
