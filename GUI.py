from email.mime import image
import pygame
from display import cards
from shuffled import Game, Arrange, Deal
from pygame.fastevent import init
from pygame.locals import(
    KEYDOWN,
    K_ESCAPE,
    QUIT,
    MOUSEBUTTONDOWN,
    WINDOWCLOSE      
)

class display:
    def __init__(self):
        print()

    def start(self):
        ask = Game(input(''))
        Game.decison('','')
        pygame.init()
        running = True
        display_surface = pygame.display.set_mode((400, 400 ))
        while running:
            for event in pygame.event.get():
                if(event.type == WINDOWCLOSE or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                    running = False
            screen = pygame.display.set_mode([800,800])
            screen.fill((255,255,255))
            Deal.hand(deck,players,cards)

        pygame.quit()  