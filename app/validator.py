

from abc import ABCMeta, abstractmethod

class UserValidator(metaclass=ABCMeta):
    @abstractmethod
    def validate(self, shogi, user_id):
        raise NotImplementedError()


class BasicUserValidator(UserValidator):
    def validate(self, shogi, user_id):
        if shogi.first:
            if not shogi.first_user_id == user_id:
                return False
        else:
            if not shogi.second_user_id == user_id:
                return False
        return True

class AllPassUserValidator(UserValidator):
    def validate(self, shogi, user_id):
        return True

