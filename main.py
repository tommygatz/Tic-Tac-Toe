import time


class player:
    name = ""
    wins = 0
    symb = ""


# clears the board
def empty_board():
    x = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
    return x


# input player names
def get_players():
    p1.name = input("Enter the name of Player 1: ")
    p1.symb = input(p1.name + ", pick X's or O's: ").upper()

    p2.name = input("Enter the name of Player 2: ")

    if p1.symb == "X":
        p2.symb = "O"
    else:
        p2.symb = "X"

    print(p2.name + " will be " + p2.symb.upper() + "'s.")
    print("\nPlayers are: " + p1.name + " vs. " + p2.name)

    return p1, p2


# display scores
def scores():
    print("The score is:\n")
    print(p1.name + ": " + str(p1.wins) + " win(s)")
    print(p2.name + ": " + str(p2.wins) + " win(s)")


# display game board
def display_board():
    print("    1 | 2 | 3")
    print("A | " + board[0] + " | " + board[1] + " | " + board[2])
    print("B | " + board[3] + " | " + board[4] + " | " + board[5])
    print("C | " + board[6] + " | " + board[7] + " | " + board[8])


# flip player state
def flip_player():
    new_turn = turn
    if new_turn == p1:
        new_turn = p2
    else:
        new_turn = p1

    return new_turn


# end game
def keep_playing():
    x = input("\nPress enter to play another game, or type 'quit' to stop playing. ")
    return x


# conversion from user input to board array key
def convert_key(x):
    values = {"A": "0", "B": "3", "C": "6"}
    row = x[0]
    column = int(x[1])
    key = int(values[row]) + column - 1
    return key


# check board for a win
def check_win():

    # check rows
    if (board[0] == p1.symb and board[1] == p1.symb and board[2] == p1.symb) or (
            board[3] == p1.symb and board[4] == p1.symb and board[5] == p1.symb) or (
            board[6] == p1.symb and board[7] == p1.symb and board[8] == p1.symb):
        result = p1
    elif (board[0] == p2.symb and board[1] == p2.symb and board[2] == p2.symb) or (
            board[3] == p2.symb and board[4] == p2.symb and board[5] == p2.symb) or (
            board[6] == p2.symb and board[7] == p2.symb and board[8] == p2.symb):
        result = p2

    # check columns
    elif (board[0] == p1.symb and board[3] == p1.symb and board[6] == p1.symb) or (
            board[1] == p1.symb and board[4] == p1.symb and board[7] == p1.symb) or (
            board[2] == p1.symb and board[5] == p1.symb and board[8] == p1.symb):
        result = p1
    elif (board[0] == p2.symb and board[3] == p2.symb and board[6] == p2.symb) or (
            board[1] == p2.symb and board[4] == p2.symb and board[7] == p2.symb) or (
            board[2] == p2.symb and board[5] == p2.symb and board[8] == p2.symb):
        result = p2

    # check diagonals
    elif (board[0] == p1.symb and board[4] == p1.symb and board[8] == p1.symb) or (
            board[2] == p1.symb and board[4] == p1.symb and board[6] == p1.symb):
        result = p1
    elif (board[0] == p2.symb and board[4] == p2.symb and board[8] == p2.symb) or (
            board[2] == p2.symb and board[4] == p2.symb and board[6] == p2.symb):
        result = p2
    else:
        result = ""

    return result


# check board for a tie
def check_tie():
    if "-" not in board:
        x = True
    else:
        x = False
    return x


# play game
board = empty_board()
p1 = player()
p2 = player()
turn = p1
play_game = ""
spot_key = 0
valid_spots = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
valid_selection = False
spots_used = []

print("Let's play Tic-Tac-Toe!\n")

get_players()

time.sleep(2)
print("\nMake your selection by typing the Row and Column. ex: 'A1' or 'C2'.")
time.sleep(2)



while play_game != "quit":
    print("\n" + turn.name + ", it is your turn.\n")
    display_board()
    valid_selection = False
    while not valid_selection:
        selection = str(input("\nMake your move: ")).upper()
        if selection.lower() != "quit":
            if selection not in valid_spots:
                print("Please make a valid selection.")
                valid_selection = False
                spot_key = 0
            elif selection in spots_used:
                print("That spot has already been played. Please try again.")
                valid_selection = False
            else:
                spot_key = int(convert_key(selection))
                valid_selection = True
        else:
            play_game = selection.lower()
            break
    board[spot_key] = turn.symb.upper()
    spots_used.append(valid_spots[spot_key])
    print('\n')
    
    winner = check_win()
    if not winner:
        tie = check_tie()
        if not tie:
            turn = flip_player()
        else:
            print("We have a tie!!")
            board = empty_board()
            spots_used = []
            play_game = keep_playing()

    else:
        print(winner.name + " is the winner!\n")
        board = empty_board()
        spots_used = []
        if winner.name == p1.name:
            p1.wins += 1
        else:
            p2.wins += 1
        print("\n")
        scores()
        play_game = keep_playing()

    continue

print("Here is the final score: ")
print(p1.name + ": " + str(p1.wins) + " win(s)")
print(p2.name + ": " + str(p2.wins) + " win(s)")
print("\nThanks for playing!")
time.sleep(3)
