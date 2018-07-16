from Figure import *
from Player import Player
from Exceptions import InvalidPosition

class Board(object):
    def __init__(self):
        List_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        List_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        self.board = {} # empty dictionary
        current_field = [] # empty list
        for item1 in List_letters:
            for item2 in List_numbers:
                current_field.append(item1 + str(item2))
                self.board[item1 + str(item2)] = None

    def Initiate_StartBoard(self):
        player_white = Player("W")
        player_black = Player("B")
        self._Add_Figure(Tor(player_white), "A1")
        self._Add_Figure(Knight(player_white), "B1")
        self._Add_Figure(Bishop(player_white), "C1")
        self._Add_Figure(Queen(player_white), "D1")
        self._Add_Figure(King(player_white), "E1")
        self._Add_Figure(Bishop(player_white), "F1")
        self._Add_Figure(Knight(player_white), "G1")
        self._Add_Figure(Tor(player_white), "H1")
        for item3 in "ABCDEFGH":
            self._Add_Figure(Pawn(player_white),item3 + str(2))
            self._Add_Figure(Pawn(player_black),item3 + str(7))
        self._Add_Figure(Tor(player_black), "A8")
        self._Add_Figure(Knight(player_black), "B8")
        self._Add_Figure(Bishop(player_black), "C8")
        self._Add_Figure(Queen(player_black), "D8")
        self._Add_Figure(King(player_black), "E8")
        self._Add_Figure(Bishop(player_black), "F8")
        self._Add_Figure(Knight(player_black), "G8")
        self._Add_Figure(Tor(player_black), "H8")
        for item4 in "ABCDEFGH":
            for i in [3, 4, 5, 6]:
                self._Add_Figure(None,item4 + str (i))

    def _Add_Figure(self, figure, position):
        self.board[position] = figure

    def Figure_At(self, position):
        return self.board[position]

    def Get_Board(self):
        return self.board

    def Is_Valid_Position(self,position):
        List_valid_position = []
        List_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        List_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        for i in List_letters:
            for j in List_numbers:
                pos = i + str(j)
                List_valid_position.append(pos)
        if position in List_valid_position:
            return True
        else:
            return False

    def Move_Figure(self, position, new_position):
        if (self.Is_Valid_Position(position) is True) and (self.Is_Valid_Position(new_position) is True):
            self._Add_Figure(self.Figure_At(position), new_position)
            self.board[position] = None
        else:
            raise InvalidPosition











