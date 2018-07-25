import numpy
import copy
from CoordinatesToSymbols import *
from Board import *
from Player import *

class Figure(object):
    def __init__(self, symbol, player):
        self.SetSymbol(symbol)
        self.SetPlayer(player)

    def SetSymbol(self, symbol):
        symbol_valid = list(["T","N","B","Q","K","P"])
        if symbol in symbol_valid:
            self.__symbol = symbol
        else:
            raise ValueError("Choose the right name for a figure: %s is not valid " % (symbol))

    def SetPlayer(self, player):
        self.__player = player

    def GetPlayer(self):
        return self.__player

    def GetSymbol(self):
        return self.__symbol

    def GetColor(self):
        return self.__player.GetColor()

    def Possible_Moves(self, board, position):  #abstract method
        #pass
        list_pos_symbols = []
        list_pos_cooordin = []
        List_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        List_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        for i in List_letters:
            for j in List_numbers:
                pos = i + str(j)
                list_pos_moves.append(pos)
       # for item in list_pos_moves:
            #list_pos_cooordin.append(SymbolToCoordinate(item))
        return list_pos_symbols



class Pawn(Figure):
    def __init__(self, player):
        super(Pawn, self).__init__("P", player)
#       Figure.__init__(self, "P", player)

    def Possible_Moves(self, board, position):

        list_pos_vert = []
        current_coordinate = SymbolToCoordinate(position)
        j_vert = current_coordinate[1]
        k_hor = current_coordinate[0]
        list_pos_vert.append(j_vert)
        list_pos_vert.append(j_vert + 1)
        list_pos_vert.append(j_vert - 1)
        list_pos_vert_copy = copy.deepcopy(list_pos_vert)

        for pos_vert in list_pos_vert_copy:
            if pos_vert > 7 or pos_vert < 0:
                list_pos_vert.remove(pos_vert)

        matrix = BoardToMatrix(board)
        list_pos_moves = []
        if self.GetPlayer().Is_White():
            # !!! Interpretor will replaces self to the Pawn, since we are in the Pawn class
            for pos_vert in list_pos_vert:
                if matrix[k_hor + 1, pos_vert] != COLOR_WHITE:
                    if k_hor < 7:
                        if k_hor == 1:
                            if matrix[k_hor + 2, pos_vert] == COLOR_NONE:
                                list_pos_moves.append((k_hor + 2, pos_vert))
                        if current_coordinate[1] != pos_vert:
                            if matrix[k_hor + 1, pos_vert] == COLOR_BLACK:
                                list_pos_moves.append((k_hor + 1, pos_vert))
                        else:
                            if matrix[k_hor + 1, pos_vert] == COLOR_NONE:
                                list_pos_moves.append((k_hor + 1, pos_vert))

        if self.GetPlayer().Is_Black():
            for pos_vert in list_pos_vert:
                if matrix[k_hor - 1, pos_vert] != COLOR_BLACK:
                    if k_hor < 7:
                        if k_hor == 6:
                            if matrix[k_hor - 2, pos_vert] == COLOR_NONE:
                                list_pos_moves.append((k_hor - 2, pos_vert))

                        if current_coordinate[1] != pos_vert:
                            if matrix[k_hor - 1, pos_vert] == COLOR_WHITE:
                                list_pos_moves.append((k_hor - 1, pos_vert))
                        else:
                            if matrix[k_hor - 1, pos_vert] == COLOR_NONE:
                                list_pos_moves.append((k_hor - 1, pos_vert))

        list_pos_symbols = []
        for item in list_pos_moves:
            list_pos_symbols.append(CoordinateToSymbol(item))

        return list_pos_symbols


class Tor(Figure):
    def __init__(self, player):
        super(Tor, self).__init__("T", player)


class Knight(Figure):
    def __init__(self, player):
        super(Knight, self).__init__("N", player)


class Bishop(Figure):
    def __init__(self, player):
        super(Bishop, self).__init__("B", player)


class Queen(Figure):
    def __init__(self, player):
        super(Queen, self).__init__("Q", player)


class King(Figure):
    def __init__(self, player):
        super(King, self).__init__("K", player)


