
import getpass
import time

import mechanize

emoji_prefix = "slackshogisss_"

emojis = {
    "images/mu.png": "mu",
    "images/fu.png": "fu",
    "images/kyou.png": "kyou",
    "images/kei.png": "kei",
    "images/gin.png": "gin",
    "images/kin.png": "kin",
    "images/kaku.png": "kaku",
    "images/hi.png": "hi",
    "images/tokin.png": "tokin",
    "images/narikyou.png": "narikyou",
    "images/narikei.png": "narikei",
    "images/narigin.png": "narigin",
    "images/uma.png": "uma",
    "images/ryu.png": "ryu",
    "images/gyoku.png": "gyoku",
    "images/ou.png": "ou",
    "images/fu_.png": "fu_enemy",
    "images/kyou_.png": "kyou_enemy",
    "images/kei_.png": "kei_enemy",
    "images/gin_.png": "gin_enemy",
    "images/kin_.png": "kin_enemy",
    "images/kaku_.png": "kaku_enemy",
    "images/hi_.png": "hi_enemy",
    "images/tokin_.png": "tokin_enemy",
    "images/narikyou_.png": "narikyou_enemy",
    "images/narikei_.png": "narikei_enemy",
    "images/narigin_.png": "narigin_enemy",
    "images/uma_.png": "uma_enemy",
    "images/ryu_.png": "ryu_enemy",
    "images/gyoku_.png": "gyoku_enemy",
    "images/ou_.png": "ou_enemy",
    "images/last_fu.png": "fu",
    "images/last_kyou.png": "kyou",
    "images/last_kei.png": "kei",
    "images/last_gin.png": "gin",
    "images/last_kin.png": "kin",
    "images/last_kaku.png": "kaku",
    "images/last_hi.png": "hi",
    "images/last_tokin.png": "tokin",
    "images/last_narikyou.png": "narikyou",
    "images/last_narikei.png": "narikei",
    "images/last_narigin.png": "narigin",
    "images/last_uma.png": "uma",
    "images/last_ryu.png": "ryu",
    "images/last_gyoku.png": "gyoku",
    "images/last_ou.png": "ou",
    "images/last_fu_.png": "fu_enemy",
    "images/last_kyou_.png": "kyou_enemy",
    "images/last_kei_.png": "kei_enemy",
    "images/last_gin_.png": "gin_enemy",
    "images/last_kin_.png": "kin_enemy",
    "images/last_kaku_.png": "kaku_enemy",
    "images/last_hi_.png": "hi_enemy",
    "images/last_tokin_.png": "tokin_enemy",
    "images/last_narikyou_.png": "narikyou_enemy",
    "images/last_narikei_.png": "narikei_enemy",
    "images/last_narigin_.png": "narigin_enemy",
    "images/last_uma_.png": "uma_enemy",
    "images/last_ryu_.png": "ryu_enemy",
    "images/last_gyoku_.png": "gyoku_enemy",
    "images/last_ou_.png": "ou_enemy",
}

def input_emojis(id_, password, team_id):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open("https://{}.slack.com/".format(team_id))
    br.select_form(nr=0)
    br["email"] = id_
    br["password"] = password
    br.submit()
    # TODO: two factor authentication

    count = 0
    for file_name in emojis:
        emoji_name = emojis[file_name]
        br.open("https://{}.slack.com/customize/emoji".format(team_id))
        br.select_form(nr=0)
        br["name"] = emoji_prefix + emoji_name
        br.form.add_file(open(file_name), "images/png", file_name, name="img")
        br.submit()
        count += 1
        print("{}/{} completed".format(count, len(emojis)))
        time.sleep(1)

if __name__ == "__main__":
    team_id = raw_input("your slack team id: ")
    id_ = raw_input("your id: ")
    password = getpass.getpass("your password: ")
    input_emojis(id_, password, team_id)

