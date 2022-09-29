import pygame
# from information import Label
from pathlib import Path


    



class cards(pygame.sprite.Sprite):
    def __init__(self,screen,card,position):
        pygame.sprite.Sprite.__init__(self)
        file = (card+'.png')
        path = ('/Users/eva/Desktop/cardsDT2022/card_images/'+file)
        if Path(path).is_file():
            pass
        else:
            print ("Special Card Input Error")
            exit()
        image = pygame.image.load(path)
        self.rect = image.get_rect()
        self.rect.left, self.rect.top = position
        xpos = self.rect.left
        ypos = self.rect.top
        screen.blit(image,self.rect)
        

class instructions(pygame.sprite.Sprite):
    def __init__(self, screen,language,position):
        pygame.sprite.Sprite.__init__(self)
        file = (language+'.png')
        path = ('/Users/eva/Desktop/cardsDT2022/'+file)
        image = pygame.image.load(path)
        self.rect = image.get_rect()
        self.rect.left, self.rect.top = position
        xpos = self.rect.left
        ypos = self.rect.top
        screen.blit(image,self.rect)