#!/usr/bin/python3


class Board():

	def __init__(self):
		self.squares = [ x for x in range(1,10) ]
		self.startSquares = list(self.squares)	# Copies the list rather than creating a second reference to it.

	def get_turns(self):
		return len(self.squares)

	turns = property(get_turns)


class Player():

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
				raise MoveError("You have taken that square already!")
			elif square in self.game.board.startSquares:
				raise MoveError("Another player has taken that square already!")
			else:
				raise MoveError("That square isn't on the board!")
		else:
			s = set(self.squares)
			for line in self.game.winMoves:
				if set(line).issubset(s):
					self.game.winner = self


class Game():

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
	"""Base class for exceptions in this module"""
	pass


class MoveError(Error):
	"""Exception raised for invalid player moves

	Attributes:
		msg -- explanation of the error
	"""
	
	def __init__(self, msg):
		self.msg = msg
