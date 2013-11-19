#!/usr/bin/python


import unittest
import tictactoe


class TicTacToeTestCase(unittest.TestCase):

	def setUp(self):
		self.players = 2
		self.cols = 3
		self.rows = 3
		self.game = tictactoe.Game(self.players, self.cols, self.rows)
		self.p1 = tictactoe.Player(self.game)

	def testGame(self):
		self.assertIsInstance(self.game,tictactoe.Game)
		self.assertEqual(self.game.players,self.players)
		self.assertEqual(self.game.cols,self.cols)
		self.assertEqual(self.game.rows,self.rows)
		self.assertEqual(self.game.turns,(self.cols*self.rows))

	def testPlayer(self):
		self.assertIsInstance(self.p1,tictactoe.Player)
		self.assertEqual(self.p1.squares,[])
		self.p1.move()
		self.assertEqual(self.game.turns,(self.cols*self.rows - 1))
		self.assertEqual(len(self.p1.squares),1)

if __name__ == '__main__':
	unittest.main()

