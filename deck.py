from card import Card
from random import shuffle

class Deck:
    deck = []
        
    #Create a card for each with each suit and value and then insert it into the deck 
    def __init__(self):
        suits = ['Spades','Hearts','Clubs','Diamonds'] 
        values = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
        for s in suits:
            for v in values:
                card = Card(s,v)
                self.deck.append(card) 
    
    #return the deck
    def getDeck(self):
        return self.deck            

    #shuffle the deck
    def shuffle(self):
        shuffle(self.deck)
    
    #draw a card from the deck
    def drawCard(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        elif len(self.deck) <= 0:
            self.__init__()
            return self.deck.pop()
        

