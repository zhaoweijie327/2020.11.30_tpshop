import pytest
from selenium.common.exceptions import NoSuchElementException

from base.page import Page
from utils import DriverUtils

@pytest.mark.run(order=4)
class Test_Settlement:

    def setup_class(self):
       DriverUtils.open_driver().get("http://127.0.0.1/")

    def teardown_class(self):
        DriverUtils.close_driver()

    def test_03_settlement(self):
        success = "订单提交成功，请您尽快付款！"
        try:
            # 点击首页的购物车显示并点击进入购物车结算
            Page.get_home_page().home_cart()
            # 进入购物车页面进行结算并提交
            suc = Page.get_addcart_page().addcart_settlement()
            if suc == success:
                print('提交成功')
        except:
            # 错误截图
            DriverUtils().screen_image()
            ex = NoSuchElementException
            raise ex