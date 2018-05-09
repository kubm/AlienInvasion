import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(game_settings, screen, "Play")

    # Create game stats instance
    stats = GameStats(game_settings)

    # Create a ship instance
    ship = Ship(game_settings, screen)
    # Make a group to store bullets
    bullets = Group()
    # Make an alien
    aliens = Group()

    gf.create_fleet(game_settings, screen, ship, aliens)
    # Main loop
    while True:

        gf.check_events(game_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(game_settings, screen, ship, aliens, bullets)
            gf.update_aliens(game_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(game_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()
