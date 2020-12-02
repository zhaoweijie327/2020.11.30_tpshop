import pytest
from selenium.common.exceptions import NoSuchElementException

from base.page import Page
from utils import DriverUtils

@pytest.mark.run(order=5)
class Test_Myorder:

    def setup_class(self):
       DriverUtils.open_driver().get("http://127.0.0.1/")

    def teardown_class(self):
        DriverUtils.close_driver()

    def test_04_myorder(self):
        # 获取 订单提交成功，我们将在第一时间给你发货！
        order_success = "订单提交成功，我们将在第一时间给你发货！"
        try:
            # 点击首页我的订单
            Page.get_home_page().homg_order()
            # 点击支付
            suc = Page.get_myorder_page().myorder_pay()
            if suc == order_success:
                print("支付成功")
        except:
            # 错误截图
            DriverUtils().screen_image()
            ex = NoSuchElementException
            raise ex