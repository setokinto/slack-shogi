
# It's for me, sorry

from fabric.api import *

env.hosts = [
    "koukilab.com",
]

def deploy():
    with cd("/var/bot/slack-shogi"):
        run("git pull")
        run("supervisorctl reload")

