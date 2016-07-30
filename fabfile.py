
# It's for me, sorry

from fabric.api import *
import slackbot_settings as settings
from urllib import request, parse

env.hosts = settings.DEPLOY_HOSTS


def deploy():
    slack("Deploy Started")
    with cd("/var/bot/slack-shogi"):
        run("git pull")
        run("supervisorctl reload")
    slack("Deploy Finished")


def slack(text):
    if settings.WEBHOOK_URL:
        payload = ("payload={\"text\": \"" + parse.quote(text) +
                   "\", \"username\": \"Mr.deploy\"}").encode("utf-8")
        request.urlopen(url=settings.WEBHOOK_URL, data=payload)
