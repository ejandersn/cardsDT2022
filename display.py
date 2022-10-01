import pygame
from pathlib import Path
import sys
import os


class Cards(pygame.sprite.Sprite):  # class for displaying cards
    def __init__(self, screen, card, position):
        pygame.sprite.Sprite.__init__(self)
        file = card + ".png"  # makes card value image path
        path = "/Users/eva/Desktop/cardsDT2022/card_images/" + file #replace path for machine
        if Path(path).is_file():  # if path exists continuie
            pass
        else:
            # if path doesnt exist reestart program
            print("Special Card Input Error")
            os.execl(sys.executable, sys.executable, *sys.argv)
        image = pygame.image.load(path)  # loads image with path
        self.rect = image.get_rect()
        self.rect.left, self.rect.top = position
        xpos = self.rect.left
        ypos = self.rect.top
        screen.blit(image, self.rect)  # renders image w/ position


class Instructions(pygame.sprite.Sprite):
    def __init__(self, screen, language, position):
        pygame.sprite.Sprite.__init__(self)
        file = language + ".png"  # makes language image path
        path = "/Users/eva/Desktop/cardsDT2022/" + file # replace path for machine
        image = pygame.image.load(path)  # loads image
        self.rect = image.get_rect()
        self.rect.left, self.rect.top = position
        xpos = self.rect.left
        ypos = self.rect.top
        screen.blit(image, self.rect)  # renders image at position
