#!/usr/bin/python3


class Board():

	def __init__(self, players = 2, cols = 3, rows = 3):
		self.players = players
		self.cols = cols
		self.rows = rows
		self.squares = [(x, y) for x in range(cols) for y in range(rows)]
		self.startSquares = list(self.squares)	# Copies the list rather than creating a second reference to it.
		self.winner = None
		self.winMoves = frozenset(((0,0),(0,1),(0,2)))

	def get_turns(self):
		return len(self.squares)

	turns = property(get_turns)


class Player():

	def __init__(self, board, squares = None):
		self.board = board
		if squares is None:	# Google for "default parameter values in python"
			squares = []
		self.squares = squares

	def move(self, square):
		try:
			self.squares.append(self.board.squares.pop(self.board.squares.index(square)))
		except ValueError:
			if square in self.squares:
				raise MoveError("You have taken that square already!")
			elif square in self.board.startSquares:
				raise MoveError("Another player has taken that square already!")
			else:
				raise MoveError("That square isn't on the board!")
		else:
			if set(map(tuple, self.squares)) == self.board.winMoves:
				self.board.winner = self


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
