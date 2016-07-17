
from enum import Enum

class Koma(Enum):
    empty = 0
    fu = 0x01
    kyosha = 0x02
    keima = 0x03
    gin = 0x04
    kin = 0x05
    kaku = 0x06
    hisha = 0x07
    gyoku = 0x08
    promoted_fu = 0x11
    promoted_kyosha = 0x12
    promoted_keima = 0x13
    promoted_gin = 0x14
    promoted_kaku = 0x16
    promoted_hisha = 0x17

    opponent_fu = 0x21
    opponent_kyosha = 0x22
    opponent_keima = 0x23
    opponent_gin = 0x24
    opponent_kin = 0x25
    opponent_kaku = 0x26
    opponent_hisha = 0x27
    opponent_gyoku = 0x28
    opponent_promoted_fu = 0x31
    opponent_promoted_kyosha = 0x32
    opponent_promoted_keima = 0x33
    opponent_promoted_gin = 0x34
    opponent_promoted_kaku = 0x36
    opponent_promoted_hisha = 0x37

# TODO : Change emoji string
koma2emoji = {
    Koma.empty: ":white_large_square:",
    Koma.fu: ":arrow_up_small:",
    Koma.kyosha: ":arrow_double_up:",
    Koma.keima: ":arrow_heading_up:",
    Koma.gin: ":arrow_upper_right:",
    Koma.kin: ":arrow_up:",
    Koma.kaku: ":heavy_multiplication_x:",
    Koma.hisha: ":heavy_plus_sign:",
    Koma.gyoku: ":mahjong:",
    Koma.promoted_fu: ":sunglasses:",
    Koma.promoted_kyosha: ":grimacing:",
    Koma.promoted_keima: ":joy:",
    Koma.promoted_gin: ":money_mouth_face:",
    Koma.promoted_kaku: ":rage3:",
    Koma.promoted_hisha: ":innocent:",

    Koma.opponent_fu: ":arrow_down_small:",
    Koma.opponent_kyosha: ":arrow_double_down:",
    Koma.opponent_keima: ":arrow_heading_down:",
    Koma.opponent_gin: ":arrow_lower_right:",
    Koma.opponent_kin: ":arrow_down:",
    Koma.opponent_kaku: ":x:",
    Koma.opponent_hisha: ":latin_cross:",
    Koma.opponent_gyoku: ":mahjong:",
    Koma.opponent_promoted_fu: ":ok_woman:",
    Koma.opponent_promoted_kyosha: ":ok_woman::skin-tone-2:",
    Koma.opponent_promoted_keima: ":ok_woman::skin-tone-3:",
    Koma.opponent_promoted_gin: ":ok_woman::skin-tone-4:",
    Koma.opponent_promoted_kaku: ":ok_woman::skin-tone-5:",
    Koma.opponent_promoted_hisha: ":ok_woman::skin-tone-6:"
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
        for x in range(9):
            for y in range(9):
                output_text += koma2emoji[board["board"][x][y]]
            output_text += "\n"
        output_text += "\n"

        # socond koma
        # TODO : Insert player name.
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
