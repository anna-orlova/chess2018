import numpy

COLOR_WHITE = -1
COLOR_BLACK = 1
COLOR_NONE = 0


def SymbolToCoordinate(symbol):

    letters = "ABCDEFGH"
    for id_letter, letter in enumerate(letters):
        # id_letter - index, letter - value of the list of tupple enumerate(letters)
        if letter in symbol and len(symbol) == 2:
            for i in range(1, 9):
                if str(i) in symbol:
                    return list((i - 1, id_letter)) # I have changed the order  id and i-1
    else:
        return "Wrong Input"

def CoordinateToSymbol(coordinate):

    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for id_letter, letter in enumerate(letters):
        if id_letter == coordinate[1] and len(coordinate) == 2:
            for j in range(0, 8):
                if coordinate[0] == j:
                    return letter + str(j+1)  # changed coordinate  0 and 1
    else:
        return ("Wrong Coordinates")

def CoordinateArrayToSymbol(matrix):
    list_symbol = []
    for i in range(0, matrix.shape[0]):
        for j in range(0, matrix.shape[1]):
            list_symbol.append(CoordinateToSymbol((i, j)))
    return list_symbol

def BoardToMatrix(board):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    numbers = range(1, 9)
    matrix = numpy.zeros((8,8), numpy.int)
    for symbol in letters:
        for item in numbers:
            position = symbol + str(item)
            a = SymbolToCoordinate(position)
            if board.Figure_At(position) is None:
                matrix[a[0], a[1]] = COLOR_NONE
            else:
                color = board.Figure_At(position).GetColor()
                if color == "W":
                    matrix[a[0], a[1]] = COLOR_WHITE
                else:
                    matrix[a[0], a[1]] = COLOR_BLACK
    return matrix

def List_Pos_Moves_to_List_symbols(list_pos_moves):
    list_pos_symbols = []
    for item in list_pos_moves:
        list_pos_symbols.append(CoordinateToSymbol(item))
    return list_pos_symbols

