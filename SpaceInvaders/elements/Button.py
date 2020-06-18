'''
Created on 14 jun. 2020

@author: crisisanchezp
'''
import pygame.font


class Button():
    
    def __init__(self, screen, cats_invasion_settings, message):
        self.screen = screen
        self.cats_invasion_settings = cats_invasion_settings
        self.message = message
        
        self.screen_rect = self.screen.get_rect()
        
        self.width, self.height = 200, 50
        
        self.button_colour = (0, 255, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        self.prep_message(message)

    def prep_message(self, message):
        '''
        Put the message as an Image on the button
        '''
        self.message_image = self.font.render(message, True, self.text_colour, self.button_colour)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center
    def draw_button(self):
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect) 
