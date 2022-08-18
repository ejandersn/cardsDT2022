import random

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
            shift.pop(0) #deletes first item in list
            random.shuffle(shift)
            print(shift) #delete 

            
ask = Game(input('')) #this is a temp replacment of another input
Game.decison('','') #this will need to be called in main file
