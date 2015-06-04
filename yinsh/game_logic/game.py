"""
Game module
"""
from yinsh.game_logic.board import Board, BoardUtils


class Game(object):
    """
    Game manager class.
    """

    def __init__(self, player1, player2):
        self.white_player = player1
        self.black_player = player2
        self.board = Board()
        self.finished = False
        self.winner = None

    def start(self):
        """
        Start game function
        :return:
        """
        BoardUtils.show_intro()
        # placement phase
        placement_moves = 5
        for i in range(0, placement_moves):
            # white placement
            self._single_placement(self.white_player, i)

            # black placement
            self._single_placement(self.black_player, i)

        print "Placement phase finished."

        # movement phase
        i = 0  # for test purpose
        while not self.finished:
            # check if markers are available
            if not self.board.is_marker_available():
                self.finished = True
                self.winner = self._get_winner()
                break

            self._move_and_check_situation(self.white_player, i)  # white moves
            if self.finished:
                break
            self._move_and_check_situation(self.black_player, i)  # black moves
            i += 1
        self.show_game_result()

    def show_game_result(self):
        """
        Shows game final result
        :return:
        """
        winner = "with a DRAW"
        if self.winner is not None:
            winner = " " + self.winner.get_type() + " wins"
        print " _____________________________ "
        print "|                             |"
        print "|       Game finished         |"
        print "|       {0}           |".format(winner)
        print "|_____________________________|"

    def _get_winner(self):
        """
        Returns game winner or None if a draw occurred. Throws error if game is not finished.
        :return:
        """
        if not self.finished:
            raise ValueError("Game not finished")
        if self.white_player.get_points() > self.black_player.get_points():
            return self.white_player
        if self.white_player.get_points() < self.black_player.get_points():
            return self.black_player
        return None

    def _single_placement(self, player, index):
        """
        Perform single ring placement
        :param player:
        :param index:
        :return:
        """
        self.board.show(self.white_player, self.black_player)
        while True:
            try:
                move = player.placement_move(index)
                self.board.place_ring(player, move)
                break
            except ValueError as err:
                print "Wrong move: ", err, " Try again."

    def _single_ring_move(self, player, index):
        """
        Perform single ring move
        :param player:
        :param index:
        :return:
        """
        self.board.show(self.white_player, self.black_player)
        while True:
            try:
                ring_move = player.ring_move(index)
                self.board.move_ring(player, ring_move)
                break
            except ValueError as err:
                print "Wrong move: ", err, " Try again."

    def _single_ring_remove(self, player, index):
        """
        Perform single ring remove
        :param player:
        :param index:
        :return:
        """
        self.board.show(self.white_player, self.black_player)
        while True:
            try:
                ring_remove = player.ring_remove(index)
                self.board.remove_ring(player, ring_remove)
                break
            except ValueError as err:
                print "Wrong move: ", err, " Try again."

    def _get_row_to_delete(self, player, index):
        """
        Get from user a row for deletion.
        :param player:
        :param index:
        :return:
        """
        self.board.show(self.white_player, self.black_player)
        while True:
            try:
                ring_move = player.five_in_row_choose(index)
                row_to_delete = self.board.get_row_to_delete(player, ring_move)
                if row_to_delete is None:
                    raise ValueError("Cannot find row to delete.")
                return row_to_delete
            except ValueError as err:
                print "Wrong move: ", err, " Try again."

    def _get_opponent(self, player):
        """
        Get player's opponent
        :param player:
        :return:
        """
        if player == self.white_player:
            opponent = self.black_player
        else:
            opponent = self.white_player

        return opponent

    def _move_and_check_situation(self, player, index):
        """
        Perform single ring move and check board situation.
        :param player:
        :param index:
        :return:
        """
        self._single_ring_move(player, index)

        # check if 5 in row occurred for player or opponent
        self._single_situation_check(player, index)
        self._single_situation_check(self._get_opponent(player), index)

    def _single_situation_check(self, player, index):
        """
        Perform single situation check for a player
        :param player:
        :param index:
        :return:
        """
        player_fives = self.board.how_many_fives_in_row(player)
        while player_fives > 0:
            if player_fives == 1:
                self.board.delete_row(self.board.get_fives_in_row_indexes(player)[0])  # delete row
            elif player_fives > 1:
                if len(set(
                        sum(self.board.get_fives_in_row_indexes(player), []))) == player_fives * 5:
                    row_to_delete = self.board.get_fives_in_row_indexes(player)[0]
                else:
                    row_to_delete = self._get_row_to_delete(player, index)
                self.board.delete_row(row_to_delete)

            # remove ring
            self._single_ring_remove(player, index)

            # add point
            player.add_point()

            if player.get_points() == 3:
                self.winner = player
                self.finished = True
                return
            player_fives = self.board.how_many_fives_in_row(player)
