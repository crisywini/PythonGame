'''
Created on 10 jun. 2020
cool images in :https://opengameart.org/content/spaceship-building-kit
@author: crisisanchezp
'''
import pygame
from pygame.sprite import Group
from settings.Settings import Settings
from elements.SpaceShip import SpaceShip
from elements.AlienCat import AlienCat
from functionalities import GameFunctions as functions
from functionalities.GameStats import GameStats 
from elements.Button import Button
from elements.Sounds import play_soundtrack

def run_game():
    pygame.init()
    cats_invasion_settings = Settings()
    screen = pygame.display.set_mode((cats_invasion_settings.screen_width, cats_invasion_settings.screen_height))
    spaceship = SpaceShip(screen, cats_invasion_settings)
    # alien_cat = AlienCat(screen, cats_invasion_settings)
    bullets = Group()
    aliens_cat = Group()
    pygame.display.set_caption('Invasión Gatuna')
    
    play_button = Button(screen, cats_invasion_settings, 'Jugar')
    stats = GameStats(cats_invasion_settings)
    
    
    functions.create_fleet(cats_invasion_settings, screen, spaceship, aliens_cat)
    play_soundtrack()
    while True:
        functions.check_events(spaceship, screen, cats_invasion_settings, bullets, stats, play_button, aliens_cat)
        if stats.game_active:
            spaceship.update()
            functions.update_bullets(bullets, aliens_cat, cats_invasion_settings, screen, spaceship)
            functions.update_cat_aliens(cats_invasion_settings, stats, aliens_cat, spaceship, screen, bullets)
            
        functions.update_screen(cats_invasion_settings, screen, spaceship, aliens_cat, bullets, stats, play_button)

                                    
def main():
    run_game()


if __name__ == '__main__':
    main()
