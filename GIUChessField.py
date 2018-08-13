from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Figure import *

class GUIChessField(QLabel):
    def __init__(self, symbol, parent=None):
        super(GUIChessField, self).__init__(parent)
        self.__symbol = symbol

    def setFigure(self, figure):
        self.__figure = figure
        if figure is None:
            self.setText(" ")
        else:
            color = str(figure.GetColor())
            symbol = str(figure.GetSymbol())
            self.setText(color + symbol)

    def mousePressEvent(self, QMouseEvent):
        self.emit(SIGNAL("clicked()"))

    def GetSymbol(self):
        return self.__symbol




