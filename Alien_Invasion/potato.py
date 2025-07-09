import pygame
from pygame.sprite import Sprite

class Potato(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load('D:/alien_invasion/Images/potato.bmp')
        self.image = pygame.transform.smoothscale(self.image, (65, 50))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает картошку"""
        self.x += self.settings.potato_speed_x * self.settings.fleet_direction
        self.y += self.settings.potato_speed_y
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        """Возвращает True если картошка у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            return True