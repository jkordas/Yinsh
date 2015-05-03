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
        placement_moves = 5
        for i in range(0, placement_moves):
            # white placement
            move = self.white_player.placement_move(i)
            self.board.place_white_open(move)

            # black placement
            move = self.black_player.placement_move(i)
            self.board.place_black_open(move)
            self.board.show()
        print "Placement phase finished."

        # movement phase
        while not self.finished:
            # check if markers are available
            if not self.board.is_marker_available():
                self.finished = True
                # check who wins
                break

            # show board
            self.board.show()

            # white moves
            ring_move = self.white_player.ring_move()
            self.board.move_white_ring(ring_move)

            # show board
            # black moves
            pass



