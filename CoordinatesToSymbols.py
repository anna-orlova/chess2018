def SymbolToCoordinate(symbol):

    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for id_letter, letter in enumerate(letters):
        # id_letter - index, letter - value of the list of tupple enumerate(letters)
        if letter in symbol:
            for i in [1, 2, 3, 4, 5, 6, 7, 8]:
                if str(i) in symbol:
                    return list([id_letter, i - 1])



    # if "A" in symbol:
    #     for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    #         if str(i) in symbol:
    #             return list([0, i-1])
    #
    # if "B" in symbol[0]:
    #     for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    #         if str(i) in symbol:
    #             return list([1, i-1])
    #         #if symbol[1] == i:
    #           #  return [1, i-1]
    #
    # if "C" in symbol[0]:
    #     for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    #         if str(i) in symbol:
    #             return list([2, i-1])
    #
    # if "D" in symbol[0]:
    #     for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    #         if str(i) in symbol:
    #             return list([3, i-1])
    #
    # if "E" in symbol[0]:
    #     for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    #         if str(i) in symbol:
    #             return list([4, i-1])
    #
    # if "F" in symbol[0]:
    #     for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    #         if str(i) in symbol:
    #             return list([5, i-1])
    #
    # if "G" in symbol[0]:
    #     for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    #         if str(i) in symbol:
    #             return list([6, i-1])
    #
    # if "H" in symbol[0]:
    #     for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    #         if str(i) in symbol:
    #             return list([7, i-1])
    else:
        return "Wrong Input"


def CoordinateToSymbol(coordinate):
    if coordinate[0] == 0:
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            if i == coordinate[1]: # Why if i in coordinate[1]: doesn't work???????
                return "A" + str(coordinate[1]+1)
    if coordinate[0] == 1:
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            if i == coordinate[1]: # Why if i in coordinate[1]: doesn't work???????
                return "B" + str(coordinate[1]+1)
    if coordinate[0] == 2:
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            if i == coordinate[1]: # Why if i in coordinate[1]: doesn't work???????
                return "C" + str(coordinate[1]+1)
    if coordinate[0] == 3:
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            if i == coordinate[1]: # Why if i in coordinate[1]: doesn't work???????
                return "D" + str(coordinate[1]+1)
    if coordinate[0] == 4:
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            if i == coordinate[1]: # Why if i in coordinate[1]: doesn't work???????
                return "E" + str(coordinate[1]+1)
    if coordinate[0] == 5:
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            if i == coordinate[1]: # Why if i in coordinate[1]: doesn't work???????
                return "F" + str(coordinate[1]+1)
    if coordinate[0] == 6:
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            if i == coordinate[1]: # Why if i in coordinate[1]: doesn't work???????
                return "G" + str(coordinate[1]+1)
    if coordinate[0] == 7:
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            if i == coordinate[1]: # Why if i in coordinate[1]: doesn't work???????
                return "H" + str(coordinate[1]+1)
    else:
        return("Wrong Coordinates")


symbol = "A1"

for c in ["A", "B", "C", "D", "E", "F", "G", "H"]:
    for i in range(1, 9):
        symbol = c + str(i)
        a = SymbolToCoordinate(symbol)
        out = CoordinateToSymbol(a)
        if symbol != out:
            print("NOOOOOOOO", symbol, a, out)
