# from data.ChatSkin.buy_chat_skin_data import buy_chat_skin_data
import base
import common
from api.ChatSkin import get_skin_list
import allure
from log import *


@allure.feature("获取聊天皮肤列表")
@allure.title("获取聊天皮肤列表成功")
@loginfo
def test_get_skin_list():
    res = base.api_get(common.get_url(), get_skin_list())
    print(res)
    assert res["status"] == "ok"