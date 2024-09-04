import unittest

from game.Square import Square
from game.piece import Piece


class TestSquare(unittest.TestCase):
    def test_empty_square(self):
        square = Square()
        self.assertTrue(square.is_empty())

    def test_put_piece(self):
        square = Square()
        piece = Piece("black")
        square.set_piece(piece)
        self.assertEqual(piece, square.get_piece())

    def test_taken_square(self):
        square = Square()
        piece = Piece("black")
        square.set_piece(piece)
        self.assertFalse(square.is_empty())
