import sys

import pygame
from pygame.examples.go_over_there import screen

from Settings.settings import Settings
from ship import Ship
from bullet import Bullet
from potato import Potato
from time import sleep
from game_stats import GameStats


class PotatoInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Potato Invasion")

        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.potatoes = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_potato()

            self._update_screen()

    def _ship_hit(self):
        """Обрабатывает столкновения корабля с картошками"""
        self.stats.ships_left -= 1

        self.potatoes.empty()
        self.bullets.empty()

        self._create_fleet()
        self.ship.center_ship()

        sleep(1)

    def _check_fleet_edges(self):
        """Меняет направление если достигнут край экрана"""
        for potato in self.potatoes.sprites():
            if potato.check_edges():
                self.settings.fleet_direction *= -1
                break

    def _update_potato(self):
        """Обновляет позиции всех картошек"""
        self._check_fleet_edges()
        self.potatoes.update()

        if pygame.sprite.spritecollideany(self.ship, self.potatoes):
            self._ship_hit()

        self._check_potato_bottom()

    def _check_potato_bottom(self):
        """Проверяет, добрались ли картошки до нижнего края экрана"""
        screen_rect = self.screen.get_rect()
        for potato in self.potatoes.sprites():
            if potato.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _create_fleet(self):
        """Создание флота вторжения"""
        potato = Potato(self)
        potato_width, potato_height = potato.rect.size
        available_space_x = self.settings.screen_width - (2 * potato_width)
        number_potatoes = available_space_x // (2 * potato_width)

        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * potato_height) - ship_height
        number_rows = available_space_y // (2 * potato_height)

        for row_number in range(number_rows):
            for potato_number in range(number_potatoes + 1):
                self._create_potato(potato_number, row_number)

    def _create_potato(self, potato_number, row_number):
        potato = Potato(self)
        potato_width, potato_height = potato.rect.size

        potato.x = potato_width + (2 * potato_number * potato_width)
        potato.rect.x = potato.x

        potato.y = potato_height + 2 * potato_height * row_number
        potato.rect.y = potato.y

        self.potatoes.add(potato)

    def _update_bullets(self):
        """Обновляет позиции снарядов и удаляет пули, которые вышли за край экрана"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= self.screen.get_rect().top:
                self.bullets.remove(bullet)

        self._check_bullet_potato_collisions()

    def _check_bullet_potato_collisions(self):
        """Обрабатывает столкновения снарядов с картошками"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.potatoes, True, True)

        if not self.potatoes:
            self._increase_difficulty()
            self.bullets.empty()
            self._create_fleet()

    def _increase_difficulty(self):
        """Увеличивает сложность игры"""
        self.settings.potato_speed_x *= 1.1
        self.settings.potato_speed_y *= 1.1

    def _fire_bullet(self):
        """Создание нового снаряда и добавление его в группу bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_events(self):
        """Обрабатывает нажатия клавиатуры и мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Проверяет нажатия клавиш"""
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Проверяет отпускания клавиш"""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False

    def _update_screen(self):
        """Обновляет и рисует новый экран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.potatoes.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    ai = PotatoInvasion()
    ai.run_game()
