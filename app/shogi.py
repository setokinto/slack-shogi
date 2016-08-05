
import re
import functools

from slackbot.bot import respond_to

from app.modules.shogi_input import ShogiInput
from app.modules.shogi_output import ShogiOutput
from app.slack_utils.user import User
from app.helper import channel_info, should_exist_shogi


@respond_to('start with <?@?([\d\w_-]+)>?')
@channel_info
def start_shogi(channel, message, opponent_name):
    slacker = message._client.webapi
    user = User(slacker)

    opponent_id = user.username_to_id(opponent_name)
    if opponent_id is None:
        # In case of mention. In mention, slack transform username to userid
        # like @username to <@UOIFJ83F>
        opponent_id = opponent_name

    if not user.user_in_channel(opponent_id, channel.channel_id):
        message.reply("Error, sorry. Opponent is not found in this channel")
        return

    shogi = ShogiInput.init(channel_id=channel.channel_id, users=[{
        "id": channel.own_id,
        "name": user.id_to_username(channel.own_id),
    }, {
        "id": opponent_id,
        "name": user.id_to_username(opponent_id),
    }])

    if shogi is None:
        message.reply("Shogi started already by a user. Sorry.\nIf you want to quit shogi which already exists, please say this command `resign`")
    else:
        message.reply("Shogi started: " + shogi.id)
        board = ShogiInput.get_shogi_board(channel.channel_id)
        board_str = ShogiOutput.make_board_emoji(board)
        message.send(board_str)

koma_names = [
    "歩兵?",
    "と金?",
    "成?香車?",
    "成?桂馬?",
    "成?銀将?",
    "金将?",
    "角行?",
    "馬",
    "飛車?",
    "龍",
    "王将?",
    "玉将?",
]

koma_names_string_regex = "|".join(koma_names)

@respond_to("([一二三四五六七八九123456789１２３４５６７８９]{2})?(同)?(" + koma_names_string_regex + ")([上右下左寄直打]{1,2})?つ?(成)?")
@channel_info
@should_exist_shogi
def koma_move(channel, message, position, dou, koma, sub_position=None, promote=None):
    movement_str = "".join(
        [x for x in [position, dou, koma, sub_position, promote] if x is not None])

    if ShogiInput.move(movement_str, channel.channel_id, channel.own_id):
        board = ShogiInput.get_shogi_board(channel.channel_id)
        board_str = ShogiOutput.make_board_emoji(board)
        message.send(board_str)
    else:
        message.reply("You cannot move this!!")
        board = ShogiInput.get_shogi_board(channel.channel_id)
        board_str = ShogiOutput.make_board_emoji(board)
        message.send(board_str)


@respond_to("今?.*の?.*状態.*を?教.*え?て?")
@respond_to("現局面.*")
@respond_to("局面.*")
@respond_to("board")
@channel_info
@should_exist_shogi
def board_info(channel, message):
    board = ShogiInput.get_shogi_board(channel.channel_id)
    board_str = ShogiOutput.make_board_emoji(board)
    message.send(board_str)


@respond_to(".*降参.*")
@respond_to(".*resign.*")
@respond_to(".*負けました.*")
@respond_to(".*まけました.*")
@respond_to(".*まいりました.*")
@respond_to(".*参りました.*")
@respond_to(".*ありません.*")
@channel_info
@should_exist_shogi
def resign(channel, message):
    message.send("最終局面")
    board = ShogiInput.get_shogi_board(channel.channel_id)
    board_str = ShogiOutput.make_board_emoji(board)
    message.send(board_str)
    ShogiInput.clear(channel.channel_id)

