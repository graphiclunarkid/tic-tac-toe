#!/usr/bin/python3


class Game():

	def __init__(self, players = 2, cols = 3, rows = 3):
		self.players = players
		self.cols = cols
		self.rows = rows
		self.board = [[x,y] for x in range(cols) for y in range(rows)]

	def get_turns(self):
		return len(self.board)

	turns = property(get_turns)


class Player():

	def __init__(self, game, squares = []):
		self.game = game
		self.squares = squares

	def move(self, square):
		self.squares.append(self.game.board.pop(self.game.board.index(square)))
