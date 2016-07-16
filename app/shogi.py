
import re

from slackbot.bot import respond_to

@respond_to('hey', re.IGNORECASE)
def res_hey(message):
    message.reply("Hey")

