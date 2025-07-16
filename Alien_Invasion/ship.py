import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, game, size):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        self.load_image = pygame.image.load('D:/alien_invasion/Images/lykashenko.bmp')
        self.image = pygame.transform.smoothscale(self.load_image,size)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left >= self.screen_rect.left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """Рисует лукашенко в указанном месте"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль по центру внизу"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
