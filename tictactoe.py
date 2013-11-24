#!/usr/bin/python3


class Game():

	def __init__(self, players = 2, cols = 3, rows = 3):
		self.players = players
		self.cols = cols
		self.rows = rows
		self.board = [(x, y) for x in range(cols) for y in range(rows)]
		self.winner = None
		self.winmoves = frozenset(((0,0),(0,1),(0,2)))

	def get_turns(self):
		return len(self.board)

	turns = property(get_turns)


class Player():

	def __init__(self, game, squares = None):
		self.game = game
		if squares is None:	# Google for "default parameter values in python"
			squares = []
		self.squares = squares

	def move(self, square):
		try:
			self.squares.append(self.game.board.pop(self.game.board.index(square)))
		except ValueError:
			raise MoveError('Square not available')
		else:
			if set(map(tuple, self.squares)) == self.game.winmoves:
				self.game.winner = self


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
