import requests
import common
import os


host = common.get_url()
print(host)

def buy_chat_skin():
    params = {
        "m": "Api",
        "c": "ChatSkin",
        "a": "buy_chat_skin"
    }
    return 111