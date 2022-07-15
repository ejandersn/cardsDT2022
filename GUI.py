from email.mime import image
import pygame
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
        print("place holder")

    def start(self):
        pygame.init()
        running = True
        display_surface = pygame.display.set_mode((400, 400 ))
        card = pygame.image.load("/Users/eva/Desktop/cardsDT2022/card_images/2C.png")
        while running:
            for event in pygame.event.get():
                if(event.type == WINDOWCLOSE or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                    running = False
            screen = pygame.display.set_mode([800,800])
            screen.fill((255,255,255))
            screen.blit(card,(1,1))
            pygame.display.flip()
        pygame.quit()   
        
        
