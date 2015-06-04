"""
Board module
"""

import os
from yinsh.utils.move import PlacementMove


class BoardUtils(object):
    """
    Utils board helper class
    """

    @staticmethod
    def show_intro():
        """
        Display game introduction
        """
        print " _____________________________ "
        print "|                             |"
        print "|            Yinsh            |"
        print "|_____________________________|"
        for elem in sorted(Board.SIGNS):
            print "  {0}: {1}".format(elem, Board.SIGNS[elem])
        print

    @staticmethod
    def is_position_in_range(x_pos, y_pos):
        """
        Check if given position is in board range
        """
        if y_pos >= len(Board.BOARD_TEMPLATE):
            return False
        if x_pos not in Board.BOARD_TEMPLATE[y_pos]:
            return False
        return True

    @staticmethod
    def check_position_in_range(x_pos, y_pos):
        """
        Throws error if position in in board range
        """
        if not BoardUtils.is_position_in_range(x_pos, y_pos):
            raise ValueError("Position x: {0}, y: {1} is not in board range.".format(x_pos, y_pos))

    @staticmethod
    def check_empty_fields(line):
        """
        Check if line has acceptable number of empty fields while jumped
        """
        is_empty_acceptable = True
        for field in line:
            if field == Board.EMPTY_FIELD:
                if not is_empty_acceptable:
                    raise ValueError("Too many empty fields.")
            else:
                is_empty_acceptable = False

    @staticmethod
    def check_jump_over_ring(line):
        """
        Check if jumped line not contains a ring
        """
        if Board.SIGNS['WHITE_RING'] in line or Board.SIGNS['BLACK_RING'] in line:
            raise ValueError("Cannot jump over rings.")

    @staticmethod
    def count_fives_in_line(player, line):
        """
        Counts how many five rows player has on board
        """
        counter = 0
        max_counter = 0
        for elem in line:
            if elem == Board.SIGNS[player.get_type() + '_MARKER']:
                counter += 1
            else:
                counter = 0

            if counter > max_counter:
                max_counter = counter
        return max_counter

    @staticmethod
    def get_jumped_line_indexes(start_x, start_y, end_x, end_y):
        """
        Calculates board indexes for given jump
        """
        if start_x == end_x and start_y == end_y:
            raise ValueError("Start and stop position have to be different.")
        if start_y == end_y:
            raise ValueError("Wrong move. Cannot move horizontally.")
        if start_x != end_x and start_x + start_y != end_x + end_y and \
                                start_x - start_y != end_x - end_y:
            raise ValueError("Wrong move. Not in straight line.")

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


class Board(object):
    """
    Game board representation.
    """
    _SIZE_X = 11
    _SIZE_Y = 19
    BOARD_TEMPLATE = [[4, 6], [3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7, 9], [2, 4, 6, 8],
                      [1, 3, 5, 7, 9], [0, 2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [0, 2, 4, 6, 8, 10],
                      [1, 3, 5, 7, 9], [0, 2, 4, 6, 8, 10],
                      [1, 3, 5, 7, 9], [0, 2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8],
                      [1, 3, 5, 7, 9],
                      [2, 4, 6, 8], [3, 5, 7], [4, 6]]
    SIGNS = {
        'BLACK_MARKER': '*',
        'BLACK_RING': 'c',
        'WHITE_MARKER': '@',
        'WHITE_RING': 'o'
    }
    EMPTY_FIELD = '.'
    _MARKERS_NUMBER = 51

    def __init__(self):
        self.board = [[' ' for _ in range(Board._SIZE_X)] for _ in range(Board._SIZE_Y)]
        for index, row in enumerate(Board.BOARD_TEMPLATE):
            for num in row:
                self.board[index][num] = Board.EMPTY_FIELD
        self.used_markers = 0

    def show(self, white_player, black_player):
        """
        Display current board state
        :param white_player:
        :param black_player:
        :return:
        """
        os.system('clear')  # on linux / os x
        print
        print " -----------------------------"
        print "|LEFT MARKERS: {0}             |".format(self._MARKERS_NUMBER - self.used_markers)
        print "|WHITE: {0}             BLACK: {1}|".format(white_player.get_points(),
                                                           black_player.get_points())
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
        """
        Single ring move
        :param player:
        :param ring_move:
        :return:
        """
        start_x = ring_move['start_x']
        start_y = ring_move['start_y']
        self._check_position_owned(player, start_x, start_y)

        end_x = ring_move['end_x']
        end_y = ring_move['end_y']
        self._check_position_empty(end_x, end_y)

        jumped_line = self._get_jumped_line(start_x, start_y, end_x, end_y)
        BoardUtils.check_empty_fields(jumped_line)  # check if not to many empty fields jumped
        BoardUtils.check_jump_over_ring(jumped_line)  # jump over ring is incorrect

        # we are sure move is correct
        # perform the move
        self._place_marker(player, PlacementMove(start_x, start_y))
        self.place_ring(player, PlacementMove(end_x, end_y))
        self._switch_markers(ring_move)  # switch markers in line
        print "Ring moved: ({0},{1}) -> ({2},{3})".format(start_x, start_y, end_x, end_y)

    def remove_ring(self, player, ring_remove):
        """
        Single ring remove
        :param player:
        :param ring_remove:
        :return:
        """
        x_pos = ring_remove['x']
        y_pos = ring_remove['y']
        self._check_position_owned(player, x_pos, y_pos)
        self.board[y_pos][x_pos] = Board.EMPTY_FIELD
        print "Ring removed from: ({0},{1})".format(x_pos, y_pos)

    def place_ring(self, player, placement_move):
        """
        Single ring placement
        :param player:
        :param placement_move:
        :return:
        """
        sign = Board.SIGNS[player.get_type() + '_RING']
        x_pos = placement_move['x']
        y_pos = placement_move['y']

        BoardUtils.check_position_in_range(x_pos, y_pos)  # check if in range
        self._check_position_empty(x_pos, y_pos)  # check if empty field
        self.board[y_pos][x_pos] = sign
        # print "Ring placed at: ({0},{1})".format(x_pos, y_pos)

    def get_field(self, x_pos, y_pos):
        """
        Returns board field with given coordinates
        :param x_pos:
        :param y_pos:
        :return:
        """
        BoardUtils.check_position_in_range(x_pos, y_pos)
        return self.board[y_pos][x_pos]

    def _place_marker(self, player, placement_move):
        """
        Single marker placement
        :param player:
        :param placement_move:
        :return:
        """
        self.used_markers += 1
        sign = Board.SIGNS[player.get_type() + '_MARKER']
        x_pos = placement_move['x']
        y_pos = placement_move['y']

        BoardUtils.check_position_in_range(x_pos, y_pos)  # check if in range
        self._check_position_owned(player, x_pos, y_pos)  # check if own field
        self.board[y_pos][x_pos] = sign

    def _switch_markers(self, ring_move):
        """
        Single marker switch
        :param ring_move:
        :return:
        """
        start_x = ring_move['start_x']
        start_y = ring_move['start_y']
        end_x = ring_move['end_x']
        end_y = ring_move['end_y']

        line_indexes = BoardUtils.get_jumped_line_indexes(start_x, start_y, end_x, end_y)
        for index_tuple in line_indexes:
            if self.board[index_tuple[0]][index_tuple[1]] == Board.SIGNS['WHITE_MARKER']:
                self.board[index_tuple[0]][index_tuple[1]] = Board.SIGNS['BLACK_MARKER']
            elif self.board[index_tuple[0]][index_tuple[1]] == Board.SIGNS['BLACK_MARKER']:
                self.board[index_tuple[0]][index_tuple[1]] = Board.SIGNS['WHITE_MARKER']

    def is_marker_available(self):
        """
        True if markers still available, False otherwise
        :return:
        """
        return Board._MARKERS_NUMBER - self.used_markers > 0

    def _check_position_empty(self, x_pos, y_pos):
        """
        Throws an error if given position is already taken
        :param x_pos:
        :param y_pos:
        :return:
        """
        BoardUtils.check_position_in_range(x_pos, y_pos)
        if self.board[y_pos][x_pos] != Board.EMPTY_FIELD:
            raise ValueError("Field x: {0}, y: {1} is not empty.".format(x_pos, y_pos))

    def _check_position_owned(self, player, x_pos, y_pos):
        """
        Throws an error if given position is not owned by player
        :param player:
        :param x_pos:
        :param y_pos:
        :return:
        """
        BoardUtils.check_position_in_range(x_pos, y_pos)
        if self.board[y_pos][x_pos] != Board.SIGNS[player.get_type() + '_RING']:
            raise ValueError("Field x: {0}, y: {1} is not owned by player.".format(x_pos, y_pos))

    def _get_jumped_line(self, start_x, start_y, end_x, end_y):
        """
        Returns line for given jump coordinates
        :param start_x:
        :param start_y:
        :param end_x:
        :param end_y:
        :return:
        """
        line_indexes = BoardUtils.get_jumped_line_indexes(start_x, start_y, end_x, end_y)
        line = [self.board[index_tuple[0]][index_tuple[1]] for index_tuple in line_indexes]
        return line

    def how_many_fives_in_row(self, player):
        """
        Calculates number of fives in row for player
        :param player:
        :return:
        """
        fives_num = len(self.get_fives_in_row_indexes(player))
        return fives_num

    def get_fives_in_row_indexes(self, player):
        """
        Returns player's fives in row board fields indexes
        :param player:
        :return:
        """
        lines_list = []
        # check vertical
        for x_pos in range(Board._SIZE_X):
            line = [(x_pos, i) for i in range(Board._SIZE_Y) if (i + x_pos % 2) % 2 == 0]
            lines_list.append(line)

        # check diagonal
        # down
        for index in range(-4, 14):
            line = [(i, index + i) for i in range(Board._SIZE_X) if
                    BoardUtils.is_position_in_range(i, index + i)]
            lines_list.append(line)

        # up
        for index in range(6, 24):
            line = [(i, index - i) for i in range(Board._SIZE_X) if
                    BoardUtils.is_position_in_range(i, index - i)]
            lines_list.append(line)

        result = []
        for line in lines_list:
            five = []
            for position in line:
                five.append(position)
                if len(five) < 5:
                    continue
                elif len(five) > 5:
                    five.pop(0)
                # filter
                correct = True
                for elem in five:
                    if self.board[elem[1]][elem[0]] != Board.SIGNS[player.get_type() + '_MARKER']:
                        correct = False
                        break

                if correct:
                    result.append(list(five))

        return result

    def delete_row(self, row_indexes):
        """
        Single row deletion
        :param row_indexes:
        :return:
        """
        self.used_markers -= 5
        for position in row_indexes:
            self.board[position[1]][position[0]] = Board.EMPTY_FIELD
        print "Row deleted: ({0},{1}) -> ({2},{3})".format(row_indexes[0][0],
                                                           row_indexes[0][1], row_indexes[4][0],
                                                           row_indexes[4][1])

    def get_row_to_delete(self, player, ring_move):
        """
        Selects row to delete
        :param player:
        :param ring_move:
        :return:
        """
        start_x = ring_move['start_x']
        start_y = ring_move['start_y']
        end_x = ring_move['end_x']
        end_y = ring_move['end_y']
        fives_in_row_indexes = self.get_fives_in_row_indexes(player)

        for five_in_row in fives_in_row_indexes:
            if five_in_row[0] == (start_x, start_y) and five_in_row[4] == (end_x, end_y):
                return five_in_row
            elif five_in_row[4] == (start_x, start_y) and five_in_row[0] == (end_x, end_y):
                return five_in_row

        return None
