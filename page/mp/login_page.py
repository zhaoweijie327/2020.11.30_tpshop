'''
利用po模式将页面分为三层（对象、操作、业务）
'''
import time

from base.base_driver import DriverBase, DriverHandles
from page.tpshop.find_element import Find_Element

# 对象层


class LoginPage(DriverBase):

    def __init__(self):
        super().__init__()

    # 定位用户名输入框
    def find_login_username(self):
        return self.find_elemnet(Find_Element.login_name)

    # 定位密码输入框
    def find_login_pwd(self):
        return self.find_elemnet(Find_Element.login_pwd)

    # 定位验证码输入框
    def find_login_code(self):
        return self.find_elemnet(Find_Element.login_code)

    # 定位登陆按钮
    def find_login_button(self):
        return self.find_elemnet(Find_Element.login_button)

    # 定位个人资料链接
    def find_personal_data(self):
        return self.find_elemnet(Find_Element.personal_data)

    # 定位修改用户名输入框
    def find_personal_nickname(self):
        return self.find_elemnet(Find_Element.personal_nickname)

    # 定位确认保存按钮
    def find_personal_save(self):
        return self.find_elemnet(Find_Element.personal_save)

# 操作层
class LoginHandles(DriverHandles):

    def __init__(self):
        self.l_page = LoginPage()

    # 输入用户名操作
    def input_login_username(self,username):
        self.input_senk(self.l_page.find_login_username(),username)

    # 输入密码操作
    def input_login_pwd(self,pwd):
        self.input_senk(self.l_page.find_login_pwd(),pwd)

    # 输入验证码操作
    def input_login_code(self,code):
        self.input_senk(self.l_page.find_login_code(), code)

    # 点击登陆操作
    def input_login_button(self):
        self.input_click(self.l_page.find_login_button())

    # 点击个人资料
    def input_personal_data(self):
        self.input_click(self.l_page.find_personal_data())

    # 输入用户名操作
    def input_personal_nickname(self,name):
        self.input_senk(self.l_page.find_personal_nickname(),name)

    # 点击保存
    def input_personal_save(self):
        self.input_click(self.l_page.find_personal_save())

# 业务层
class LoginBuissens:

    def __init__(self):
        self.l_handles = LoginHandles()

    # 登陆
    def login_login(self,username,pwd,code,name):
        # 输入用户名
        self.l_handles.input_login_username(username)
        # 输入密码
        self.l_handles.input_login_pwd(pwd)
        # 输入验证码
        self.l_handles.input_login_code(code)
        # 点击登陆
        self.l_handles.input_login_button()
        # 点击个人资料
        self.l_handles.input_personal_data()
        # 输入修改的用户名
        self.l_handles.input_personal_nickname(name)
        # 点击保存
        self.l_handles.input_personal_save()
        # DriverUtils.screen_image()
        time.sleep(5)

