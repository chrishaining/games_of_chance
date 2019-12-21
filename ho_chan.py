#In this game, we roll two dice and the player guesses whether the resulting number will be odd or even. For example, if the first die scores 1 and the second die scores 2, the total score is 3 (odd).

#import packages - random, maybe numpy, maybe matplotlib
import random

#create a list of possible numbers (let's make it two lists - imagine there are two dice)
#(possible refactor - even if I want to have two numbers, I don't really need two lists - I could just repeat a function for one list)
first_die = [1, 2, 3, 4, 5, 6]
second_die = [1, 2, 3, 4, 5, 6]

#create a list of results. starts empty
odd_or_even_result = ""

#create a function to roll the dice. this will include adding the result to the results list
#use random.choice() to select a single item from a list.
def roll_dice():
    print("Here goes - the dice are rolling...")
    odd_or_even_result = ""
    result = 0
    first_die_result = random.choice(first_die)
    second_die_result = random.choice(second_die)
    result += first_die_result + second_die_result
    print("... The first die scores a {first}. And the second die scores a {second}.".format(first=first_die_result, second=second_die_result))
    if result % 2 == 0:
        odd_or_even_result += "even"
    else:
        odd_or_even_result += "odd"
    return odd_or_even_result

# print(roll_dice())

#get the user to guess the outcome
def guess_the_outcome():
    print("I'm going to roll two dice. Your task is to guess whether the total number showing on the two dice will be odd or even.")
    guess = input("Do you think the dice will roll odds or even?: ").lower()
    return guess


# guess()

#play a round (combine roll dice and guess)
def play():
    guess = guess_the_outcome()
    outcome = roll_dice()
    print("A reminder: you guessed {}.".format(guess))
    print("And the outcome was ... {}.".format(outcome))
    if guess == outcome:
        print("You're a winner!")
    else:
        print("You lost.")

play()
