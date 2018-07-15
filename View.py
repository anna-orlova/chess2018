from Board import *

def titleForFigure(f):
    if f is None:
        return "No"
    else:
        return f.GetSymbol() + f.GetColor() # return a string object


class View(object):
    def __init__(self, Board):
        self._board = Board

    def Show(self):
        print ("   A    B    C    D    E    F    G    H")
        print("_" * 40)


        for item2 in [8,7,6,5,4,3,2,1]:
            string1 = ""
            for item1 in "ABCDEFGH":
                #string1 = "|"
                f = self._board.Figure_At(item1 + str(item2))
                string1 = string1 + titleForFigure(f) + "|  "
            print(str(item2) + "|" + string1)
                #current_field = item1+str(item2)


                #print("_" * 40)
                #print(current_field)
                #if self._board.Get_Board== None:
                    #print("OO",  "|")
                #else:
                #print (self._board.Figure_At(item1 + str(item2)), "|")
            print("_" * 40)

        print ("   A    B    C    D    E    F    G    H")