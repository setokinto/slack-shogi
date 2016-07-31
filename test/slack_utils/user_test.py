
import unittest

from app.slack_utils.user import User


class MockedSlacker:

    @property
    def users(self):
        return MockedUser()

    @property
    def groups(self):
        return MockedGroup()

    @property
    def channels(self):
        return MockedChannel()


class MockedUser:

    def list(self):
        return MockedBody({
            "ok": True,
            "members": [
                {
                    "id": "U023BECGF",
                    "name": "bobby",
                    "deleted": False,
                    "color": "9f69e7",
                    "profile": {
                            "first_name": "Bobby",
                            "last_name": "Tables",
                            "real_name": "Bobby Tables",
                            "email": "bobby@slack.com",
                            "skype": "my-skype-name",
                            "phone": "+1 (123) 456 7890",
                            "image_24": "https:\/\/...",
                            "image_32": "https:\/\/...",
                            "image_48": "https:\/\/...",
                            "image_72": "https:\/\/...",
                            "image_192": "https:\/\/..."
                    },
                    "is_admin": True,
                    "is_owner": True,
                    "has_2fa": True,
                    "has_files": False
                },
                {
                    "id": "U023BECGA",
                    "name": "bobby2",
                    "deleted": False,
                    "color": "9f69e2",
                    "profile": {
                            "first_name": "Bobby2",
                            "last_name": "Tables2",
                            "real_name": "Bobby Table2s",
                            "email": "bobby2@slack.com",
                            "skype": "my-skype-name2",
                            "phone": "+1 (123) 456 7891",
                            "image_24": "https:\/\/...",
                            "image_32": "https:\/\/...",
                            "image_48": "https:\/\/...",
                            "image_72": "https:\/\/...",
                            "image_192": "https:\/\/..."
                    },
                    "is_admin": True,
                    "is_owner": True,
                    "has_2fa": False,
                    "has_files": True
                },
            ]
        }
        )

class MockedGroup:

    def info(self, group_id):
        if not group_id[0] == "G":
            raise Exception()
        return MockedBody(
            {
                "ok": True,
                "group": {
                    "id": "G023BECGF",
                    "name": "fun",
                    "created": 1360782804,
                    "creator": "U024BE7LH",
                    "is_archived": False,
                    "is_general": False,
                    "is_member": True,
                    "is_starred": True,
                    "members": [
                            "U023BECGA",
                    ],
                    "topic": {},
                    "purpose": {},
                    "last_read": "1401383885.000061",
                    "latest": {},
                    "unread_count": 0,
                    "unread_count_display": 0
                }
            }
        )

class MockedChannel:

    def info(self, channel_id):
        if not channel_id[0] == "C":
            raise Exception()
        
        return MockedBody(
            {
                "ok": True,
                "channel": {
                    "id": "C023BECGA",
                    "name": "fun",
                    "created": 1360782804,
                    "creator": "U024BE7LH",
                    "is_archived": False,
                    "is_general": False,
                    "is_member": True,
                    "is_starred": True,
                    "members": [
                            "U023BECGA",
                    ],
                    "topic": {},
                    "purpose": {},
                    "last_read": "1401383885.000061",
                    "latest": {},
                    "unread_count": 0,
                    "unread_count_display": 0
                }
            }
        )


class MockedBody:

    def __init__(self, body):
        self._body = body

    @property
    def body(self):
        return self._body


class UserTest(unittest.TestCase):

    def setUp(self):
        self.user = User(MockedSlacker())

    def test_find_userid_from_username(self):
        user_id = self.user.username_to_id("bobby")
        self.assertEqual(user_id, "U023BECGF")

        user_id2 = self.user.username_to_id("bobby2")
        self.assertEqual(user_id2, "U023BECGA")

    def test_find_username_from_userid(self):
        username = self.user.id_to_username("U023BECGF")
        self.assertEqual(username, "bobby")

        username = self.user.id_to_username("U023BECGA")
        self.assertEqual(username, "bobby2")

    def test_return_None_non_exists_user_name(self):
        user_id = self.user.username_to_id("not_bobby")
        self.assertEqual(user_id, None)

    def test_find_userid_with_atmark_prefix(self):
        user_id = self.user.username_to_id("@bobby")
        self.assertEqual(user_id, "U023BECGF")

        user_id2 = self.user.username_to_id("@bobby2")
        self.assertEqual(user_id2, "U023BECGA")

    def test_user_in_channel_return_True_when_user_exists(self):
        exists = self.user.user_in_channel("U023BECGA", "C023BECGA")
        self.assertTrue(exists)

    def test_user_in_channel_return_False_when_user_not_exists(self):
        notexists = self.user.user_in_channel("UNONONONONO", "C023BECGA")
        self.assertFalse(notexists)

    def test_user_in_privatechannel_return_True_when_user_exists(self):
        exists = self.user.user_in_channel("U023BECGA", "G023BECGF")
        self.assertTrue(exists)

    def test_user_in_private_channel_return_False_when_user_not_exists(self):
        notexists = self.user.user_in_channel("UNONONONONO", "G023BECGF")
        self.assertFalse(notexists)
        
