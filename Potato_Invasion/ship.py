import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, game, size):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        self.load_image = pygame.image.load('/Potato_Invasion/Images/lykashenko.bmp')
        self.load_reverse_image = pygame.image.load('/Potato_Invasion/Images/reverse_lykashenko.bmp')
        self.image = pygame.transform.smoothscale(self.load_image,size)
        self.reverse_image = pygame.transform.smoothscale(self.load_reverse_image, size)
        self.rect = self.image.get_rect()
        self.reverse_rect = self.reverse_image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.reverse_rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
        self.last_move = 1 #1- право, -1 - лево

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.x += self.settings.ship_speed
            self.last_move = 1
        if self.moving_left and self.rect.left >= self.screen_rect.left:
            self.x -= self.settings.ship_speed
            self.last_move = -1
        self.rect.x = self.x
        self.reverse_rect.x = self.x

    def blitme(self):
        """Рисует лукашенко в указанном месте"""
        if self.last_move == 1:
            self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.reverse_image, self.reverse_rect)

    def center_ship(self):
        """Размещает корабль по центру внизу"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.reverse_rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
