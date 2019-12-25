import random
# Create a function that simulates two players picking a card randomly from a deck of cards. The higher number wins.

# Once again, this function should have a parameter that allows a player to bet an amount of money on whether they have a higher card. In this game, there can be a tie. What should be returned if there is a tie?

#create a list of ranks
ACE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT =8
NINE = 9
TEN = 10
JACK = 10
QUEEN = 10
KING = 10


#create a list of suits

#combine the two lists to create a dictionary of cards (variable name is deck)

#randomly select two cards from the deck. One card goes to player1, the other to player2. Make sure that each player gets a different card. This could mean using the sample method to select two cards, putting the two cards into a list and then assigning them to the players. Or I could use the choose method and delete a card from the deck once the card has been chosen.
# player1_card = random.choose(deck)
# player2_card = random.choose(deck)

#find the highest card.
#1. check the rank of both cards
#2. elif statement to display "Player1 wins" if player1 card rank is higher; "Player2 wins" if player2 card rank is higher; "It's a draw" if the ranks are the same (possibly make a royal beat a normal ten)
