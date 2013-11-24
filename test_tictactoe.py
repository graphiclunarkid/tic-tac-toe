#!/usr/bin/python3


import unittest
import tictactoe


class TicTacToeTestCase(unittest.TestCase):

	def setUp(self):
		self.players = 2
		self.cols = 3
		self.rows = 3
		self.game = tictactoe.Game(self.players, self.cols, self.rows)
		self.p1 = tictactoe.Player(self.game)

	def tearDown(self):
		self.game = None
		self.p1 = None

	def test_game(self):
		self.assertIsInstance(self.game,tictactoe.Game)
		self.assertEqual(self.game.players,self.players)
		self.assertEqual(self.game.cols,self.cols)
		self.assertEqual(self.game.rows,self.rows)
		self.assertEqual(self.game.turns,(self.cols*self.rows))

	def test_player(self):
		self.assertIsInstance(self.p1,tictactoe.Player)
		self.assertEqual(self.p1.squares,[])

	def test_legal_move(self):
		move1 = (0,0)
		self.p1.move(move1)
		self.assertEqual(self.game.turns,(self.cols*self.rows - 1))
		self.assertEqual(len(self.p1.squares),1)
		self.assertListEqual(self.p1.squares, [move1])
		self.assertListEqual(self.game.board,[(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])

	def test_illegal_move(self):
		move1 = (-1,-1)
		with self.assertRaises(ValueError) as contextManager:
			self.p1.move(move1)
		exception = contextManager.exception
		self.assertEqual(exception.message, 'Square not available')

	def test_repeat_move(self):
		move1 = (0,0)
		self.p1.move(move1)
		self.assertRaises(ValueError, self.p1.move, move1)

	def test_win_condition(self):
		moves = [square for square in self.game.board if square[0] == 0]
		for move in moves:
			self.p1.move(move)
		self.assertIs(self.p1,self.game.winner)


if __name__ == '__main__':
	unittest.main()

