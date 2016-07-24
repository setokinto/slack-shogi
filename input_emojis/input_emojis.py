
import getpass
import time
import sys

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
    "images/last_fu.png": "last_fu",
    "images/last_kyou.png": "last_kyou",
    "images/last_kei.png": "last_kei",
    "images/last_gin.png": "last_gin",
    "images/last_kin.png": "last_kin",
    "images/last_kaku.png": "last_kaku",
    "images/last_hi.png": "last_hi",
    "images/last_tokin.png": "last_tokin",
    "images/last_narikyou.png": "last_narikyou",
    "images/last_narikei.png": "last_narikei",
    "images/last_narigin.png": "last_narigin",
    "images/last_uma.png": "last_uma",
    "images/last_ryu.png": "last_ryu",
    "images/last_gyoku.png": "last_gyoku",
    "images/last_ou.png": "last_ou",
    "images/last_fu_.png": "last_fu_enemy",
    "images/last_kyou_.png": "last_kyou_enemy",
    "images/last_kei_.png": "last_kei_enemy",
    "images/last_gin_.png": "last_gin_enemy",
    "images/last_kin_.png": "last_kin_enemy",
    "images/last_kaku_.png": "last_kaku_enemy",
    "images/last_hi_.png": "last_hi_enemy",
    "images/last_tokin_.png": "last_tokin_enemy",
    "images/last_narikyou_.png": "last_narikyou_enemy",
    "images/last_narikei_.png": "last_narikei_enemy",
    "images/last_narigin_.png": "last_narigin_enemy",
    "images/last_uma_.png": "last_uma_enemy",
    "images/last_ryu_.png": "last_ryu_enemy",
    "images/last_gyoku_.png": "last_gyoku_enemy",
    "images/last_ou_.png": "last_ou_enemy",
}

def input_emojis(id_, password, team_id, two_factor, force_update=False):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open("https://{}.slack.com/".format(team_id))
    br.select_form(nr=0)
    br["email"] = id_
    br["password"] = password
    br.submit()
    if two_factor:
        br.select_form(nr=0)
        br["2fa_code"] = two_factor
        br.submit()

    count = 0
    for file_name in emojis:
        emoji_name = emojis[file_name]
        response = br.open("https://{}.slack.com/customize/emoji".format(team_id))
        if response.read().find(":"+emoji_name+":") >= 0 and not force_update:
            # Simple resume. Does it work?
            continue
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
    two_factor = raw_input("authentication code for two factor(If needed) :")
    input_emojis(id_, password, team_id, two_factor)

