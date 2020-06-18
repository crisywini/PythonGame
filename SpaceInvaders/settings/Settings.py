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
        self.background_color = (70, 98, 140)
        
        self.spaceship_limit = 3
        
        self.bullet_width = 7
        self.bullet_height = 20
        self.bullet_color = 60, 60, 60
        
        self.fleet_drop_speed = 10
        
        
        self.speed_up_scale = 1.1
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        self.spaceship_speed_factor = 2 #La nave se mueve 1.5 pixeles en vez de 1 pixel
        self.bullet_speed_factor = 5
        self.alien_cat_speed_factor = 1
        #Fleet direction 1 -> right -1 -> left
        self.fleet_direction = 1
    def increase_speed(self):
        self.spaceship_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_cat_speed_factor *= self.speed_up_scale
