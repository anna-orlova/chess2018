from Board import Board
from View import View

board = Board()
board.Initiate_StartBoard()

view = View(board)
view.Show()
print (board.Figure_At("H1"))
