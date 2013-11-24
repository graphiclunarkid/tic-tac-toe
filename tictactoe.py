#!/usr/bin/python3


class Board():

	""" A class to represent a tic-tac-toe board, which comprises 9 squares

	Attributes:
		squares -- List of squares that are available to be picked.

		startSquares -- List of squares that were available when the
		game started.

		turns -- The max number of turns remaining (number of squares
		left to be picked).
	"""

	def __init__(self):
		self.squares = [ x for x in range(1,10) ]
		self.startSquares = list(self.squares)	# Copies the list rather than creating a second reference to it.

	def get_turns(self):
		return len(self.squares)

	turns = property(get_turns)


class Player():

	""" A class to represent a player.

	Attributes:
		squares -- The set of squares this player has picked.

	Methods:
		move -- Attempt to pick the specified square.  Throws a
		MoveError exception if the square doesn't exist or has been
		taken already.  Sets the player as the game winner if their set
		of picked squares contains a winning line.
	"""

	def __init__(self, game, squares = None):
		self.game = game
		if squares is None:	# Google for "default parameter values in python"
			squares = []
		self.squares = squares

	def move(self, square):
		try:
			self.squares.append(self.game.board.squares.pop(self.game.board.squares.index(square)))
		except ValueError:
			if square in self.squares:
				raise MoveError("You have taken that square already")
			elif square in self.game.board.startSquares:
				raise MoveError("The other player has taken that square already")
			else:
				raise MoveError("That square isn't on the board!")
		else:
			s = set(self.squares)
			for line in self.game.winMoves:
				if set(line).issubset(s):
					self.game.winner = self


class Game():

	""" A class to represent a game of tic-tac-toe.

	Attributes:
		winner -- The player object that has won the game.

		board -- Object containing the playing surface

		players -- The number of players involved in this game. (Two
		for real games, but some of the tests use a single player)

		playerList -- List of player objects involved in this game.

		winMoves -- List of lists representing all possible winning
		combinations of squares (rows, columns and diagonals.)
	"""

	def __init__(self, players = 2):
		self.winner = None
		self.board = Board()
		self.playerList = [Player(self) for p in range(players)]

		self.winMoves = []

		# Horizontal rows
		self.winMoves.append( [ 1, 2, 3 ] ) 
		self.winMoves.append( [ 4, 5, 6 ] ) 
		self.winMoves.append( [ 7, 8, 9 ] ) 

		# Vertical columns
		self.winMoves.append( [ 1, 4, 7 ] ) 
		self.winMoves.append( [ 2, 5, 8 ] ) 
		self.winMoves.append( [ 3, 6, 9 ] ) 

		# Diagonals
		self.winMoves.append( [ 1, 5, 9 ] ) 
		self.winMoves.append( [ 3, 5, 7 ] ) 

	def get_players(self):
		return len(self.playerList)

	players = property(get_players)


class Error(Exception):

	""" Base class for exceptions in this module.
	"""
	
	pass


class MoveError(Error):

	""" Exception raised for invalid player moves.

	Attributes:
		msg -- Explanation of the error.
	"""
	
	def __init__(self, msg):
		self.msg = msg


def getMove(player):

	""" A function to prompt players for their moves.
	
	If the player picks a move not in the "squares" list a KeyError
	exception is thrown however we pass this so that the MoveError
	exception will be thrown by the Player.move() method instead.

	Returns:
		The user's input, converted to an integer if it represented a
		valid square.
	"""

	squares = { "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9 }
	choice = input("Player " + str(player + 1) + ", pick a square (1-9): ")
	try:
		return squares[choice]
	except KeyError:
		pass


if __name__ == '__main__':

	""" This is the main game loop.

	Process:
		1. Create a new game with two players
		2. First player is prompted to pick a square
		3. Rotate between all players until one wins or all squares
		have been picked.
		4. Print a message depending on the outcome of the game
	"""

	g = Game()
	while g.board.turns > 0 and g.winner is None:
		currentPlayer = 1 - (g.board.turns % g.players)
		move = getMove(currentPlayer)
		try:
			g.playerList[currentPlayer].move(move)
		except MoveError as e:
			print(e.msg)
	if g.winner is None:
		print("It's a draw!")
	else:
		print("Player", currentPlayer + 1, "wins!")

