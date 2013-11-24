#!/usr/bin/python3


import tictactoe


def getMove(player):
	squares = { "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9 }
	choice = input("Player " + str(player) + ", Pick a square (1-9): ")
	try:
		return squares[choice]
	except KeyError:
		pass


if __name__ == '__main__':
	g = tictactoe.Game()
	while g.board.turns > 0 and g.winner is None:
		currentPlayer = g.board.turns % g.players
		move = getMove(currentPlayer)
		try:
			g.playerList[currentPlayer].move(move)
		except tictactoe.MoveError as e:
			print(e.msg)
	if g.winner is None:
		print("It's a draw!")
	else:
		print("Player", currentPlayer, "wins!")
