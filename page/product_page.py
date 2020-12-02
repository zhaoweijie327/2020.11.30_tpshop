'''
利用po模式将页面分为三层（对象、操作、业务）
'''
import time
from base.base_driver import DriverBase, DriverHandles
from page.find_element import Find_Element

# 添加购物车/立即购买
# 对象层
from utils import DriverUtils


class ProductPage(DriverBase):

    def __init__(self):
        super().__init__()

    # 定位产品名字
    def find_product_name(self):
        return self.find_elemnet(Find_Element.product_name)

    # 定位加入购物车
    def find_product_cart(self):
        return self.find_elemnet(Find_Element.product_cart)

    # 定位立即购买
    def find_product_icart(self):
        return self.find_elemnet(Find_Element.product_immediately_cart)

    # 定位ifram页面
    def find_product_ifram(self):
        return self.find_elemnet(Find_Element.product_ifram)

    # 定位添加成功信息
    def find_product_success(self):
        return self.find_elemnet(Find_Element.product_success)


# 操作层
class ProductHandles(DriverHandles):

    def __init__(self):
        self.p_page = ProductPage()

    # 点击产品名字操作
    def input_product_name(self):
        self.input_gundongtiao(self.p_page.driver)
        self.input_click(self.p_page.find_product_name())

    # 点击加入购物车
    def input_product_cart(self):
        return self.input_click(self.p_page.find_product_cart())

    # 点击立即购买
    def input_product_icart(self):
        self.input_click(self.p_page.find_product_icart())

    # 页面切换获取添加成功信息
    def input_product_ifram_success(self):
        # 进入子页面ifram
        self.input_ifram(self.p_page.driver,self.p_page.find_product_ifram())
        # 获取添加成功信息
        sucss = self.input_text(self.p_page.find_product_success())
        # 页面刷新
        self.p_page.driver.refresh()
        return sucss

# 业务层
class ProductBuissens:

    def __init__(self):
        self.p_handles = ProductHandles()

    # 成功添加购物车
    def product_add_cart(self):
        # 点击商品名称跳转到商品详情页
        self.p_handles.input_product_name()
        # 点击加入购物车
        self.p_handles.input_product_cart()
        # 获取添加成功信息
        sucss = self.p_handles.input_product_ifram_success()
        # 成功截图
        # DriverUtils().screen_image()
        time.sleep(2)
        return sucss

    # 立即购买
    def product_icart(self):
        # 立即购买
        self.p_handles.input_product_icart()

