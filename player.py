from move import PlacementMove, RingMove
import time


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
        print "Player: {0}".format(self.name)
        print "Placement Type: {0}".format("PlacementMove")
        input_text = raw_input("Position (eg. 1 3): ")
        input_array = input_text.split(" ")
        assert (len(input_array) == 2)

        # TODO: validate
        return PlacementMove(int(input_array[0]), int(input_array[1]))

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
        time.sleep(0.5)  # to get exception at the end of output
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