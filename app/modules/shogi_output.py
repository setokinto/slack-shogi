
from app.modules.shogi import Koma

emoji_prefix = "slackshogisss_"
emoji_separetor = ":"

koma2emoji = {
    Koma.empty: emoji_separetor + emoji_prefix + "mu" + emoji_separetor,
    Koma.fu: emoji_separetor + emoji_prefix + "fu" + emoji_separetor,
    Koma.kyosha: emoji_separetor + emoji_prefix + "kyou" + emoji_separetor ,
    Koma.keima: emoji_separetor + emoji_prefix + "kei" + emoji_separetor,
    Koma.gin: emoji_separetor + emoji_prefix + "gin" + emoji_separetor,
    Koma.kin: emoji_separetor + emoji_prefix + "kin" + emoji_separetor,
    Koma.kaku: emoji_separetor + emoji_prefix + "kaku" + emoji_separetor,
    Koma.hisha: emoji_separetor + emoji_prefix + "hi" + emoji_separetor,
    Koma.gyoku: emoji_separetor + emoji_prefix + "ou" + emoji_separetor,
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
    Koma.opponent_gyoku: emoji_separetor + emoji_prefix + "gyoku" + emoji_separetor,
    Koma.opponent_promoted_fu: emoji_separetor + emoji_prefix + "tokin_enemy" + emoji_separetor,
    Koma.opponent_promoted_kyosha: emoji_separetor + emoji_prefix + "narikyou_enemy" + emoji_separetor,
    Koma.opponent_promoted_keima: emoji_separetor + emoji_prefix + "narikei_enemy" + emoji_separetor,
    Koma.opponent_promoted_gin: emoji_separetor + emoji_prefix + "narigin_enemy" + emoji_separetor,
    Koma.opponent_promoted_kaku: emoji_separetor + emoji_prefix + "uma_enemy" + emoji_separetor,
    Koma.opponent_promoted_hisha: emoji_separetor + emoji_prefix + "ryu_enemy" + emoji_separetor,
}

class ShogiOutput:
    @staticmethod
    def make_board_emoji(board_info):
        output_text = "後手 {} ： ".format(board_info["info"]["second"]["name"])
        cnt = 0
        if board_info["second"]:
            for koma in board_info["second"]:
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
        for y in range(9):
            for x in range(9):
                output_text += koma2emoji[board["board"][y][x]]
            output_text += "\n"
        output_text += "\n"

        # socond koma
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
                output_text += koma2emoji[koma] + " "
        else:
            output_text += "持ち駒なし"

        output_text += "\n"

        return output_text
