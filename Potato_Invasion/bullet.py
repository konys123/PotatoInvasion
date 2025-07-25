import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop
        self.rect.x += 50 * game.ship.last_move
        self.y = float(self.rect.y)

    def update(self):
        """Обновляет позицию пули"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Рисует пулю над лукашенко"""
        pygame.draw.rect(self.screen, self.color, self.rect)
