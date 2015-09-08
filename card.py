class Card:
    stringValue = '' #String value of card such as 2,Queen,King,Ace...etc
    intValue = 0
    isAce = False 
    suit = ''

    def __init__(self,suit,value):
        cardValues = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11} 
        self.stringValue = value
        self.suit = suit 
        self.intValue= cardValues[value]
        if value == "Ace": #check if card is an ace and set to true 
            self.isAce == True

    def __str__(self):
        return "%s of %s" % (self.stringValue,self.suit)
        
    def getValue(self): #return the value of the card
        return self.intValue

    def getSuit(self): #return the suit of the card
        return self.suit 


    def isAce(self): #return if the card is an ace
        return self.isAce

