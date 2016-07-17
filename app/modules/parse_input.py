
import re
from app.module.shogi import Koma

class ParseInput:
    self.koma_names = [
        "歩",
        "と",
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

str2info = {
    "一" : 0
    "１" : 0

}

    @staticmethod
    def parse(input_str):
        "([一二三四五六七八九123456789１２３４５６７８９]{2})("+koma_names_string_regex+")([上右下左]{1,2})?(成)?"
