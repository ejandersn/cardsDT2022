from textwrap import wrap
import random
import pygame
from display import cards

class Game:
    def decison(game,screen):
        Arrange.fileHandler('',game,screen)

class Arrange:
    def fileHandler(self,game,screen):
        with open(game+'.txt', "r", encoding='utf-8-sig') as f:
            contents = f.read()
            deck =  contents
            deck = wrap(deck,2)
            Arrange.shuffle(screen,deck)
    
    def shuffle(screen,deck):
        random.shuffle(deck)
        # print (deck)
        input = 4 #mod input
        if input == 4:
            players = 5 #needs input replacment
        num = len(deck) #replace with user input for boundary testing
        card_num = int(num/input)
        Deal.hand(screen,deck,players,card_num)
        
class Deal:
    def hand(screen,deck,players,card_num):
        ypos = 100
        xpos = 50 
        for x in range (players):
            hand = deck[((x-1)*card_num):(x*card_num)]
            hand.insert(14,'bk')
            iteration = x
            a = 0
            for x in hand:
                card = x
                if iteration == 2:
                    ypos = 180
                elif iteration == 3:
                    ypos = 260
                if iteration == 4:
                    ypos = 340
                a = a + 1
                # screen = pygame.display.set_mode([800,800])
                cards(screen,card,[(xpos*a),ypos])

                









