
import re
from app.modules.shogi import Koma

str2info = {
    "一": 0, "１": 0, "1": 0,
    "二": 1, "２": 1, "2": 1,
    "三": 2, "３": 2, "3": 2,
    "四": 3, "４": 3, "4": 3,
    "五": 4, "５": 4, "5": 4,
    "六": 5, "６": 5, "6": 5,
    "七": 6, "７": 6, "7": 6,
    "八": 7, "８": 7, "8": 7,
    "九": 8, "９": 8, "9": 8
}

str2koma = {
    "歩" : Koma.fu, "と" : Koma.promoted_fu,
    "成歩" : Koma.promoted_fu, "成と" : Koma.promoted_fu,

    "香" : Koma.kyosha, "香車" : Koma.kyosha,
    "成香" : Koma.promoted_kyosha, "成香車" : Koma.promoted_kyosha,

    "桂" : Koma.keima, "桂馬" : Koma.keima,
    "成桂" : Koma.promoted_keima, "成桂馬" : Koma.promoted_keima,

    "銀" : Koma.gin, "銀将" : Koma.gin,
    "成銀" : Koma.promoted_gin, "成銀将" : Koma.promoted_gin,

    "金" : Koma.kin, "金将" : Koma.kin,
    "成金" : Koma.kin, "成金将" : Koma.kin,

    "角" : Koma.kaku, "角行" : Koma.kaku, "馬" : Koma.promoted_kaku,
    "成角" : Koma.promoted_kaku, "成角行" : Koma.promoted_kaku,
    "成馬" : Koma.promoted_kaku,

    "飛" : Koma.hisha, "飛車" : Koma.hisha, "龍" : Koma.promoted_hisha,
    "成飛" : Koma.promoted_hisha, "成飛車" : Koma.promoted_hisha,
    "成龍" : Koma.promoted_hisha,

    "王" : Koma.gyoku, "玉" : Koma.gyoku,
    "王将" : Koma.gyoku, "玉将" : Koma.gyoku,
    "成王" : Koma.gyoku, "成玉" : Koma.gyoku,
    "成王将" : Koma.gyoku, "成玉将" : Koma.gyoku
}

str2oppkoma = {
    "歩" : Koma.opponent_fu, "と" : Koma.opponent_promoted_fu,
    "成歩" : Koma.opponent_promoted_fu, "成と" : Koma.opponent_promoted_fu,

    "香" : Koma.opponent_kyosha, "香車" : Koma.opponent_kyosha,
    "成香" : Koma.opponent_promoted_kyosha,
    "成香車" : Koma.opponent_promoted_kyosha,

    "桂" : Koma.opponent_keima, "桂馬" : Koma.opponent_keima,
    "成桂" : Koma.opponent_promoted_keima,
    "成桂馬" : Koma.opponent_promoted_keima,

    "銀" : Koma.opponent_gin, "銀将" : Koma.opponent_gin,
    "成銀" : Koma.opponent_promoted_gin,
    "成銀将" : Koma.opponent_promoted_gin,

    "金" : Koma.opponent_kin, "金将" : Koma.opponent_kin,
    "成金" : Koma.opponent_kin, "成金将" : Koma.opponent_kin,

    "角" : Koma.opponent_kaku, "角行" : Koma.opponent_kaku,
    "馬" : Koma.opponent_promoted_kaku,
    "成角" : Koma.opponent_promoted_kaku,
    "成角行" : Koma.opponent_promoted_kaku,
    "成馬" : Koma.opponent_promoted_kaku,

    "飛" : Koma.opponent_hisha, "飛車" : Koma.opponent_hisha,
    "龍" : Koma.opponent_promoted_hisha,
    "成飛" : Koma.opponent_promoted_hisha,
    "成飛車" : Koma.opponent_promoted_hisha,
    "成龍" : Koma.opponent_promoted_hisha,

    "王" : Koma.opponent_gyoku, "玉" : Koma.opponent_gyoku,
    "王将" : Koma.opponent_gyoku, "玉将" : Koma.opponent_gyoku,
    "成王" : Koma.opponent_gyoku, "成玉" : Koma.opponent_gyoku,
    "成王将" : Koma.opponent_gyoku, "成玉将" : Koma.opponent_gyoku
}

koma_names = [
    "歩", "と",
    "香", "香車",
    "桂", "桂馬",
    "銀", "銀将",
    "金", "金将",
    "角", "角行", "馬",
    "飛", "飛車", "龍",
    "王", "玉", "王将", "玉将"
]

koma_names += list(map(lambda n: "成"+n, koma_names))

def transposition_num(num):
    """
    transposition axis(y) number.
    0 => 8, 1 => 7, ..., 8 => 0
    """
    return (4 - num) + 4

class ParseInput:
    @staticmethod
    def parse(input_str, shogi):
        """
        parse input text and get (from, to) Coordinate.
        """

        # TODO : "同"という表現への対応
        if input_str[0] in str2info and input_str[0] in str2info:
            to_x = transposition_num(str2info[input_str[0]])
            to_y = str2info[input_str[1]]
        else:
            # TODO : Send Error Message
            return False

        slice_idx = 2
        if input_str[slice_idx] == "同":
            slice_idx = 3
        input_str = input_str[slice_idx:]


        from_flag = 0
        if input_str.find("上") != -1:
            from_flag = 1
            input_str = input_str.replace("上", "")

        if input_str.find("右") != -1:
            from_flag += 2
            input_str = input_str.replace("右", "")

        # 3 => 右上

        if input_str.find("引") != -1:
            from_flag += 4
            input_str = input_str.replace("引", "")

        # 5 => None
        # 6 => 右引
        # 7 => None

        if input_str.find("左") != -1:
            from_flag += 8
            input_str = input_str.replace("左", "")

        # 9 => 左上
        # 10,11 => None
        # 12 => 左引
        # 13~15 => None

        if input_str.find("寄") != -1:
            from_flag = 16
            input_str = input_str.replace("寄", "")

        if input_str.find("直") != -1:
            from_flag = 17
            input_str = input_str.replace("直", "")


        promote = False
        if input_str[-1] == ("成"):
            if input_str[-2] == ("不"):
                input_str = input_str.replace("不成", "")
            else:
                # TODO : Detect to be able to promote
                promote = True
                input_str = input_str.replace("成", "")

        if input_str.find("打") != -1:
            from_x = -1
            from_y = -1

        else:
            is_first_turn = shogi.first

            # if in this block, input_str is only koma name
            if input_str in koma_names:
                if is_first_turn:
                    koma = str2koma[input_str]
                else:
                    koma = str2oppkoma[input_str]

                candidate_komas = shogi.find_koma(koma)
                movable_komas = []
                for candidate_koma in candidate_komas:
                    if shogi.movable(candidate_koma[0],
                                     candidate_koma[1],
                                     to_x, to_y, promote):
                        movable_komas.append(candidate_koma)

                if len(movable_komas) == 0:
                    return False

                elif len(movable_komas) == 1:
                    from_x = movable_komas[0][0]
                    from_y = movable_komas[0][1]

                else:
                    turn = is_first_turn  # for pep
                    # "上"
                    if from_flag == 1:
                        for t in movable_komas: # t => "t"arget
                            if (turn and t[1] > to_y) or \
                               (not turn and t[1] < to_y):
                                from_x, from_y = t
                                from_flag = 0
                                break


                    # "右"
                    elif from_flag == 2:
                        for t in movable_komas:
                            if (turn and t[0] > to_x) or \
                               (not turn and t[0] < to_x):
                                from_x, from_y = t
                                from_flag = 0
                                break

                    # "右上"
                    elif from_flag == 3:
                        for t in movable_komas:
                            if (turn and t[0] > to_x and t[1] > to_y) or \
                               (not turn and t[0] < to_x and t[1] < to_y):
                                from_x, from_y = t
                                from_flag = 0
                                break

                    # "引"
                    elif from_flag == 4:
                        for t in movable_komas:
                            if (turn and t[1] < to_y) or \
                               (not turn and t[1] > to_y):
                                from_x, from_y = t
                                from_flag = 0
                                break

                    # "右引"
                    elif from_flag == 6:
                        for t in movable_komas:
                            if (turn and t[0] > to_x and t[1] < to_y) or \
                               (not turn and t[0] < to_x and t[1] > to_y):
                                from_x, from_y = t
                                from_flag = 0
                                break

                    # "左"
                    elif from_flag == 8:
                        for t in movable_komas:
                            if (turn and t[0] < to_x) or \
                               (not turn and t[0] > to_x):
                                from_x, from_y = t
                                from_flag = 0
                                break

                    # "左上"
                    elif from_flag == 9:
                        for t in movable_komas:
                            if (turn and t[0] < to_x and t[1] > to_y) or \
                               (not turn and t[0] > to_x and t[1] < to_y):
                                from_x, from_y = t
                                from_flag = 0
                                break

                    # "左引"
                    elif from_flag == 12:
                        for t in movable_komas:
                            if (turn and t[0] < to_x and t[1] < to_y) or \
                               (not turn and t[0] > to_x and t[1] > to_y):
                                from_x, from_y = t
                                from_flag = 0
                                break

                    # "寄"
                    elif from_flag == 16:
                        for t in movable_komas:
                            if (t[0] == to_x):
                                from_x, from_y = t
                                from_flag = 0
                                break

                    # "直"
                    elif from_flag == 17:
                        for t in movable_komas:
                            if (t[1] == to_y):
                                from_x, from_y = t
                                from_flag = 0
                                break

                    # TODO : Send Error Message
                    if from_flag != 0:
                        return False

            else:
                # TODO : Send Error Message
                return False

        return (from_x, from_y, to_x, to_y, promote)
