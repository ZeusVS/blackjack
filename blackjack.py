import secrets, os, time, math

# Create some initial values
money = 1000
hands_won = 0
hands_lost = 0
hands_tied = 0
highest_bank = money

# Define a new class for the playing cards
class Card:
    def __init__(self, card_face, value, symbol, amount):
       self.card_face = card_face
       self.value = value
       self.symbol = symbol
       self.amount = amount

def place_bet():
    global money
    global bet
    # Lets players choose how much they want to bet
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Bank: ${money}')
        bet = input("How much $ do you want to bet this game?\n")
        try:
            bet = int(bet)
        except:
            continue
        if 1 <= bet <= money:
            money -= bet
            break

def show_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Bank: ${money}')
    print(f'Bet:  ${bet}'.ljust(40), end="")
    print(f'Cards left: {len(cards)}'.rjust(40))
    print("=" * 80)
    print("Player hand:".ljust(40), end="")
    print(f'Player total: {player_total}'.rjust(40))
    print_cards(player_hand)
    print()
    print("=" * 80)
    print("Dealer hand:".ljust(40), end="")
    print(f'Dealer total: {dealer_total}'.rjust(40))
    print_cards(dealer_hand)
    print()
    print("=" * 80)

def print_cards(cards):
    print("+---------+ " * len(cards))
    for i in cards:
        print(f"| {str(i.card_face).ljust(2)}      | ", end ="")
    print()
    print("|         | " * len(cards))
    for i in cards:
        print(f"|    {i.symbol}    | ", end ="")
    print()
    print("|         | " * len(cards))
    for i in cards:
        print(f"|      {str(i.card_face).rjust(2)} | ", end ="")
    print()
    print("+---------+ " * len(cards))
    # create the correct print commands to print a card

# Pick a card from the deck
def deal(hand, total):
    drawn_card = secrets.choice(cards)
    cards.remove(drawn_card)
    hand.append(drawn_card)
    if drawn_card.value == 1:
        if total <= 10:
            drawn_card.value = 11
    total += drawn_card.value
    time.sleep(1)
    return total

# (Re)create the complete deck of cards
def shuffle():
    # First print shuffling on screen to show the player the deck is shuffled again
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(4):
        print()
    print("            __                   ______    ______   __  __                      \n\
           |  \                 /      \  /      \ |  \|  \                     \n\
   _______ | $$____   __    __ |  $$$$$$\|  $$$$$$\| $$ \$$ _______    ______   \n\
  /       \| $$    \ |  \  |  \| $$_  \$$| $$_  \$$| $$|  \|       \  /      \  \n\
 |  $$$$$$$| $$$$$$$\| $$  | $$| $$ \    | $$ \    | $$| $$| $$$$$$$\|  $$$$$$\ \n\
  \$$    \ | $$  | $$| $$  | $$| $$$$    | $$$$    | $$| $$| $$  | $$| $$  | $$ \n\
  _\$$$$$$\| $$  | $$| $$__/ $$| $$      | $$      | $$| $$| $$  | $$| $$__| $$ \n\
 |       $$| $$  | $$ \$$    $$| $$      | $$      | $$| $$| $$  | $$ \$$    $$ \n\
  \$$$$$$$  \$$   \$$  \$$$$$$  \$$       \$$       \$$ \$$ \$$   \$$ _\$$$$$$$ \n\
                                                                     |  \__| $$ \n\
                                                                      \$$    $$ \n\
                                                                       \$$$$$$  ")
    time.sleep(2)
    # 
    cards = []
    for i in ["♥", "♦", "♣", "♠"]:
        for j in range(10) :
            cards.append(Card(j+1,j+1,i,decks))
        for j in ["J", "Q", "K"]:
            cards.append(Card(j,10,i,decks))
    cards = cards * decks
    print(len(cards))
    return cards

# Basic print state
def print_state(state):
    # Wait before printing the final screen so players can see all cards
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Bank: ${money}')
    print(f'Bet: ${bet}')
    print("=" * 80)
    for i in range(2):
        print()
    
    if state == 'won':
        print_won()
    elif state == 'tie':
        print_tie()
    elif state == 'lost':
        print_lost()
    # Wait before starting next game
    time.sleep(3)

# Print won statement
def print_won():
    print(r'''       __      __                                                            __ 
      |  \    /  \                                                          |  \
       \$$\  /  $$______   __    __        __   __   __   ______   _______  | $$
        \$$\/  $$/      \ |  \  |  \      |  \ |  \ |  \ /      \ |       \ | $$
         \$$  $$|  $$$$$$\| $$  | $$      | $$ | $$ | $$|  $$$$$$\| $$$$$$$\| $$
          \$$$$ | $$  | $$| $$  | $$      | $$ | $$ | $$| $$  | $$| $$  | $$ \$$
          | $$  | $$__/ $$| $$__/ $$      | $$_/ $$_/ $$| $$__/ $$| $$  | $$ __ 
          | $$   \$$    $$ \$$    $$       \$$   $$   $$ \$$    $$| $$  | $$|  \
           \$$    \$$$$$$   \$$$$$$         \$$$$$\$$$$   \$$$$$$  \$$   \$$ \$$''')

# Print lost statement
def print_lost():
    print(r'''       __      __                          __                        __      __ 
      |  \    /  \                        |  \                      |  \    |  \ 
       \$$\  /  $$______   __    __       | $$  ______    _______  _| $$_   | $$ 
        \$$\/  $$/      \ |  \  |  \      | $$ /      \  /       \|   $$ \  | $$ 
         \$$  $$|  $$$$$$\| $$  | $$      | $$|  $$$$$$\|  $$$$$$$ \$$$$$$  | $$ 
          \$$$$ | $$  | $$| $$  | $$      | $$| $$  | $$ \$$    \   | $$ __  \$$ 
          | $$  | $$__/ $$| $$__/ $$      | $$| $$__/ $$ _\$$$$$$\  | $$|  \ __  
          | $$   \$$    $$ \$$    $$      | $$ \$$    $$|       $$   \$$  $$|  \ 
           \$$    \$$$$$$   \$$$$$$        \$$  \$$$$$$  \$$$$$$$     \$$$$  \$$''')

# Print tie statement
def print_tie():
    print(r'''       ______   __   __                                   __      __            __ 
      |      \ |  \ |  \                                 |  \    |  \          |  \ 
       \$$$$$$_| $$_| $$ _______         ______         _| $$_    \$$  ______  | $$ 
        | $$ |   $$ \\$ /       \       |      \       |   $$ \  |  \ /      \ | $$ 
        | $$  \$$$$$$  |  $$$$$$$        \$$$$$$\       \$$$$$$  | $$|  $$$$$$\| $$ 
        | $$   | $$ __  \$$    \        /      $$        | $$ __ | $$| $$    $$ \$$ 
       _| $$_  | $$|  \ _\$$$$$$\      |  $$$$$$$        | $$|  \| $$| $$$$$$$$ __  
      |   $$ \  \$$  $$|       $$       \$$    $$         \$$  $$| $$ \$$     \|  \ 
       \$$$$$$   \$$$$  \$$$$$$$         \$$$$$$$          \$$$$  \$$  \$$$$$$$ \$$''')

def continue_playing():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Bank: ${money}'.ljust(40), end="")
        print(f'Highest Bank: ${highest_bank}'.rjust(40))
        print()
        print("=" * 80)
        print(f'Win:  {hands_won}')
        print(f'Tie:  {hands_tied}')
        print(f'Lose: {hands_lost}')
        print("=" * 80)
        answer = input("Do you want to (K)eep Playing or (C)ash Out?\n").upper()
        if answer == 'K':
            return True
        elif answer == 'C':
            return False


# Let player choose with how many decks they want to play -> Only once at startup
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    decks = input("How many decks do you want to play with? (1-6)\n")
    try:
        decks = int(decks)
    except:
        continue
    if 1 <= decks <= 6:
        break

#start out by creating the card deck
cards = shuffle()

# Main game loops
while True:
    # Reset player & dealer hands and total score        
    player_hand = []
    dealer_hand = []
    player_total = 0
    dealer_total = 0
    first_move = True
    player_bust = False
    dealer_bust = False

    # Check if the user wants to continue playing after the first hand
    if hands_lost + hands_tied + hands_lost > 0:
        if continue_playing() == False:
            break

    # If less than half cards remain, shuffle (recreate) entire card deck
    if len(cards) < 52 * decks / 2:
        cards = shuffle()
    
    # Start the game logic
    place_bet()
    show_game()

    # Start every game with giving the player 2 cards and the dealer 1 card (Eropean blackjack no-hole-card)
    player_total = deal(player_hand, player_total)
    show_game()

    dealer_total = deal(dealer_hand, dealer_total)
    show_game()

    player_total = deal(player_hand, player_total)
    show_game()

    # Player's turn untill leaving this loop
    while True:
        # Ask player what his next move is
        while True:
            if first_move == True:
                move = input("Pick your next move: \n(H)it, (S)tand, (D)ouble Down, (F)old\n").upper()
                if move in ['S', 'H', 'D', 'F']:
                    if move == 'D' and money < bet:
                        continue
                    first_move = False
                    break
            else:
                move = input("Pick your next move: \n(H)it or (S)tand\n").upper()
                if move in ['S', 'H']:
                    break
        if move == 'F':
            money += math.floor(bet / 2)
            player_bust = True
            break
        elif move == 'S':
            break
        elif move == 'D':
            money -= bet
            bet *= 2
            show_game()
            player_total = deal(player_hand, player_total)
            show_game()
            break
        elif move == 'H':
            player_total = deal(player_hand, player_total)
            if player_total > 21:
                for player_card in player_hand:
                    if player_card.value == 11:
                        player_total -= 10
                        player_card.value = 1
                        break
            show_game()
        
        if player_total > 21:
            player_bust = True
            break
        elif player_total == 21:
            break

    # Dealer's turn untill leaving this loop
    while not player_bust:
        if dealer_total < 17:
            dealer_total = deal(dealer_hand, dealer_total)
            if dealer_total > 21:
                for dealer_card in dealer_hand:
                    if dealer_card.value == 11:
                        dealer_total -= 10
                        dealer_card.value = 1
                        break
            show_game()
        elif dealer_total > 21:
            dealer_bust = True       
            break
        else:
            break
    
    if player_bust:
        print_state('lost')
        hands_lost += 1
    elif dealer_bust:
        print_state('won')
        money += 2 * bet
        hands_won += 1
    else:
        # Compare scores if both didn't go bust
        if player_total > dealer_total:
            print_state('won')
            money += 2 * bet
            hands_won += 1
        elif player_total == dealer_total:
            print_state('tie')
            hands_tied += 1
        else:
            print_state('lost')
            hands_lost += 1
    highest_bank = max(highest_bank, money)

print('Thank you for playing!')

# TODO: make it possible to change ace value from 11 to 1 in case there is an ace in hand and total > 21