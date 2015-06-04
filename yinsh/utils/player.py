"""
Player module
"""
from yinsh.utils.move import RingMove, PlacementMove

PLAYER_TYPE = {
    'WHITE': "WHITE",
    'BLACK': 'BLACK'
}


class Player(object):
    """
    Represents game player. Responsible for gathering user moves.
    """

    def __init__(self, name, _type):
        self.name = name
        self.type = _type
        self.points = 0

    def get_type(self):
        """
        Type getter
        """
        return self.type

    def get_name(self):
        """
        Name getter
        """
        return self.name

    def get_points(self):
        """
        Points getter
        """
        return self.points

    def add_point(self):
        """
        Add user a point and display info
        """
        self.points += 1
        print "Player: {0} scores a point.".format(self.name)

    def placement_move(self, _):
        """
        Get input for ring placement
        """
        print "Player: {0}".format(self.name)
        print "Move Type: {0}".format("Placement move")
        input_text = raw_input("Position (x y - separated with space): ")
        input_array = input_text.split(" ")
        if len(input_array) != 2:
            raise ValueError('Provide 2 numbers separated with space.')

        return PlacementMove(int(input_array[0]), int(input_array[1]))

    def ring_move(self, _):
        """
        Get input for ring movement
        """
        print "Player: {0}".format(self.name)
        print "Move Type: {0}".format("Ring move")
        start_input_text = raw_input("Start position (x y - separated with space): ")
        start_input_array = start_input_text.split(" ")
        if len(start_input_array) != 2:
            raise ValueError('Provide 2 numbers separated with space for start field.')

        end_input_text = raw_input("Stop position (x y - separated with space): ")
        end_input_array = end_input_text.split(" ")
        if len(end_input_array) != 2:
            raise ValueError('Provide 2 numbers separated with space for end field.')

        return RingMove(int(start_input_array[0]), int(start_input_array[1]),
                        int(end_input_array[0]), int(end_input_array[1]))

    def ring_remove(self, _):
        """
        Get input for ring remove
        """
        print "Player: {0}".format(self.name)
        print "Move Type: {0}".format("Ring remove")
        input_text = raw_input("Position (x y - separated with space): ")
        input_array = input_text.split(" ")
        if len(input_array) != 2:
            raise ValueError('Provide 2 numbers separated with space.')

        return PlacementMove(int(input_array[0]), int(input_array[1]))

    def five_in_row_choose(self, _):
        """
        Get input for five in row choose
        """
        print "Player: {0}".format(self.name)
        print "Move Type: {0}".format("Row remove")
        start_input_text = raw_input("Start position (x y - separated with space): ")
        start_input_array = start_input_text.split(" ")
        if len(start_input_array) != 2:
            raise ValueError('Provide 2 numbers separated with space for start field.')

        end_input_text = raw_input("End position (x y - separated with space): ")
        end_input_array = end_input_text.split(" ")
        if len(end_input_array) != 2:
            raise ValueError('Provide 2 numbers separated with space for end field.')

        return RingMove(int(start_input_array[0]), int(start_input_array[1]),
                        int(end_input_array[0]), int(end_input_array[1]))


class WhitePlayerStub(Player):
    """
    White player stub for test purpose.
    """

    def __init__(self):
        Player.__init__(self, "WhitePlayerStub", PLAYER_TYPE['WHITE'])

    def placement_move(self, iteration):
        """
        White player stub - placement move implementation
        """
        if iteration == 0:
            move = PlacementMove(2, 2)
        if iteration == 1:
            move = PlacementMove(4, 2)
        if iteration == 2:
            move = PlacementMove(4, 10)
        if iteration == 3:
            move = PlacementMove(8, 8)
        if iteration == 4:
            move = PlacementMove(9, 3)
        return move

    @staticmethod
    def _ring_move_one_to_ten(iteration):
        """
        Superfluous method to deal with too many branches pylint warning
        """
        if iteration == 0:
            move = RingMove(4, 2, 4, 0)
        if iteration == 1:
            move = RingMove(4, 0, 4, 4)
        if iteration == 2:
            move = RingMove(9, 3, 8, 4)
        if iteration == 3:
            move = RingMove(8, 4, 7, 3)
        if iteration == 4:
            move = RingMove(7, 3, 6, 2)
        if iteration == 5:
            move = RingMove(6, 2, 5, 1)
        if iteration == 6:
            move = RingMove(5, 1, 3, 3)
        if iteration == 7:
            move = RingMove(3, 3, 4, 4)
        if iteration == 8:
            move = RingMove(4, 4, 5, 3)
        if iteration == 9:
            move = RingMove(2, 2, 6, 6)
        if iteration == 10:
            move = RingMove(8, 8, 7, 9)

        return move

    def ring_move(self, iteration):
        """
        White player stub - ring move implementation
        """
        if iteration < 11:
            move = WhitePlayerStub._ring_move_one_to_ten(iteration)
        if iteration == 11:
            move = RingMove(7, 9, 9, 11)
        if iteration == 12:
            move = RingMove(5, 3, 5, 1)
        if iteration == 13:
            move = RingMove(4, 10, 6, 12)
        if iteration == 14:
            move = RingMove(9, 11, 8, 12)
        if iteration == 15:
            move = RingMove(6, 12, 7, 13)
        if iteration == 16:
            move = RingMove(7, 13, 3, 9)
        if iteration == 17:
            move = RingMove(3, 9, 1, 7)
        if iteration == 18:
            move = RingMove(6, 6, 2, 10)
        if iteration == 19:
            move = RingMove(8, 12, 6, 14)
        return move

    def ring_remove(self, iteration):
        """
        White player stub - ring remove implementation
        """
        if iteration == 6:
            move = PlacementMove(4, 4)
        return move


class BlackPlayerStub(Player):
    """
    Black player stub for test purpose.
    """

    def __init__(self):
        Player.__init__(self, "BlackPlayerStub", PLAYER_TYPE['BLACK'])

    def placement_move(self, iteration):
        """
        Black player stub - placement move implementation
        """
        if iteration == 0:
            move = PlacementMove(2, 8)
        if iteration == 1:
            move = PlacementMove(4, 6)
        if iteration == 2:
            move = PlacementMove(5, 11)
        if iteration == 3:
            move = PlacementMove(3, 7)
        if iteration == 4:
            move = PlacementMove(9, 7)
        return move

    @staticmethod
    def _ring_move_one_to_ten(iteration):
        """
        Superfluous method to deal with too many branches pylint warning
        """
        if iteration == 0:
            move = RingMove(3, 7, 4, 8)
        if iteration == 1:
            move = RingMove(5, 11, 5, 5)
        if iteration == 2:
            move = RingMove(5, 5, 5, 7)
        if iteration == 3:
            move = RingMove(2, 8, 0, 10)
        if iteration == 4:
            move = RingMove(4, 6, 3, 5)
        if iteration == 5:
            move = RingMove(3, 5, 2, 6)
        if iteration == 6:
            move = RingMove(9, 7, 8, 6)
        if iteration == 7:
            move = RingMove(0, 10, 1, 11)
        if iteration == 8:
            move = RingMove(1, 11, 2, 10)
        if iteration == 9:
            move = RingMove(2, 10, 3, 11)
        if iteration == 10:
            move = RingMove(3, 11, 4, 12)

        return move

    def ring_move(self, iteration):
        """
        Black player stub - ring move implementation
        """
        if iteration < 11:
            move = BlackPlayerStub._ring_move_one_to_ten(iteration)
        if iteration == 11:
            move = RingMove(4, 12, 5, 13)
        if iteration == 12:
            move = RingMove(5, 13, 8, 16)
        if iteration == 13:
            move = RingMove(8, 16, 1, 9)
        if iteration == 14:
            move = RingMove(1, 9, 6, 14)
        if iteration == 15:
            move = RingMove(5, 7, 6, 8)
        if iteration == 16:
            move = RingMove(6, 8, 8, 10)
        if iteration == 17:
            move = RingMove(4, 8, 5, 9)
        if iteration == 18:
            move = RingMove(8, 6, 7, 7)
        return move

    def ring_remove(self, iteration):
        """
        Black player stub - ring remove implementation
        """
        if iteration == 14:
            move = PlacementMove(2, 6)
        if iteration == 16:
            move = PlacementMove(6, 14)
        if iteration == 19:
            move = PlacementMove(8, 10)
        return move

    def five_in_row_choose(self, iteration):
        """
        Black player stub - five in row choose implementation
        """
        if iteration == 14:
            move = RingMove(1, 9, 5, 13)
        if iteration == 16:
            move = RingMove(4, 6, 8, 10)
        return move
