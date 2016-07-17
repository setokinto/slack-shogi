import unittest
from app.modules.shogi import Shogi, Koma

class ShogiTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_move_76fu(self):
        shogi = Shogi()
        shogi.move(2, 6, 2, 5, False)
        self.assertEqual(shogi.board[5][2], Koma.fu)
        self.assertEqual(shogi.board[6][2], Koma.empty)

