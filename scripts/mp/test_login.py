import logging
import pytest
from base.mp.page import Page
from config import BAS_URL
from utils import DriverUtils, data_path, is_exists_element


@pytest.mark.run(order=2)
class Test_Mp_Login:

    def setup_class(self):
       DriverUtils.open_driver().get("http://ttmp.research.itcast.cn/#/login")

    def teardown_class(self):
        DriverUtils.close_driver()

    @pytest.mark.parametrize("username,code,message",data_path(BAS_URL + '/data/mp.json','login'))
    def test_01_login(self,username,code,message):
        try:
            # ��½
            Page.get_login_page().mp_login_login(self.username,code)
            # ����
            is_exists_element(message)
            # ������־
            logging.info("---------------->��½�ɹ�")
        except Exception:
            print("��½���ɹ�����鿴ҳ���Ƿ�������")
            # �����ͼ
            DriverUtils().screen_image()
            raise