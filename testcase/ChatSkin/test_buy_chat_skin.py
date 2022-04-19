from data.ChatSkin import buy_chat_skin_data
import base
import common
from api.ChatSkin import buy_chat_skin
import allure


@allure.feature("购买皮肤")
class TestBuyChatSkin:

    @allure.story("购买一个存在的皮肤")
    def test_buy_chat_skin_exits(self):
        # print(buy_chat_skin_data.buy_chat_skin_idexits())
        res = base.api_post(common.get_url(), buy_chat_skin(), buy_chat_skin_data.buy_chat_skin_idexits())
        print(res)
        assert res["status"] == "ok"


    @allure.story("购买一个不存在的皮肤")
    def test_buy_chat_skin_noexits(self):
        res = base.api_post(common.get_url(), buy_chat_skin(), buy_chat_skin_data.buy_chat_skin_idnoexits())
        assert res["status"] == "error"
        assert res["message"]["message"] == "聊天皮肤不存在"


    @allure.story("入参时皮肤ID为空")
    def test_buy_chat_skin_empty(self):
        res = base.api_post(common.get_url(), buy_chat_skin(), buy_chat_skin_data.buy_chat_skin_idempty())
        assert res["status"] == "error"
        assert res["message"]["message"] == "聊天皮肤不存在"


# test_buy_chat_skin()
