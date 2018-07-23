import numpy

def SymbolToCoordinate(symbol):

    letters = "ABCDEFGH"
    for id_letter, letter in enumerate(letters):
        # id_letter - index, letter - value of the list of tupple enumerate(letters)
        if letter in symbol and len(symbol) == 2:
            for i in range(1, 9):
                if str(i) in symbol:
                    return list([id_letter, i - 1])
    else:
        return "Wrong Input"

def CoordinateToSymbol(coordinate):

    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for id_letter, letter in enumerate(letters):
        if id_letter == coordinate[0] and len(coordinate) == 2:
            for j in range(0, 8):
                if coordinate[1] == j:
                    return letter + str(j+1)
    else:
        return ("Wrong Coordinates")

def CoordinateArrayToSymbol(list):
    list_symbol = []
    for i in range(0, list.shape[0]):
        for j in range(0, list.shape[1]):
            if list[i, j] == 1:
                list_symbol.append(CoordinateToSymbol([i, j]))
    return list_symbol