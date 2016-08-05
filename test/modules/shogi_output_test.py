
import unittest
from app.modules.shogi_input import ShogiInput
from app.modules.shogi_output import ShogiOutput


class ShogiTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_shogi_output_format(self):
        # for syntax error and runtime error
        channel_id = "channel_id"
        shogi = ShogiInput.init(channel_id, [{"id": "user1", "name": "user1name"}, {"id": "user2", "name": "user2name"}])
        board = ShogiInput.get_shogi_board(channel_id)
        board_str = ShogiOutput.make_board_emoji(board)
        self.assertIsNotNone(board_str)

    def test_shogi_output_number_format(self):
        # for syntax error and runtime error
        channel_id = "channel_id"
        shogi = ShogiInput.init(channel_id, [{"id": "user1", "name": "user1name"}, {"id": "user2", "name": "user2name"}])
        board = ShogiInput.get_shogi_board(channel_id)
        board_str = ShogiOutput.make_board_emoji(board, is_number=True)
        self.assertIsNotNone(board_str)

    def test_shogi_output_reverse_format(self):
        # for syntax error and runtime error
        channel_id = "channel_id"
        shogi = ShogiInput.init(channel_id, [{"id": "user1", "name": "user1name"}, {"id": "user2", "name": "user2name"}])
        board = ShogiInput.get_shogi_board(channel_id)
        board_str = ShogiOutput.make_board_emoji_reverse(board)
        self.assertIsNotNone(board_str)
