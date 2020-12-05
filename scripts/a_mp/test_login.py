#-*-coding:utf-8 -*-
import logging
import time

import pytest

import config
from base.mp.page import Page
from config import BAS_URL
from utils import DriverUtils, data_path, is_exists_element


@pytest.mark.run(order=2)
class Test_Mp_Login:

    titles = time.strftime("%H%M%S")

    def setup_class(self):
       self.driver = DriverUtils.open_driver()
       self.driver.get("http://ttmp.research.itcast.cn/")

    def teardown_class(self):
        DriverUtils.close_driver()

    @pytest.mark.parametrize("username,code,message,title,content,zhuanti",data_path(BAS_URL + '/data/mp.json','login'))
    def test_01_login(self,username,code,message,title,content,zhuanti):
        self.title_name = title + self.titles
        try:
            # 登陆
            Page.get_login_page().mp_login_login(username,code)
            # 断言
            is_exists_element(message)
            # 存入日志
            logging.info("---------------->登陆成功")
            # 点击内容管理和发布文章
            Page.get_home_page().mp_home_ca()
            # 确认发布文章内容
            Page.get_pusair_page().mp_pusair_contant(self.title_name,content,self.driver,zhuanti)
            logging.info("---------------->发布成功")
        except Exception:
            print("操作失败，请查看页面是否有问题")
            # 错误截图
            DriverUtils().screen_image()
            raise
        config.TITLE = self.title_name
        print(config.TITLE)
