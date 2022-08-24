deck = ['TH', '4C', '3S', 'JC', '4S', 'JD', '3D', 'AC', 'AS', '4D', '2D', 'TD', '5C', '2H', '9H', 'AD', '8H', 'AH', 'QS', '8D', '7D', '7C', 'TC', 'KH', '2C', '6H', 'KC', 'QD', '7S', '5H', '8S', 'KD', 'QC', '4H', '7H', 'TS', '9S', 'JS', '2S', '6S', '3H', '9D', 'QH', '5S', '3C', 'KS', '8C', '5D', '9C', 'JH', '6D', '6C']

class Deal:

    def hand(deck,players):
        for x in range(players):
            hand = (deck[((x-1)*13):(x*13)])
            print(hand)
        
input = 4
Deal.hand(deck,(input+1))
