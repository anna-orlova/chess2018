from Board import Board
from View import View
from Player import Player
from CoordinatesToSymbols import *
from Exceptions import *

board = Board(Player("W"), Player("B"))
board.Initiate_StartBoard()

view = View(board)
view.Run()

