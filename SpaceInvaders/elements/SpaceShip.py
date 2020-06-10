'''
Created on 10 jun. 2020

@author: crisisanchezp
'''
import pygame 


class SpaceShip():

    def __init__(self, screen, cats_invasion_settings):
        self.screen = screen
        self.cats_invasion_settings = cats_invasion_settings
        
        self.image = pygame.image.load('../images/spaceShip1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.center = float(self.rect.centerx)  # Para guardar un decimal de la posición de la nave
        
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            
            self.rect.centerx += self.cats_invasion_settings.spaceship_speed_factor
            #print(self.rect.centerx)
        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.cats_invasion_settings.spaceship_speed_factor
            #print(self.rect.centerx)
        #self.rect.centerx = self.center  # Ubica el rectangulo de la nave en el centro

    def blitme(self):
        '''
        Pygame method blit() to draw the image.
        '''
        self.screen.blit(self.image, self.rect)
