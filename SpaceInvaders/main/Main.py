'''
Created on 10 jun. 2020
cool images in :https://opengameart.org/content/spaceship-building-kit
@author: crisisanchezp
'''
import pygame
from pygame.sprite import Group
from settings.Settings import Settings
from elements.SpaceShip import SpaceShip
from functionalities import GameFunctions as functions

def run_game():
    pygame.init()
    cats_invasion_settings = Settings()
    screen = pygame.display.set_mode((cats_invasion_settings.screen_width, cats_invasion_settings.screen_height))
    spaceship = SpaceShip(screen, cats_invasion_settings)
    bullets = Group()
    pygame.display.set_caption('Invasión Gatuna')
    while True:
        functions.check_events(spaceship, screen, cats_invasion_settings, bullets)
        spaceship.update()
        bullets.update()
        functions.update_screen(cats_invasion_settings, screen, spaceship, bullets)
                                    
def main():
    run_game()
if __name__ == '__main__':
    main()