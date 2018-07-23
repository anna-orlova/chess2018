import numpy
from CoordinatesToSymbols import CoordinateToSymbol, SymbolToCoordinate, CoordinateArrayToSymbol

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

    def GetSymbol(self):
        return self.__symbol

    def GetColor(self):
        return self.__player.GetColor()

    def Possible_Moves(self, board, position):  #abstract method
        #pass
        list_pos_moves = []
        list_pos_cooordin = []
        List_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        List_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        for i in List_letters:
            for j in List_numbers:
                pos = i + str(j)
                list_pos_moves.append(pos)
       # for item in list_pos_moves:
            #list_pos_cooordin.append(SymbolToCoordinate(item))
        return list_pos_moves



class Pawn(Figure):
    def __init__(self, player):
        super(Pawn, self).__init__("P", player)
        self.__player = player
#       Figure.__init__(self, "P", player)

    def Possible_Moves(self, board,  position):
        all_possible_coordinates = []
        for c in ["A", "B", "C", "D", "E", "F", "G", "H"]:
            for i in range(1, 9):
                symbol = c + str(i)
                a = SymbolToCoordinate(symbol)
                all_possible_coordinates.append(a)

        matrix = numpy.zeros((8, 8))
        list_pos_vert = []
        current_coordinate = SymbolToCoordinate(position)
        j_vert = current_coordinate[0]
        k_hor = current_coordinate[1]
        list_pos_vert.append(j_vert)
        list_pos_vert.append(j_vert + 1)
        list_pos_vert.append(j_vert - 1)

        if self.__player.Is_White():
            for item in list_pos_vert:
                matrix[item, k_hor + 1] = 1
                if k_hor == 1:
                    matrix[j_vert, k_hor+2] = 1

        if not self.__player.Is_White():
            for item in list_pos_vert:
                matrix[item, k_hor - 1] = 1
                if k_hor == 6:
                    matrix[j_vert, k_hor - 2] = 1

        list_symbols = CoordinateArrayToSymbol(matrix)
        return list_symbols










        i_position = SymbolToCoordinate()
        i_position = int(position[1])
        if self.__player.Is_White():
            return position[0] + str(i_position+1)
        else:
            return position[0] + str(i_position-1)




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


