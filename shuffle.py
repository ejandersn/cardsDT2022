import random
import pygame
from display import cards
class Game:
    def __init__(self,game):
        self.game = game
    
    def decison(self,game):
        Arrange.fileHandler('',ask.game)
            
class Arrange:
    def fileHandler(self,game):
        with open(game+'.txt') as f:
            contents = f.read()
            shift = ([contents[i:i+2] for i in range(-1, len(contents), 2)])
            shift.pop(0) #try deck = shift.pop(0)
            # strArray = contents.split()
            # cards = shift.pop(0)
            Arrange.shuffle(shift)
            
    def shuffle(deck):
        random.shuffle(deck)
        input = 4 #temp replacment of another input
        Deal.hand(deck,(input+1))
        
class Deal:
    def hand(deck,players):
        ypos = 200
        for x in range(players):
            hand = (deck[((x-1)*13):(x*13)]) #note this range is only applicable to 4 peoople 
            a=0
            for i in hand:
                if a == 0:
                    ypos = ypos + 80
                card = i
                a = a+1
                screen = pygame.display.set_mode([800,800])
                cards(screen,card,[(50*a),ypos])
            
            
ask = Game(input('')) #this is a temp replacment of another input
Game.decison('','') #this will need to be called in main file

