#!/usr/bin/python


import unittest
import tictactoe


class TicTacToeTestCase(unittest.TestCase):
	def testGame(self):
		self.game = tictactoe.Game()
		self.assertIsInstance(self.game,tictactoe.Game)
		self.assertEqual(self.game.players,2)
		self.assertEqual(self.game.cols,3)
		self.assertEqual(self.game.rows,3)
		self.assertEqual(self.game.turns,9)


if __name__ == '__main__':
	unittest.main()

