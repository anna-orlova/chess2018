class Player(object):
    def __init__(self, color):
        self._SetColor(color)

    def _SetColor(self, color):
        valid_color = ["W", "B"]
        if color in valid_color:
            self.__color = color
        else:
            raise ValueError("Choose the right color for a figure: %s is not valid " % (color))

    def GetColor(self):
        return self.__color