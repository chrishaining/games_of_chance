import random
from matplotlib import pyplot as plt
# import numpy as np

#list of the two possible outcomes of flipping a coin
possibilities = ["Heads", "Tails"]

# create a list of outcomes
outcomes = []

# flip the coin. 
def coin_flip():
  outcome = random.choice(possibilities)
  print("The result is ... {outcome}.".format(outcome=outcome))
  return outcome

def add_outcome_to_list(outcome):
  outcomes.append(outcome)
  return outcomes

def play():
  outcome = coin_flip()
  add_outcome_to_list(outcome)

def play_multiple_times(number):
  for i in range(number):
    play()
  print("The full list of results is {}.".format(outcomes))

play_multiple_times(100)

total_heads = outcomes.count("Heads")
total_tails = outcomes.count("Tails")
total_outcomes = [total_heads, total_tails]
names = ["Heads", "Tails"]

def calculate_probability():
  heads_probability = outcomes.count("Heads") / len(outcomes)
  tails_probability = outcomes.count("Tails") / len(outcomes)
  print("Probability of heads is: {}.".format(heads_probability))
  print("Probability of tails is: {}.".format(tails_probability))

calculate_probability()

# add probability the pie chart

plt.pie(total_outcomes, autopct='%0.2f%%')
plt.legend(names)
plt.show()