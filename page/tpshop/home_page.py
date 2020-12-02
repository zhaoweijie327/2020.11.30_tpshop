'''
利用po模式将页面分为三层（对象、操作、业务）
'''
import time

from base.base_driver import DriverBase, DriverHandles
from page.tpshop.find_element import Find_Element

# 首页
# 对象层


class HomePage(DriverBase):

    def __init__(self):
        super().__init__()

    # 定位点击登陆
    def find_home_login(self):
        return self.find_elemnet(Find_Element.home_login)

    # 定位欢迎登陆信息
    def find_home_welcome(self):
        return self.find_elemnet(Find_Element.home_welcome)

    # 定位搜索框
    def find_home_search(self):
        return self.find_elemnet(Find_Element.home_search)

    # 定位搜索按钮
    def find_home_search_button(self):
        return self.find_elemnet(Find_Element.home_search_button)

    # 定位购物车显示区
    def find_home_cart(self):
        return self.find_elemnet(Find_Element.home_cart)

    # 定位购物车结算
    def find_home_settlement(self):
        return self.find_elemnet(Find_Element.home_cart_settlement)

    # 定位我的订单
    def find_home_order(self):
        return self.find_elemnet(Find_Element.home_order)

    # 定位安全退出
    def find_home_out(self):
        return self.find_elemnet(Find_Element.home_loginout)

# 操作层
class HomeHandles(DriverHandles):

    def __init__(self):
        self.h_page = HomePage()

    # 点击登陆操作
    def input_home_login(self):
        self.input_click(self.h_page.find_home_login())

    # 获取欢迎登陆信息
    def input_home_welcome(self):
        return self.input_text(self.h_page.find_home_welcome())

    # 搜索框输入内容
    def input_home_search(self,text):
        self.input_senk(self.h_page.find_home_search(),text)

    # 点击搜索按钮
    def input_home_search_button(self):
        self.input_click(self.h_page.find_home_search_button())

    # 鼠标操作移动到购物车显示区
    def input_home_cart(self):
        self.input_actions(self.h_page.driver,self.h_page.find_home_cart())

    # 点击购物车结算按钮
    def input_home_settlement(self):
        self.input_click(self.h_page.find_home_settlement())

    # 点击我的订单
    def input_home_order(self):
        self.input_click(self.h_page.find_home_order())

    # 点击安全退出
    def input_home_out(self):
        self.input_click(self.h_page.find_home_out())

# 业务层
class HomeBuissens:

    def __init__(self):
        self.h_handles = HomeHandles()

    # 登陆
    def home_login(self):
        try:
            # 点击完全退出
            self.h_handles.input_home_out()
        except:
            # 点击登陆
            self.h_handles.input_home_login()
            # 获取欢迎登陆信息
            return self.h_handles.input_home_welcome()
        time.sleep(2)

    # 搜索
    def home_search(self,text):
        # 输入搜索内容
        self.h_handles.input_home_search(text)
        # 点击搜索按钮
        self.h_handles.input_home_search_button()

    # 购物车
    def home_cart(self):
        # 移动到购物车显示区域
        self.h_handles.input_home_cart()
        time.sleep(3)
        # 点击购物车结算
        self.h_handles.input_home_settlement()

    # 我的订单
    def homg_order(self):
        # 点击我的订单
        self.h_handles.input_home_order()