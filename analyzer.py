import random
class Decision:
    def __init__(self,game):
        self.game = game
    
    def game_decison(self,game):
        if ask.game == 'bridge':
            deck = Standard.fileHandler()
            
class Standard:
    def __init__(self):
        print()
   
    def fileHandler():
        with open('deck52.txt') as f:
            contents = f.read()
            n = 2
            shift = ([contents[i:i+n] for i in range(-1, len(contents), n)])
            shift.pop(0) #deletes first item in list
            random.shuffle(shift)
            if ask.game == 'bridge':
                print()
                
            print(shift) #delete 

            
ask = Decision(input(''))
Decision.game_decison('','')
print(ask.game)