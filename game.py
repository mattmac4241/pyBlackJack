from deck import Deck
from player import Player

'''The game of blackjack, two users(one player the other the dealer)
if the player goes over 21 they lose, if the player stays under 22 and 
is greater then the dealer or the dealer goes over 21, then the user wins. 
If the dealer and player tie then it's a push and no one loses.'''


class Game(object):

    def __init__(self):
        print "Hello, welcome to blackjack what is your name?"
        name = raw_input()
        self.player1 = Player(name,False) #Initialize the user
        self.dealer = Player('Dealer',True)
        self.deck = Deck() #Inititalize the deck
        self.game()  
      
    def game(self):
        self.deal(self.player1) #deal cards to player1
        self.deal(self.dealer) #deal cards to dealer
        self.hitOrStand(self.player1)
        if self.busted(self.player1) == False:
            self.dealerStandOrHit(self.dealer)   
        
            if(self.busted(self.dealer) == False):
                self.checkWinner()
            else:
                print "DEALER BUSTED YOU WON!"


    #deal out two cards to a player
    def deal(self,player):
        for i in range(2):
            self.dealCard(player)
            if (player.getScore() == 21)and (player.isDealer() == False):
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
            return
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

    #dealer hits on less then 17
    def dealerStandOrHit(self,player):
        if player.getScore() < 17:
            self.dealCard(player)



game = Game()
