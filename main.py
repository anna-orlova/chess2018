from Board import Board
from View import View
from Player import Player

board = Board(Player("W"), Player("B"))
board.Initiate_StartBoard()

view = View(board)
view.Run()

