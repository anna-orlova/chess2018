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
        pass
#       create a list with all fields A1,A2,...,B1,B2,...
#        return self.board



class Pawn(Figure):
    def __init__(self, player):
        super(Pawn, self).__init__("P", player)
#        Figure.__init__(self, "P", player)

    def Possible_Moves(self, board, position):
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