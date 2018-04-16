import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create a ship instance
    ship = Ship(game_settings, screen)
    # Make a group to store bullets
    bullets = Group()
    # Make an alien
    aliens = Group()

    gf.create_fleet(game_settings, screen, ship, aliens)
    # Main loop
    while True:

        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        print(len(bullets))
        gf.update_aliens(game_settings, aliens)
        gf.update_screen(game_settings, screen, ship, aliens, bullets)


run_game()
