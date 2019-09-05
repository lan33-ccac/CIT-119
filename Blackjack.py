##################################################################
# Module: Blackjack.py
# Exercise: Ch9_Exercise_9
# Purpose: Simulates simplified blackjack deck
# Last update: 11/9/18
# Author: Lisa Nydick
##################################################################

#Global constants and variables declarations
SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
CARDS = ['Ace of', '2 of', '3 of', '4 of', '5 of', '6 of', '7 of', '8 of', '9 of', '10 of', 'Jack of', 'Queen of', 'King of']
DECK_SIZE = 52
MAX_HAND = 21
PLAYER1='Player 1'
PLAYER2 ='Player 2'
TIE = 'tie'
CARDS_TEXT = 'Cards: '
HAND_VALUE = 'Hand Value:'
GAME_OUTCOME = '\nGame Outcome: '
WON = 'Won.'
GAME_TIED = 'Game was tied.  Dealing a new hand.'


##############################################################################
def main():
    deck_dict = {}
    player1_cards = []
    player1_points = 0
    player2_cards = []
    player2_points = 0
    winner = TIE


    # Repeat game as long as the outcome is a tie, which it is set to initially
    while winner == TIE:
        # build the deck dictionary
        deck_dict = build_deck()

        #deal cards for the hand
        player1_cards, player1_points, player2_cards, player2_points = deal_cards(deck_dict)

        #determine winner
        winner = get_winner(player1_points, player2_points)

    # Display player card lists, hand values, and game outcome
    display_output(player1_cards, player1_points, player2_cards, player2_points, winner)

##############################################################################
# Function creates a dictionary of card values
##############################################################################
def build_deck():
    deck = {}

    deck = {'Ace of Spades':11, '2 of Spades':2, '3 of Spades':3, '4 of Spades':4,
           '5 of Spades':5, '6 of Spades':6, '7 of Spades':7, '8 of Spades':8,
           '9 of Spades':9, '10 of Spades':10, 'Jack of Spades':10,
           'Queen of Spades':10, 'King of Spades':10,

           'Ace of Hearts':11, '2 of Hearts':2, '3 of Hearts':3, '4 of Hearts':4,
           '5 of Hearts':5, '6 of Hearts':6, '7 of Hearts':7, '8 of Hearts':8,
           '9 of Hearts':9, '10 of Hearts':10, 'Jack of Hearts':10,
           'Queen of Hearts':10, 'King of Hearts':10,

           'Ace of Clubs':11, '2 of Clubs':2, '3 of Clubs':3, '4 of Clubs':4,
           '5 of Clubs':5, '6 of Clubs':6, '7 of Clubs':7, '8 of Clubs':8,
           '9 of Clubs':9, '10 of Clubs':10, 'Jack of Clubs':10,
           'Queen of Clubs':10, 'King of Clubs':10,

           'Ace of Diamonds':11, '2 of Diamonds':2, '3 of Diamonds':3, '4 of Diamonds':4,
           '5 of Diamonds':5, '6 of Diamonds':6, '7 of Diamonds':7, '8 of Diamonds':8,
           '9 of Diamonds':9, '10 of Diamonds':10, 'Jack of Diamonds':10,
           'Queen of Diamonds':10, 'King of Diamonds':10
           }

    return deck

##############################################################################
# Function returns a random suit and a random card within the suit
##############################################################################
def get_random_card():

    rand_suit_index = 0
    rand_card_index = 0
    random_card = ''

    from random import randrange
    rand_suit_index = randrange(0, 3)   #4 possible suits
    rand_card_index = randrange(0, 12)  #13 possible cards

    # Look up rand_card_index in CARDS global variable list, and concatenate it with the randomly selected SUITS index
    random_card =  CARDS[rand_card_index] + ' ' + SUITS[rand_suit_index]


    return random_card

##############################################################################
# Function deals card until one player wins
##############################################################################
def deal_cards(deck):
    player_1_cards = []
    player_1_hand_value = 0
    player_2_cards = []
    player_2_hand_value = 0
    current_deck_len = DECK_SIZE

    while current_deck_len > 0 and player_1_hand_value <= MAX_HAND and player_2_hand_value <= MAX_HAND:

        # deal card to first player
        card = get_random_card()

       # catch deck.pop KeyError, which will occur if the selected card has already been popped from the deck
        try:
            value = deck.pop(card)          # remove item from dictionary
            player_1_cards.append(card)     # append drawn card to player's card list
            player_1_hand_value += value    # increment value of player's hand
            if value == 11 and player_1_hand_value > MAX_HAND:  # Test for Ace (value=11).  If the default Ace value will put the player over the hand limit, subract 10 from the total
                player_1_hand_value = player_1_hand_value - 10
        except KeyError:
            value = 0
            card = ''
            continue    # go back to start of loop




        # deal card to second player
        card = get_random_card()

        # catch deck.pop KeyError, which will occur if the selected card has already been popped from the deck
        try:
            value = deck.pop(card)          # remove item from dictionary
            player_2_cards.append(card)     # append drawn card to player's card list
            player_2_hand_value += value    # increment value of player's hand
            if value == 11 and player_2_hand_value > MAX_HAND:  # Test for Ace (value=11).  If the default Ace value will put the player over the hand limit, subract 10 from the total
                player_2_hand_value = player_2_hand_value - 10
        except KeyError:
            value = 0
            card = ''
            continue   #go back to start of loop


        # Reset the deck length so we don't run out of cards
        current_deck_len = len(deck)

    return player_1_cards, player_1_hand_value, player_2_cards, player_2_hand_value


##############################################################################
# Function determines winner
##############################################################################
def get_winner(player1_pts, player2_pts):
    winner = ''

    # If a player's hand goes over 21, the other player wins (unless both go over)
    if player1_pts <= MAX_HAND and player2_pts > MAX_HAND:
        winner = PLAYER1
    elif player1_pts > MAX_HAND and player2_pts <= MAX_HAND:
        winner = PLAYER2
    elif player1_pts == MAX_HAND and player2_pts == MAX_HAND:  #if both players hands = 21 then it's a tie
        winner = TIE
    else:    # both players are over limit, so it's a tie
        winner = TIE

    return winner


##############################################################################
# Function for displaying console output
##############################################################################
def display_output(p1_cards_list, p1_points, p2_cards_list, p2_points, winner):

    print(PLAYER1, CARDS_TEXT, end='')
    i = 0
    listlen = 0
    listlen = len(p1_cards_list)
    for i in range(listlen):
        if i == listlen-1:
            print(p1_cards_list[i])
        else:
            print(p1_cards_list[i], end=', ')

    print(PLAYER1, HAND_VALUE, p1_points)

    print(PLAYER2, CARDS_TEXT, end='')
    i = 0
    listlen = 0
    listlen = len(p2_cards_list)
    for i in range(listlen):
        if i == listlen-1:
            print(p2_cards_list[i])
        else:
            print(p2_cards_list[i], end=', ')
    print(PLAYER2, HAND_VALUE, p2_points)

    print(GAME_OUTCOME, end='')
    if winner == PLAYER1:
        print(PLAYER1, WON)
    elif winner == PLAYER2:
        print(PLAYER2, WON)
    else:    #it was a tie
        print(GAME_TIED)


##############################################################################
main()
