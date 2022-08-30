import pygame

class cards(pygame.sprite.Sprite):
    def __init__(self,screen,card,position):
        pygame.sprite.Sprite.__init__(self)
        file = (card+'.png')
        path = ('/Users/eva/Desktop/cardsDT2022/card_images/'+file)
        image = pygame.image.load(path)
        self.rect = image.get_rect()
        self.rect.left, self.rect.top = position
        screen.blit(image,self.rect)  
