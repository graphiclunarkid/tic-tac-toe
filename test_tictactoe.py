#!/usr/bin/python3


import unittest
import tictactoe


class TicTacToeTestCase(unittest.TestCase):
	"""Base class for test cases in this module"""

	def setUp(self, players = 1):
		self.players = players
		self.cols = 3
		self.rows = 3
		self.game = tictactoe.Game(self.players, self.cols, self.rows)

	def tearDown(self):
		self.game = None


class Test_Structure(TicTacToeTestCase):
	"""TDD: build objects needed for this module
	These tests aren't very useful any more but cost nothing to keep
	"""

	def test_board(self):
		self.assertIsInstance(self.game.board,tictactoe.Board)
		self.assertEqual(self.game.board.cols,self.cols)
		self.assertEqual(self.game.board.rows,self.rows)
		self.assertEqual(self.game.board.turns,(self.cols*self.rows))

	def test_player(self):
		self.assertIsInstance(self.game.playerList[0],tictactoe.Player)
		self.assertEqual(self.game.playerList[0].squares,[])

	def test_game(self):
		self.assertEqual(self.game.players,self.players)

class Test_Behaviour(TicTacToeTestCase):
	"""Test module objects behave correctly when their methods are called"""

	def setUp(self):
		super().setUp(2)

	def test_legal_move(self):
		move1 = (0,0)
		self.game.playerList[0].move(move1)
		self.assertEqual(self.game.board.turns,(self.cols*self.rows - 1))
		self.assertEqual(len(self.game.playerList[0].squares),1)
		self.assertListEqual(self.game.playerList[0].squares, [move1])
		self.assertListEqual(self.game.board.squares,[(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])

	def test_illegal_move(self):
		move1 = (-1,-1)
		with self.assertRaises(tictactoe.MoveError) as cm:
			self.game.playerList[0].move(move1)
		e = cm.exception
		self.assertEqual(e.msg, "That square isn't on the board!")

	def test_repeat_move_same_player(self):
		move1 = (0,0)
		with self.assertRaises(tictactoe.MoveError) as cm:
			self.game.playerList[0].move(move1)
			self.game.playerList[0].move(move1)
		e = cm.exception
		self.assertEqual(e.msg, "You have taken that square already!")

	def test_repeat_move_other_player(self):
		move1 = (0,0)
		with self.assertRaises(tictactoe.MoveError) as cm:
			self.game.playerList[0].move(move1)
			self.game.playerList[1].move(move1)
		e = cm.exception
		self.assertEqual(e.msg, "Another player has taken that square already!")


class Test_Gameplay(TicTacToeTestCase):
	"""Tests that the game runs correctly"""

	def test_win_condition(self):
		moves = [square for square in self.game.board.squares if square[0] == 0]
		for move in moves:
			self.game.playerList[0].move(move)
		self.assertIs(self.game.playerList[0],self.game.winner)


if __name__ == '__main__':
	unittest.main()

