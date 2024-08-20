import unittest

from game.pawn import Pawn


class UnitTests(unittest.TestCase):
    def test_pawn(self):
        pawn = Pawn("black")
        self.assertEqual(pawn.get_color(), "black")
