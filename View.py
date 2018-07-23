from Board import *
from Player import *
from Exceptions import *

def titleForFigure(f):
    if f is None:
        return "No"
    else:
        return f.GetSymbol() + f.GetColor() # return a string object


class View(object):
    def __init__(self, board):
        self._board = board

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
        b = self._board.Get_Current_Player().GetColor()
        print ("Current Player:", b)

    def Run(self):
        self.Show()
        while True:
            move_from = raw_input("Move from:")
            move_to = raw_input("Move_to:")
            try:
                self._board.Move_Figure(move_from, move_to)

            except InvalidPosition:
                print("Invalid input")
                continue

            except NoFigure:
                print("No Figure")
                continue

            except WrongFigureColor:
                print ("Wrong Figure Color")
                continue

            except WrongMove:
                print("Wrong Move")
                continue

           # self._board.Toggle_Player()
            self.Show()






