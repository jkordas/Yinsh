__author__ = 'jkordas'
import sys


class Board(object):
    _SIZE_X = 11
    _SIZE_Y = 19
    _BOARD_TEMPLATE = [[4, 6], [3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7, 9], [2, 4, 6, 8], [1, 3, 5, 7, 9],
                       [0, 2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [0, 2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [0, 2, 4, 6, 8, 10],
                       [1, 3, 5, 7, 9], [0, 2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8], [1, 3, 5, 7, 9],
                       [2, 4, 6, 8], [3, 5, 7], [4, 6]]
    _BLACK_OPEN = 'c'
    _BLACK = '*'
    _WHITE_OPEN = 'o'
    _WHITE = '@'
    _EMPTY_FIELD = '.'
    _MARKERS_NUMBER = 51

    @staticmethod
    def is_move_in_range(x, y):
        if x not in Board._BOARD_TEMPLATE[y]:
            return False
        return True

    def __init__(self):
        self.board = [[' ' for _ in range(Board._SIZE_X)] for _ in range(Board._SIZE_Y)]
        for index, row in enumerate(Board._BOARD_TEMPLATE):
            for num in row:
                self.board[index][num] = Board._EMPTY_FIELD
        self.used_markers = 0

    def show(self):
        print " ---------------------------"
        print "|    0 1 2 3 4 5 6 7 8 9 10 |"
        for index, row in enumerate(self.board):
            line = "|"
            if index < 10:
                line += " "
            print line, index,
            for item in row:
                print item,
            print " |"

    def place_black(self, x, y):
        self.board[y][x] = Board._BLACK

    def place_white(self, x, y):
        self.board[y][x] = Board._WHITE

    def place_black_open(self, placement_move):
        self.place_open(placement_move, Board._BLACK_OPEN)

    def place_white_open(self, placement_move):
        self.place_open(placement_move, Board._WHITE_OPEN)

    def place_open(self, placement_move, sign):
        x = placement_move.get_x()
        y = placement_move.get_y()
        # check if in range
        if not self.is_move_in_range(x, y):
            raise ValueError("Move x: {0}, y: {1} is not in board range.".format(x, y))

        # check if empty field
        if self.board[y][x] != Board._EMPTY_FIELD:
            raise ValueError("Field x: {0}, y: {1} is not empty.".format(x, y))

        self.board[y][x] = sign

    def is_marker_available(self):
        return Board._MARKERS_NUMBER - self.used_markers > 0
