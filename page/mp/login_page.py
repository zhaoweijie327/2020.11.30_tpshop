'''
利用po模式将页面分为三层（对象、操作、业务）
'''
import time

from base.base_driver import DriverBase, DriverHandles
from page.mp.mp_find_element import Mp_Find_Element


# 对象层
class Mp_LoginPage(DriverBase):

    def __init__(self):
        super().__init__()

    # 定位用户名输入框
    def find_login_username(self):
        return self.find_elemnet(Mp_Find_Element.login_username)

    # 定位验证码输入框
    def find_login_code(self):
        return self.find_elemnet(Mp_Find_Element.login_code)

    # 定位登陆按钮
    def find_login_button(self):
        return self.find_elemnet(Mp_Find_Element.login_button)


# 操作层
class Mp_LoginHandles(DriverHandles):

    def __init__(self):
        self.ml_page = Mp_LoginPage()

    # 输入用户名操作
    def input_login_username(self,username):
        self.input_senk(self.ml_page.find_login_username(),username)

    # 输入验证码操作
    def input_login_code(self,code):
        self.input_senk(self.ml_page.find_login_code(), code)

    # 点击登陆操作
    def input_login_button(self):
        self.input_click(self.ml_page.find_login_button())


# 业务层
class Mp_LoginBuissens:

    def __init__(self):
        self.ml_handles = Mp_LoginHandles()

    # 登陆
    def mp_login_login(self,username,code):
        # 输入用户名
        self.ml_handles.input_login_username(username)
        # 输入验证码
        self.ml_handles.input_login_code(code)
        # 点击登陆
        self.ml_handles.input_login_button()
        time.sleep(2)

