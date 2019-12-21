#import packages - random, maybe numpy, maybe matplotlib
import random
from matplotlib import pyplot as plt
import numpy as np


#create a list of possible numbers (let's make it two lists - imagine there are two dice)
#(possible refactor - even if I want to have two numbers, I don't really need two lists - I could just repeat a function for one list)
first_die = [1, 2, 3, 4, 5, 6]
second_die = [1, 2, 3, 4, 5, 6]

#create a list of results. starts empty
results = []

#create a function to roll the dice. this will include adding the result to the results list
#use random.choice() to select a single item from a list.
def roll_dice():
    first_die_result = random.choice(first_die)
    second_die_result = random.choice(second_die)
    results.append(first_die_result+second_die_result)

# roll_dice()
# print(results)

#in order to give enough results for a histogram, create a function to roll the dice multiple times
def roll_multiple_dice(rolls):
    counter = 0
    while counter < rolls:
        roll_dice()
        counter += 1
    print("The dice have been rolled {} times.".format(rolls))

#call the dice roll method and print the results
roll_multiple_dice(100)
# print(results)

#calculate and show the standard deviation
# std = round(np.std(results), 2)
# print("The standard deviation is {}.".format(std))


#create a histogram for the results (requires)
def make_histogram(array):
    plt.hist(array, bins=10)
    plt.xlabel('number rolled')
    plt.ylabel('frequency')
    plt.show()

make_histogram(results)
