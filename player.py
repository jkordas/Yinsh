from move import PlacementMove, RingMove

__author__ = 'jkordas'


class PlayerType(object):
    WHITE = "WHITE"
    BLACK = 'BLACK'

class Player(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def get_type(self):
        return self.type

    def placement_move(self, iteration):
        # TODO get user input
        pass

    def ring_move(self, iteration):
        # TODO get user input
        pass


class WhitePlayerStub(Player):
    def __init__(self):
        Player.__init__(self, "WhitePlayerStub", PlayerType.WHITE)

    def placement_move(self, iteration):
        if iteration == 0:
            return PlacementMove(2, 2)
        if iteration == 1:
            return PlacementMove(4, 2)
        if iteration == 2:
            return PlacementMove(4, 10)
        if iteration == 3:
            return PlacementMove(8, 8)
        if iteration == 4:
            return PlacementMove(9, 3)

    def ring_move(self, iteration):
        if iteration == 0:
            return RingMove(4, 2, 4, 0)
        raise AssertionError('Not ready yet')


class BlackPlayerStub(Player):
    def __init__(self):
        Player.__init__(self, "WhitePlayerStub", PlayerType.BLACK)

    def placement_move(self, iteration):
        if iteration == 0:
            return PlacementMove(2, 8)
        if iteration == 1:
            return PlacementMove(4, 6)
        if iteration == 2:
            return PlacementMove(5, 11)
        if iteration == 3:
            return PlacementMove(8, 10)
        if iteration == 4:
            return PlacementMove(9, 7)

    def ring_move(self, iteration):
        if iteration == 0:
            return RingMove(4, 10, 4, 8)
        raise AssertionError('Not ready yet')