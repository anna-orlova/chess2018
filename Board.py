from Figure import *

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
        self._Add_Figure(Tor("W"), "A1")
        self._Add_Figure(Knight("W"), "B1")
        self._Add_Figure(Bishop("W"), "C1")
        self._Add_Figure(Queen("W"), "D1")
        self._Add_Figure(King("W"), "E1")
        self._Add_Figure(Bishop("W"), "F1")
        self._Add_Figure(Knight("W"), "G1")
        self._Add_Figure(Tor("W"), "H1")
        for item3 in "ABCDEFGH":
            self._Add_Figure(Pawn("W"),item3 + str(2))
            self._Add_Figure(Pawn("B"),item3 + str(7))
        self._Add_Figure(Tor("B"), "A8")
        self._Add_Figure(Knight("B"), "B8")
        self._Add_Figure(Bishop("B"), "C8")
        self._Add_Figure(Queen("B"), "D8")
        self._Add_Figure(King("B"), "E8")
        self._Add_Figure(Bishop("B"), "F8")
        self._Add_Figure(Knight("B"), "G8")
        self._Add_Figure(Tor("B"), "H8")
        for item4 in "ABCDEFGH":
            for i in [3, 4, 5, 6]:
                self._Add_Figure(None,item4 + str (i))

    def _Add_Figure(self, figure, position):
        self.board[position] = figure

    def Figure_At(self, position):
        return self.board[position]

    def Get_Board(self):
        return self.board