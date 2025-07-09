class GameStats:
    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()

    def reset_stats(self):
        """Инициализирует статистику"""
        self.ships_left = self.settings.ship_limit
