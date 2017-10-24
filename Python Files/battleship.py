# Battleship ex project that I made when learned from codecademy.
# State: Finished

from random import randint
import os
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
	allowed_input = "0123456789"
	guess_row = (raw_input("Guess Row:"))
	if guess_row not in allowed_input:
		print "Enter a number."
	else:
		guess_row = int(guess_row)
	guess_col = (raw_input("Guess Col:"))
	if guess_col not in allowed_input:
		print "Enter a number."
	else:
		guess_col = int(guess_col)
	if turn < 3:
		print "Turn", turn + 1
		print_board(board)
		
	if guess_row == ship_row and guess_col == ship_col:
		print "Congratulations! You sunk my battleship!"
		break
	else:
		if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
			print "Oops, that's not even in the ocean."
		elif(board[guess_row][guess_col] == "X"):
			print "You guessed that one already."
		else:
			print "You missed my battleship!"
			board[guess_row][guess_col] = "X"
		if turn == 3:
			os.system('cls')
			print "Game Over"
