
import uuid
import random

from app.slack_utils.user import User as UserFinder
from app.modules.shogi import Shogi as ShogiModule
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
        if shogi.first:
            if not shogi.first_user_id == user_id:
                return False # TODO: DifferentUserException
        else:
            if not shogi.second_user_id == user_id:
                return False # TODO: DifferentUserException
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

