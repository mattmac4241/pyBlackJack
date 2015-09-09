'''Player class represents a player for the game 
and contains the hand that the user has and the score
also has special type dealer'''

class Player():
   # score = 0 #the players hand score
   # hand = [] #contains the hand of the player
   # name = '' #The player's name
   # isDealer = False
    #setup player declaring if they are a dealer or not, dealer is the computer and the player is not
    def __init__(self,name,isDealer):
        self.hand = []
        self.score = 0
        self.name = name    
        self.isDealer = isDealer
        self.hasAce = False
    def __str__(self):
        return self.name

    def dealtCard(self,card):

        if card.isAce() == True:
            self.hasAce = True    
        self.hand.append(card)
        score = self.score + card.getValue()
        if score > 21 and self.hasAce == True:
            self.hasAce = False
            self.score -= 10
        self.score += card.getValue() 
        if self.isDealer == False:
            print 'You were dealt a %s' % card 
            print 'Your score is %s' % str(self.score)
    #return the player's score
    def getScore(self):
        return self.score

    def strHand(self):
        cards = ''
        for i in self.hand:
            cards += i.__str__() + ', '
        return "%s was dealt %s" % (self.name,cards)
    
    def getName(self):
        return self.name

    #return the players hand
    def getHand(self):
        return self.hand

    def isDealer(self):
        print self.isDealer
        return self.isDealer

    def hasAce(self):
        return self.hasAce
