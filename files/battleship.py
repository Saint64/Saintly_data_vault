from random import randint

#initializing board
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

#starting the game and printing the board
print "Let's play Battleship!"
print_board(board)

#defining where the ship is
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
'''The reason the 0 is in brackets is to differentiate the column set 
of variables from the  row set of random variables.  If the variables
were both defined by the variable board, than the x and y coordinates
of the battle ship would be equal.'''
ship_row = random_row(board)
ship_col = random_col(board)

#asking the user for a guess
for turn in range(25):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    # if the user's right, the game ends
    if guess_row == ship_row and guess_col == ship_col:
        print "HCKR. Let me get my AK47 1v1 ill rek u no gg bro."
        break
    else:
        #warning if the guess is out of the board
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "DUDE! FRIENDLY FIRE IS ENABLED!! WATCH YOUR AIM, YOU DINGUS!!!."
        
        #warning if the guess was already made
        elif(board[guess_row][guess_col] == "X"):
            print "Uh, you already sunk that ship, genuis."
        
        #if the guess is wrong, mark the point with an X and start again
        else:
            print "HA! Your aim sucks."
            board[guess_row][guess_col] = "X"
        
        # Print turn and board again here
        print "Turn " + str(turn+1) + " out of 25." 
        print_board(board)

#if the user have made 25 tries, it's game over
if turn >= 24:
    print "You lose, sucker!"