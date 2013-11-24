#!/usr/bin/python3


import tictactoe


def getMove(player):
       squares = { "1":(0,0), "2":(0,1), "3":(0,2), "4":(1,0), "5":(1,1), "6":(1,2), "7":(2,0), "8":(2,1), "9":(2,2) }
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
               except MoveError as e:
                       print(e.msg)
       if g.winner is None:
               print("It's a draw!")
       else:
               print(g.winner, "wins!")
