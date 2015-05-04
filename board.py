__author__ = 'jkordas'


class Board(object):
    _SIZE_X = 11
    _SIZE_Y = 19
    _BOARD_TEMPLATE = [[4, 6], [3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7, 9], [2, 4, 6, 8], [1, 3, 5, 7, 9],
                       [0, 2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [0, 2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [0, 2, 4, 6, 8, 10],
                       [1, 3, 5, 7, 9], [0, 2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8], [1, 3, 5, 7, 9],
                       [2, 4, 6, 8], [3, 5, 7], [4, 6]]
    _SIGNS = {
        'BLACK_MARKER': '*',
        'BLACK_RING': 'c',
        'WHITE_MARKER': '@',
        'WHITE_RING': 'o'
    }
    _EMPTY_FIELD = '.'
    _MARKERS_NUMBER = 51

    @staticmethod
    def _is_position_in_range(x, y):
        if x not in Board._BOARD_TEMPLATE[y]:
            return False
        return True

    @staticmethod
    def _check_position_in_range(x, y):
        if not Board._is_position_in_range(x, y):
            raise ValueError("Position x: {0}, y: {1} is not in board range.".format(x, y))

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

    def move_ring(self, player, ring_move):
        start_x = ring_move.get_start_x()
        start_y = ring_move.get_start_y()
        self._check_position_owned(player, start_x, start_y)

        end_x = ring_move.get_end_x()
        end_y = ring_move.get_end_y()
        self._check_position_empty(player, end_x, end_y)

        # TODO check if not to many empty fields jumped
        # TODO is jump over ring correct?

        # we are sure move is correct

        # TODO perform the move


    def place_ring(self, player, placement_move):
        sign = Board._SIGNS[player.get_type() + '_RING']
        x = placement_move.get_x()
        y = placement_move.get_y()
        # check if in range
        Board._check_position_in_range(x, y)

        # check if empty field
        Board._check_position_empty(x, y)

        self.board[y][x] = sign

    def _place_marker(self, player, placement_move):
        # TODO
        pass

    def _switch_marker(self, player, placement_move):
        # TODO
        pass

    def is_marker_available(self):
        return Board._MARKERS_NUMBER - self.used_markers > 0

    def _check_position_empty(self, x, y):
        Board._check_position_in_range(x, y)
        if self.board[y][x] != Board._EMPTY_FIELD:
            raise ValueError("Field x: {0}, y: {1} is not empty.".format(x, y))

    def _check_position_owned(self, player, x, y):
        Board._check_position_in_range(x, y)
        if self.board[y][x] != Board._SIGNS[player.get_type() + '_RING']:
            raise ValueError("Field x: {0}, y: {1} is not owned by player.".format(x, y))
