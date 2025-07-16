class GameStats:
    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Инициализирует статистику"""
        self.ships_left = self.settings.ship_limit
        self.settings.init_dynamic_settings()
        self.score = 0
        self.level = 1
