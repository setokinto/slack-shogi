import unittest
from app.modules.shogi import Koma
from app.modules.shogi_input import Shogi
from app.modules.parse_input import ParseInput

def create_shogi():
  return Shogi("channel_id", [
    {"id": "user1", "name": "name1"},
    {"id": "user2", "name": "name2"},
  ])

class ShogiTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_parse1(self):
        shogi = create_shogi()
        self.assertEqual(ParseInput.parse("７６歩", shogi),
                         (2, 6, 2, 5, False, Koma.fu))
        self.assertEqual(ParseInput.parse("7六歩", shogi),
                         (2, 6, 2, 5, False, Koma.fu))
        self.assertEqual(ParseInput.parse("７5歩", shogi), False)
        self.assertEqual(ParseInput.parse("34歩", shogi), False)

        shogi.move(2, 6, 2, 5, False)
        self.assertEqual(ParseInput.parse("34歩", shogi),
                         (6, 2, 6, 3, False, Koma.opponent_fu))
        self.assertEqual(ParseInput.parse("35歩", shogi), False)
        self.assertEqual(ParseInput.parse("75歩", shogi), False)

    def test_parse2(self):
        shogi = create_shogi()
        self.assertEqual(ParseInput.parse("58金右", shogi),
                         (5, 8, 4, 7, False, Koma.kin))
        self.assertEqual(ParseInput.parse("58金左", shogi),
                         (3, 8, 4, 7, False, Koma.kin))
        self.assertEqual(ParseInput.parse("58金直", shogi), False)
        self.assertEqual(ParseInput.parse("58金寄", shogi), False)
        self.assertEqual(ParseInput.parse("58金引", shogi), False)
        shogi.move(4, 8, 5, 7, False)
        shogi.move(5, 8, 4, 8, False)
        shogi.first = True
        self.assertIn([3, 8], shogi.find_koma(Koma.kin))
        self.assertIn([4, 8], shogi.find_koma(Koma.kin))
        self.assertEqual(ParseInput.parse("58金直", shogi),
                         (4, 8, 4, 7, False, Koma.kin))
        self.assertEqual(ParseInput.parse("58金左", shogi),
                         (3, 8, 4, 7, False, Koma.kin))
        self.assertEqual(ParseInput.parse("58金右", shogi), False)
        self.assertEqual(ParseInput.parse("58金寄", shogi), False)
        self.assertEqual(ParseInput.parse("58金引", shogi), False)

    def test_parse3(self):
        shogi = create_shogi()
        shogi.move(2, 6, 2, 5, False)  # 76歩
        shogi.move(6, 2, 6, 3, False)  # 34歩
        self.assertEqual(ParseInput.parse("22角成", shogi),
                         (1, 7, 7, 1, True, Koma.kaku))
        self.assertEqual(ParseInput.parse("22角不成", shogi),
                         (1, 7, 7, 1, False, Koma.kaku))
        self.assertEqual(ParseInput.parse("22角", shogi),
                         (1, 7, 7, 1, False, Koma.kaku))
        self.assertEqual(ParseInput.parse("11角成", shogi), False)

        shogi.move(1, 7, 7, 1, True)
        self.assertEqual(ParseInput.parse("22同銀", shogi),
                         (6, 0, 7, 1, False, Koma.opponent_gin))
        self.assertEqual(ParseInput.parse("22銀", shogi),
                         (6, 0, 7, 1, False, Koma.opponent_gin))
        self.assertEqual(ParseInput.parse("22銀成", shogi), False)

    def test_parse_drop(self):
        shogi = create_shogi()
        shogi.board[6][0] = Koma.empty
        shogi.first_tegoma = [Koma.fu]
        shogi.first = True
        self.assertEqual(ParseInput.parse("95歩打", shogi),
                         (-1, -1, 0, 4, False, Koma.fu))
        self.assertEqual(ParseInput.parse("95歩打成", shogi), False)

    def test_parse_same(self):
        shogi = create_shogi()
        shogi.move(2, 6, 2, 5, False)  # 76歩
        shogi.move(2, 2, 2, 3, False)  # 74歩
        shogi.move(2, 5, 2, 4, False)  # 75歩
        self.assertEqual(ParseInput.parse("同歩", shogi),
                         (2, 3, 2, 4, False, Koma.opponent_fu))

        shogi = create_shogi()
        shogi.move(5, 8, 4, 1, False)  # 49の金を一気に52へ
        self.assertEqual(ParseInput.parse("同金右", shogi),
                         (3, 0, 4, 1, False, Koma.opponent_kin))

    @unittest.skip("see https://github.com/setokinto/slack-shogi/issues/19")
    def test_parse_ambiguous(self):
        shogi = create_shogi()
        self.assertEqual(ParseInput.parse("58金", shogi), False)

