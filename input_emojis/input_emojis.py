
import getpass
import time

import mechanize

emojis = {
    "images/test.png": "testforim",
    "images/test2.png": "testforim2",
}

def input_emojis(id_, password):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open("https://setokinto.slack.com/")
    br.select_form(nr=0)
    br["email"] = id_
    br["password"] = password
    br.submit()
    #TODO : Two factor authorization

    count = 0
    for file_name in emojis:
        emoji_name = emojis[file_name]
        br.open("https://setokinto.slack.com/customize/emoji")
        br.select_form(nr=0)
        br["name"] = emoji_name
        br.form.add_file(open(file_name), "images/png", file_name, name="img")
        br.submit()
        count += 1
        print("{}/{} completed".format(count, len(emojis)))
        time.sleep(1)

if __name__ == "__main__":
    # TODO: Use in team except for setokinto 
    id_ = raw_input("your id: ")
    password = getpass.getpass("your password: ")
    input_emojis(id_, password)

