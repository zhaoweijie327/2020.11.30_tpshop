import time
from base.base_driver import DriverBase, DriverHandles
from page.find_element import Find_Element


from utils import DriverUtils

# 购物车点击结算，提交订单
# 对象层
class AddcartPage(DriverBase):

    def __init__(self):
        super().__init__()

    # 定位结算按钮
    def find_addcard_settlement(self):
        return self.find_elemnet(Find_Element.s_cart_settlement)

    # 定位提交订单按钮
    def find_addcart_order(self):
        return self.find_elemnet(Find_Element.s_cart_submit_order)

    # 定位提交成功信息
    def find_addcart_success(self):
        return self.find_elemnet(Find_Element.s_cart_order)

# 操作层
class AddcartHandles(DriverHandles):

    def __init__(self):
        self.a_page = AddcartPage()

    # 点击结算操作
    def input_addcard_settlement(self):
        self.input_click(self.a_page.find_addcard_settlement())

    # 点击提交订单操作
    def input_addcard_order(self):
        # 滚动条操作
        self.input_gundongtiao(self.a_page.driver)
        self.input_click(self.a_page.find_addcart_order())

    # 获取提交成功信息
    def input_addcart_success(self):
        return self.input_text(self.a_page.find_addcart_success())

# 业务层
class AddcartBuissens:

    def __init__(self):
        self.a_handles = AddcartHandles()

    # 成功结算提交订单
    def addcart_settlement(self):
        # 点击结算
        self.a_handles.input_addcard_settlement()
        time.sleep(3)
        # 点击提交订单
        self.a_handles.input_addcard_order()
        # 获取提交成功信息
        suc = self.a_handles.input_addcart_success()
        return suc
        # DriverUtils.screen_image()