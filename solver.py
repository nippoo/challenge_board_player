import numpy as np
n_games = 200

def check_valid_board(brd):
# Checks if a given 3 x 3 board is valid.
# Returns 0 (invalid), 1 (valid), 2 (black win), 3 (white win)

	black_pos = (brd == 1)
	white_pos = (brd == 2)

	# Check there aren't too many pieces on the board
	if((np.count_nonzero(black_pos) > 3) | (np.count_nonzero(white_pos) > 3)):
		print(brd)
		print("Too many pieces")
		return 0

	# Check there's a valid number of white/black pieces
	if(0 > (np.count_nonzero(black_pos) - np.count_nonzero(white_pos)) > 1):
		print(brd)
		print("Piece mismatch")
		return 0

	winning_positions = np.array(	[[[True, True, True],
									[False, False, False],
									[False, False, False]],

									[[False, False, False],
									[True, True, True],
									[False, False, False]],

									[[False, False, False],
									[False, False, False],
									[True, True, True]],

									[[True, False, False],
									[True, False, False],
									[True, False, False]],

									[[False, True, False],
									[False, True, False],
									[False, True, False]],

									[[False, False, True],
									[False, False, True],
									[False, False, True]],

									[[True, False, False],
									[False, True, False],
									[False, False, True]],

									[[False, False, True],
									[False, True, False],
									[True, False, False]]])
	# Has black won?
	if(any(np.array_equal(x, black_pos) for x in winning_positions)):
		print("Black wins!")
		return 2

	# Has white won?
	if(any(np.array_equal(x, white_pos) for x in winning_positions)):
		print("White wins!")
		return 3

	return 1

def black_player(brd):
	# Randomly places a valid piece; if all 3 are on the board, randomly moves one
	empty_pos = (brd == 0)
	my_pos = (brd == 1)
	opponent_pos = (brd == 2)

	if(np.count_nonzero(my_pos) < 3): # place a new piece!
		x,y = np.where(empty_pos)
		i = np.random.randint(len(x))
		brd[x[i], y[i]] = 1
		return brd

	else:
		return brd

def white_player(brd):
	# Randomly places a valid piece; if all 3 are on the board, randomly moves one
	empty_pos = (brd == 0)
	my_pos = (brd == 2)
	opponent_pos = (brd == 1)

	if(np.count_nonzero(my_pos) < 3): # place a new piece!
		x,y = np.where(empty_pos)
		i = np.random.randint(len(x))
		brd[x[i], y[i]] = 2
		return brd

	else:
		return brd

def play_game(max_turns):
	# Start with no pieces
	curr_board = np.zeros([3, 3]) # 0 blank, 1 black, 2 white
	turnno = 1

	while((turnno <= max_turns)):
		print("\nTurn number: {}".format(turnno))
		if turnno % 2 == 1:
			print("Black to play!")
			curr_board = black_player(curr_board)
		else:
			print("White to play")
			curr_board = white_player(curr_board)
		turnno += 1
		print(curr_board)

		a = check_valid_board(curr_board)
		if(a == 0):
			exit("Invalid board, exiting")
		if(a == 1):
			continue
		else: #there's been a winner!
			return a

black_wins = 0
white_wins = 0

for i in range(n_games):
	a = play_game(6)
	if a == 2:
		black_wins +=1
	elif a == 3:
		white_wins +=1

print("Played {} games. Black wins {} times, white wins {} times".format(n_games, black_wins, white_wins))