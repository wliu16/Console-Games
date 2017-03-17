class tic_tac_to(object):
	player_sign = ['X', 'O']

	def __init__(self):
		self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
		self.test_row = [0, 0, 0]
		self.test_col = [0, 0, 0]
		self.test_dia = 0
		self.test_antidia = 0

	def valid_user_input(self, x, y):
		if x in xrange(0, 3) and y in xrange(0, 3) and self.board[x][y] == '-':
			return True
		else:
			return False

	def print_board(self):
		for x in xrange(0, 3):
			for y in xrange(0, 3):
				if y == 0:
					print '|',
				print self.board[x][y], '|',
				if y == 2:
					print '\n'

	def make_move(self, num_player, x, y):
		sign = 1 if num_player == 0 else -1

		self.board[x][y] = tic_tac_to.player_sign[num_player]
		self.test_row[x] += sign
		self.test_col[y] += sign
		if x == y:
			self.test_dia += sign
		if x + y == 2:
			self.test_antidia += sign

	def check_win(self, num_player):
		sign = 1 if num_player == 0 else -1

		for i in self.test_row:
			if i == sign * 3:
				return True
		for i in self.test_col:
			if i == sign * 3:
				return True
		if self.test_dia == sign * 3:
			return True
		if self.test_antidia == sign * 3:
			return True
		return False

	def check_full(self):
		for row in self.board:
			for cell in row:
				if cell == '-':
					return False
		return True

	# algo for computer put
	def algo(self, num_comp):
		sign = 1 if num_comp == 0 else -1

		# step1: to win
		if self.test_dia == 2 * sign:
			for x in xrange(0, 3):
				if self.board[x][x] == '-':
					return [x, x]
		if self.test_antidia == 2 * sign:
			for x in xrange(0, 3):
				if self.board[x][2 - x] == '-':
					return [x, 2 - x]
		for x in xrange(0, 3):
			if self.test_row[x] == 2 * sign:
				for y in xrange(0, 3):
					if self.board[x][y] == '-':
						return [x, y]
		for y in xrange(0, 3):
			if self.test_col[y] == 2 * sign:
				for x in xrange(0, 3):
					if self.board[x][y] == '-':
						return [x, y]

		# step2: check and block user's almost win
		if self.test_dia == -2 * sign:
			for x in xrange(0, 3):
				if self.board[x][x] == '-':
					return [x, x]
		if self.test_antidia == -2 * sign:
			for x in xrange(0, 3):
				if self.board[x][2 - x] == '-':
					return [x, 2 - x]
		for x in xrange(0, 3):
			if self.test_row[x] == -2 * sign:
				for y in xrange(0, 3):
					if self.board[x][y] == '-':
						return [x, y]
		for y in xrange(0, 3):
			if self.test_col[y] == -2 * sign:
				for x in xrange(0, 3):
					if self.board[x][y] == '-':
						return [x, y]

		# step3: make almost_win
		if self.test_dia == sign:
			for x in xrange(0, 3):
				if self.board[x][x] == '-':
					return [x, x]
		if self.test_antidia == sign:
			for x in xrange(0, 3):
				if self.board[x][2 - x] == '-':
					return [x, 2 - x]
		for x in xrange(0, 3):
			if self.test_row[x] == sign:
				for y in xrange(0, 3):
					if self.board[x][y] == '-':
						return [x, y]
		for y in xrange(0, 3):
			if self.test_col[y] == sign:
				for x in xrange(0, 3):
					if self.board[x][y] == '-':
						return [x, y]

		# step4: prefer center
		if self.board[1][1] == '-':
			return [1, 1]

		# step5:put in a random
		for x in xrange(0, 3):
			for y in xrange(0, 3):
				if self.board[x][y] == '-':
					return [x, y]
# ----end algo-----------------------------
#------------------end class definition----------------------


# --------------start playing ------------
play = True
while play:
	print "Welcome to tic tac to!"
	game = tic_tac_to()

	answer = raw_input("Do you want to play first? (y/n)\n")
	while answer != 'y' and answer != 'n':
		print "not valid input"
		answer = raw_input("Do you want to play first? (y/n)\n")
	#assgin num and sign to players
	if answer == 'y':
		user = 0
		computer = 1
	else:
		computer = 0
		user = 1
		#computer makes first move
		first_move = game.algo(computer)
		game.make_move(computer, first_move[0], first_move[1])

	while True:
		game.print_board()

		#user input
		user_input = int(raw_input("Where do you want to put? (enter a number from 1 to 9)\n"))
		while not game.valid_user_input((user_input - 1) / 3, (user_input - 1) % 3):
			print "Input not valid. "
			user_input = int(raw_input("Where do you want to put? (enter a number from 1 to 9)\n"))

		#user move
		game.make_move(user, (user_input - 1) / 3, (user_input - 1) % 3)
		if game.check_win(user):
			play = raw_input("You win! Play again? (y/n)\n")
			if play == 'n':
				play = False
			break
		if game.check_full():
			play = raw_input("Board full. Play again? (y/n)\n")
			if play == 'n':
				play = False
			break

		#computer move
		comp_move = game.algo(computer)
		game.make_move(computer, comp_move[0], comp_move[1])
		if game.check_win(computer):
			game.print_board()
			play = raw_input("You lose. Play again? (y/n)\n")
			if play == 'n':
				play = False
			break
		if game.check_full():
			game.print_board()
			play = raw_input("Board full. Play again? (y/n)\n")
			if play == 'n':
				play = False
			break
