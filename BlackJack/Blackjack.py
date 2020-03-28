import random
from time import sleep
import Blackjack_Func as bf
          #Spades,  Hearts,  Diamonds,  Clubs
suits = ('\u2660', '\u2665', '\u2666','\u2663')
ranks = ('2','3', '4', '5', '6', '7', '8',
        '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
          '8':8,'9':9, '10':10, 'J':10, 'Q':10,
          'K':10, 'A':11 }

playing = True

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        result = input("Would you like to hit or stand? ")
        if result[0].lower() == 'h':
            bf.hit(deck,hand)
            break
        elif result[0].lower() == 's':
            playing = False
            break
        else:
            print("Not a valid input! Try again...")
            continue

#Classes
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                my_card = Card(suit, rank)
                self.deck.append(my_card)
                
    
    def __str__(self):
        list_of_deck = []
        for card in self.deck:
            list_of_deck.append(card.__str__())
        return str(list_of_deck)

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        if(card.rank == "A"):
            self.aces += 1
        self.value += values[card.rank]
    
    def adjust_for_ace(self):
        if self.value > 21 and self.aces > 0:
            i = 0
            while i < self.aces:
                self.value -= 10
                if self.value < 21:
                    break

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self, blackJack):
        if blackJack:
            self.total += (3/2) * self.bet
        else:
            self.total += self.bet * 2 
    
    def lose_bet(self):
        self.total -= self.bet


#Game Starts
rounds = 0
while True:
    
    # Print an opening statement
    print('Welcome to Blackjack! Winnings are 3 to 2! Have fun!')
    
    # Create & shuffle the deck, deal two cards to each player
    dealerDeck = Deck()
    dealerDeck.shuffle()
    
    dealerHand = Hand()
    playerHand = Hand()
    
    dealerHand.add_card(dealerDeck.deal())
    dealerHand.add_card(dealerDeck.deal())
    
    playerHand.add_card(dealerDeck.deal())
    playerHand.add_card(dealerDeck.deal())
        
    # Set up the Player's chips
    if rounds == 0:
        playerChips = Chips()
        print('Here are a $100 chips to get you started')
    
    # Prompt the Player for their bet
    playerChips.bet = 0
    bf.take_bet(playerChips)
     
    
    # Show cards (but keep one dealer card hidden)
    bf.show_some(playerHand, dealerHand)
    
    while playing: 
        blackJack = False
        if playerHand.value != 21:
            hit_or_stand(dealerDeck, playerHand)
        else:
            print('BLACKJACK!!!')
            playing = False
            blackJack = True     
        # Show cards (but keep one dealer card hidden)
        if playing:
            bf.show_some(playerHand, dealerHand)
        
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if playerHand.value > 21:
            bf.player_busts(playerChips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        elif not playing and not blackJack:
            bf.show_all(playerHand,dealerHand)
            while dealerHand.value < 17:
                print('Dealer is dealing...')
                sleep(2.0)
                dealerHand.add_card(dealerDeck.deal())

                # Show all cards
                bf.show_all(playerHand,dealerHand)
                
                # Run different winning scenarios
            if dealerHand.value > 21:
                bf.dealer_busts(playerChips)
            elif dealerHand.value > playerHand.value:
                bf.dealer_wins(playerChips)
            elif dealerHand.value == playerHand.value:
                bf.tie(playerChips)
            else:
                bf.player_wins(playerChips, blackJack)
        elif blackJack:
            bf.player_wins(playerChips, blackJack)
    
    # Inform Player of their chips total 
    print(f'Here are your total chips: ${playerChips.total}')
    
    # Ask to play again
    if playerChips.total > 0:
        choice = input("Keep playing? (Y/N): ")
        if choice.lower() == 'y':
            rounds += 1
            playing = True
            continue
        elif choice.lower() == 'n':
            print(f'Thanks for playing! Your total chips are ${playerChips.total}')
            break
    elif playerChips.total == 0:
        print("You have no more money! Thanks for playing!")
        break
    else:
        print("You owe us money! We'll be there soon to break your fuckin' legs...")
        