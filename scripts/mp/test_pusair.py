import logging
import time

import pytest

import config
from base.mp.page import Page
from utils import DriverUtils, data_path, is_exists_element


@pytest.mark.run(order=3)
class Test_Mp_Login:

    __time = int(time.time()*1000)

    def setup_class(self):
       self.driver = DriverUtils.open_driver()

    def teardown_class(self):
        DriverUtils.close_driver()

    @pytest.mark.parametrize("title,content,zhuanti",data_path(config.BAS_URL + '/data/mp.json','pusair'))
    def test_02_pusair(self,title,content,zhuanti):
        self.title_name = title + self.__time
        try:
            # 点击内容管理发布文章
            Page.get_home_page().mp_home_ca()
            # 发布内容
            Page.get_pusair_page().mp_pusair_contant(self.title_name,content,self.driver,zhuanti)
            # 存入日志
            logging.info("---------------->发布成功")
            # 存储标题
            config.TITLE = self.title_name
        except Exception:
            print("登陆不成功，请查看页面是否有问题")
            # 错误截图
            DriverUtils().screen_image()
            raise

