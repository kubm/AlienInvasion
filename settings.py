class Settings():
    """Class containing settings for Alien Invasion"""

    def __init__(self):
        """Initialize the settings"""
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.50

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that will be changing"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        self.alien_points = 50

        # fleet_direction > 0 means right; <0 means left
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print("New alien points: " + str(self.alien_points))
