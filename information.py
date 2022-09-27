from tkinter import *
from tkinter import messagebox
import pygame

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 128)


class Instructions:
    def english_message():
        messagebox.showinfo('Players','Answer quetions in terminal')
        messagebox.showinfo('Shuffle','To shuffle/display deck press S')
        messagebox.showinfo('Players','To enter a new number of players press P')
        messagebox.showinfo('Automated Games','To play automated game Snap press 1')
        messagebox.showinfo('Automated Games','To play automated game Bridge press 2')
        
    def māori_message():
        messagebox.showinfo('Players','Whakautua nga patai kei te tauranga')
        messagebox.showinfo('Shuffle','Hei riwhi/whakaatu i te rahoraho pehia S')
        messagebox.showinfo('Players','Hei whakauru i te nama hou o nga kaitakaro pehia te P')
        messagebox.showinfo('Automated Games','Hei purei kemu aunoa Snap perehi 1')
        messagebox.showinfo('Automated Games','Ki te purei keemu aunoa Bridge perehi 2')
        
class Labels:
    def __init__(self,screen,iteration,ypos,xpos):
        pygame.display.set_caption('Show Text')
        font = pygame.font.Font('freesansbold.ttf', 15)
        text = font.render(('Player'), True, black, white)
        textRect = text.get_rect()
        textRect.center = (800 // 2, 800 // 2)
        locationx = xpos
        locationy = ypos - 20
        screen.blit(text,(locationx,locationy))