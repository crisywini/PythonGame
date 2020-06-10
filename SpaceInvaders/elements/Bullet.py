'''
Created on 10 jun. 2020

@author: crisisanchezp
'''
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    
    def __init__(self, screen, cats_invasion_settings, spaceship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, cats_invasion_settings.bullet_width,
                                cats_invasion_settings.bullet_height)
        
        self.rect.centerx = spaceship.rect.centerx
        self.rect.top = spaceship.rect.top
        
        self.y = float(self.rect.y)
        
        self.color = cats_invasion_settings.bullet_color
        self.speed_factor = cats_invasion_settings.bullet_speed_factor
    def update(self):
        self.y -= self.speed_factor 
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
        
        
        
        
        
        
        
        
        
        