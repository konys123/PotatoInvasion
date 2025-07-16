class Settings:

    def __init__(self):
        self.screen_width = 0
        self.screen_height = 0
        self.bg_color = (230, 230, 230)

        self.ship_limit = 1

        self.bullet_speed = 1
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        self.number_rows = 2
        self.speedup_scale = 2
        self.score_scale = 1.5

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """Инициализирует настройки меняющиеся в ходе игры"""
        self.potato_speed_x = 0.2
        self.potato_speed_y = 0.1

        self.ship_speed = 1

        self.fleet_direction = 1 # 1 - вправо, -1 - влево

        self.potato_points = 50