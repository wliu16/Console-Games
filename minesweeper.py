class minesweeper(object):
	def __init__(self, size, num_mines):
		self.size = size
		self.mine_map = [[0 for _ in xrange(0, size)] for _ in xrange(0, size)]
		self.summary_map = [[0 for _ in xrange(0, size)] for _ in xrange(0, size)]
		self.visited = [[0 for _ in xrange(0, size)] for _ in xrange(0, size)]

		import random
		count = 0
		while count < min(num_mines, size * size):
			x = random.randint(0, size - 1)
			y = random.randint(0, size - 1)
			if self.mine_map[x][y] == 0:
				self.mine_map[x][y] = 1
				count += 1

		neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		for x in xrange(0, size):
			for y in xrange(0, size):
				for nei in neighbors:
					i = x + nei[0]
					j = y + nei[1]
					if i in xrange(0, size) and j in xrange(0, size) and self.mine_map[i][j] == 1:
						self.summary_map[x][y] += 1


	def check_mine(self, x, y):
		self.visited[x][y] = 1
		return self.mine_map[x][y] == 1


	def print_map(self):
		coord = [str(x) for x in xrange(0, self.size)]
		print "   ", "   ".join(coord)
		for x in xrange(0, self.size):
			print x,
			for y in xrange(0, self.size):
				if self.visited[x][y] == 0:
					ch = ' ' 
				elif self.mine_map[x][y] == 1:
					ch = '*'
				else:
					ch = str(self.summary_map[x][y])
				print "|", ch,
			print "|\n"


	def check_finish(self):
		for x in xrange(0, self.size):
			for y in xrange(0, self.size):
				if self.mine_map[x][y] == 0 and self.visited[x][y] == 0:
					return False
		return True



# -------start playing ----------
play = True
while play:
	print "Welcome to Minesweeper!"

	size_map = int(raw_input("size of map? \n"))
	num_mines = int(raw_input("number of mines?\n"))
	game = minesweeper(size_map, num_mines)
	game.print_map()

	while True:
		user_input = raw_input("which coordinate do you want to sweep? (Format: x,y)\n")
		coord = map(int, user_input.split(','))
		if len(coord) != 2:
			continue 

		if game.check_mine(coord[0], coord[1]):
			print "You got mine!\n"
			game.print_map()
			break
		else:
			game.print_map()
			if game.check_finish():
				print "You win!\n"
				break

	play_again = raw_input("Play again? (y/n)\n")
	while play_again != "y" and play_again != "n":
		print "invalid input.\n"
		play_again = raw_input("Play again? (y/n)\n")
	if play_again == "n":
		play = False