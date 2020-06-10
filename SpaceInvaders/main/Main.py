'''
Created on 10 jun. 2020

@author: crisisanchezp
'''
import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 700))
    pygame.display.set_caption('Invasión gatuna')
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        pygame.display.flip()
                                    
def main():
    run_game()
if __name__ == '__main__':
    main()