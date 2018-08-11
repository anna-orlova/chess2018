import unittest
from Board import Board
from Player import Player
from Figure import *

class TestBoard(unittest.TestCase):

    def test_Initiate_StartBoard(self):
        player_one = Player("W")
        board = Board(player_one, Player("B"))
        board.Initiate_StartBoard()

        self.assertEqual(board.Figure_At("A2"), Pawn(player_one))
        self.assertEqual(board.Figure_At("B2"), Pawn(player_one))
        self.assertEqual(board.Figure_At("C2"), Pawn(player_one))
