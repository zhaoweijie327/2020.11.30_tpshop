import pytest
from selenium.common.exceptions import NoSuchElementException

from base.page import Page
from utils import DriverUtils

@pytest.mark.run(order=3)
class Test_Add_Cart:

    def setup_class(self):
       DriverUtils.open_driver().get("http://127.0.0.1/")

    def teardown_class(self):
        DriverUtils.close_driver()

    def test_02_add_cart(self):
        product_name = "小米9"
        add_sucss = "添加成功"
        try:
            # 首页搜索
            Page.get_home_page().home_search(product_name)
            # 点击商品跳到商品详情页，把商品添加到购物车
            sucss = Page.get_product_page().product_add_cart()
            if sucss == add_sucss:
                print("添加购物车成功")
        except:
            print("添加失败")
            # 错误截图
            DriverUtils().screen_image()
            ex = NoSuchElementException
            raise ex