import requests
import common
import os


# host = common.get_url()
# print(host)

def buy_chat_skin():
    params = {
        "m": "Api",
        "c": "ChatSkin",
        "a": "buy_chat_skin"
    }
    return params

def get_skin_list():
    params = {
        "m": "Api",
        "c": "ChatSkin",
        "a": "get_skin_list",
        "page": " ",
        "pagesize": ""

    }
    return params