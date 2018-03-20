class Settings():
    def __init__(self):
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (60, 63, 65)
        # Настройки корабля
        self.ship_speed_factor = 1.5
        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 2
        self.bullet_height = 4
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 10