'''
Created on 10 jun. 2020
cool images in :https://opengameart.org/content/spaceship-building-kit
@author: crisisanchezp
'''
import sys
import pygame
from settings.Settings import Settings
from elements.SpaceShip import SpaceShip
def run_game():
    pygame.init()
    cats_invasion_settings = Settings()
    screen = pygame.display.set_mode((cats_invasion_settings.screen_width, cats_invasion_settings.screen_height))
    spaceship = SpaceShip(screen)
    pygame.display.set_caption('Invasión Gatuna')
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        screen.fill(cats_invasion_settings.background_color)
        spaceship.blitme()
        pygame.display.flip()
                                    
def main():
    run_game()
if __name__ == '__main__':
    main()