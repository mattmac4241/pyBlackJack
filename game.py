from deck import Deck
from player import Player

'''The game of blackjack, two users(one player the other the dealer)
if the player goes over 21 they lose, if the player stays under 22 and 
is greater then the dealer or the dealer goes over 21, then the user wins. 
If the dealer and player tie then it's a push and no one loses.'''


class Game:
    deck = None
    player1 = None
    dealer = None 

    def __init__(self):
        print "Hello, welcome to blackjack what is your name?"
        name = raw_input()
        self.player1 = Player(name,False) #Initialize the user
        self.dealer = Player('Dealer',True)  #Initialize the dealer
        self.deck = Deck() #Inititalize the deck
        print 'Hello %s, let\'s play Blackjack' % self.player1.getName()
        print self.dealer.getName()
        self.deal(self.player1) #deal cards to player1
        self.deal(self.dealer) #deal cards to dealer
        self.hitOrStand(self.player1)
    #deal out two cards to a player
    def deal(self,player):
        for i in range(2):
            self.dealCard(player)
            if (player.score == 21) and (player.isDealer == False):
                print 'BLACKJACK! YOU WIN!'

    #check if player score is greater then 21
    def busted(self,player):
        if player.score >21:
            return True
        else:
            return False

    #deal an individual card
    def dealCard(self,player):
        card = self.deck.drawCard()
        player.dealtCard(card)
        
    #Ask the player if they want to hit or stand
    def hitOrStand(self,player):
        print "Would you like to Hit or Stand?" 
        answer = raw_input()
        if answer.lower() == 'stand':
            self.checkWinner() 
        else:    
            self.dealCard(player)
            #Check if player busted after dealing card
            if self.busted(player) == False: 
                self.hitOrStand(player)
            else:       
                print "BUSTED!! YOU LOOSE!!"
    
    #check which player won
    def checkWinner(self):
        print self.dealer.strHand()
        pScore = self.player1.score #player's score
        dScore = self.dealer.score  #dealer's score
        if pScore > dScore:
            print "YOU WIN!!!!"
        elif pScore < dScore:
            print 'Sorry,You loose!'
        else:
            print "PUSH! It's a tie!"

game = Game()
