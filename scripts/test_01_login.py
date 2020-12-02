import pytest
from selenium.common.exceptions import NoSuchElementException

from base.page import Page
from utils import DriverUtils

@pytest.mark.run(order=2)
class Test_Login:

    def setup_class(self):
       DriverUtils.open_driver().get("http://127.0.0.1/")

    def teardown_class(self):
        DriverUtils.close_driver()

    def test_01_login(self):
        # 用户名
        username = "13702449143"
        # 密码
        pwd = "kg83200477"
        # 验证码
        code = "8888"
        # 修改用户名
        nick_name = "招伟杰"
        # 获取欢迎登陆文本信息
        welcome = "欢迎登录"
        # 首页点击登陆跳转登陆页面
        msg = Page.get_home_page().home_login()
        try:
            if msg == welcome:
                # 登陆页面登陆操作
                Page.get_login_page().login_login(username,pwd,code,nick_name)
                print("登陆并修改用户名成功")
            else:
                print("登陆不成功，请查看页面是否有问题")
        except:
            # 错误截图
            DriverUtils().screen_image()
            ex = NoSuchElementException
            raise ex