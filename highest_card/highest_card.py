import random
# Create a function that simulates two players picking a card randomly from a deck of cards. The higher number wins.

# Once again, this function should have a parameter that allows a player to bet an amount of money on whether they have a higher card. In this game, there can be a tie. What should be returned if there is a tie?

#create a list of ranks (or dictionary?)
# ranks = {
# 'ACE': 1,
# 'TWO': 2,
# 'THREE': 3,
# 'FOUR': 4,
# 'FIVE': 5,
# 'SIX': 6,
# 'SEVEN': 7,
# 'EIGHT':8,
# 'NINE': 9,
# 'TEN': 10,
# 'JACK': 10,
# 'QUEEN': 10,
# 'KING': 10
# }

ranks = [
{'ACE': 1},
{'TWO': 2},
{'THREE': 3},
{'FOUR': 4},
{'FIVE': 5},
{'SIX': 6},
{'SEVEN': 7},
{'EIGHT':8},
{'NINE': 9},
{'TEN': 10},
{'JACK': 10},
{'QUEEN': 10},
{'KING': 10}
]

# print(ranks)
#create a list of suits
suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES']
# print(suits)

#combine the two lists to create a dictionary of cards (variable name is deck)
# deck = {}
# def fill_deck():
#     for suit in suits:
#         deck.update({suit: ranks})
#     return deck

deck = []
# def fill_deck():
#     for suit in suits:
#         deck.append({suit: ranks})
#     return deck

def fill_deck():
    for suit in suits:
        for rank in ranks:
            deck.append({suit: rank})

fill_deck()
# print(deck)
# print(deck[-1])
#randomly select two cards from the deck. One card goes to player1, the other to player2. Make sure that each player gets a different card. This could mean using the sample method to select two cards, putting the two cards into a list and then assigning them to the players. Or I could use the choose method and delete a card from the deck once the card has been chosen.
card = {}
def player1_cards():
    card.update(random.choice(deck))
    # suit_name = suit.keys()
    # ranks = suit.values()
    # rank = ranks[0]
    # rank = random.choice(ranks)
    # rank = random.choice(list(suit))
    # return "You chose {rank} of {suit_name}.".format(rank=rank, suit_name=suit_name)
    # return suit_name
    return card
print(player1_cards())
# player2_card = random.choice(deck)
print(card)
#find the highest card.
#1. check the rank of both cards
#2. elif statement to display "Player1 wins" if player1 card rank is higher; "Player2 wins" if player2 card rank is higher; "It's a draw" if the ranks are the same (possibly make a royal beat a normal ten)
def find_card_value(card):
    rank_value = card.values()
    rank_score = {}
    rank_points = 0
    for key, value in card.items():
        rank_score.update(value)
    for key, value in rank_score.items():
        rank_points += value
    return rank_points
print(find_card_value(card))
