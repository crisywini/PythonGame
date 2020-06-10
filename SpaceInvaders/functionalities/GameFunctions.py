'''
Created on 10 jun. 2020

@author: crisisanchezp
'''
import sys 
import pygame
from elements.Bullet import Bullet

def check_keydown_events(event, spaceship, screen, cats_invasion_settings, bullets):
    if event.key == pygame.K_RIGHT:
        spaceship.moving_right = True
    if event.key == pygame.K_LEFT:
        spaceship.moving_left = True
    if event.key == pygame.K_SPACE:
        new_bullet = Bullet(screen, cats_invasion_settings, spaceship)
        bullets.add(new_bullet)
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


def update_screen(cats_invasion_settings, screen, spaceship, bullets):
    screen.fill(cats_invasion_settings.background_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    spaceship.blitme() 
    
    pygame.display.flip()  # muestra lo ultimo dibujado en pantalla
    
    
