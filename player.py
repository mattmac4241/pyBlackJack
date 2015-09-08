
'''Player class represents a player for the game 
and contains the hand that the user has and the score
also has special type dealer'''

class Player():
    score = 0 #the players hand score
    hand = [] #contains the hand of the player
    isDealer = False

    #setup player declaring if they are a dealer or not, dealer is the computer and the player is not
    def __init__(self,isDealer):
        self.isDealer = isDealer
    
    #used for the inital hand dealt 
    def deltHand(self,card1,card2):         
        self.hand.append(card1)
        self.hand.append(card2)
        self.score += card1.getValue() + card2.getValue()
    
    #delt new card
    def deltCard(self,card):
        self.hand.append(card)
        self.score += card.getValue()

    #return the player's score
    def getValue(self):
        return self.score()



