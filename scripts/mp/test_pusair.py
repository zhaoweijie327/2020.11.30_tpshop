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
            # ������ݹ���������
            Page.get_home_page().mp_home_ca()
            # ��������
            Page.get_pusair_page().mp_pusair_contant(self.title_name,content,self.driver,zhuanti)
            # ������־
            logging.info("---------------->�����ɹ�")
            # �洢����
            config.TITLE = self.title_name
        except Exception:
            print("��½���ɹ�����鿴ҳ���Ƿ�������")
            # �����ͼ
            DriverUtils().screen_image()
            raise

