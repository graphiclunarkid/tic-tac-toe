#!/usr/bin/python3


import unittest
import tictactoe


class TicTacToeTestCase(unittest.TestCase):
	"""Base class for test cases in this module"""

	def setUp(self, players = 1):
		self.players = players
		self.game = tictactoe.Game(self.players)

	def tearDown(self):
		self.game = None


class Test_Structure(TicTacToeTestCase):
	"""TDD: build objects needed for this module
	These tests aren't very useful any more but cost nothing to keep
	"""

	def test_board(self):
		self.assertIsInstance(self.game.board,tictactoe.Board)
		self.assertEqual(self.game.board.turns, 9)

	def test_player(self):
		self.assertIsInstance(self.game.playerList[0], tictactoe.Player)
		self.assertEqual(self.game.playerList[0].squares, [])

	def test_game(self):
		self.assertEqual(self.game.players, self.players)


class Test_Behaviour(TicTacToeTestCase):
	"""Test module objects behave correctly when their methods are called"""

	def setUp(self):
		super().setUp(2)

	def test_legal_move(self):
		move1 = 1
		self.game.playerList[0].move(move1)
		self.assertEqual(self.game.board.turns, 8)
		self.assertEqual(len(self.game.playerList[0].squares), 1)
		self.assertListEqual(self.game.playerList[0].squares, [move1])
		self.assertListEqual(self.game.board.squares, [ 2, 3, 4, 5, 6, 7, 8, 9 ])

	def test_illegal_move(self):
		move1 = 0
		with self.assertRaises(tictactoe.MoveError) as cm:
			self.game.playerList[0].move(move1)
		e = cm.exception
		self.assertEqual(e.msg, "That square isn't on the board!")

	def test_repeat_move_same_player(self):
		move1 = 1
		with self.assertRaises(tictactoe.MoveError) as cm:
			self.game.playerList[0].move(move1)
			self.game.playerList[0].move(move1)
		e = cm.exception
		self.assertEqual(e.msg, "You have taken that square already")

	def test_repeat_move_other_player(self):
		move1 = 1
		with self.assertRaises(tictactoe.MoveError) as cm:
			self.game.playerList[0].move(move1)
			self.game.playerList[1].move(move1)
		e = cm.exception
		self.assertEqual(e.msg, "The other player has taken that square already")


class Test_Gameplay(unittest.TestCase):
	"""Tests that the game runs correctly"""

	def setUp(self):
		self.moveList = []

	def doMoves(self):
		for moves in self.moveList:
			g = tictactoe.Game(1)
			for move in moves:
				g.playerList[0].move(move)
			self.assertIs(g.playerList[0], g.winner)
			g = None

	def test_win_conditions_rows(self):

		# Horizontal rows
		self.moveList.append( [ 1, 2, 3 ] )
		self.moveList.append( [ 4, 5, 6 ] )
		self.moveList.append( [ 7, 8, 9 ] )
		self.doMoves()

	def test_win_conditions_cols(self):
		# Vertical columns
		self.moveList.append( [ 1, 4, 7 ] )
		self.moveList.append( [ 2, 5, 8 ] )
		self.moveList.append( [ 3, 6, 9 ] )
		self.doMoves()

	def test_win_conditions_diags(self):
		# Diagonals
		self.moveList.append( [ 1, 5, 9 ] )
		self.moveList.append( [ 3, 5, 7 ] )
		self.doMoves()

	def test_win_conditions_reverse(self):
		# Reversed rows/cols/diags to check order is unimportant
		self.moveList.append( [ 2, 3, 1 ] )
		self.moveList.append( [ 8, 5, 2 ] )
		self.moveList.append( [ 9, 5, 1 ] )
		self.doMoves()

	def test_win_conditions_long(self):
		# Longer move sequences containing winning sets
		self.moveList.append( [ 9, 1, 6, 7, 8 ] )
		self.moveList.append( [ 1, 3, 7, 9, 5 ] )
		self.moveList.append( [ 2, 4, 6, 8, 5 ] )
		self.doMoves()

	def test_draw_conditions(self):
		# Should result in a draw (i.e. no win condition contained in set)
		self.moveList.append( [ 5, 9, 2, 4, 7 ] )
		self.moveList.append( [ 7, 1, 6, 2, 8 ] )
		for moves in self.moveList:
			g = tictactoe.Game(1)
			for move in moves:
				g.playerList[0].move(move)
			self.assertIs(g.winner, None)
			g = None


if __name__ == '__main__':
	unittest.main()

