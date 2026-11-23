import random
playing = False
# min amount to bet
buyin_min = 1000
buyin_min = int(input("Enter buy-in amount: "))
print("Your bet amount is: ",buyin_min)
bet = 1
# game message
restart_msg = "Press d to deal again / Press q to quit"
# game card suits
game_suits = ("H", "D", "S", "C")
# game card order
card_ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
# game card values
card_vals = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

# card class for game cards
class Card:
    # initialize constructor for new card
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    # method for card representation
    def __str__(self):
        return self.suit + self.rank
    # method to get card suit
    def getCardSuit(self):
        return self.suit
    # method to get card rank
    def getCardRank(self):
        return self.rank
    # method to show the card
    def drawCard(self):
        print(self.suit + self.rank)

# class for player game hand
class Hand:
    # initialize constructire for empty hand
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False
    # method for styling player hand
    def __str__(self):
        hand = ""
        # iterate each card and append name to hand 
        for card in self.cards:
            card_name = card.__str__()
            hand += " " +card_name
        return "Player hand %s" %hand
    # method to card card to player hand
    def addCard(self, card):
        # add card to list
        self.cards.append(card)
        # check for ace
        if card.rank == "A":
            self.ace = True
        # add card value
        self.value += card_vals[card.rank]
    # method to calcluate value of player hand
    def calcHandVal(self):
        # check if contains ace and card value 
        if (self.ace == True and self.value + 10 <= 21):
            # update player hand value with ace value of 10
            return self.value + 10
        # keep normal total
        else:
            return self.value
    # method to show player hand
    def drawCard(self, hidden):
        # first card is hidden
        if (hidden == True and playing == True):
            # start from 2nd card
            starting_card = 1
        # show all cards
        else:
            starting_card = 0
        # iterate from starting card to last card
        for x in range(starting_card, len(self.cards)):
            self.cards[x].drawCard()

# class for card deck
class Deck:
    def __init__(self):
        self.deck = []
        for suit in game_suits:
            for rank in card_ranks:
                self.deck.append(Card(suit, rank))
    # emthod to randomly shuffle card deck
    def shuffleDeck(self):
        random.shuffle(self.deck)
    # method to deal card from deck
    def dealCard(self):
        single_card = self.deck.pop()
        return single_card
    # method to add formatting to deck
    def __str__(self):
        deck_comp = " "
        for card in self.cards:
            deck_comp += " " +str(card)
        return "The deck is "+deck_comp

# function for player bet initiation
def makeBet():
    global bet
    bet = 0
    print("Enter how much would you like to bet? (Number cannot be a decimal): ")
    # iterate until bet amount valid
    while bet == 0:
        # read and convert player bet to string
        bet_comp = input()
        bet_comp = int(bet_comp)
        # check bet within min and allocated amount
        if (bet_comp >=1 and bet_comp <= buyin_min):
            bet = bet_comp
        # invalid bet amount
        else:
            print("Invalid bet, only " +str(buyin_min) + " remaining.") 

# function to deal cards
def dealCard():
    # game variables
    global result, playing, deck, player_hand, dealer_hand, buyin_min, bet
    # create new game deck
    deck = Deck()
    deck.shuffleDeck()
    makeBet()
    # iitialize hands for player and dealer
    player_hand = Hand()
    dealer_hand = Hand()
    result = "Hit or Stay? Press h to hit or hit s to stay: "
    # check whether game already in progress
    if playing == True:
        # player folds
        print("Fold, sorry.")
        # reduce amount
        buyin_min -= bet 
    playing = True
    nextGameStep()

# function for drawing card
def hit():
    global result, playing, deck, player_hand, dealer_hand, buyin_min, bet
    # allow only if game is active
    if playing:
        # check whether player busted
        if player_hand.calcHandVal() <= 21:
            # deal card from deck
            player_hand.addCard(deck.dealCard())
        print("Player hand is %s" %player_hand)
        # whether card from deck pushed player over 21
        if player_hand.calcHandVal() > 21:
            result = "Busted!" + restart_msg
            # reduce bet amount from player
            buyin_min -= bet
            playing = False
    # cannot hit and wait for player input
    else:
        result = "Sorry, cannot hit." + restart_msg
    nextGameStep()

# function for dealer hand
def stay():
    global result, playing, deck, player_hand, dealer_hand, buyin_min, bet
    # check game status
    if playing == False:
        # player hand value 
        if player_hand.calcHandVal() > 0:
            result = "Sorry, cannot stay."
    else:
        # dealer draws until value becomes more than 17
        while (dealer_hand.calcHandVal() < 17):
            # deal card to dealer
            dealer_hand.addCard(deck.dealCard())
        # check whether dealer goes over 21
        # if so prompt player win 
        # add amount to bet
        # end current game 
        if (dealer_hand.calcHandVal() > 21):
            result = "Dealer loses, you win!" + restart_msg
            buyin_min += bet
            playing = False
        # hand values are same
        # game is tied
        elif (dealer_hand.calcHandVal() == player_hand.calcHandVal()):
            result = "Tied, now push" + restart_msg
            playing = False
        # dealer has winning hand
        # reduce bet amount from player
        # end current game
        else:
            result = "Dealer wins!" + restart_msg
            buyin_min -= bet
            playing = False
    nextGameStep()

# function for game steps to be taken by player
def nextGameStep():
    # print player and dealer hand
    print("")
    print("Player hand: "),player_hand.drawCard(hidden=False)
    print("")
    print("Player hand value: "+str(player_hand.calcHandVal()))
    print("")
    print("Dealer hand: "),dealer_hand.drawCard(hidden=True)
    # check game over
    if playing == False:
        # show dealer hand
        print("Dealer total of: "+str(dealer_hand.calcHandVal()))
        print("Bet total: "+str(buyin_min))
    # game not over
    else:
        print(" another card upside down")
    print("")
    print(result)
    playerInput()

# function to quit game
def exitGame():
    print("Thank you for playing....")
    exit()

# function to read player input
def playerInput():
    plyinp = input().lower()
    # gameplay conditions with their triggers
    if plyinp == "h":
        hit()
    elif plyinp == "s":
        stay()
    elif plyinp == "d":
        dealCard()
    elif plyinp == "q":
        exitGame()
    else:
        print("Invalid input, (h, s, d or q) only: ")
        playerInput()

# function to show game message
def gameIntro():
    summary = "Welcome to Blackjack. Goal is to get as close to 21 without exceeding it. Dealer hits until 17 reached, Aces count as 1 or 11. Card is denoted by letter followed by the suit."
    print(summary)

#create new initial deck and shuffle it
deck = Deck()
deck.shuffleDeck()
# create initial player and dealer hand
print("")
player_hand = Hand()
print("")
dealer_hand = Hand()

# show game message and deal card
gameIntro()
dealCard()