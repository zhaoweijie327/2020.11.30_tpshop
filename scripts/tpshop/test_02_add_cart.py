import logging

import pytest

from base.tpshop.page import Page
from config import BAS_URL
from utils import DriverUtils, data_path


@pytest.mark.run(order=3)
class Test_Add_Cart:

    def setup_class(self):
       DriverUtils.open_driver().get("http://127.0.0.1/")

    def teardown_class(self):
        DriverUtils.close_driver()

    @pytest.mark.parametrize("product_name,msg", data_path(BAS_URL + '/data/tpshop.json', 'product'))
    def test_02_add_cart(self,product_name,msg):
        try:
            # 首页搜索
            Page.get_home_page().home_search(product_name)
            # 点击商品跳到商品详情页，把商品添加到购物车
            message = Page.get_product_page().product_add_cart()
            # 断言
            assert msg == message
            logging.info("------------------->%s" %msg)
        except Exception:
            print("添加失败")
            # 错误截图
            DriverUtils().screen_image()
            raise