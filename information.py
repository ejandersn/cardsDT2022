from tkinter import *
from tkinter import messagebox
import pygame

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 128)

class Labels:
    def player(screen,ypos,xpos):
        pygame.display.set_caption('Show Text')
        font = pygame.font.Font('freesansbold.ttf', 15)
        text = font.render(('Player'), True, black, white)
        textRect = text.get_rect()
        textRect.center = (800 // 2, 800 // 2)
        locationx = xpos
        locationy = ypos - 20
        screen.blit(text,(locationx,locationy))
        
    def power(screen):
            # value = value.decode("utf-8")
            # iteration = iteration.decode("utf-8")
            bro = ("Power cards:")
            pygame.display.set_caption('Show Text')
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render(bro, True, black, white)
            textRect = text.get_rect()
            textRect.center = (800 // 2, 800 // 2)
            locationx = 800
            locationy = 50
            screen.blit(text,(locationx,locationy))
            