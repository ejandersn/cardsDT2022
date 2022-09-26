from email.mime import image
import pygame
from display import cards
from shuffle import Game, Arrange, Deal
from pygame.fastevent import init
from pygame.locals import(
    KEYDOWN,
    K_ESCAPE,
    QUIT,
    MOUSEBUTTONDOWN,
    WINDOWCLOSE,
    K_d,
    K_0,
    K_s
       
)

class display:
    def __init__(self):
        print()

    def start(self):
        pygame.init()
        running = True
        display_surface = pygame.display.set_mode((400, 400 ))
        x = 0
        deck = []
        while running:
            x = x + 1
            for event in pygame.event.get():
                if(event.type == WINDOWCLOSE or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                    running = False
                if (event.type == KEYDOWN and event.key == K_s):
                    deck = Arrange.fileHandler('deck52')
                    shuffle = Arrange.shuffle(deck)
                    
            screen = pygame.display.set_mode([800,800])
            screen.fill((255,255,255))
            Deal.hand(screen,deck)


        pygame.quit()  