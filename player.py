from move import PlacementMove, RingMove

__author__ = 'jkordas'


class Player(object):
    def __init__(self, name):
        self.name = name

    def placement_move(self, iteration):
        if self.name == "White-player":
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

        if self.name == "Black-player":
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

    def ring_move(self):
        if self.name == "White-player":
            return RingMove(4, 2, 4, 0)