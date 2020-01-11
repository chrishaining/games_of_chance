import numpy as np 

# create an empty board using a 2D array
board = np.array(
[["0", "1", "2"],
["3", "4", "5"],
["6", "7", "8"]])

# print(board)

# set co-ordinates for each of the squares
# def find_square(player_choice):
#     switcher = {
#         "0": board[0, 0],
#         "1": board[0, 1],
#         "2": board[0, 2],
#         "3": board[1, 0],
#         "4": board[1, 1],
#         "5": board[1, 2],
#         "6": board[2, 0],
#         "7": board[2, 1],
#         "8": board[2, 2],

#     } 
    # coordinates = switcher.get(player_choice, "Invalid choice")
    # return "Coordinates: {}".format(coordinates)
    # return switcher.get(player_choice)

# check the switcher is working (expect the answer for find_square("8") to be 8)
# print(find_square("8"))
# print(find_square("8"))

# second attempt to set the co-ordinates for each of the squares. The switcher didn't work.
def find_square(player_choice):
        coordinates = np.argwhere(board == player_choice)
        return coordinates

# test find_square. Expect input of "8" to return 2,2.
# print(find_square("8"))

# reset a square's value to X. This is the long way round. 
def set_square(player_choice):
    if player_choice == "0": 
        board[0, 0] = "X"
    elif player_choice == "1": 
        board[0, 1] = "X"
    elif player_choice == "2": 
        board[0, 2] = "X"
    elif player_choice == "3": 
        board[1, 0] = "X"
    elif player_choice == "4": 
        board[1, 1] = "X"
    elif player_choice == "5": 
        board[1, 2] = "X"
    elif player_choice == "6": 
        board[2, 0] = "X"
    elif player_choice == "7": 
        board[2, 1] = "X"
    elif player_choice == "8": 
        board[2, 2] = "X"
    else:
        print("You've entered an invalid choice.")

#get the user to add to the board
def add_a_square():
    print("We're going to play noughts and crosses.")
    square = input("Pick a square: ")
    check_if_square_has_been_used()
    set_square(square)
    print(board)

# add_a_square()
# print(board)

# check if a square has already been used
# def check_if_square_has_been_used():
#     for item in board:
#         if item == "X":
#             return "That's already been used"

def check_if_square_has_been_used():
    if board.size > 0:
     if np.any(board == "X"):
        return "That's already been used"


def play():
    while np.any(board != "X"):
        add_a_square()

play()