

from enum import IntEnum


class Koma(IntEnum):
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

    def is_first(self):
        if 0x01 <= self.value < 0x20:
            return True
        elif 0x20 <= self.value < 0x40:
            return False

    def is_keima(self):
        if self is Koma.keima:
            return True
        if self is Koma.opponent_keima:
            return True
        return False

    def can_promote(self):
        if self is Koma.kin or self is Koma.gyoku or self is Koma.opponent_kin or self is Koma.opponent_gyoku:
            return False
        if self.value & 0x10:
            return False
        return True

    def promote(self):
        try:
            return Koma(self.value | 0x10)
        except ValueError:
            return self

    def unpromote(self):
        try:
            return Koma(self.value & 0x2F)
        except ValueError:
            return self

    def go_enemy(self):
        if self.is_first():
            return Koma(self.value + 0x20)
        else:
            return Koma(self.value - 0x20)


class Shogi:
    # TODO: implement komaochi

    def __init__(self):
        self.first = True
        self.first_tegoma = []
        self.second_tegoma = []
        self.last_move_x = None
        self.last_move_y = None
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
        koma = self.board[from_y][from_x]
        koma_for_komadai = self.board[to_y][to_x]
        if koma_for_komadai is not Koma.empty:
            koma_for_komadai = koma_for_komadai.unpromote().go_enemy()
            if self.first:
                self.first_tegoma.append(koma_for_komadai)
            else:
                self.second_tegoma.append(koma_for_komadai)
        self.board[from_y][from_x] = Koma.empty
        if promote:
            self.board[to_y][to_x] = koma.promote()
        else:
            self.board[to_y][to_x] = koma
        self.first = not self.first
        self.last_move_x = to_x
        self.last_move_y = to_y

    def movable(self, from_x, from_y, to_x, to_y, promote):
        board = self.board
        from_koma = board[from_y][from_x]
        to_koma = board[to_y][to_x]

        if from_koma is Koma.empty:
            return False
        if not self.first == from_koma.is_first():
            return False
        if not promote:
            if (from_koma is Koma.fu or from_koma is Koma.kyosha) and to_y == 0:
                return False
            if from_koma is Koma.keima and to_y <= 1:
                return False
            if (from_koma is Koma.opponent_fu or from_koma is Koma.opponent_kyosha) and to_y == 8:
                return False
            if from_koma is Koma.opponent_keima and 7 <= to_y:
                return False
        if promote:
            if not from_koma.can_promote():
                return False
            if from_koma.is_first():
                if not (0 <= from_y <= 2 or 0 <= to_y <= 2):
                    return False
            else:
                if not (6 <= from_y <= 8 or 6 <= to_y <= 8):
                    return False

        for movable_position in movable_positions[from_koma]:
            if from_x + movable_position[0] == to_x and from_y + movable_position[1] == to_y:
                if to_koma is Koma.empty or not to_koma.is_first() == self.first:
                    if self.checkObstacle(from_x, from_y, to_x, to_y):
                        return True
        return False

    def drop(self, koma, to_x, to_y):
        if self.first:
            self.first_tegoma.remove(koma)
        else:
            self.second_tegoma.remove(koma)
        koma_for_komadai = self.board[to_y][to_x]
        self.board[to_y][to_x] = koma
        if koma_for_komadai is not Koma.empty:
            koma_for_komadai = koma_for_komadai.unpromote().go_enemy()
            if self.first:
                self.first_tegoma.append(koma_for_komadai)
            else:
                self.second_tegoma.append(koma_for_komadai)
        self.first = not self.first
        self.last_move_x = to_x
        self.last_move_y = to_y

    def droppable(self, koma, to_x, to_y):
        if self.first:
            tegoma = self.first_tegoma
        else:
            tegoma = self.second_tegoma
        if koma in tegoma and self.board[to_y][to_x] is Koma.empty:
            if koma is Koma.fu or koma is Koma.opponent_fu:
                for y_board in self.board:
                    if y_board[to_x] is koma:
                        # 2fu
                        return False
            if koma is Koma.fu or koma is Koma.kyosha:
                if to_y == 0:
                    return False
            if koma is Koma.keima:
                if to_y <= 1:
                    return False
            if koma is Koma.opponent_fu or koma is Koma.opponent_kyosha:
                if to_y == 8:
                    return False
            if koma is Koma.opponent_keima:
                if to_y >= 7:
                    return False
            return True
        return False

    def checkObstacle(self, from_x, from_y, to_x, to_y):
        if self.board[from_y][from_x].is_keima():
            return True
        while True:
            to_x = _approach(from_x, to_x)
            to_y = _approach(from_y, to_y)
            if from_x == to_x and from_y == to_y:
                break
            road_koma = self.board[to_y][to_x]
            if road_koma is Koma.empty:
                continue
            else:
                return False
        return True

    def find_koma(self, koma):
        koma_positions = []
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] == koma:
                    koma_positions.append([x, y])
        return koma_positions


def _approach(to, by):
    if to < by:
        return by - 1
    elif to > by:
        return by + 1
    else:
        return by

movable_positions = {
    Koma.fu: [[0, -1]],
    Koma.kyosha: [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [0, -8]],
    Koma.keima: [[-1, -2], [1, -2]],
    Koma.gin: [[-1, -1], [0, -1], [1, -1], [-1, 1], [1, 1]],
    Koma.kin: [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [0, 1]],
    Koma.kaku: [[-8, -8], [8, -8], [-7, -7], [7, -7], [-6, -6], [6, -6], [-5, -5], [5, -5], [-4, -4], [4, -4], [-3, -3], [3, -3], [-2, -2], [2, -2], [-1, -1], [1, -1], [-1, 1], [1, 1], [-2, 2], [2, 2], [-3, 3], [3, 3], [-4, 4], [4, 4], [-5, 5], [5, 5], [-6, 6], [6, 6], [-7, 7], [7, 7], [-8, 8], [8, 8]],
    Koma.hisha: [[0, -8], [0, -7], [0, -6], [0, -5], [0, -4], [0, -3], [0, -2], [0, -1], [-8, 0], [-7, 0], [-6, 0], [-5, 0], [-4, 0], [-3, 0], [-2, 0], [-1, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8]],
    Koma.gyoku: [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]],
}
movable_positions[Koma.promoted_fu] = movable_positions[Koma.promoted_kyosha] = movable_positions[
    Koma.promoted_kyosha] = movable_positions[Koma.promoted_gin] = movable_positions[Koma.kin]
movable_positions[Koma.promoted_kaku] = movable_positions[
    Koma.kaku] + [[0, -1], [-1, 0], [1, 0], [0, 1]]
movable_positions[Koma.promoted_hisha] = movable_positions[
    Koma.hisha] + [[-1, -1], [1, -1], [-1, 1], [1, 1]]

movable_positions[Koma.opponent_fu] = [[0, 1]]
movable_positions[Koma.opponent_kyosha] = [
    [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8]]
movable_positions[Koma.opponent_keima] = [[1, 2], [-1, 2]]
movable_positions[Koma.opponent_gin] = [
    [1, 1], [0, 1], [-1, 1], [1, -1], [-1, -1]]
movable_positions[Koma.opponent_kin] = [
    [1, 1], [0, 1], [-1, 1], [1, 0], [-1, 0], [0, -1]]
movable_positions[Koma.opponent_kaku] = movable_positions[Koma.kaku]
movable_positions[Koma.opponent_hisha] = movable_positions[Koma.hisha]
movable_positions[Koma.opponent_gyoku] = movable_positions[Koma.gyoku]

movable_positions[Koma.opponent_promoted_fu] = movable_positions[Koma.opponent_promoted_kyosha] = movable_positions[
    Koma.opponent_promoted_keima] = movable_positions[Koma.opponent_promoted_gin] = movable_positions[Koma.opponent_kin]

movable_positions[Koma.opponent_promoted_kaku] = movable_positions[
    Koma.promoted_kaku]
movable_positions[Koma.opponent_promoted_hisha] = movable_positions[
    Koma.promoted_hisha]
