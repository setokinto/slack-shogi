import unittest
from app.modules.shogi import Shogi
from app.modules.parse_input import ParseInput

class ShogiTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_parse1(self):
        shogi = Shogi()
        self.assertEqual(ParseInput.parse("７６歩", shogi), (2,6, 2,5, False))
        self.assertEqual(ParseInput.parse("7六歩", shogi), (2,6, 2,5, False))
        self.assertEqual(ParseInput.parse("７5歩", shogi), False)
        self.assertEqual(ParseInput.parse("34歩", shogi), False)
        shogi.move(2, 6, 2, 5, False)
        self.assertEqual(ParseInput.parse("34歩", shogi), (6,2, 6,3, False))
        self.assertEqual(ParseInput.parse("35歩", shogi), False)
        self.assertEqual(ParseInput.parse("75歩", shogi), False)

    def test_parse2(self):
        shogi = Shogi()
        self.assertEqual(ParseInput.parse("58金右", shogi), (5,8, 4,7, False))
        self.assertEqual(ParseInput.parse("58金左", shogi), (3,8, 4,7, False))
        self.assertEqual(ParseInput.parse("58金直", shogi), False)
        self.assertEqual(ParseInput.parse("58金寄", shogi), False)
        self.assertEqual(ParseInput.parse("58金引", shogi), False)
        shogi.move(4, 8, 4, 4, False)
        shogi.move(5, 8, 4, 8, False)
        shogi.first = True
        self.assertEqual(ParseInput.parse("58金直", shogi), (4,8, 4,7, False))
        self.assertEqual(ParseInput.parse("58金左", shogi), (3,8, 4,7, False))
        self.assertEqual(ParseInput.parse("58金右", shogi), False)
        self.assertEqual(ParseInput.parse("58金寄", shogi), False)
        self.assertEqual(ParseInput.parse("58金引", shogi), False)

    def test_parse3(self):
        shogi = Shogi()
        shogi.move(2, 6, 2, 5, False)
        shogi.move(6, 2, 6, 3, False)
        self.assertEqual(ParseInput.parse("22角成", shogi), (1,7, 7,1, True))
        self.assertEqual(ParseInput.parse("22角不成", shogi),(1,7, 7,1, False))
        self.assertEqual(ParseInput.parse("22角", shogi), (1,7, 7,1, False))
        self.assertEqual(ParseInput.parse("11角成", shogi), False)
        shogi.move(1, 7, 7, 1, True)
        self.assertEqual(ParseInput.parse("22同銀", shogi), (6,0, 7,1, False))
        self.assertEqual(ParseInput.parse("22銀", shogi), (6,0, 7,1, False))
        self.assertEqual(ParseInput.parse("22銀成", shogi), False)
