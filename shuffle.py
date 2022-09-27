from textwrap import wrap
import random
import pygame
from display import cards
from information import Instructions, Labels

class Arrange:
    def fileHandler(game):
        with open(game+'.txt', "r", encoding='utf-8-sig') as f:
            contents = f.read()
            deck =  contents
            deck = wrap(deck,2)
            return deck
    
    def shuffle(deck):
        random.shuffle(deck)
        return deck
        
class Deal:
    def hand(screen,deck,input):
        if input < 5:
            players = input + 1 #needs input replacment
        else:
            exit()

        num = len(deck)  #replace with user input for boundary testing
        card_num = int(num/input)
        ypos = 100
        xpos = 50 
        for x in range (players):
            hand = deck[((x-1)*card_num):(x*card_num)]
            length = len(hand)
            hand.insert(length + 1,'bk')
            iteration = x
            if players == 5:
                if iteration == 2:
                        ypos = 300
                elif iteration == 3:
                        ypos = 500
                if iteration == 4:
                        ypos = 700
            if players == 4:
                if iteration == 2:
                        ypos = 350
                elif iteration == 3:
                        ypos = 550 
            if players == 3:
                if iteration == 2: 
                    ypos = 500
            b = 0
            a = 0
            for x in hand:
                if a == 1 and b < 12:
                    Labels(screen,iteration,ypos,xpos)
                card = x
                if length > 14:
                    if a > 12:
                        ypos = ypos + 100 #between row same player split
                        a = 0
                b = b + 1
                a = a + 1
                cards(screen,card,[(xpos*a),ypos])


