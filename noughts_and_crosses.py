import numpy as np 

# create an empty board using a 2D array
board = np.array(
[["", "", ""],
["", "", ""],
["", "", ""]])

print(board)


#get the user to add to the board
def user_call():
    print("I'm going to flip a coin.")
    call = input("Do you call heads or tails?: ").title()
    return call