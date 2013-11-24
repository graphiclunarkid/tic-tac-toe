#!/usr/bin/python3


import unittest
import tictactoe


class TicTacToeTestCase(unittest.TestCase):

	""" Base class for structure and behaviour test-case classes in this
	module.

	Methods:
		setUp -- Creates a tictactoe game instance with the specified
		number of players
	
		tearDown -- Makes sure the game instance is destroyed between
		tests.
	"""

	def setUp(self, players = 1):
		self.players = players
		self.game = tictactoe.Game(self.players)

	def tearDown(self):
		self.game = None


class Test_Structure(TicTacToeTestCase):

	""" Test class that helped in building objects needed for this module.
	These tests aren't very useful any more but cost nothing to keep.

	Methods:
		test_board -- Tests that the Board class can be instantiated
		and that it has 9 turns (3x3 grid).

		test_player -- Tests that the Player class can be instantiated
		and that it starts with an empty set of picked squares.

		test_game -- Tests that the Game class can be instantiated and
		that it creates the correct number of players.
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

	""" Test module objects behave correctly when their methods are called
	
	Methods:
		setUp -- Overrides base class setUp to instantiate a two-player game.

		test_legal_move -- Tests that a legal move can be made.
		Makes sure that a move decrements the number of turns left in
		the game, increments the number of squares picked by the
		player, that the player's list of picked squares contains the
		square just picked, and that the list of remaining squares does
		not.

		test_illegal_move -- checks that passing an illegal square to
		the move method raises an exception with an appropriate
		message.
		
		test_repeat_move_same_player -- Checks that a player can't pick
		the same square twice (appropriate message if they try).
		
		test_repeat_move_other_player -- Checks that a player can't
		pick a square that has been picked by another player already
		(appropriate message if they try).
	"""

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
	""" Tests that the game runs correctly.
	Actually just tests that win and draw conditions are correct at the
	moment.
	TODO: Test that turns alternate correctly
	NOTE: This class is not a subclass of TicTacToeTestCase

	Methods:
		setUp -- Preate an empty list of moves

		doMoves -- Perform a predetermined list of moves and test that
		the win condition is detected. Creates a new game object for
		each sequence of moves.

		test_win_conditions_rows -- Check that picking all squares in a
		row wins the game.

		test_win_conditions_cols -- Check that picking all squares in a
		column wins the game.

		test_win_conditions_diags -- Check that picking all squares in
		a diagonal line wins the game.

		test_win_conditions_reverse -- Check that the game can be won
		regardless of the order in which squares are picked.

		test_win_conditions_long -- Check that move sequences longer
		than winning lines result in winning the game.

		test_draw_conditions -- Check that max-length move sequences
		that don't contain a win line do not win the game (a draw by
		inference)
	"""

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

