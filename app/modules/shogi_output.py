
from enum import Enum


class Koma(Enum):
    # TODO: Merge Shogi module
    empty = 0
    fu = 0x01
    kyosha = 0x02
    keima = 0x03
    gin = 0x04
    kin = 0x05
    kaku = 0x06
    hisha = 0x07
    gyoku = 0x08
    promoted_fu = 0x10 + Koma.fu.value
    promoted_kyosha = 0x10 + Koma.kyosha.value
    promoted_keima = 0x10 + Koma.keima.value
    promoted_gin = 0x10 + Koma.gin.value
    promoted_kaku = 0x10 + Koma.kaku.value
    promoted_hisha = 0x10 + Koma.hisha.value

    opponent_fu = 0x20 + Koma.fu.value
    opponent_kyosha = 0x20 + Koma.kyosha.value
    opponent_keima = 0x20 + Koma.fu.value
    opponent_gin = 0x20 + Koma.keima.value
    opponent_kin = 0x20 + Koma.gin.value
    opponent_kaku = 0x20 + Koma.kaku.value
    opponent_hisha = 0x20 + Koma.hisha.value
    opponent_gyoku = 0x20 + Koma.gyoku.value
    opponent_promoted_fu = 0x30 + Koma.fu.value
    opponent_promoted_kyosha = 0x30 + Koma.kyosha.value
    opponent_promoted_keima = 0x30 + Koma.keima.value
    opponent_promoted_gin = 0x30 + Koma.gin.value
    opponent_promoted_kaku = 0x30 + Koma.kaku.value
    opponent_promoted_hisha = 0x30 + Koma.hisha.value


# TODO : Change emoji string
koma2emoji = {
    Koma.empty: ":white_large_square:",
    Koma.fu: "::arrow_up_small:",
    Koma.kyosha: ":arrow_double_up:",
    Koma.keima: ":arrow_heading_up:",
    Koma.gin: ":arrow_upper_right:",
    Koma.kin: ":arrow_up: ",
    Koma.kaku: ":heavy_multiplication_x:",
    Koma.hisha: ":heavy_plus_sign:",
    Koma.gyoku: ":mahjong:",
    Koma.promoted_fu: ":sunglasses:",
    Koma.promoted_kyosha: ":grimacing:",
    Koma.promoted_keima: ":joy: ",
    Koma.promoted_gin: ":money_mouth_face:",
    Koma.promoted_kaku: ":rage3: ",
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
    def make_board_emoji(board):
        # TODO: Make board with emoji
        output_text = ""
        for x in range(9):
            for y in range(9):
                output_text += koma2emoji[board["board"][x][y]]
            output_text += "\n"

        return output_text
