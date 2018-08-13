from PyQt4.QtCore import *
from PyQt4.QtGui import *

class GUIChessField(QPushButton):
    def __init__(self, symbol, parent=None):
        super(GUIChessField, self).__init__(parent)
        self.__symbol = symbol

    def GetSymbol(self):
        return self.__symbol




