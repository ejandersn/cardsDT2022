
class Decision:
    def __init__(self,game):
        self.game = game
    
    def analysis(self,game):
        if ask.game == 'bridge':
            print('here')
            deck = Standard.fileHandler()
            
class Standard:
    def __init__(self):
        print()
   
    def fileHandler():
        with open('deck51.txt') as f:
            contents = f.read()
            spades = (contents[1:27])
            hearts = (contents[27:53])
            diamonds = (contents[53:79])
            clubs = (contents[79:105])
            print(clubs)
            
ask = Decision(input(''))
Decision.analysis('','')
print(ask.game)