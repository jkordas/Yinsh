from board import Board

__author__ = 'jkordas'


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
        # placement phase
        placement_moves = 5  # TODO: only for test! change to 5
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
                # TODO check who wins
                break

            self._move_and_check_situation(self.white_player, i)  # white moves
            self._move_and_check_situation(self.black_player, i)  # black moves
            i += 1

    def _single_placement(self, player, index):
        self.board.show()
        while True:
            try:
                move = player.placement_move(index)
                self.board.place_ring(player, move)
                break
            except ValueError as e:
                print "Wrong move: ", e, " Try again."

    def _single_ring_move(self, player, index):
        self.board.show()
        while True:
            try:
                ring_move = player.ring_move(index)
                self.board.move_ring(player, ring_move)
                break
            except ValueError as e:
                print "Wrong move: ", e, " Try again."

    def _move_and_check_situation(self, player, index):
        self._single_ring_move(player, index)

        # TODO check if 5 in row occurred for player or opponent
        player_fives = self.board.how_many_fives_in_row(player)
        if player_fives > 0:
            # TODO
            pass

        if player == self.white_player:
            opponent = self.black_player
        else:
            opponent = self.white_player

        opponent_fives = self.board.how_many_fives_in_row(opponent)
        if opponent_fives > 0:
            # TODO
            pass
