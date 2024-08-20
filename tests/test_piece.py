import unittest

from game.piece import Piece


class UnitTests(unittest.TestCase):
    def test_piece_color(self):
        piece = Piece("black")
        self.assertEqual(piece.get_color(), "black")