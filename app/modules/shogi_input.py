
import uuid
from app.slack_utils.user import User
from app.modules.shogi import Shogi as ShogiModule

class ShogiManager:
    def __init__(self):
        self.shogi = {}
    def is_creatable(self, channel_id):
        if channel_id in self.shogi:
            return False
        else:
            return True
    def create(self, channel_id, user_ids):
        if self.is_creatable(channel_id):
            shogi = Shogi(channel_id, user_ids)
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
    def init(channel_id, user_ids):
        if ShogiInput.creatable_new_shogi(channel_id, user_ids):
            shogi = ShogiInput.manager.create(channel_id, user_ids)
            return shogi
        else:
            return None
    @staticmethod
    def creatable_new_shogi(channel_id, user_ids):
        for user_id in user_ids:
            if user_id is None:
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
    def move(position, koma, sub_position, promote):
        # TODO:
        return False
    @staticmethod
    def basic_move(channel_id, from_x, from_y, to_x, to_y, promote):
        shogi = ShogiInput.manager.get_shogi(channel_id)
        shogi.move(from_x, from_y, to_x, to_y, promote)
    @staticmethod
    def get_shogi_board(channel_id):
        # TODO:
        shogi = ShogiInput.manager.get_shogi(channel_id)
        if shogi is None:
            return None
        return {
                   "first":[],
                   "second": [],
                   "board": shogi.board,
                   "info": {
                       "first": {
                           "name": "millay",
                       },
                       "second": {
                           "name": "not millay",
                       }
                   }
               }

class Shogi:
    def __init__(self, channel_id, user_ids):
        self.shogi = ShogiModule()
        self.channel_id = channel_id
        self.user_ids = user_ids
        self.id = uuid.uuid4().hex
    def move(self, from_x, from_y, to_x, to_y, promote):
        self.shogi.move(from_x, from_y, to_x, to_y, promote)
    @property
    def board(self):
        return self.shogi.board

