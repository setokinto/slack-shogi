
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
    def get_shogi_board(channel_id):
        # TODO:
        return {
                   "first":[],
                   "second": [],
                   "board": [
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],
                   ],
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
    def move(from_x, from_y, to_x, to_y, promote):
        pass

