from Exceptions import *

class Player_Turn(object):

    def __init__(self, Move_start=None, Move_end=None):
        self.SetMove_start(Move_start)
        self.SetMove_end(Move_end)

    def SetMove_start(self, start):
        self.__Move_start = start

    def SetMove_end(self, end):
        self.__Move_end = end


    def GetMove_start(self):
        return self.__Move_start

    def GetMove_end(self):
        return self.__Move_end

    def addInput(self, symbol):
        if self.__Move_start == None:
            self.__Move_start = symbol
        else:
            if self.__Move_end == None:
                self.__Move_end = symbol
            else:
                raise InvalidPosition

    def isTurnComplete(self):
        if self.GetMove_start() is not None and self.GetMove_end() is not None:
            return True
        else:
            return False

    def Reset(self):
        self.SetMove_start(None)
        self.SetMove_end(None)




