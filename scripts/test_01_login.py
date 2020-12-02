import logging

import pytest
from selenium.common.exceptions import NoSuchElementException

from base.page import Page
from config import BAS_URL
from utils import DriverUtils, data_path


@pytest.mark.run(order=2)
class Test_Login:

    def setup_class(self):
       DriverUtils.open_driver().get("http://127.0.0.1/")

    def teardown_class(self):
        DriverUtils.close_driver()

    @pytest.mark.parametrize("username,pwd,code,nick_name,msg",data_path(BAS_URL + '/data/tpshop.json','login'))
    def test_01_login(self,username,pwd,code,nick_name,msg):
        # 首页点击登陆跳转登陆页面
        message = Page.get_home_page().home_login()
        try:
            # 断言
            assert message == msg
            Page.get_login_page().login_login(username,pwd,code,nick_name)
            # 存入日志
            logging.info("用户名：%s....密码：%s...验证码：%s...修改用户名：%s" %(username,pwd,code,nick_name))
            logging.info("---------------->登陆并修改用户名成功")
        except Exception:
            print("登陆不成功，请查看页面是否有问题")
            # 错误截图
            DriverUtils().screen_image()
            raise