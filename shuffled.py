from textwrap import wrap
import random
import pygame
from display import cards

class Game:
    def decison(game):
        Arrange.fileHandler('',game)

class Arrange:
    def fileHandler(self,game):
        with open(game+'.txt', "r", encoding='utf-8-sig') as f:
            contents = f.read()
            deck =  contents
            deck = wrap(deck,2)
            # print (deck)
            Arrange.shuffle(deck)
    
    def shuffle(deck):
        random.shuffle(deck)
        players = 4 #needs input replacment/mod as 4 = 1,5
        
        Deal.hand(deck,players)
        
class Deal:
    def hand(deck,players):
        ypos = 100
        xpos = 50 
        a = 0
        for x in deck[0:13]:
           card = x
           a = a + 1
           screen = pygame.display.set_mode([800,800])
           cards(screen,card,[(xpos*a),ypos])
        a = 0
        for x in deck[13:26]:
            ypos = 180
            card = x
            a = a + 1
            screen = pygame.display.set_mode([800,800])
            cards(screen,card,[(xpos*a),ypos])
        a = 0
        for x in deck[26:39]:
            ypos = 260
            card = x
            a = a + 1
            screen = pygame.display.set_mode([800,800])
            cards(screen,card,[(xpos*a),ypos])
        a = 0
        deck.insert(53,'bk')
        print (deck)
        b = 1
        i = 0 
        for x in deck[39:53]:
            i = i + 1
            ypos = 340
            card = x
            a = a + 1
            screen = pygame.display.set_mode([800,800])
            cards(screen,card,[(xpos*a),ypos])
            
        
            
            
           
     
         #    if a == 14:
        #        ypos = ypos + 80
        #        a = 0
     
     
        # for x in range(1,5):
        #     hand = (deck[((x-1)*13):(x*13)]) #note this range is only applicable to 4
        #     for x in hand:
        #         card = x

              
              
              
              
              
              
              
              
              
              
              
                
    def display():
         pass       
            
            # print(hand)
            # a=0
            # ypos = 200
            # for i in hand:
            #     if a == 0:
            #         ypos = ypos + 80
            #     card = i
            #     a = a+1
            #     screen = pygame.display.set_mode([800,800])
            #     cards(screen,card,[(50*a),ypos])   
   
        
            
        
            
            
            
ask = Game.decison('deck52')








