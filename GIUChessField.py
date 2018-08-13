from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Figure import *

class GUIChessField(QLabel):

    FPictures = "C:\\Users\\Anna\\Documents\\Chess2018\\Pictures\\"
    Files_svg = {"WP": FPictures + "W_Pawn.svg", "WT": FPictures + "W_Tor.svg",
                 "WN": FPictures + "W_Knight.svg", "WB": FPictures + "W_Bishop.svg",
                 "WQ": FPictures + "W_Queen.svg", "WK": FPictures + "W_King.svg",
                 "BP": FPictures + "B_Pawn.svg", "BT": FPictures + "B_Tor.svg",
                 "BN": FPictures + "B_Knight.svg", "BB": FPictures + "B_Bishop.svg",
                 "BQ": FPictures + "B_Queen.svg", "BK": FPictures + "B_King.svg"}

    def __init__(self, symbol, parent=None):
        super(GUIChessField, self).__init__(parent)
        self.__symbol = symbol


    def setFigure(self, figure):
        self.__figure = figure
        if figure is None:
            self.setText(" ")
        else:
            color = str(figure.GetColor())
            sym = str(figure.GetSymbol())
            index = color + sym
            self.setText(color + sym)
            print(self.Files_svg[index])

    def mousePressEvent(self, QMouseEvent):
        self.emit(SIGNAL("clicked()"))

    def GetSymbol(self):
        return self.__symbol




