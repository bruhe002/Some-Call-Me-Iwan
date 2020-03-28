

def take_bet(chips):
    
    while True:
        try:
            result = int(input("Place a bet: "))
        except TypeError: 
            print("That is not a valid number!")
            continue
        if chips.total-result < 0:
            print("You don't have enough money")
            continue
        else:
            chips.bet += result
            break

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def show_some(player,dealer):
    print('\n')
    print("Dealer's Hand: ")
    for card in dealer.cards:
        if card == dealer.cards[0]:
            print("\tTHIS CARD IS HIDDEN!")
        else:
            print(f"\t{card}")
    
    print("\n")
    
    print("Player's hand: ")
    for card in player.cards:
        print(f"\t{card}")
    print(f'Value: {player.value}')
    print('\n')
    
def show_all(player,dealer):
    
    print("Dealer's hand: ")
    for card in dealer.cards:
        print(f'\t{card}')
    print(f"Value: {dealer.value}")
    if dealer.value > 21:
        print('Dealer BUSTS!')
    elif dealer.value == 21:
        print('Dealer BLACKJACK!')
    
    print("\nPlayer's hand: ")
    for card in player.cards:
        print(f'\t{card}')
    print(f"Value: {player.value}")
    print('\n')

def player_busts(playerChips):
    print("You busted! Thanks for playing!")
    playerChips.lose_bet()

def player_wins(playerChips, blackJack):
    if blackJack:
        print(f"You win! Here are your winnings: ${playerChips.bet + (1.5 * playerChips.bet)}")
    else:
        print(f"You win! Here are your winnings: ${playerChips.bet * 2}")
    playerChips.win_bet(blackJack)

def dealer_busts(playerChips):
    print(f"You win! Here are your winnings: ${playerChips.bet * 2}")
    playerChips.win_bet(False)
    
def dealer_wins(playerChips):
    print("Dealer wins! Thanks for playing!")
    playerChips.lose_bet()

def tie(playerChips):
    print(f"It's a tie! Here's your money back: ${playerChips.bet}")
    