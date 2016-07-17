
import re

from slackbot.bot import respond_to

from app.modules.shogi_input import ShogiInput
from app.modules.shogi_output import ShogiOutput
from app.slack_utils.user import User

@respond_to('hey', re.IGNORECASE)
def res_hey(message):
    message.reply("Hey")

@respond_to('start with <?@?([\d\w_-]+)>?')
def start_shogi(message, opponent_name):
    slacker = message._client.webapi
    user = User(slacker)

    channel_id = message.body["channel"]
    own_id = message.body["user"]
    opponent_id = user.username_to_id(opponent_name)
    if opponent_id is None:
        # In case of mention. In mention, slack transform username to userid like @username to <@UOIFJ83F>
        opponent_id = opponent_name

    if not user.user_in_channel(opponent_id, channel_id):
        message.reply("Error, sorry. Opponent is not found in this channel")
        return

    shogi = ShogiInput.init(channel_id=channel_id, user_ids=[
        own_id,
        opponent_id,
    ])

    if shogi is None:
        message.reply("Error, sorry")
    else:
        message.reply("Shogi started: " + shogi.id)

koma_names = [
    "歩",
    "歩兵",
    "と",
    "と金",
    "香",
    "香車",
    "桂",
    "桂馬",
    "銀",
    "銀将",
    "金",
    "金将",
    "角",
    "角行",
    "馬",
    "飛",
    "飛車",
    "龍",
    "王",
    "玉",
    "王将",
    "玉将",
]

koma_names += list(map(lambda n: "成"+n, koma_names))
koma_names_string_regex = "|".join(koma_names)

@respond_to("([一二三四五六七八九123456789１２３４５６７８９]{2})("+koma_names_string_regex+")([上右下左]{1,2})?(成)?")
def koma_move(message, position, koma, sub_position, promote):
    channel_id = message.body["channel"]
    if not ShogiInput.exists(channel_id):
        message.reply("start withから初めてね")
        return
    own_id = message.body["user"]
    if ShogiInput.koma_is_movable(channel_id, own_id, position, koma, sub_position, promote):
        ShogiInput.move(position, koma, sub_position, promote)
        board = ShogiInput.get_shogi_board(channel_id)
        board_str = ShogiOutput.make_board_emoji(board)
        message.send(board_str)
    else:
        message.reply("You cannot move this!!")

@respond_to("([123456789][123456789][123456789][123456789]成?)")
def koma_move_basic(message, movement):
    from_x = 9-int(movement[0])
    from_y = int(movement[1])-1
    to_x = 9-int(movement[2])
    to_y = int(movement[3])-1
    promote = len(movement) >= 5
    channel_id = message.body["channel"]
    if not ShogiInput.exists(channel_id):
        message.reply("start withから初めてね")
        return
    ShogiInput.basic_move(channel_id, from_x, from_y, to_x, to_y, promote)
    board = ShogiInput.get_shogi_board(channel_id)
    board_str = ShogiOutput.make_board_emoji(board)
    message.send(board_str)

