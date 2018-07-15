class Figure(object):
    def __init__(self, symbol, color):
        self.SetSymbol(symbol)
        self.SetColor(color)

    def SetSymbol(self, symbol):
        symbol_valid = list(["T","N","B","Q","K","P"])
        if symbol in symbol_valid:
            self.__symbol = symbol
        else:
            raise ValueError("Choose the right name for a figure: %s is not valid " % (symbol))

    def SetColor(self, color):
        color_valid = list(["W", "B"])
        if color in color_valid:
            self.__color = color
        else:
            raise ValueError("Choose the right color for a figure: %s is not valid " % (color))

    def GetSymbol(self):
        return self.__symbol

    def GetColor(self):
        return self.__color


class Pawn(Figure):
    def __init__(self, color):
        super(Pawn,self).__init__("P", color)


class Tor(Figure):
    def __init__(self, color):
        super(Tor, self).__init__("T", color)


class Knight(Figure):
    def __init__(self, color):
        super(Knight, self).__init__("N", color)


class Bishop(Figure):
    def __init__(self, color):
        super(Bishop, self).__init__("B", color)


class Queen(Figure):
    def __init__(self, color):
        super(Queen, self).__init__("Q", color)


class King(Figure):
    def __init__(self, color):
        super(King, self).__init__("K", color)