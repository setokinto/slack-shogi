[![CircleCI](https://circleci.com/gh/setokinto/slack-shogi.svg?style=svg)](https://circleci.com/gh/setokinto/slack-shogi)
[![Code Climate](https://codeclimate.com/github/setokinto/slack-shogi/badges/gpa.svg)](https://codeclimate.com/github/setokinto/slack-shogi)
[![Test Coverage](https://codeclimate.com/github/setokinto/slack-shogi/badges/coverage.svg)](https://codeclimate.com/github/setokinto/slack-shogi/coverage)
[![Issue Count](https://codeclimate.com/github/setokinto/slack-shogi/badges/issue_count.svg)](https://codeclimate.com/github/setokinto/slack-shogi)

Slack-Shogi
-----------
This is a room with a shogi board.

# How to use
1. Create a Bot https://your-team-name.slack.com/apps/A0F7YS25R-bots
2. Copy config file `cp slackbot_settings.py.default slackbot_settings.py`
3. Replace your api key with your bot from slack

# Commands
`@shogibot: start with @username`  
`@shogibot: board`  
`@shogibot: 76歩`  
`@shogibot: resign` or `@shogibot: 参りました`  
And more!

If you want to try it, use this command `@shogibot: start with @your_user_name`

# How to input shogi emojis
We proide an images for playing shogi, and a script to input images to your slack team.
The script required your slack id and password because an api which saves a new emoji does not exist.
Emoji example is here:
![Shogi](https://raw.githubusercontent.com/setokinto/slack-shogi/master/input_emojis/images/example.png)

It requires Python2 for mehanize.
```
% cd input_emojis
% pip install mechanize
% python input_emojis.py
your slack team id: [your_team_id]
your id (email): [your_id@example.com]
your password: [******]
authentication code for two factor(If needed) : [two-factor code or empty if you don't use two-factor-authentication]
...
...
...
Completed!!
```

If you already inputted emojis and has a difference for adding emojis, you can use `--patch` option for this script. The script called with this optioin ignores emojis which already registed.

# Thanks for
- [Slackbot](https://github.com/lins05/slackbot)
- [Slacker](https://github.com/os/slacker)
- [Slack](https://slack.com)

# LICENSE
MIT

