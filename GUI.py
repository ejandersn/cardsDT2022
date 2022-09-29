import pygame
from display import instructions
from shuffle import Arrange, Deal, SpecialCards
from tkinter import *
from pygame.locals import(
    KEYDOWN,
    K_ESCAPE,
    WINDOWCLOSE,
    K_s,
    K_p,
    K_1,
    K_2,
    K_w
)

class display:
    

        
    def players():
        pass

    def start(self):
        green = (0, 255, 0)
        blue = (0, 0, 128)
        asklang = input('english or māori? ')
        language = 'english'
        
        pygame.init()
        running = True
        display_surface = pygame.display.set_mode((800, 800))
        
        x = 0
        deck = []
        special_list = []
        while running:
            a = 0
            x = x + 1
            for event in pygame.event.get(): #make better
                if(event.type == WINDOWCLOSE or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                    running = False
                if (event.type == KEYDOWN and event.key == K_s):
                    deck = Arrange.fileHandler('deck52')
                    shuffle = Arrange.shuffle(deck)
                if (event.type == KEYDOWN and event.key == K_p):
                    players = int(input('Number of Players:'))
                if (event.type == KEYDOWN and event.key == K_1): #snap
                    players = 2
                    special_cards = ('')
                    special_list = SpecialCards.makeList(special_cards)
                if (event.type == KEYDOWN and event.key == K_2): #bridge
                    players = 4 
                    special_cards = ('ACKCQCJCASKSQSJSADKDQDJDAHKHQHJH')
                    special_list = SpecialCards.makeList(special_cards)
                if (event.type == KEYDOWN and event.key == K_w):
                    special_cards = input('Please enter all special cards in the format 4H 6C') 
                    special_list = SpecialCards.makeList(special_cards)
                    
                        
                    
            screen = pygame.display.set_mode([1200,800])
            screen.fill((255,255,255))
            
            if x == 1:              
                if asklang == 'maori' or asklang == 'māori' or asklang == 'tereo' or asklang == 'te reo':
                    language = 'tereo'
                else:
                    language = 'english'
                ask = input('Custom Game (y/n)')
                if ask == 'y':
                    players = int(input('Number of Players:'))
                else:
                    game = input('Bridge or Snap')
                    if game == 'bridge':
                        players = 4
                        special_cards = ('ACKCQCJCASKSQSJSADKDQDJDAHKHQHJH')
                        special_list = SpecialCards.makeList(special_cards)
                        #put in special cards automatically
                    elif game == 'snap':
                        players = 2
                        special_cards = ('')
                        special_list = SpecialCards.makeList(special_cards)
                    else:
                        players = int(input('Number of Players:'))
            instructions(screen,language,(750,375))
            Deal.hand(screen,deck,players)
            SpecialCards.deal(special_list,screen)
            pygame.display.update()

        pygame.quit()  