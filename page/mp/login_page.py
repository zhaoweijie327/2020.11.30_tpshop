'''
����poģʽ��ҳ���Ϊ���㣨���󡢲�����ҵ��
'''
import time

from base.base_driver import DriverBase, DriverHandles
from page.tpshop.find_element import Find_Element

# �����


class LoginPage(DriverBase):

    def __init__(self):
        super().__init__()

    # ��λ�û��������
    def find_login_username(self):
        return self.find_elemnet(Find_Element.login_name)

    # ��λ���������
    def find_login_pwd(self):
        return self.find_elemnet(Find_Element.login_pwd)

    # ��λ��֤�������
    def find_login_code(self):
        return self.find_elemnet(Find_Element.login_code)

    # ��λ��½��ť
    def find_login_button(self):
        return self.find_elemnet(Find_Element.login_button)

    # ��λ������������
    def find_personal_data(self):
        return self.find_elemnet(Find_Element.personal_data)

    # ��λ�޸��û��������
    def find_personal_nickname(self):
        return self.find_elemnet(Find_Element.personal_nickname)

    # ��λȷ�ϱ��水ť
    def find_personal_save(self):
        return self.find_elemnet(Find_Element.personal_save)

# ������
class LoginHandles(DriverHandles):

    def __init__(self):
        self.l_page = LoginPage()

    # �����û�������
    def input_login_username(self,username):
        self.input_senk(self.l_page.find_login_username(),username)

    # �����������
    def input_login_pwd(self,pwd):
        self.input_senk(self.l_page.find_login_pwd(),pwd)

    # ������֤�����
    def input_login_code(self,code):
        self.input_senk(self.l_page.find_login_code(), code)

    # �����½����
    def input_login_button(self):
        self.input_click(self.l_page.find_login_button())

    # �����������
    def input_personal_data(self):
        self.input_click(self.l_page.find_personal_data())

    # �����û�������
    def input_personal_nickname(self,name):
        self.input_senk(self.l_page.find_personal_nickname(),name)

    # �������
    def input_personal_save(self):
        self.input_click(self.l_page.find_personal_save())

# ҵ���
class LoginBuissens:

    def __init__(self):
        self.l_handles = LoginHandles()

    # ��½
    def login_login(self,username,pwd,code,name):
        # �����û���
        self.l_handles.input_login_username(username)
        # ��������
        self.l_handles.input_login_pwd(pwd)
        # ������֤��
        self.l_handles.input_login_code(code)
        # �����½
        self.l_handles.input_login_button()
        # �����������
        self.l_handles.input_personal_data()
        # �����޸ĵ��û���
        self.l_handles.input_personal_nickname(name)
        # �������
        self.l_handles.input_personal_save()
        # DriverUtils.screen_image()
        time.sleep(5)

