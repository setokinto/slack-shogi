
class User:  # TODO: rename this class

    def __init__(self, slacker):
        self._slacker = slacker
        self.users = self._slacker.users.list().body["members"]

    def username_to_id(self, username):
        """ return string user_id or None"""
        users = self.users
        if username[0] == "@":
            username = username[1:]
        for user in users:
            if user["name"] == username:
                return user["id"]
        return None

    def id_to_username(self, id_):
        users = self.users
        for user in users:
            if user["id"] == id_:
                return user["name"]

    def user_in_channel(self, user_id, channel_id):
        users = self._slacker.channels.info(channel_id).body[
            "channel"]["members"]
        for user in users:
            if user == user_id:
                return True
        return False
