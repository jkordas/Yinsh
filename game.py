from board import Board

__author__ = 'jkordas'


class Game(object):
    def __init__(self, player1, player2):
        self.white_player = player1
        self.black_player = player2
        self.board = Board()
        self.finished = False
        self.winner = None

    def start(self):
        # placement phase
        placement_moves = 1  # TODO: only for test! change to 5
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

            # show board
            self.board.show()

            # white moves
            ring_move = self.white_player.ring_move(i)
            self.board.move_ring(self.white_player, ring_move)
            # TODO check if 5 in row occurred for player or opponent

            # show board
            # black moves
            # TODO

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
