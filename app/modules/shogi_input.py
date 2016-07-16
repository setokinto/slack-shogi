
import uuid
from app.slack_utils.user import User

class ShogiInput:
    @staticmethod
    def init(channel_id, user_ids):
        if ShogiInput.creatable_new_shogi(channel_id, user_ids):
            # TODO: Manage shogi instance for judge creatable or not
            return Shogi(channel_id, user_ids)
        else:
            return None
    @staticmethod
    def creatable_new_shogi(channel_id, user_ids):
        for user_id in user_ids:
            if user_id is None:
                return False
        # TODO: If exists shogi for this channel, return false
        return True
    @staticmethod
    def koma_is_movable(channel_id, user_id, position, koma, sub_position, promote):
        # TODO: check can move with shogi module
        return True
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
        self.channel_id = channel_id
        self.user_ids = user_ids
        self.id = uuid.uuid4().hex

