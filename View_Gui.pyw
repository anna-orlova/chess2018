from CoordinatesToSymbols import *
from Board import *
from Player import *
from Exceptions import *
import sys
from GIUChessField import *
from Player import *
from Player_Turn import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class View_Gui(QDialog):

    def __init__(self, board, parent=None):
        super(View_Gui, self).__init__(parent)
        self._board = board
        self.buttons = dict()
        self.letters = dict()
        self.numbers = dict()
        buttonLayout = QVBoxLayout()
        List_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        List_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        self.buttons = {}  # empty dictionary
        self.cur_Player = QLabel(" ")
        self.layout = QGridLayout()
        self.player_turn = Player_Turn()

        for item1 in List_letters:
            for item2 in List_numbers:
                self.buttons[item1 + str(item2)] = GUIChessField(item1+str(item2))

        for item in List_numbers:
            self.numbers[item] = QLabel(str(item))
        for item in self.numbers.items():
            i = item[0]
            name = item[1]
            self.layout.addWidget(name, i, 0)

        for item, letter in enumerate(List_letters):
            self.letters[item] = QLabel(letter)
        for item in self.letters.items():
            i = item[0]
            name = item[1]
            self.layout.addWidget(name, 9, i+1)

        for item in self.buttons.items():
            button = item[1]
            i = 8 - SymbolToCoordinate(item[0])[0]
            j = 1 + SymbolToCoordinate(item[0])[1]
            self.layout.addWidget(button, i, j)

        self.updateUi()
        self.layout.addWidget(self.cur_Player, 9, 0)
        self.setLayout(self.layout)
        self.paint_Figures()


        for item in self.buttons.items():
#            if symbol in self.buttons.values():
            obj = item[1]
            self.connect(obj, SIGNAL("clicked()"),
                         self.handleButtonClick)

    def handleButtonClick(self):
        gui_chess_field = self.sender()
        symbol = gui_chess_field.GetSymbol()
        #symbol = self.gui_chess_field.GetSymbol()
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
            self.updateUi()
            self.paint_Figures()

    def updateUi(self):
        Current_Player = self._board.Get_Current_Player().GetColor()
        self.cur_Player.setText(Current_Player)

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





