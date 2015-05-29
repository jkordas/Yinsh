from move import PlacementMove

__author__ = 'jkordas'


class Board(object):
    """
    Game board representation.
    """
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
    def show_intro():
        print " ___________________________"
        print "|                           |"
        print "|           Yinsh           |"
        print "|___________________________|"
        for elem in sorted(Board._SIGNS):
            print "  {0}: {1}".format(elem, Board._SIGNS[elem])
        print

    @staticmethod
    def _is_position_in_range(x, y):
        if y >= len(Board._BOARD_TEMPLATE):
            return False
        if x not in Board._BOARD_TEMPLATE[y]:
            return False
        return True

    @staticmethod
    def _check_position_in_range(x, y):
        if not Board._is_position_in_range(x, y):
            raise ValueError("Position x: {0}, y: {1} is not in board range.".format(x, y))

    @staticmethod
    def _check_empty_fields(line):
        is_empty_acceptable = True
        for field in line:
            if field == Board._EMPTY_FIELD:
                if not is_empty_acceptable:
                    raise ValueError("Too many empty fields.")
            else:
                is_empty_acceptable = False

    @staticmethod
    def _check_jump_over_ring(line):
        if Board._SIGNS['WHITE_RING'] in line or Board._SIGNS['BLACK_RING'] in line:
            raise ValueError("Cannot jump over rings.")

    @staticmethod
    def _count_fives_in_line(player, line):
        counter = 0
        max_counter = 0
        for elem in line:
            if elem == Board._SIGNS[player.get_type() + '_MARKER']:
                counter += 1
            else:
                counter = 0

            if counter > max_counter:
                max_counter = counter
        return max_counter

    @staticmethod
    def _get_jumped_line_indexes(start_x, start_y, end_x, end_y):
        if start_x == end_x and start_y == end_y:
            raise ValueError("Start and stop position have to be different.")

        if start_x == end_x:  # vertical line
            low = max(start_y, end_y)  # horizontal low
            high = min(start_y, end_y)  # horizontal high
            line = [(i, start_x) for i in range(high + 2, low, 2)]
            return line
        reverse = False

        if start_y > end_y:  # going up horizontal
            low_x = start_x
            low_y = start_y
            high_x = end_x
            high_y = end_y
        else:
            low_x = end_x
            low_y = end_y
            high_x = start_x
            high_y = start_y
            reverse = True

        line = []
        # check direction
        if low_x < high_x:
            # right
            for i in range(1, low_y - high_y):
                line.append((low_y - i, low_x + i))
        else:
            # left
            for i in range(1, low_y - high_y):
                line.append((low_y - i, low_x - i))

        if reverse:
            line.reverse()

        return line

    def __init__(self):
        self.board = [[' ' for _ in range(Board._SIZE_X)] for _ in range(Board._SIZE_Y)]
        for index, row in enumerate(Board._BOARD_TEMPLATE):
            for num in row:
                self.board[index][num] = Board._EMPTY_FIELD
        self.used_markers = 0

    def show(self):
        print " -----------------------------"
        print "|    0 1 2 3 4 5 6 7 8 9 10   |"
        for index, row in enumerate(self.board):
            line = "|"
            if index < 10:
                line += " "
            print line, index,
            for item in row:
                print item,
            if index < 10:
                print "  {0}|".format(index)
            else:
                print " {0}|".format(index)
        print "|    0 1 2 3 4 5 6 7 8 9 10   |"
        print " -----------------------------"

    def move_ring(self, player, ring_move):
        start_x = ring_move.get_start_x()
        start_y = ring_move.get_start_y()
        self._check_position_owned(player, start_x, start_y)

        end_x = ring_move.get_end_x()
        end_y = ring_move.get_end_y()
        self._check_position_empty(end_x, end_y)

        jumped_line = self._get_jumped_line(start_x, start_y, end_x, end_y)
        self._check_empty_fields(jumped_line)  # check if not to many empty fields jumped
        self._check_jump_over_ring(jumped_line)  # jump over ring is incorrect

        # we are sure move is correct
        # perform the move
        self._place_marker(player, PlacementMove(start_x, start_y))
        self.place_ring(player, PlacementMove(end_x, end_y))
        self._switch_markers(ring_move)  # switch markers in line

    def place_ring(self, player, placement_move):
        sign = Board._SIGNS[player.get_type() + '_RING']
        x = placement_move.get_x()
        y = placement_move.get_y()

        Board._check_position_in_range(x, y)  # check if in range
        self._check_position_empty(x, y)  # check if empty field
        self.board[y][x] = sign

    def get_field(self, x, y):
        Board._check_position_in_range(x, y)
        return self.board[y][x]

    def _place_marker(self, player, placement_move):
        sign = Board._SIGNS[player.get_type() + '_MARKER']
        x = placement_move.get_x()
        y = placement_move.get_y()

        Board._check_position_in_range(x, y)  # check if in range
        self._check_position_owned(player, x, y)  # check if own field
        self.board[y][x] = sign

    def _switch_markers(self, ring_move):
        start_x = ring_move.get_start_x()
        start_y = ring_move.get_start_y()
        end_x = ring_move.get_end_x()
        end_y = ring_move.get_end_y()

        line_indexes = self._get_jumped_line_indexes(start_x, start_y, end_x, end_y)
        for index_tuple in line_indexes:
            if self.board[index_tuple[0]][index_tuple[1]] == Board._SIGNS['WHITE_MARKER']:
                self.board[index_tuple[0]][index_tuple[1]] = Board._SIGNS['BLACK_MARKER']
            elif self.board[index_tuple[0]][index_tuple[1]] == Board._SIGNS['BLACK_MARKER']:
                self.board[index_tuple[0]][index_tuple[1]] = Board._SIGNS['WHITE_MARKER']

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

    def _get_jumped_line(self, start_x, start_y, end_x, end_y):
        line_indexes = Board._get_jumped_line_indexes(start_x, start_y, end_x, end_y)
        line = [self.board[index_tuple[0]][index_tuple[1]] for index_tuple in line_indexes]
        return line

    def how_many_fives_in_row(self, player):
        fives_counter = 0
        # check vertical
        for x in range(Board._SIZE_X):
            line = [self.board[i][x] for i in range(Board._SIZE_Y) if (i + x % 2) % 2 == 0]
            max_counter = Board._count_fives_in_line(player, line)
            if max_counter >= 5:
                fives_counter += (max_counter - 4)

        # check diagonal
        # down
        for index in range(-4, 14):
            line = [self.board[index + i][i] for i in range(Board._SIZE_X) if Board._is_position_in_range(i, index + i)]
            max_counter = Board._count_fives_in_line(player, line)
            if max_counter >= 5:
                fives_counter += (max_counter - 4)

        # up
        for index in range(6, 24):
            line = [self.board[index - i][i] for i in range(Board._SIZE_X) if Board._is_position_in_range(i, index - i)]
            max_counter = Board._count_fives_in_line(player, line)
            if max_counter >= 5:
                fives_counter += (max_counter - 4)

        return fives_counter
