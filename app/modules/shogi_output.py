
from app.modules.shogi import Koma

emoji_prefix = "slackshogisss_"
emoji_separetor = ":"

koma2emoji = {
    Koma.empty: emoji_separetor + emoji_prefix + "mu" + emoji_separetor,
    Koma.fu: emoji_separetor + emoji_prefix + "fu" + emoji_separetor,
    Koma.kyosha: emoji_separetor + emoji_prefix + "kyou" + emoji_separetor,
    Koma.keima: emoji_separetor + emoji_prefix + "kei" + emoji_separetor,
    Koma.gin: emoji_separetor + emoji_prefix + "gin" + emoji_separetor,
    Koma.kin: emoji_separetor + emoji_prefix + "kin" + emoji_separetor,
    Koma.kaku: emoji_separetor + emoji_prefix + "kaku" + emoji_separetor,
    Koma.hisha: emoji_separetor + emoji_prefix + "hi" + emoji_separetor,
    Koma.gyoku: emoji_separetor + emoji_prefix + "gyoku" + emoji_separetor,
    Koma.promoted_fu: emoji_separetor + emoji_prefix + "tokin" + emoji_separetor,
    Koma.promoted_kyosha: emoji_separetor + emoji_prefix + "narikyou" + emoji_separetor,
    Koma.promoted_keima: emoji_separetor + emoji_prefix + "narikei" + emoji_separetor,
    Koma.promoted_gin: emoji_separetor + emoji_prefix + "narigin" + emoji_separetor,
    Koma.promoted_kaku: emoji_separetor + emoji_prefix + "uma" + emoji_separetor,
    Koma.promoted_hisha: emoji_separetor + emoji_prefix + "ryu" + emoji_separetor,

    Koma.opponent_fu: emoji_separetor + emoji_prefix + "fu_enemy" + emoji_separetor,
    Koma.opponent_kyosha: emoji_separetor + emoji_prefix + "kyou_enemy" + emoji_separetor,
    Koma.opponent_keima: emoji_separetor + emoji_prefix + "kei_enemy" + emoji_separetor,
    Koma.opponent_gin: emoji_separetor + emoji_prefix + "gin_enemy" + emoji_separetor,
    Koma.opponent_kin: emoji_separetor + emoji_prefix + "kin_enemy" + emoji_separetor,
    Koma.opponent_kaku: emoji_separetor + emoji_prefix + "kaku_enemy" + emoji_separetor,
    Koma.opponent_hisha: emoji_separetor + emoji_prefix + "hi_enemy" + emoji_separetor,
    Koma.opponent_gyoku: emoji_separetor + emoji_prefix + "ou_enemy" + emoji_separetor,
    Koma.opponent_promoted_fu: emoji_separetor + emoji_prefix + "tokin_enemy" + emoji_separetor,
    Koma.opponent_promoted_kyosha: emoji_separetor + emoji_prefix + "narikyou_enemy" + emoji_separetor,
    Koma.opponent_promoted_keima: emoji_separetor + emoji_prefix + "narikei_enemy" + emoji_separetor,
    Koma.opponent_promoted_gin: emoji_separetor + emoji_prefix + "narigin_enemy" + emoji_separetor,
    Koma.opponent_promoted_kaku: emoji_separetor + emoji_prefix + "uma_enemy" + emoji_separetor,
    Koma.opponent_promoted_hisha: emoji_separetor + emoji_prefix + "ryu_enemy" + emoji_separetor,
}

x_number2emoji = {
    1: emoji_separetor + emoji_prefix + "one" + emoji_separetor,
    2: emoji_separetor + emoji_prefix + "two" + emoji_separetor,
    3: emoji_separetor + emoji_prefix + "three" + emoji_separetor,
    4: emoji_separetor + emoji_prefix + "four" + emoji_separetor,
    5: emoji_separetor + emoji_prefix + "five" + emoji_separetor,
    6: emoji_separetor + emoji_prefix + "six" + emoji_separetor,
    7: emoji_separetor + emoji_prefix + "seven" + emoji_separetor,
    8: emoji_separetor + emoji_prefix + "eight" + emoji_separetor,
    9: emoji_separetor + emoji_prefix + "nine" + emoji_separetor,
}

y_number2emoji = {
    1: emoji_separetor + emoji_prefix + "iti" + emoji_separetor,
    2: emoji_separetor + emoji_prefix + "ni" + emoji_separetor,
    3: emoji_separetor + emoji_prefix + "san" + emoji_separetor,
    4: emoji_separetor + emoji_prefix + "yon" + emoji_separetor,
    5: emoji_separetor + emoji_prefix + "go" + emoji_separetor,
    6: emoji_separetor + emoji_prefix + "roku" + emoji_separetor,
    7: emoji_separetor + emoji_prefix + "nana" + emoji_separetor,
    8: emoji_separetor + emoji_prefix + "hati" + emoji_separetor,
    9: emoji_separetor + emoji_prefix + "kyu" + emoji_separetor,
}


def make_user_text(user_name, motigoma,
                   is_first=True, is_turn=True, reverse=False):
    return_text = ""
    if is_turn:
        return_text = "[手番]"

    if is_first:
        return_text += " 先手 {}  ".format(user_name)
    else:
        return_text += " 後手 {}  ".format(user_name)
    user_info_char_num = len(return_text)  # for new line

    if motigoma:
        cnt = 0
        for cur_koma in motigoma:
            cnt += 1
            if cnt == 5:
                return_text += "\n" + (" " * user_info_char_num)
                cnt = 1
            return_text += koma2emoji[cur_koma] + " "
    else:
        return_text += "持ち駒なし"

    return_text += "\n\n"
    return return_text


def make_board_info_text(board_info, reverse=False):
    return_text = ""
    x_labels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y_labels = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    loop_iter = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    if reverse:
        loop_iter.reverse()

    if not reverse:
        for y_label in y_labels:
            return_text += y_number2emoji[y_label]
        return_text += "\n"
    for y in loop_iter:
        if reverse:
            return_text += y_number2emoji[list(reversed(y_labels))[y]]
        for x in loop_iter:
            cur_koma = board_info["board"][y][x]
            if reverse and cur_koma != Koma.empty:
                cur_koma = cur_koma.go_enemy()

            if x == board_info["_shogi"].last_move_x and \
               y == board_info["_shogi"].last_move_y:
                return_text += koma2emoji[cur_koma].replace(
                    emoji_prefix,
                    emoji_prefix + "last_")
            else:
                return_text += koma2emoji[cur_koma]
        if not reverse:
            return_text += x_number2emoji[x_labels[y]]
        return_text += "\n"

    if reverse:
        return_text += "{}{}blank{}".format(emoji_separetor,
                                            emoji_prefix,
                                            emoji_separetor)
        for x_label in x_labels:
            return_text += x_number2emoji[x_label]
    return_text += "\n"

    return return_text


class ShogiOutput:
    @staticmethod
    def make_board_emoji(board_info):
        out_text = ""

        out_text += make_user_text(board_info["info"]["second"]["name"],
                                   board_info["second"],
                                   is_first=False,
                                   is_turn=not board_info["turn"])

        # board
        out_text += make_board_info_text(board_info,
                                         reverse=False)

        # first koma
        out_text += make_user_text(board_info["info"]["first"]["name"],
                                   board_info["first"],
                                   is_first=True,
                                   is_turn=board_info["turn"])

        return out_text

    @staticmethod
    def make_board_emoji_reverse(board_info):
        out_text = ""

        # first koma
        out_text += make_user_text(board_info["info"]["first"]["name"],
                                   board_info["first"],
                                   is_first=True,
                                   is_turn=board_info["turn"])

        # board
        out_text += make_board_info_text(board_info,
                                         reverse=True)

        # socond koma
        out_text += make_user_text(board_info["info"]["second"]["name"],
                                   board_info["second"],
                                   is_first=False,
                                   is_turn=not board_info["turn"])

        return out_text
