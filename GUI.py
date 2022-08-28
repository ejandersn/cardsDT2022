from email.mime import image
from display import Display

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
    def start(self):
        pygame.init()
        display_surface = pygame.display.set_mode((400, 400 ))
        screen = pygame.display.set_mode([800,800])
        running = True
        while running:
            for event in pygame.event.get():
                if(event.type == WINDOWCLOSE or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                    running = False
            screen.fill((255,255,255))
            Display(100,100,screen) 
                     
        pygame.quit()   