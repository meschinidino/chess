import unittest

from game.piece import Piece
from game.square import Square


class TestSquare(unittest.TestCase):
    def test_empty_square(self):
        square = Square("black")
        self.assertEqual(square.get_color(), "black")
    def test_taken_square(self):
        piece = Piece("black")
        square = Square("black")
        square.set_piece(piece)
        self.assertTrue(square.has_piece())