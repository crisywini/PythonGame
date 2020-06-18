'''
Created on 14 jun. 2020

@author: crisisanchezp
'''
class GameStats():
    
    def __init__(self, cats_invasion_settings):
        self.cats_invasion_settings =cats_invasion_settings
        
        self.game_active = False
        self.reset_stats()
    def reset_stats(self):
        self.ships_left = self.cats_invasion_settings.spaceship_limit