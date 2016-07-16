
class User:
    def __init__(self, slacker):
        self._slacker = slacker

    def username_to_id(self, username):
        """ return string user_id or None"""
        users = self._slacker.users.list().body["members"] # TODO: cache
        if username[0] == "@":
            username = username[1:]
            print(username)
        for user in users:
            if user["name"] == username:
                return user["id"]
        return None
    def user_in_channel(self, user_id, channel_id):
        users = self._slacker.channels.info(channel_id).body["channel"]["members"]
        print(users)
        for user in users:
            if user == user_id:
                return True
        return False
