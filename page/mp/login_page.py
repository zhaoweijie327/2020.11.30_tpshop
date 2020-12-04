'''
����poģʽ��ҳ���Ϊ���㣨���󡢲�����ҵ��
'''
import time

from base.base_driver import DriverBase, DriverHandles
from page.mp.mp_find_element import Mp_Find_Element


# �����
class Mp_LoginPage(DriverBase):

    def __init__(self):
        super().__init__()

    # ��λ�û��������
    def find_login_username(self):
        return self.find_elemnet(Mp_Find_Element.login_username)

    # ��λ��֤�������
    def find_login_code(self):
        return self.find_elemnet(Mp_Find_Element.login_code)

    # ��λ��½��ť
    def find_login_button(self):
        return self.find_elemnet(Mp_Find_Element.login_button)


# ������
class Mp_LoginHandles(DriverHandles):

    def __init__(self):
        self.ml_page = Mp_LoginPage()

    # �����û�������
    def input_login_username(self,username):
        self.input_senk(self.ml_page.find_login_username(),username)

    # ������֤�����
    def input_login_code(self,code):
        self.input_senk(self.ml_page.find_login_code(), code)

    # �����½����
    def input_login_button(self):
        self.input_click(self.ml_page.find_login_button())


# ҵ���
class Mp_LoginBuissens:

    def __init__(self):
        self.ml_handles = Mp_LoginHandles()

    # ��½
    def mp_login_login(self,username,code):
        # �����û���
        self.ml_handles.input_login_username(username)
        # ������֤��
        self.ml_handles.input_login_code(code)
        # �����½
        self.ml_handles.input_login_button()
        time.sleep(2)

