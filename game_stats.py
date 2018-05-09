class GameStats():
    """tracking statistics for the game"""

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()

        # Start game inactice
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
