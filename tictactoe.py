#!/usr/bin/python3


class Game():

	def __init__(self, players = 2, cols = 3, rows = 3):
		self.players = players
		self.cols = cols
		self.rows = rows
		self.board = [(x, y) for x in range(cols) for y in range(rows)]
		self.startBoard = list(self.board)	# Copies the list rather than creating a second reference to it.
		self.winner = None
		self.winMoves = frozenset(((0,0),(0,1),(0,2)))

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
			if square in self.squares:
				raise MoveError("You have taken that square already!")
			elif square in self.game.startBoard:
				raise MoveError("Another player has taken that square already!")
			else:
				raise MoveError("That square isn't on the board!")
		else:
			if set(map(tuple, self.squares)) == self.game.winMoves:
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
