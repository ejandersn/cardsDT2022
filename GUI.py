import pygame
from shuffle import Arrange, Deal
from tkinter import *
from information import Instructions
from pygame.locals import(
    KEYDOWN,
    K_ESCAPE,
    WINDOWCLOSE,
    K_s,
    K_p,
    K_1,
    K_2
)

class display:
    

        
    def players():
        pass

    def start(self):
        green = (0, 255, 0)
        blue = (0, 0, 128)
        language = input('english or māori? ')
        
        if language == 'maori' or language == 'māori':
            Instructions.māori_message()
        else:
            Instructions.english_message()
        
        pygame.init()
        Tk().wm_withdraw()
        running = True
        display_surface = pygame.display.set_mode((800, 800))
        
        x = 0
        deck = []
        while running:
            a = 0
            x = x + 1
            for event in pygame.event.get():
                if(event.type == WINDOWCLOSE or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                    running = False
                if (event.type == KEYDOWN and event.key == K_s):
                    deck = Arrange.fileHandler('deck52')
                    shuffle = Arrange.shuffle(deck)
                if (event.type == KEYDOWN and event.key == K_p):
                    players = int(input('Number of Players:'))
                if (event.type == KEYDOWN and event.key == K_1):
                    players = 2
                if (event.type == KEYDOWN and event.key == K_2):
                    players = 4          
                    
            screen = pygame.display.set_mode([800,800])
            screen.fill((255,255,255))
            # display_surface.blit(text, textRect)
            if x == 1:
                ask = input('Custom Game (y/n)')
                if ask == 'y':
                    players = int(input('Number of Players:'))
                else:
                    game = input('Bridge or Snap')
                    if game == 'bridge':
                        players = 4
                    elif game == 'snap':
                        players = 2
                    else:
                        players = int(input('Number of Players:'))
            Deal.hand(screen,deck,players)
            pygame.display.update()

        pygame.quit()  