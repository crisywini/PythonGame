'''
Created on 10 jun. 2020

@author: crisisanchezp
'''
import pygame 


class SpaceShip():

    def __init__(self, screen):
        self.screen = screen
        
        self.image = pygame.image.load('../images/spaceShip1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''
        Pygame method blit() to draw the image.
        '''
        self.screen.blit(self.image, self.rect)
