from Figure import *
from Player import Player
from Exceptions import *


class Board(object):
    def __init__(self, player_one, player_two):
        self.__player_one = player_one
        self.__player_two = player_two

        if self.__player_one.Is_White():
            self._current_player = self.__player_one # !!!!! question if we change then the right, will be changed the left, and vise versa?
        else:
            self._current_player = self.__player_two

        List_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        List_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        self.data = {}# empty dictionary
        #current_field = []# empty list
        for item1 in List_letters:
            for item2 in List_numbers:
                #current_field.append(item1 + str(item2))
                self.data[item1 + str(item2)] = None

    def Initiate_StartBoard(self):
# Change to self.players
#        player_white = Player("W")
#        player_black = Player("B")
        self._Add_Figure(Tor(self.__player_one), "A1")
        self._Add_Figure(Knight(self.__player_one), "B1")
        self._Add_Figure(Bishop(self.__player_one), "C1")
        self._Add_Figure(Queen(self.__player_one), "D1")
        self._Add_Figure(King(self.__player_one), "E1")
        self._Add_Figure(Bishop(self.__player_one), "F1")
        self._Add_Figure(Knight(self.__player_one), "G1")
        self._Add_Figure(Tor(self.__player_one), "H1")
        for item3 in "ABCDEFGH":
            self._Add_Figure(Pawn(self.__player_one),item3 + str(2))
            self._Add_Figure(Pawn(self.__player_two),item3 + str(7))
        self._Add_Figure(Tor(self.__player_two), "A8")
        self._Add_Figure(Knight(self.__player_two), "B8")
        self._Add_Figure(Bishop(self.__player_two), "C8")
        self._Add_Figure(Queen(self.__player_two), "D8")
        self._Add_Figure(King(self.__player_two), "E8")
        self._Add_Figure(Bishop(self.__player_two), "F8")
        self._Add_Figure(Knight(self.__player_two), "G8")
        self._Add_Figure(Tor(self.__player_two), "H8")
        for item4 in "ABCDEFGH":
            for i in [3, 4, 5, 6]:
                self._Add_Figure(None,item4 + str (i))

    def Toggle_Player(self):
        if self._current_player == self.__player_one:
            self._current_player = self.__player_two
        else:
            self._current_player = self.__player_one

    def Get_Current_Player(self):
        return self._current_player

    def _Add_Figure(self, figure, position):
        self.data[position] = figure

    def Position_of_Figure(self, figure):
        for item in self.data.keys():
            if self.Figure_At(item) == figure:
                return item


    def Figure_At(self, position):
        return self.data[position]

    def Get_Board(self):
        return self.data

    def Is_Valid_Position(self,position):
        List_valid_position = []
        List_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        List_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        for i in List_letters:
            for j in List_numbers:
                pos = i + str(j)
                List_valid_position.append(pos)
        if position in List_valid_position:
            return True
        else:
            return False

    def Move_Figure(self, position, new_position):

        if (self.Is_Valid_Position(position) is False) or (self.Is_Valid_Position(new_position) is False):
            # current_color = self.Figure_At(position).GetColor()
            raise InvalidPosition

        if self.Figure_At(position) is None:
            raise EmptyField

        if self.Get_Current_Player().GetColor() != self.Figure_At(position).GetColor():
            raise WrongFigureColor

        a_figure = self.Figure_At(position)
        pos_move = a_figure.Possible_Moves(self, position)
        if not new_position in pos_move:
            raise WrongMove

        self._Add_Figure(self.Figure_At(position), new_position)
        self.data[position] = None
        self.Toggle_Player()
        #current_figure = Figure.GetColor()

    def is_King_threatened(self, player):
        self._player = player
        color = self._player.GetColor()
        current_King = King(color)
        position = self.Position_of_Figure(current_King)
        current_coordinate = SymbolToCoordinate(position)
        j_vert = current_coordinate[1]
        k_hor = current_coordinate[0]
        matrix = BoardToMatrix(self.data)
        list_pos_hor_points = []
        if Figure.GetPlayer(player).Is_White():
            Active = COLOR_WHITE
            Passive = COLOR_BLACK
        else:
            Active = COLOR_BLACK
            Passive = COLOR_WHITE

        k = k_hor + 1
        while k < 8:
            if matrix[k, j_vert] != Active:
                if matrix[k, j_vert] != Passive:
                    list_pos_hor_moves.append((k, j_vert))
                    k += 1
                else:
                    list_pos_hor_moves.append((k, j_vert))
                    break
            else:
                break
        k = k_hor - 1
        while k >= 0:
            if matrix[k, j_vert] != Active:
                if matrix[k, j_vert] != Passive:
                    list_pos_hor_moves.append((k, j_vert))
                    k -= 1
                else:
                    list_pos_hor_moves.append((k, j_vert))
                    break
            else:
                break
        return list_pos_hor_moves
























