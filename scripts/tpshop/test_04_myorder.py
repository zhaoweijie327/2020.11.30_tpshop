import logging
import pytest
from base.tpshop.page import Page
from config import BAS_URL
from utils import DriverUtils, data_path

@pytest.mark.run(order=5)
class Test_Myorder:

    def setup_class(self):
       DriverUtils.open_driver().get("http://127.0.0.1/")

    def teardown_class(self):
        DriverUtils.close_driver()

    @pytest.mark.parametrize("msg", data_path(BAS_URL + '/data/tpshop.json', 'myorder'))
    def test_04_myorder(self,msg):
        try:
            # 点击首页我的订单
            Page.get_home_page().homg_order()
            # 点击支付
            suc = Page.get_myorder_page().myorder_pay()
            # 断言
            if suc == msg:
                print("支付成功")
            logging.info("------------------->支付成功")
        except Exception:
            print("支付失败")
            # 错误截图
            DriverUtils().screen_image()
            raise