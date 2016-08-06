
import unittest
from app.modules.shogi_input import ShogiInput, UserDifferentException, KomaCannotMoveException
from app.modules.shogi import Koma


class ShogiTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_shogi_input_is_initable(self):
        shogi = ShogiInput.init("channel_id", [{
            "id": "user1",
            "name": "user1name",
        }, {
            "id": "user2",
            "name": "user2name",
        }
        ])
        self.assertEqual(shogi.channel_id, "channel_id")

        shogi = ShogiInput.init("channel_id", [{
            "id": "user1",
            "name": "user1name",
        }, {
            "id": "user2",
            "name": "user2name",
        }
        ])
        self.assertIsNone(shogi)

        ShogiInput.clear("channel_id")
        shogi = ShogiInput.init("channel_id", [{
            "id": "user1",
            "name": "user1name",
        }, {
            "id": "user2",
            "name": "user2name",
        }
        ])
        self.assertEqual(shogi.channel_id, "channel_id")

    def test_clear_for_non_exists_channnel(self):
        self.assertIsNone(ShogiInput.clear("channel_id_non_exists"))

    def test_move_method_should_work(self):
        channel_id = "test_move_method_should_work"
        shogi = ShogiInput.init(channel_id, [{
            "id": "user1",
            "name": "user1name",
        }, {
            "id": "user2",
            "name": "user2name",
        }])

        ShogiInput.move("76歩", channel_id, shogi.first_user_id)
        self.assertEqual(shogi.board[5][2], Koma.fu)

    def test_move_method_should_raise_UserDifferentException(self):
        channel_id = "test_move_method_should_raise_UserDifferentException"
        shogi = ShogiInput.init(channel_id, [{
            "id": "user1",
            "name": "user1name",
        }, {
            "id": "user2",
            "name": "user2name",
        }])

        with self.assertRaises(UserDifferentException):
            ShogiInput.move("76歩", channel_id, shogi.second_user_id)
        with self.assertRaises(UserDifferentException):
            ShogiInput.move("76歩", channel_id, "shogi.second_user_id")

    def test_move_method_should_raise_KomaCannotMoveException(self):
        channel_id = "test_move_method_should_raise_KomaCannotMoveException"
        shogi = ShogiInput.init(channel_id, [{
            "id": "user1",
            "name": "user1name",
        }, {
            "id": "user2",
            "name": "user2name",
        }])

        with self.assertRaises(KomaCannotMoveException):
            ShogiInput.move("75歩", channel_id, shogi.first_user_id)
        with self.assertRaises(KomaCannotMoveException):
            ShogiInput.move("34歩", channel_id, shogi.first_user_id)
        with self.assertRaises(KomaCannotMoveException):
            ShogiInput.move("15151歩", channel_id, shogi.first_user_id)
        with self.assertRaises(KomaCannotMoveException):
            ShogiInput.move("Wow, it's great.", channel_id, shogi.first_user_id)

    def test_set_any_user_validator(self):
        channel_id = "test_set_validotr"
        shogi = ShogiInput.init(channel_id, [{
            "id": "user1",
            "name": "user1name",
        }, {
            "id": "user2",
            "name": "user2name",
        }])
        ShogiInput.move("76歩", channel_id, shogi.first_user_id)
        with self.assertRaises(UserDifferentException):
            ShogiInput.move("34歩", channel_id, shogi.first_user_id)
        ShogiInput.setAllMode(channel_id)
        ShogiInput.move("34歩", channel_id, shogi.first_user_id)

    def test_matta(self):
        channel_id = "test_matta"
        shogi = ShogiInput.init(channel_id, [{
            "id": "user1",
            "name": "user1name",
        }, {
            "id": "user2",
            "name": "user2name",
        }])
        ShogiInput.move("76歩", channel_id, shogi.first_user_id)
        self.assertEqual(shogi.board[5][2], Koma.fu)
        ShogiInput.matta(channel_id, shogi.second_user_id)
        self.assertEqual(shogi.board[5][2], Koma.empty)
        ShogiInput.move("76歩", channel_id, shogi.first_user_id)
        self.assertEqual(shogi.board[5][2], Koma.fu)

