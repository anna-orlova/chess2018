class InvalidPosition(Exception):
    def __init__(self):
        super(InvalidPosition, self).__init__()

class EmptyField(Exception):
    def __init__(self):
        super(EmptyField, self).__init__()

class WrongFigureColor(Exception):
    def __init__(self):
        super(WrongFigureColor, self).__init__()

class WrongMove(Exception):
    def __init__(self):
        super(WrongMove, self).__init__()

class NoFigure(Exception):
    def __init__(self):
        super(NoFigure, self).__init__()


