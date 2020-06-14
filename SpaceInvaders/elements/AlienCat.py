'''
Created on 10 jun. 2020

@author: crisisanchezp
'''
import pygame
from pygame.sprite import Sprite


class AlienCat(Sprite):

    def __init__(self, screen, cats_invasion_settings):
        super(AlienCat, self).__init__()
        self.screen = screen
        self.cats_invasion_settings = cats_invasion_settings
        
        self.image = pygame.image.load('../images/alienCat.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = 0
        self.rect.y = 0
        
        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.cats_invasion_settings.alien_cat_speed_factor * 
                   self.cats_invasion_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
            
            
