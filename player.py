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
        print "Placement Type: {0}".format("Placement move")
        input_text = raw_input("Position (x y - separated with space): ")
        input_array = input_text.split(" ")
        if len(input_array) != 2:
            raise ValueError('Provide 2 numbers separated with space.')

        return PlacementMove(int(input_array[0]), int(input_array[1]))

    def ring_move(self, iteration):
        print "Player: {0}".format(self.name)
        print "Placement Type: {0}".format("Ring move")
        start_input_text = raw_input("Start position (x y - separated with space): ")
        start_input_array = start_input_text.split(" ")
        if len(start_input_array) != 2:
            raise ValueError('Provide 2 numbers separated with space for start field.')

        end_input_text = raw_input("Start position (x y - separated with space): ")
        end_input_array = end_input_text.split(" ")
        if len(end_input_array) != 2:
            raise ValueError('Provide 2 numbers separated with space for end field.')

        return RingMove(int(start_input_array[0]), int(start_input_array[1]),
                        int(end_input_array[0]), int(end_input_array[1]))


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