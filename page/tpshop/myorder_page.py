'''
利用po模式将页面分为三层（对象、操作、业务）
'''
import time
from base.base_driver import DriverBase, DriverHandles
from page.tpshop.find_element import Find_Element


# 支付
# 对象层
class MyorderPage(DriverBase):

    def __init__(self):
        super().__init__()

    # 定位立即支付按钮
    def find_myorder_pay(self):
        return self.find_elemnet(Find_Element.my_order_pay)

    # 定位货到付款
    def find_myorder_delivery(self):
        return self.find_elemnet(Find_Element.pay_delivery)

    # 定位确认支付
    def find_myorder_confirm(self):
        return self.find_elemnet(Find_Element.pay_confirm)

    # 定位支付成功文本信息
    def find_myorder_success_pay(self):
        return self.find_elemnet(Find_Element.success_pay)

# 操作层
class MyorderHandles(DriverHandles):

    def __init__(self):
        self.m_page = MyorderPage()

    # 点击立即支付
    def input_myorder_pay(self):
        self.input_windows(self.m_page.driver)
        self.input_click(self.m_page.find_myorder_pay())

    # 点击货到付款
    def input_myorder_delivery(self):
        self.input_windows(self.m_page.driver)
        self.input_click(self.m_page.find_myorder_delivery())

    # 点击确认支付
    def input_myorder_confirm(self):
        self.input_click(self.m_page.find_myorder_confirm())

    # 获取支付成功文本信息
    def input_myorder_success_pay(self):
        return self.input_text(self.m_page.find_myorder_success_pay())

# 业务层
class MyorderBuissens:

    def __init__(self):
        self.m_handles = MyorderHandles()

    # 支付
    def myorder_pay(self):
        # 点击立即支付
        self.m_handles.input_myorder_pay()
        time.sleep(2)
        # 点击货到付款
        self.m_handles.input_myorder_delivery()
        # 点击确认支付
        self.m_handles.input_myorder_confirm()
        # 获取支付成功信息
        suc = self.m_handles.input_myorder_success_pay()
        return suc