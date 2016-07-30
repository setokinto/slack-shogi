
import functools

from app.modules.shogi_input import ShogiInput

def channel_info(f):
    @functools.wraps(f)
    def _warp(*args, **kwargs):
        message = args[0]
        channel_id = message.body["channel"]
        own_id = message.body["user"]
        
        channel_info = ChannelInfo(channel_id, own_id)
        args = (channel_info,) + args
        f(*args, **kwargs)
    return _warp

def should_exist_shogi(f):
    @functools.wraps(f)
    def _warp(*args, **kwargs):
        channel = args[0]
        message = args[1]
        if not ShogiInput.exists(channel.channel_id):
            message.reply("start withから初めてね")
            return

        f(*args, **kwargs)
    return _warp

class ChannelInfo:
    def __init__(self, channel_id, own_id):
        self.channel_id = channel_id
        self.own_id = own_id

