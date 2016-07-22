
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

koma2emoji_re = {
    Koma.empty: emoji_separetor + emoji_prefix + "mu" + emoji_separetor,
    Koma.fu: emoji_separetor + emoji_prefix + "fu_enemy" + emoji_separetor,
    Koma.kyosha: emoji_separetor + emoji_prefix + "kyou_enemy" + emoji_separetor,
    Koma.keima: emoji_separetor + emoji_prefix + "kei_enemy" + emoji_separetor,
    Koma.gin: emoji_separetor + emoji_prefix + "gin_enemy" + emoji_separetor,
    Koma.kin: emoji_separetor + emoji_prefix + "kin_enemy" + emoji_separetor,
    Koma.kaku: emoji_separetor + emoji_prefix + "kaku_enemy" + emoji_separetor,
    Koma.hisha: emoji_separetor + emoji_prefix + "hi_enemy" + emoji_separetor,
    Koma.gyoku: emoji_separetor + emoji_prefix + "gyoku_enemy" + emoji_separetor,
    Koma.promoted_fu: emoji_separetor + emoji_prefix + "tokin_enemy" + emoji_separetor,
    Koma.promoted_kyosha: emoji_separetor + emoji_prefix + "narikyou_enemy" + emoji_separetor,
    Koma.promoted_keima: emoji_separetor + emoji_prefix + "narikei_enemy" + emoji_separetor,
    Koma.promoted_gin: emoji_separetor + emoji_prefix + "narigin_enemy" + emoji_separetor,
    Koma.promoted_kaku: emoji_separetor + emoji_prefix + "uma_enemy" + emoji_separetor,
    Koma.promoted_hisha: emoji_separetor + emoji_prefix + "ryu_enemy" + emoji_separetor,

    Koma.opponent_fu: emoji_separetor + emoji_prefix + "fu" + emoji_separetor,
    Koma.opponent_kyosha: emoji_separetor + emoji_prefix + "kyou" + emoji_separetor,
    Koma.opponent_keima: emoji_separetor + emoji_prefix + "kei" + emoji_separetor,
    Koma.opponent_gin: emoji_separetor + emoji_prefix + "gin" + emoji_separetor,
    Koma.opponent_kin: emoji_separetor + emoji_prefix + "kin" + emoji_separetor,
    Koma.opponent_kaku: emoji_separetor + emoji_prefix + "kaku" + emoji_separetor,
    Koma.opponent_hisha: emoji_separetor + emoji_prefix + "hi" + emoji_separetor,
    Koma.opponent_gyoku: emoji_separetor + emoji_prefix + "ou" + emoji_separetor,
    Koma.opponent_promoted_fu: emoji_separetor + emoji_prefix + "tokin" + emoji_separetor,
    Koma.opponent_promoted_kyosha: emoji_separetor + emoji_prefix + "narikyou" + emoji_separetor,
    Koma.opponent_promoted_keima: emoji_separetor + emoji_prefix + "narikei" + emoji_separetor,
    Koma.opponent_promoted_gin: emoji_separetor + emoji_prefix + "narigin" + emoji_separetor,
    Koma.opponent_promoted_kaku: emoji_separetor + emoji_prefix + "uma" + emoji_separetor,
    Koma.opponent_promoted_hisha: emoji_separetor + emoji_prefix + "ryu" + emoji_separetor,
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


x_labels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y_labels = [9, 8, 7, 6, 5, 4, 3, 2, 1]


class ShogiOutput:

    @staticmethod
    def make_board_emoji(board_info, is_number=False):
        # second koma
        output_text = ""
        if not board_info["turn"]:
            output_text = "[手番]"

        output_text += "後手 {} ： ".format(board_info["info"]["second"]["name"])
        cnt = 0
        if board_info["second"]:
            for koma in sorted(board_info["second"]):
                cnt += 1
                # if a number of motigoma is more than 7,
                # go to next line.
                if cnt == 7:
                    output_text += "\n　　    "
                    cnt = 1
                output_text += koma2emoji[koma] + " "
        else:
            output_text += "持ち駒なし"

        output_text += "\n\n"

        # board
        if is_number:
            for y_label in y_labels:
                output_text += y_number2emoji[y_label]
            output_text += "\n"
        for y in range(9):
            for x in range(9):
                if x == board_info["_shogi"].shogi.last_move_x and \
                   y == board_info["_shogi"].shogi.last_move_y:
                    output_text += koma2emoji[
                        board_info["board"][y][x]
                    ].replace(emoji_prefix,
                              emoji_prefix + "last_"
                              )
                else:
                    output_text += koma2emoji[board_info["board"][y][x]]
            if is_number:
                output_text += x_number2emoji[x_labels[y]]
            output_text += "\n"
        output_text += "\n"

        # first koma
        if board_info["turn"]:
            output_text += "[手番]"

        output_text += "先手 {} ： ".format(board_info["info"]["first"]["name"])
        cnt = 0
        if board_info["first"]:
            for koma in sorted(board_info["first"]):
                cnt += 1
                # if a number of motigoma is more than 7,
                # go to next line.
                if cnt == 7:
                    output_text += "\n　　    "
                    cnt = 1
                output_text += koma2emoji[koma] + " "
        else:
            output_text += "持ち駒なし"

        output_text += "\n"

        return output_text

    @staticmethod
    def make_board_emoji_reverse(board_info):
        # first koma
        output_text = ""
        if board_info["turn"]:
            output_text = "[手番]"

        output_text += "先手 {} ： ".format(board_info["info"]["first"]["name"])
        cnt = 0
        if board_info["first"]:
            for koma in board_info["first"]:
                cnt += 1
                # if a number of motigoma is more than 7,
                # go to next line.
                if cnt == 7:
                    output_text += "\n　　    "
                    cnt = 1
                output_text += koma2emoji_re[koma] + " "
        else:
            output_text += "持ち駒なし"

        output_text += "\n\n"

        # board
        for y in reversed(range(9)):
            output_text += y_number2emoji[list(reversed(y_labels))[y]]
            for x in reversed(range(9)):
                if x == board_info["_shogi"].shogi.last_move_x and \
                   y == board_info["_shogi"].shogi.last_move_y:
                    output_text += koma2emoji_re[board_info["board"][y][x]].                    replace(emoji_prefix, emoji_prefix + "last_")
                else:
                    output_text += koma2emoji_re[board_info["board"][y][x]]
            output_text += "\n"
        output_text += ":slackshogisss_blank:"
        for x_label in x_labels:
            output_text += x_number2emoji[x_label]
        output_text += "\n"

        # socond koma
        if not board_info["turn"]:
            output_text += "[手番]"

        output_text += "後手 {} ： ".format(board_info["info"]["second"]["name"])
        cnt = 0
        if board_info["second"]:
            for koma in board_info["second"]:
                cnt += 1
                # if a number of motigoma is more than 7,
                # go to next line.
                if cnt == 7:
                    output_text += "\n　　    "
                    cnt = 1
                output_text += koma2emoji_re[koma] + " "
        else:
            output_text += "持ち駒なし"

        output_text += "\n"

        return output_text
