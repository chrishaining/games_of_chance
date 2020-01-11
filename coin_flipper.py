import random

#list of the two possible outcomes of flipping a coin
possibilities = ["Heads", "Tails"]

# flip the coin. 
def coin_flip(player_call):
  outcome = random.choice(possibilities)
  if outcome == player_call:
    return "You chose {player_call}. The result is ... {outcome}. You won!".format(player_call=player_call, outcome=outcome)
  else:
    return "You chose {player_call}. The result is ... {outcome}. You lost!".format(player_call=player_call, outcome=outcome)
  return outcome

game1=coin_flip("Heads")
game2=coin_flip("Heads")
game3=coin_flip("Tails")
print("Game 1: {}".format(game1))
print("Game 2: {}".format(game2))
print("Game 3: {}".format(game3))
