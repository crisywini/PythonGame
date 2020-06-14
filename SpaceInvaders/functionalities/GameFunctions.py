'''
Created on 10 jun. 2020

@author: crisisanchezp
'''
import sys 
import pygame
from elements.Bullet import Bullet
from elements.AlienCat import AlienCat
from elements.Sounds import play_shot
from elements.Sounds import play_cat_mad


def check_keydown_events(event, spaceship, screen, cats_invasion_settings, bullets):
    if event.key == pygame.K_RIGHT:
        spaceship.moving_right = True
    if event.key == pygame.K_LEFT:
        spaceship.moving_left = True
    if event.key == pygame.K_SPACE:
        play_shot()
        fire_bullet(cats_invasion_settings, screen, spaceship, bullets)
    if event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, spaceship):
    if event.key == pygame.K_RIGHT:
        spaceship.moving_right = False
    if event.key == pygame.K_LEFT:
        spaceship.moving_left = False


def check_events(spaceship, screen, cats_invasion_settings, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, spaceship, screen, cats_invasion_settings, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spaceship)


def get_number_aliens_cats_x(cats_invasion_settings, alien_cat_width):
    available_space_x = cats_invasion_settings.screen_width - 2 * alien_cat_width
    number_aliens_x = int(available_space_x / (2 * alien_cat_width))
    return number_aliens_x


def create_alien(cats_invasion_settings, screen, aliens_cat, aliens_cat_number, row_number):
    alien = AlienCat(screen, cats_invasion_settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * aliens_cat_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens_cat.add(alien)
def check_bullet_cats_collisions(bullets, aliens_cat, cats_invasion_settings, screen, spaceship):
    collisions = pygame.sprite.groupcollide(bullets, aliens_cat, True, True)
    if(collisions):
        play_cat_mad()
    if len(aliens_cat) == 0:
        bullets.empty()
        create_fleet(cats_invasion_settings, screen, spaceship, aliens_cat)
def update_bullets(bullets, aliens_cat, cats_invasion_settings, screen, spaceship):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_cats_collisions(bullets, aliens_cat, cats_invasion_settings, screen, spaceship)

            
def fire_bullet(cats_invasion_settings, screen, spaceship, bullets):
    new_bullet = Bullet(screen, cats_invasion_settings, spaceship)
    bullets.add(new_bullet)


def get_number_rows(cats_invasion_settings, spaceship_height, alien_cat_height):
    available_space_y = (cats_invasion_settings.screen_height - (3 * alien_cat_height) - spaceship_height)
    number_rows = int(available_space_y / (2 * alien_cat_height))
    return number_rows

    
def create_fleet(cats_invasion_settings, screen, spaceship, aliens_cat):
    alien_cat = AlienCat(screen, cats_invasion_settings)
    number_aliens_cat_x = get_number_aliens_cats_x(cats_invasion_settings, alien_cat.rect.width)
    number_rows = get_number_rows(cats_invasion_settings, spaceship.rect.height, alien_cat.rect.height)
    for row in range(number_rows):
        for alien in  range(number_aliens_cat_x):
            create_alien(cats_invasion_settings, screen, aliens_cat, alien, row)


def update_screen(cats_invasion_settings, screen, spaceship, aliens_cat, bullets):
    screen.fill(cats_invasion_settings.background_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    spaceship.blitme() 
    aliens_cat.draw(screen)
    # alien_cat.blitme()
    
    pygame.display.flip()  # muestra lo ultimo dibujado en pantalla


def update_cat_aliens(cats_invasion_settings, cat_aliens, spaceship):
    check_fleet_edges(cats_invasion_settings, cat_aliens)
    cat_aliens.update()
    if pygame.sprite.spritecollideany(spaceship, cat_aliens):
        print('Ship hit')

    
def change_fleet_direction(cats_invasion_settings, aliens_cat):
    for alien in aliens_cat.sprites():
        alien.rect.y += cats_invasion_settings.fleet_drop_speed
    cats_invasion_settings.fleet_direction *= -1

    
def check_fleet_edges(cats_invasion_settings, aliens_cat):
    for alien in aliens_cat.sprites():
        if alien.check_edges():
            change_fleet_direction(cats_invasion_settings, aliens_cat)
            break
