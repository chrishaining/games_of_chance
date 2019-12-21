import random

#add the player's account (so, how much they have won. Account starts at 100)
account = 100

#list of the two possible outcomes of flipping a coin
possibilities = ["Heads", "Tails"]

#A function that takes the player's stake and their choice of Heads or Tails. Then randomly select an outcome. Based on that outcome, the player wins double their stake or loses their stake. The winnings/losses are then added to/taken from the
# def coin_flip(stake, player_call):
#   outcome = random.choice(possibilities)
#   change_to_account = 0
#   if outcome == player_call:
#     change_to_account += stake *2
#     # change_account_balance(change_to_account)
#     print("And the result is ... {outcome}. You won £{amount}".format(outcome=outcome, amount=change_to_account))
#     balance = change_account_balance(change_to_account)
#   else:
#     change_to_account -= stake
#     # change_account_balance(change_to_account)
#     print("And the result is ... {outcome}. You lost £{stake}".format(outcome=outcome, stake=stake))
#     balance = change_account_balance(change_to_account)
#   return "Your account now stands at £{}.".format(balance)

#Call the function
# print(coin_flip(50, "Heads"))

def coin_flip(stake, player_call):
  outcome = random.choice(possibilities)
  change = 0
  victory = False
  if outcome == player_call:
    change += stake *2
    victory = True
    print("And the result is ... {outcome}.".format(outcome=outcome))
  else:
    change -= stake
    print("And the result is ... {outcome}.".format(outcome=outcome))
  return change

def change_account_balance():
    new_balance = account + change
    return new_balance

def play(stake, player_call):
    coin_flip(stake, player_call)
    change_account_balance()
    print("Your new balance is {}.".format(new_balance))

play(50, "Heads")
