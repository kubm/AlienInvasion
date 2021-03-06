import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Class representing players ship"""

    def __init__(self, settings, screen):
        """Initialize ship and set its starting position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.settings = settings

        # Load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store decimal value of ship's center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the moving flag"""
        # Update the ship's center value, not rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            print("Moving right")
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            print("Moving left")
            self.center -= self.settings.ship_speed_factor
        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Re-center the ship"""
        self.center = self.screen_rect.centerx
