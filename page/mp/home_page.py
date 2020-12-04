'''
����poģʽ��ҳ���Ϊ���㣨���󡢲�����ҵ��
'''
import time

from base.base_driver import DriverBase, DriverHandles
from page.mp.mp_find_element import Mp_Find_Element


# �����
class Mp_HomePage(DriverBase):

    def __init__(self):
        super().__init__()

    # ��λ���ݹ���
    def find_home_content(self):
        return self.find_elemnet(Mp_Find_Element.home_content)

    # ��λ��������
    def find_home_article(self):
        return self.find_elemnet(Mp_Find_Element.home_article)

# ������
class Mp_HomeHandles(DriverHandles):

    def __init__(self):
        self.mp_page = Mp_HomePage()

    # ģ�������ݹ������
    def input_home_content(self):
        self.input_click(self.mp_page.find_home_content())

    # ģ�����������²���
    def input_home_article(self):
        self.input_click(self.mp_page.find_home_article())

# ҵ���
class Mp_HomeBuissens:

    def __init__(self):
        self.mh_handles = Mp_HomeHandles()

    # ������ݹ���������
    def mp_home_ca(self):
        # ������ݹ���
        self.mh_handles.input_home_content()
        # ������·���
        self.mh_handles.input_home_content()
        time.sleep(2)

