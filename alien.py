import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent single alien ship in the fleet"""

    def __init__(self, settings, screen):
        super(Alien, self).__init__()
        self.settings = settings
        self.screen = screen

        # Load the alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien ship at its location """
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right"""
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x
