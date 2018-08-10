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
        symbol_valid = list(["T", "N", "B", "Q", "K", "P"])
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

    def Possible_Moves(self, board, position):  # abstract method
        # pass
        list_pos_symbols = []
        list_pos_cooordin = []
        List_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        List_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        for i in List_letters:
            for j in List_numbers:
                pos = i + str(j)
                list_pos_moves.append(pos)
                # for item in list_pos_moves:
                # list_pos_cooordin.append(SymbolToCoordinate(item))
        return list_pos_symbols

    def Pos_Diagonal_moves(self, board, position):

        current_coordinate = SymbolToCoordinate(position)
        j_vert = current_coordinate[1]
        k_hor = current_coordinate[0]
        matrix = BoardToMatrix(board)
        list_pos_diag_moves = []
        if self.GetPlayer().Is_White():
            Active = COLOR_WHITE
            Passive = COLOR_BLACK
        else:
            Active = COLOR_BLACK
            Passive = COLOR_WHITE

        j = j_vert + 1
        k = k_hor + 1
        while j < 8 and k < 8:
            if matrix[k, j] != Active:
                if matrix[k, j] != Passive:
                    list_pos_diag_moves.append((k, j))
                    j += 1
                    k += 1
                else:
                    list_pos_diag_moves.append((k, j))
                    break
            else:
                break
        j = j_vert - 1
        k = k_hor + 1
        while j >= 0 and k < 8:
            if matrix[k, j] != Active:
                if matrix[k, j] != Passive:
                    list_pos_diag_moves.append((k, j))
                    j -= 1
                    k += 1
                else:
                    list_pos_diag_moves.append((k, j))
                    break
            else:
                break

        j = j_vert + 1
        k = k_hor - 1
        while j < 8 and k >= 0:
            if matrix[k, j] != Active:
                if matrix[k, j] != Passive:
                    list_pos_diag_moves.append((k, j))
                    j += 1
                    k -= 1
                else:
                    list_pos_diag_moves.append((k, j))
                    break
            else:
                break
        j = j_vert - 1
        k = k_hor - 1
        while j >= 0 and k >= 0:
            if matrix[k, j] != Active:
                if matrix[k, j] != Passive:
                    list_pos_diag_moves.append((k, j))
                    j -= 1
                    k -= 1
                else:
                    list_pos_diag_moves.append((k, j))
                    break
            else:
                break
        return list_pos_diag_moves

    def Pos_Vertical_moves(self, board, position):

        current_coordinate = SymbolToCoordinate(position)
        j_vert = current_coordinate[1]
        k_hor = current_coordinate[0]
        matrix = BoardToMatrix(board)
        list_pos_vert_moves = []
        if self.GetPlayer().Is_White():
            ###Active and Passive player
            Active = COLOR_WHITE
            Passive = COLOR_BLACK
        else:
            Active = COLOR_BLACK
            Passive = COLOR_WHITE

        j = j_vert + 1

        while j < 8:
            if matrix[k_hor, j] != Active:
                if matrix[k_hor, j] != Passive:
                    list_pos_vert_moves.append((k_hor, j))
                    j += 1
                else:
                    list_pos_vert_moves.append((k_hor, j))
                    break
            else:
                break
        j = j_vert - 1
        while j >= 0:
            if matrix[k_hor, j] != Active:
                if matrix[k_hor, j] != Passive:
                    list_pos_vert_moves.append((k_hor, j))
                    j -= 1
                else:
                    list_pos_vert_moves.append((k_hor, j))
                    break
            else:
                break
        return list_pos_vert_moves

    def Pos_Horizont_moves(self, board, position):

        current_coordinate = SymbolToCoordinate(position)
        j_vert = current_coordinate[1]
        k_hor = current_coordinate[0]
        matrix = BoardToMatrix(board)
        list_pos_hor_moves = []
        if self.GetPlayer().Is_White():
            Active = COLOR_WHITE
            Passive = COLOR_BLACK
        else:
            Active = COLOR_BLACK
            Passive = COLOR_WHITE

        k = k_hor + 1
        while k < 8:
            if matrix[k, j_vert] != Active:
                if matrix[k, j_vert] != Passive:
                    list_pos_hor_moves.append((k, j_vert))
                    k += 1
                else:
                    list_pos_hor_moves.append((k, j_vert))
                    break
            else:
                break
        k = k_hor - 1
        while k >= 0:
            if matrix[k, j_vert] != Active:
                if matrix[k, j_vert] != Passive:
                    list_pos_hor_moves.append((k, j_vert))
                    k -= 1
                else:
                    list_pos_hor_moves.append((k, j_vert))
                    break
            else:
                break
        return list_pos_hor_moves


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
                        if k_hor == 1 and pos_vert == j_vert:
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
                        if k_hor == 6 and  pos_vert == j_vert:
                            if matrix[k_hor - 2, pos_vert] == COLOR_NONE:
                                list_pos_moves.append((k_hor - 2, pos_vert))

                        if current_coordinate[1] != pos_vert:
                            if matrix[k_hor - 1, pos_vert] == COLOR_WHITE:
                                list_pos_moves.append((k_hor - 1, pos_vert))
                        else:
                            if matrix[k_hor - 1, pos_vert] == COLOR_NONE:
                                list_pos_moves.append((k_hor - 1, pos_vert))

        list_pos_symbols = List_Pos_Moves_to_List_symbols(list_pos_moves)
        return list_pos_symbols



class Tor(Figure):
    def __init__(self, player):
        super(Tor, self).__init__("T", player)

    def Possible_Moves(self, board, position):
        list_pos_moves = self.Pos_Horizont_moves(board, position) + self.Pos_Vertical_moves(board, position)
        list_pos_symbols = List_Pos_Moves_to_List_symbols(list_pos_moves)
        return list_pos_symbols


class Knight(Figure):
    def __init__(self, player):
        super(Knight, self).__init__("N", player)

    def Possible_Moves(self, board, position):
        current_coordinate = SymbolToCoordinate(position)
        j_vert = current_coordinate[1]
        k_hor = current_coordinate[0]
        list_pos_moves = [(k_hor + 2, j_vert + 1), (k_hor + 2, j_vert - 1),
                          (k_hor - 2, j_vert + 1), (k_hor - 2, j_vert - 1),
                          (k_hor + 1, j_vert + 2), (k_hor + 1, j_vert - 2),
                          (k_hor - 1, j_vert + 2), (k_hor - 1, j_vert - 2)]
        list_pos_moves_copy = copy.deepcopy(list_pos_moves)
        for item1 in list_pos_moves_copy:
            if item1[0] > 7 or item1[0] < 0:
                if item1 in list_pos_moves:
                    list_pos_moves.remove(item1)
            if item1[1] > 7 or item1[1] < 0:
                if item1 in list_pos_moves:
                    list_pos_moves.remove(item1)

        matrix = BoardToMatrix(board)
        list_pos_moves_copy = copy.deepcopy(list_pos_moves)
        if self.GetPlayer().Is_White():
            for item in list_pos_moves_copy:
                if matrix[item[0], item[1]] == COLOR_WHITE:
                    list_pos_moves.remove(item)
        if self.GetPlayer().Is_Black():
            for item in list_pos_moves_copy:
                if matrix[item[0], item[1]] == COLOR_BLACK:
                    list_pos_moves.remove(item)

        list_pos_symbols = List_Pos_Moves_to_List_symbols(list_pos_moves)
        return list_pos_symbols


class Bishop(Figure):
    def __init__(self, player):
        super(Bishop, self).__init__("B", player)

    def Possible_Moves(self, board, position):
        list_pos_moves = self.Pos_Diagonal_moves(board, position)
        list_pos_symbols = List_Pos_Moves_to_List_symbols(list_pos_moves)
        return list_pos_symbols


class Queen(Figure):
    def __init__(self, player):
        super(Queen, self).__init__("Q", player)

    def Possible_Moves(self, board, position):
        list_pos_moves = self.Pos_Diagonal_moves(board, position) + self.Pos_Horizont_moves(board,
                                                                                            position) + self.Pos_Vertical_moves(
            board, position)
        list_pos_symbols = List_Pos_Moves_to_List_symbols(list_pos_moves)
        return list_pos_symbols


class King(Figure):
    def __init__(self, player):
        super(King, self).__init__("K", player)

    def Possible_Moves(self, board, position):

        # list_pos_vert = []
        current_coordinate = SymbolToCoordinate(position)
        j_vert = current_coordinate[1]
        k_hor = current_coordinate[0]
        list_pos_moves = [(k_hor + 1, j_vert), (k_hor - 1, j_vert),
                          (k_hor, j_vert + 1), (k_hor + 1, j_vert + 1),
                          (k_hor - 1, j_vert + 1), (k_hor, j_vert - 1),
                          (k_hor + 1, j_vert - 1), (k_hor - 1, j_vert - 1)]
        list_pos_moves_copy = copy.deepcopy(list_pos_moves)
        for item1 in list_pos_moves_copy:
            if item1[0] > 7 or item1[0] < 0:
                list_pos_moves.remove(item1)
            if item1[1] > 7 or item1[1] < 0:
                list_pos_moves.remove(item1)

        matrix = BoardToMatrix(board)
        list_pos_moves_copy = copy.deepcopy(list_pos_moves)
        if self.GetPlayer().Is_White():
            for item in list_pos_moves_copy:
                if matrix[item[0], item[1]] == COLOR_WHITE:
                    list_pos_moves.remove(item)
        if self.GetPlayer().Is_Black():
            for item in list_pos_moves_copy:
                if matrix[item[0], item[1]] == COLOR_BLACK:
                    list_pos_moves.remove(item)
        list_pos_symbols = List_Pos_Moves_to_List_symbols(list_pos_moves)
        return list_pos_symbols
