'''
Created on 10 jun. 2020

@author: crisisanchezp
'''
import sys 
import pygame

def check_events():
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
def update_screen(cats_invasion_settings, screen, spaceship):
    screen.fill(cats_invasion_settings.background_color)
    spaceship.blitme() 
    
    pygame.display.flip()#muestra lo ultimo dibujado en pantalla