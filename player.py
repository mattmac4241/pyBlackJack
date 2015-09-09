
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
    def __str__(self):
        return self.name

    #used for the inital hand dealt 
    def dealtHand(self,card1,card2):         
        self.hand.append(card1)
        self.hand.append(card2)
        self.score += card1.getValue() + card2.getValue()
    
    #delt new card
    def dealtCard(self,card):
        self.hand.append(card)
        self.score += card.getValue()
        if self.isDealer == False:
            print 'You were dealt a %s' % card 
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
