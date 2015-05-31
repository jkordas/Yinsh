import unittest

from board import Board
from move import PlacementMove, RingMove
from player import Player, PlayerType


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.white_player = Player("TestWhitePlayer", PlayerType.WHITE)
        self.black_player = Player("TestBlackPlayer", PlayerType.BLACK)

    def place_five_in_row(self):
        self.board.place_ring(self.white_player, PlacementMove(4, 0))
        self.board._place_marker(self.white_player, PlacementMove(4, 0))
        self.board.place_ring(self.white_player, PlacementMove(5, 1))
        self.board._place_marker(self.white_player, PlacementMove(5, 1))
        self.board.place_ring(self.white_player, PlacementMove(6, 2))
        self.board._place_marker(self.white_player, PlacementMove(6, 2))
        self.board.place_ring(self.white_player, PlacementMove(7, 3))
        self.board._place_marker(self.white_player, PlacementMove(7, 3))
        self.board.place_ring(self.white_player, PlacementMove(8, 4))
        self.board._place_marker(self.white_player, PlacementMove(8, 4))

    def test_white_ring_placement(self):
        self.board.place_ring(self.white_player, PlacementMove(2, 2))
        self.assertEqual(Board._SIGNS['WHITE_RING'], self.board.get_field(2, 2), "White ring placement fails")

    def test_black_ring_placement(self):
        self.board.place_ring(self.black_player, PlacementMove(2, 4))
        self.assertEqual(Board._SIGNS['BLACK_RING'], self.board.get_field(2, 4), "Black ring placement fails")

    def test_ring_placement_wrong_position(self):
        self.assertRaises(ValueError, lambda: self.board.place_ring(self.white_player, PlacementMove(1, 0)))

    def test_ring_placement_position_taken(self):
        self.board.place_ring(self.black_player, PlacementMove(2, 4))
        self.assertRaises(ValueError, lambda: self.board.place_ring(self.white_player, PlacementMove(2, 4)))

    def test_jumped_line_diagonal(self):
        self.board.place_ring(self.black_player, PlacementMove(2, 2))
        self.board.place_ring(self.white_player, PlacementMove(5, 5))

        line = self.board._get_jumped_line(2, 2, 6, 6)
        expected = [Board._EMPTY_FIELD, Board._EMPTY_FIELD, Board._SIGNS['WHITE_RING']]
        self.assertEqual(expected, line, "Jump line test failed. Expected {0}, Got: {1}".format(expected, str(line)))

        line = self.board._get_jumped_line(5, 5, 6, 6)
        expected = []
        self.assertEqual(expected, line, "Jump line test failed. Expected {0}, Got: {1}".format(expected, str(line)))

        line = self.board._get_jumped_line(6, 6, 2, 2)
        expected = [Board._SIGNS['WHITE_RING'], Board._EMPTY_FIELD, Board._EMPTY_FIELD]
        self.assertEqual(expected, line, "Jump line test failed. Expected {0}, Got: {1}".format(expected, str(line)))

    def test_jumped_line_vertical(self):
        self.board.place_ring(self.black_player, PlacementMove(2, 2))
        self.board.place_ring(self.white_player, PlacementMove(2, 4))

        line = self.board._get_jumped_line(2, 2, 2, 10)
        expected = [Board._SIGNS['WHITE_RING'], Board._EMPTY_FIELD, Board._EMPTY_FIELD]
        self.assertEqual(expected, line, "Jump line test failed. Expected {0}, Got: {1}".format(expected, str(line)))

    def test_jump_too_many_empty_fields(self):
        self.board.place_ring(self.black_player, PlacementMove(2, 2))
        self.board.place_ring(self.white_player, PlacementMove(2, 6))
        self.board.move_ring(self.white_player, RingMove(2, 6, 3, 5))

        self.assertRaises(ValueError, lambda: self.board.move_ring(self.black_player, RingMove(2, 2, 2, 10)))

    def test_jump_over_ring(self):
        self.board.place_ring(self.black_player, PlacementMove(2, 2))
        self.board.place_ring(self.white_player, PlacementMove(2, 4))

        self.assertRaises(ValueError, lambda: self.board.move_ring(self.black_player, RingMove(2, 2, 2, 6)))

    def test_ring_move(self):
        self.board.place_ring(self.black_player, PlacementMove(2, 2))
        self.board.place_ring(self.white_player, PlacementMove(2, 6))

        self.board.move_ring(self.white_player, RingMove(2, 6, 3, 5))
        self.assertEqual(Board._SIGNS['WHITE_MARKER'], self.board.get_field(2, 6))

        self.board.move_ring(self.white_player, RingMove(3, 5, 1, 7))
        self.assertEqual(Board._SIGNS['BLACK_MARKER'], self.board.get_field(2, 6))

    def test_fives_in_row_vertical(self):
        self.board.place_ring(self.black_player, PlacementMove(2, 2))
        self.board._place_marker(self.black_player, PlacementMove(2, 2))
        self.board.place_ring(self.black_player, PlacementMove(2, 4))
        self.board._place_marker(self.black_player, PlacementMove(2, 4))

        self.assertEqual(0, self.board.how_many_fives_in_row(self.black_player))
        self.assertEqual(0, self.board.how_many_fives_in_row(self.white_player))

        self.board.place_ring(self.black_player, PlacementMove(2, 6))
        self.board._place_marker(self.black_player, PlacementMove(2, 6))
        self.board.place_ring(self.black_player, PlacementMove(2, 8))
        self.board._place_marker(self.black_player, PlacementMove(2, 8))
        self.board.place_ring(self.black_player, PlacementMove(2, 10))
        self.board._place_marker(self.black_player, PlacementMove(2, 10))
        self.assertEqual(1, self.board.how_many_fives_in_row(self.black_player))
        self.assertEqual(0, self.board.how_many_fives_in_row(self.white_player))

        self.board.place_ring(self.black_player, PlacementMove(2, 12))
        self.board._place_marker(self.black_player, PlacementMove(2, 12))
        self.assertEqual(2, self.board.how_many_fives_in_row(self.black_player))
        self.assertEqual(0, self.board.how_many_fives_in_row(self.white_player))

    def test_fives_in_row_diagonal(self):
        self.board.place_ring(self.white_player, PlacementMove(2, 2))
        self.board._place_marker(self.white_player, PlacementMove(2, 2))
        self.board.place_ring(self.white_player, PlacementMove(4, 4))
        self.board._place_marker(self.white_player, PlacementMove(4, 4))

        self.assertEqual(0, self.board.how_many_fives_in_row(self.black_player))
        self.assertEqual(0, self.board.how_many_fives_in_row(self.white_player))

        self.board.place_ring(self.white_player, PlacementMove(3, 3))
        self.board._place_marker(self.white_player, PlacementMove(3, 3))
        self.board.place_ring(self.white_player, PlacementMove(5, 5))
        self.board._place_marker(self.white_player, PlacementMove(5, 5))
        self.board.place_ring(self.white_player, PlacementMove(6, 6))
        self.board._place_marker(self.white_player, PlacementMove(6, 6))
        self.assertEqual(1, self.board.how_many_fives_in_row(self.white_player))
        self.assertEqual(0, self.board.how_many_fives_in_row(self.black_player))

        self.board.place_ring(self.white_player, PlacementMove(7, 7))
        self.board._place_marker(self.white_player, PlacementMove(7, 7))
        self.assertEqual(2, self.board.how_many_fives_in_row(self.white_player))
        self.assertEqual(0, self.board.how_many_fives_in_row(self.black_player))

    def test_fives_in_row_diagonal_edge(self):
        self.place_five_in_row()
        self.assertEqual(1, self.board.how_many_fives_in_row(self.white_player))
        self.assertEqual(0, self.board.how_many_fives_in_row(self.black_player))

        self.board.place_ring(self.white_player, PlacementMove(9, 5))
        self.board._place_marker(self.white_player, PlacementMove(9, 5))
        self.assertEqual(2, self.board.how_many_fives_in_row(self.white_player))
        self.assertEqual(0, self.board.how_many_fives_in_row(self.black_player))

    def test_fives_in_row_indexes(self):
        self.place_five_in_row()
        result = self.board.get_fives_in_row_indexes(self.white_player)
        self.assertEqual([[(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)]], result)

        self.board.place_ring(self.white_player, PlacementMove(9, 5))
        self.board._place_marker(self.white_player, PlacementMove(9, 5))
        self.assertEqual([[(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], [(5, 1), (6, 2), (7, 3), (8, 4), (9, 5)]],
                         self.board.get_fives_in_row_indexes(self.white_player))

    def test_fives_in_row_delete(self):
        self.place_five_in_row()
        result = self.board.get_fives_in_row_indexes(self.white_player)
        self.assertEqual([[(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)]], result)
        self.board.delete_row(result[0])

        result = self.board.get_fives_in_row_indexes(self.white_player)
        self.assertEqual([], result)







if __name__ == '__main__':
    unittest.main()
