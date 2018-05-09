class Settings():
    """Class containing settings for Alien Invasion"""

    def __init__(self):
        """Initialize the settings"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 1

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 1
        self.drop_speed = 10
        # fleet_direction > 0 means right; <0 means left
        self.fleet_direction = 1
