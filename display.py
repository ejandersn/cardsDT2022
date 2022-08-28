import pygame
class Display(pygame.sprite.Sprite):
    def __init__(self, width, height,screen):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('/Users/eva/Desktop/cardsDT2022/card_images/KS.png')
        self.image = pygame.Surface([10,10])
        # self.rect.left, self.rect.top = [50,50]
        self.rect = image.get_rect()
        screen.blit(self.image,self.rect)  