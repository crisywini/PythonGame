'''
Created on 10 jun. 2020

@author: crisisanchezp
'''
import pygame
from pygame.sprite import Sprite

class AlienCat(Sprite):
    def __init__(self,  screen, cats_invasion_settings):
        super(AlienCat, self).__init__()
        self.screen = screen
        self.cats_invasion_settings = cats_invasion_settings
        
        self.image = pygame.image.load('../images/alienCat.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = 0
        self.rect.y = 0
        
        self.x = float(self.rect.x)
    def blitme(self):
        self.screen.blit(self.image, self.rect)