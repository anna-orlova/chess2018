from CoordinatesToSymbols import *
from Board import *
from Player import *
from Exceptions import *
import sys
from Player_Turn import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class View_Gui(QDialog):

    def __init__(self, board, parent=None):
        super(View_Gui, self).__init__(parent)
        self._board = board
        self.buttons = dict()
        buttonLayout = QVBoxLayout()
        List_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        List_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        self.buttons = {}  # empty dictionary
        for item1 in List_letters:
            for item2 in List_numbers:
                self.buttons[item1 + str(item2)] = QPushButton(item1+str(item2))
        self.layout = QGridLayout()
        self.player_turn = Player_Turn()

        for item in self.buttons.items():
            button = item[1]
            i = 7 - SymbolToCoordinate(item[0])[0]
            j = SymbolToCoordinate(item[0])[1]
            self.layout.addWidget(button, i, j)

        #self.layout.addWidget
        self.setLayout(self.layout)
        self.paint_Figures()

        for item in self.buttons.items():
#            if symbol in self.buttons.values():
            obj = item[1]
            self.connect(obj, SIGNAL("clicked()"),
                         lambda symbol=item[0]:
                         self.handleButtonClick(symbol))



    def handleButtonClick(self, symbol):
        self.player_turn.addInput(symbol)
        if self.player_turn.isTurnComplete() == True:
            start = self.player_turn.GetMove_start()
            end = self.player_turn.GetMove_end()
            try:
                self._board.Move_Figure(start, end)

            except InvalidPosition:
                print("Invalid position")
                pass

            except WrongFigureColor:
                print("Wrong Figure Color")
                pass

            except NoFigure:
                print("No Figure")
                pass

            except WrongMove:
                print("Wrong Move")
                pass

            self.player_turn.Reset()
            self.paint_Figures()

    def titleForFigure(self, f):
        if f is None:
            return "No"
        else:
            return f.GetSymbol() + f.GetColor()  # return a string object

    def paint_Figures(self):
        for item in self.buttons.items():
            button = item[1]
            key = item[0]
            figure = self._board.Figure_At(key)
            if figure is None:
                button.setText("")
            else:
                title = self.titleForFigure(figure)
                button.setText(title)



app = QApplication(sys.argv)
board = Board(Player("W"), Player("B"))
board.Initiate_StartBoard()
form = View_Gui(board)
form.show()
app.exec_()





