import random

#list of the two possible outcomes of flipping a coin
possibilities = ["Heads", "Tails"]

#get the user to guess the outcome
def user_call():
    print("I'm going to flip a coin.")
    call = input("Do you call heads or tails?: ").title()
    return call


# flip the coin. 
def coin_flip(player_call):
  outcome = random.choice(possibilities)
  if outcome == player_call:
    return "You chose {player_call}. The result is ... {outcome}. You won!".format(player_call=player_call, outcome=outcome)
  else:
    return "You chose {player_call}. The result is ... {outcome}. You lost!".format(player_call=player_call, outcome=outcome)
  return outcome

def play():
  player_call = user_call()
  print(coin_flip(player_call))

play()
