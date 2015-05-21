from board import Board
from move import PlacementMove
from player import Player, PlayerType

__author__ = 'jkordas'

import unittest


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player = Player("TestWhitePlayer", PlayerType.WHITE)

    def test_ring_placement(self):
        self.board.place_ring(self.player, PlacementMove(2, 2))
        self.assertEqual(self.board.get_field(2, 2), Board._SIGNS['WHITE_RING'], "White ring placement fails")

    def test_ring_placement_exception(self):
        self.assertRaises(ValueError, lambda: self.board.place_ring(self.player, PlacementMove(1, 0)))


if __name__ == '__main__':
    unittest.main()
