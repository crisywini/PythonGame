'''
Created on 10 jun. 2020

@author: crisisanchezp
'''


class Settings():
    '''
    This class is needed to add some functionalities of the game
    '''

    def __init__(self):
        '''
        Init method of Settings
        '''
        self.screen_width = 1200
        self.screen_height = 700
        self.background_color = (230, 230, 230)
        
        self.spaceship_speed_factor = 2 #La nave se mueve 1.5 pixeles en vez de 1 pixel
        
        self.bullet_speed_factor = 1
        self.bullet_width = 7
        self.bullet_height = 20
        self.bullet_color = 60, 60, 60
