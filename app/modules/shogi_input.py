
import uuid
import random

from app.slack_utils.user import User as UserFinder
from app.modules.shogi import Koma, Shogi as ShogiModule
from app.modules.parse_input import ParseInput


class ShogiManager:
    def __init__(self):
        self.shogi = {}
    def is_creatable(self, channel_id):
        if channel_id in self.shogi:
            return False
        else:
            return True
    def create(self, channel_id, users):
        if self.is_creatable(channel_id):
            shogi = Shogi(channel_id, users)
            self.shogi[channel_id] = shogi
            return shogi
        else:
            raise Exception()
    def createYaneuraou(self,channel_id):
        if self.is_creatable(channel_id):
            shogi = ShogiWithYaneuraOu(channel_id)
            self.shogi[channel_id] = shogi
            return shogi
        else:
            raise Exception()
    def get_shogi(self, channel_id):
        if channel_id in self.shogi:
            return self.shogi[channel_id]
        else:
            return None
    def is_exists(self, channel_id):
        return channel_id in self.shogi
    def clear(self, channel_id):
        if channel_id in self.shogi:
            del self.shogi[channel_id]

class ShogiInput:
    manager = ShogiManager()
    @staticmethod
    def init(channel_id, users):
        if ShogiInput.creatable_new_shogi(channel_id, users):
            shogi = ShogiInput.manager.create(channel_id, users)
            return shogi
        else:
            return None
    @staticmethod
    def initWithYaneuraOu(channel_id):
        if ShogiInput.creatable_new_shogi(channel_id, []):
            shogi = ShogiInput.manager.createYaneuraou(channel_id)
            return shogi
        else:
            return None
    @staticmethod
    def creatable_new_shogi(channel_id, users):
        for user in users:
            if user["id"] is None:
                return False
        if ShogiInput.manager.is_creatable(channel_id):
            return True
        else:
            return False
    @staticmethod
    def exists(channel_id):
        return ShogiInput.manager.is_exists(channel_id)
    @staticmethod
    def koma_is_movable(channel_id, user_id, position, koma, sub_position, promote):
        # TODO: check can move with shogi module
        return True
    @staticmethod
    def clear(channel_id):
        ShogiInput.manager.clear(channel_id)
    @staticmethod
    def move(movement_str, channel_id, user_id):
        shogi = ShogiInput.manager.get_shogi(channel_id)
        """
        if shogi.first:
            if not shogi.first_user_id == user_id:
                return False # TODO: DifferentUserException
        else:
            if not shogi.second_user_id == user_id:
                return False # TODO: DifferentUserException
        """
        movement = ParseInput.parse(movement_str, shogi.shogi) # TODO: use Shogi object in this file and test
        if movement == False:
            return False
        else:
            from_x, from_y, to_x, to_y, promote, koma = movement

        if from_x == -1 and from_y == -1 and shogi.droppable(koma, to_x, to_y):
            shogi.drop(koma, to_x, to_y)
            return True
        elif shogi.movable(from_x, from_y, to_x, to_y, promote):
            shogi.move(from_x, from_y, to_x, to_y, promote)
            return True
        else:
            return False
    @staticmethod
    def basic_move(channel_id, from_x, from_y, to_x, to_y, promote):
        shogi = ShogiInput.manager.get_shogi(channel_id)
        shogi.move(from_x, from_y, to_x, to_y, promote)
    @staticmethod
    def get_shogi(channel_id):
        return ShogiInput.manager.get_shogi(channel_id)
    @staticmethod
    def get_shogi_board(channel_id):
        shogi = ShogiInput.manager.get_shogi(channel_id)
        if shogi is None:
            return None
        return {
                   "first": shogi.shogi.first_tegoma,
                   "second": shogi.shogi.second_tegoma,
                   "board": shogi.board,
                   "info": {
                       "first": {
                           "id": shogi.first_user_id,
                           "name": shogi.first_user_name,
                       },
                       "second": {
                           "id": shogi.second_user_id,
                           "name": shogi.second_user_name,
                       }
                   },
                   "turn": shogi.first,
                   "_shogi": shogi,
               }

def move_to_usi(from_x, from_y, to_x, to_y, promote):
    if promote:
        promote_str = "+"
    else:
        promote_str = ""
    return pos_to_usi(from_x, from_y) + pos_to_usi(to_x, to_y) + promote_str

def drop_to_usi(koma, to_x, to_y):
    return koma_to_usi(koma).upper() + "*" + pos_to_usi(to_x, to_y)

def pos_to_usi(x, y):
    return str(9-x) + chr(ord("a")+y)

def koma_to_usi(koma):
    ret_usi_koma = ""
    if koma.is_promoted():
        ret_usi_koma += "+"
    koma = koma.unpromote()
    if koma is Koma.fu:
        usi_koma = "P"
    elif koma is Koma.opponent_fu:
        usi_koma = "p"
    elif koma is Koma.kyosha:
        usi_koma = "L"
    elif koma is Koma.opponent_kyosha:
        usi_koma = "l"
    elif koma is Koma.keima:
        usi_koma = "N"
    elif koma is Koma.opponent_keima:
        usi_koma = "n"
    elif koma is Koma.gin:
        usi_koma = "S"
    elif koma is Koma.opponent_gin:
        usi_koma = "s"
    elif koma is Koma.kin:
        usi_koma = "G"
    elif koma is Koma.opponent_kin:
        usi_koma = "g"
    elif koma is Koma.kaku:
        usi_koma = "B"
    elif koma is Koma.opponent_kaku:
        usi_koma = "b"
    elif koma is Koma.hisha:
        usi_koma = "R"
    elif koma is Koma.opponent_hisha:
        usi_koma = "r"
    elif koma is Koma.gyoku:
        usi_koma = "K"
    elif koma is Koma.opponent_gyoku:
        usi_koma = "k"
    ret_usi_koma += usi_koma
    return ret_usi_koma

def usi_to_koma(usi_koma):
    if usi_koma == "P":
        return Koma.fu
    elif usi_koma == "p":
        return Koma.opponent_fu
    elif usi_koma == "L":
        return Koma.kyosha
    elif usi_koma == "l":
        return Koma.opponent_kyosha
    elif usi_koma == "N":
        return Koma.keima
    elif usi_koma == "n":
        return Koma.opponent_keima
    elif usi_koma == "S":
        return Koma.gin
    elif usi_koma == "s":
        return Koma.opponent_gin
    elif usi_koma == "G":
        return Koma.kin
    elif usi_koma == "g":
        return Koma.opponent_kin
    elif usi_koma == "B":
        return Koma.kaku
    elif usi_koma == "b":
        return Koma.opponent_kaku
    elif usi_koma == "R":
        return Koma.hisha
    elif usi_koma == "r":
        return Koma.opponent_hisha
    elif usi_koma == "K":
        return Koma.gyoku
    elif usi_koma == "k":
        return Koma.opponent_gyoku

def usi_to_ss(usi_move):
    if usi_move[1] == "*":
        x, y = usi_to_pos(usi_move[2], usi_move[3])
        koma = usi_to_koma(usi_move[0])
        koma = koma.go_enemy()
        return (-1, -1, x, y, False, koma)
    else:
        from_x, from_y = usi_to_pos(usi_move[0], usi_move[1])
        to_x, to_y = usi_to_pos(usi_move[2], usi_move[3])
        promote = usi_move[-1] == "+"
        return (from_x, from_y, to_x, to_y, promote, None)

def usi_to_pos(x, y):
    return 9-int(x), ord(y) - ord("a")

class Shogi:
    def __init__(self, channel_id, users):
        self.shogi = ShogiModule()
        self.channel_id = channel_id
        self.user_ids = [ x["id"] for x in users]
        random.shuffle(users)
        self.first_user_id = users[0]["id"]
        self.first_user_name = users[0]["name"]
        self.second_user_id = users[1]["id"]
        self.second_user_name = users[1]["name"]
        self.id = uuid.uuid4().hex
    def move(self, from_x, from_y, to_x, to_y, promote):
        self.shogi.move(from_x, from_y, to_x, to_y, promote)
    def drop(self, koma, to_x, to_y):
        self.shogi.drop(koma, to_x, to_y)
    def movable(self, from_x, from_y, to_x, to_y, promote):
        return self.shogi.movable(from_x, from_y, to_x, to_y, promote)
    def droppable(self, koma, to_x, to_y):
        return self.shogi.droppable(koma, to_x, to_y)
    @property
    def first(self):
        return self.shogi.first
    @property
    def board(self):
        return self.shogi.board



from abc import ABCMeta

class ShogiBot(metaclass=ABCMeta):
    def think(self):
        pass


class ShogiWithYaneuraOu(Shogi, ShogiBot):
    def __init__(self, channel_id):
        self.shogi = ShogiModule()
        self.channel_id = channel_id
        self.first_user_id = "XXXXXX"
        self.first_user_name = "みんな"
        self.second_user_id = "XXXXXX"
        self.second_user_name = "やねうら王"
        self.id = uuid.uuid4().hex
        self.history = []
    def move(self, from_x, from_y, to_x, to_y, promote):
        super().move(from_x, from_y, to_x, to_y, promote)
        self.history.append(move_to_usi(from_x, from_y, to_x, to_y, promote))
    def drop(self, koma, to_x, to_y):
        super().drop(koma, to_x, to_y)
        self.history.append(drop_to_usi(koma, to_x, to_y))
    def think(self):
        from subprocess import Popen, PIPE
        import re
        p = Popen(["./YaneuraOu-by-gcc"], bufsize=0, executable=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0,stdout=PIPE, stdin=PIPE)
        p.stdin.write("usi\n".encode())

        options = [
                "Threads value 4",
                "Hash value 400",
                ]
        for option in options:
            p.stdin.write(("setoption name " + option + "\n").encode())

        p.stdin.write("usinewgame\n".encode())
        p.stdin.write(("position startpos moves " + " ".join(self.history) + "\n").encode())
        p.stdin.write("go byoyomi 5000\n".encode())
        print("OK?")
        while 1:    
            c = p.stdout.readline().decode("utf-8") 
            if 'bestmove' in c:
                usi_move = re.search("bestmove ([\d\w\+\*]*) ", c).group(1)
                print(usi_move)
                p.kill()
                return usi_to_ss(usi_move)

