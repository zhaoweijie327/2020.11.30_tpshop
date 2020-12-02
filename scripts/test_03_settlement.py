import logging

import pytest
from selenium.common.exceptions import NoSuchElementException
from base.page import Page
from config import BAS_URL
from utils import DriverUtils, data_path


@pytest.mark.run(order=4)
class Test_Settlement:

    def setup_class(self):
       DriverUtils.open_driver().get("http://127.0.0.1/")

    def teardown_class(self):
        DriverUtils.close_driver()

    @pytest.mark.parametrize("msg", data_path(BAS_URL + '/data/tpshop.json', 'settlement'))
    def test_03_settlement(self,msg):
        try:
            # 点击首页的购物车显示并点击进入购物车结算
            Page.get_home_page().home_cart()
            # 进入购物车页面进行结算并提交
            message = Page.get_addcart_page().addcart_settlement()
            # 断言
            if message == msg:
                logging.info("------------------->提交成功")
        except Exception:
            # 错误截图
            DriverUtils().screen_image()
            raise