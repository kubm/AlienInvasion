import sys

import pygame


def check_keydown(event, ship):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        print("up")
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        print("down")
        ship.moving_down = True


def check_keyup(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        print("not up")
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        print("not down")
        ship.moving_down = False


def check_events(ship):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)


def update_screen(settings, screen, ship):
    """ Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(settings.bg_color)
    ship.blitme()

    # Make the screen visible
    pygame.display.flip()
