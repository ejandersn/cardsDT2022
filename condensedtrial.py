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

class cards(pygame.sprite.Sprite):
    def __init__(self, width, height,screen):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('/Users/eva/Desktop/cardsDT2022/card_images/2C.png')
        self.rect = image.get_rect()
        self.rect.left, self.rect.top = [400,400]
        screen.blit(image,self.rect)  

class display:
    def __init__(self):
        print()

    def start(self):
        pygame.init()
        running = True
        display_surface = pygame.display.set_mode((400, 400 ))
        while running:
            for event in pygame.event.get():
                if(event.type == WINDOWCLOSE or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                    running = False
            screen = pygame.display.set_mode([800,800])
            screen.fill((255,255,255))
            cards(100,100,screen)
        pygame.quit()  
        
Begindisplay = display();
Begindisplay.start()