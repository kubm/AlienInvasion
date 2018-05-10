import sys
from time import sleep
from bullet import Bullet
from alien import Alien
import pygame


def check_keydown(event, settings, screen, ship, bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset game speed
        settings.initialize_dynamic_settings()
        # Hide mouse cursor
        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True

        # Reset scoreboard
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(settings, screen, ship, aliens)
        ship.center_ship


def update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """ Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(settings.bg_color)

    # Redraw all the bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Draw the score
    sb.show_score()

    # Draw the button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # Make the screen visible
    pygame.display.flip()


def check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets):
    # Check for any bullets that have hit alien ships
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()

        # Increase level
        stats.level += 1
        sb.prep_level()

        create_fleet(settings, screen, ship, aliens)


def update_bullets(settings, screen, stats, sb, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets"""
    bullets.update()

    # Deleting bullets that disappeared from screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets)


def get_number_aliens_x(settings, alien_width):
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(settings, screen, aliens, alien_number, row_number):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(settings, ship_height, alien_height):
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_fleet(settings, screen, ship, aliens):
    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    # Create fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.drop_speed
    settings.fleet_direction *= -1


def ship_hit(settings, stats, screen, ship, aliens, bullets, sb):
    if stats.ships_left > 0:
        # Reduce number of player ships
        stats.ships_left -= 1

        # Update scoreboard
        sb.prep_ships()

        # Emty the bullets and aliens lists
        aliens.empty()
        bullets.empty()

        # Re create fleet and re-center the ship
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        # Pause for a moment
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(settings, stats, screen, ship, aliens, bullets, sb):
    check_fleet_edges(settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets, sb)

    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets, sb)


def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets, sb):
    """ Check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, aliens, bullets, sb)
            break


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
