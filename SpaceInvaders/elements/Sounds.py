'''
Created on 14 jun. 2020
to sounds: https://freesound.org/people/jobro/sounds/35684/
@author: crisisanchezp
'''
import pygame
def load_sounds():
    sounds = []
    sounds.append(pygame.mixer.Sound('../resources/sounds/shot.wav'))
    return sounds

def play_shot():
    shot = pygame.mixer.Sound('../resources/sounds/shot.wav')
    shot.play()
    
def play_cat_mad():
    cat = pygame.mixer.Sound('../resources/sounds/catMad.wav')
    cat.play()
def play_spaceship_explosion():
    explosion = pygame.mixer.Sound('../resources/sounds/spaceShipExplosion.wav')
    explosion.play()
    
def play_soundtrack():
    soundtrack = pygame.mixer.Sound('../resources/sounds/fondoCats2.wav')
    soundtrack.play(1)
    
    
    
    
    