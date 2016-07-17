

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
    

class ShogiCantMoveException(Exception):
    pass

class Shogi:
    # TODO: implement komaochi
    def __init__(self):
        self.first = True
        self.first_tegoma = []
        self.second_tegoma = []
        self.board = [
            [
                Koma.opponent_kyosha,
                Koma.opponent_keima,
                Koma.opponent_gin,
                Koma.opponent_kin,
                Koma.opponent_gyoku,
                Koma.opponent_kin,
                Koma.opponent_gin,
                Koma.opponent_keima,
                Koma.opponent_kyosha,
            ],
            [
                Koma.empty,
                Koma.opponent_hisha,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.opponent_kaku,
                Koma.empty,
            ],
            [
                Koma.opponent_fu,
                Koma.opponent_fu,
                Koma.opponent_fu,
                Koma.opponent_fu,
                Koma.opponent_fu,
                Koma.opponent_fu,
                Koma.opponent_fu,
                Koma.opponent_fu,
                Koma.opponent_fu,
            ],
            [
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
            ],
            [
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
            ],
            [
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
            ],
            [
                Koma.fu,
                Koma.fu,
                Koma.fu,
                Koma.fu,
                Koma.fu,
                Koma.fu,
                Koma.fu,
                Koma.fu,
                Koma.fu,
            ],
            [
                Koma.empty,
                Koma.kaku,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.empty,
                Koma.hisha,
                Koma.empty,
            ],
            [
                Koma.kyosha,
                Koma.keima,
                Koma.gin,
                Koma.kin,
                Koma.gyoku,
                Koma.kin,
                Koma.gin,
                Koma.keima,
                Koma.kyosha,
            ],
        ]
    def move(self, from_x, from_y, to_x, to_y, promote):
        """
            if from_x and from_y is -1, the koma is from komadai
        """
        koma = self.board[from_y][from_x]
        # TODO: check for movable
        if False: # not movable:
            raise ShogiCantMoveException()
        koma_for_komadai = self.board[to_y][to_x]
        if koma_for_komadai is not Koma.empty:
            # TODO: move to komadai
            pass
        self.board[from_y][from_x] = Koma.empty
        self.board[to_y][to_x] = koma # TODO: in case promote is true
        self.first = not self.first

