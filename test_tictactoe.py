#!/usr/bin/python


import unittest
import tictactoe


class TicTacToeTestCase(unittest.TestCase):

	def setUp(self):
		self.players = 2
		self.cols = 3
		self.rows = 3
		self.game = tictactoe.Game(self.players, self.cols, self.rows)

	def testGame(self):
		self.game = tictactoe.Game()
		self.assertIsInstance(self.game,tictactoe.Game)
		self.assertEqual(self.game.players,self.players)
		self.assertEqual(self.game.cols,self.cols)
		self.assertEqual(self.game.rows,self.rows)
		self.assertEqual(self.game.turns,(self.cols*self.rows))

	def testPlayer(self):
		self.player = tictactoe.Player()
		self.assertIsInstance(self.player,tictactoe.Player)
		self.assertEqual(self.player.squares,[])


if __name__ == '__main__':
	unittest.main()

