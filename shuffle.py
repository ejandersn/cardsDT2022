from textwrap import wrap
import random
import pygame
from display import cards, powercards
from information import  Labels

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
        for i in range (players):
            hand = deck[((i-1)*card_num):(i*card_num)]
            length = len(hand)
            hand.insert(length + 1,'bk')
            iteration = i
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
            for z in hand:
                card = z
                if a == 1 and b < 12:
                    Labels.player(screen,ypos,xpos)
                if length > 14:
                    if a > 12:
                        ypos = ypos + 100 #between row same player split
                        a = 0
                b = b + 1
                a = a + 1
                cards(screen,card,[(xpos*a),ypos])
                
class SpecialCards:
    def makeList(input):
        input = str(input)
        remove_space = input.replace(' ','')
        special_list = wrap(remove_space,2)
        length = len(special_list)
        special_list.insert(length + 1,'bk')
        return special_list
    
    def deal(list,screen):
        a = 0
        b = 0
        ypos = 100
        xpos = 750
        length = len(list)
        Labels.power(screen)
        for x in list:
            b = b + 1
            if length > 6:
                if b == 9:
                    ypos = 200
                    a = 0
                if b == 18:
                    ypos = 300
                    a = 0
            card = x
            cards(screen,card,[(xpos + a),ypos])
            a = a + 50
            
            



